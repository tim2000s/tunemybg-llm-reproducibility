"""Chat backends. Each backend starts a fresh conversation per run and replays the full
history on every turn, mirroring a new chat in a consumer UI."""

from __future__ import annotations

import json
import os
import random
import re
import time
from dataclasses import dataclass, field
from typing import Any

import requests

from .prompts import attachment_block

_THINK_RE = re.compile(r"<think>.*?</think>\s*", re.DOTALL)


@dataclass
class Turn:
    text: str
    latency_s: float
    finish_reason: str | None = None
    usage: dict[str, Any] = field(default_factory=dict)
    model_reported: str | None = None
    extra: dict[str, Any] = field(default_factory=dict)


class TransientError(Exception):
    """Retryable failure (rate limit, 5xx, connection reset)."""


def _retry(fn, attempts: int = 5, base_delay: float = 5.0, label: str = ""):
    last: Exception | None = None
    for i in range(attempts):
        try:
            return fn()
        except TransientError as e:
            last = e
            delay = min(base_delay * (2 ** i) + random.uniform(0, 2), 120)
            print(f"    [{label}] transient error ({e}); retry {i + 1}/{attempts} in {delay:.0f}s")
            time.sleep(delay)
    raise RuntimeError(f"{label}: gave up after {attempts} attempts: {last}")


class Conversation:
    """Base: keeps an OpenAI-style list of {'role','content'} messages."""

    def __init__(self, backend: "Backend"):
        self.backend = backend
        self.messages: list[dict[str, Any]] = []

    def send(self, user_text: str, attachment: tuple[str, str] | None = None) -> Turn:
        content = self._user_content(user_text, attachment)
        self.messages.append({"role": "user", "content": content})
        turn = self.backend._complete(self.messages)
        self.messages.append({"role": "assistant", "content": turn.text})
        return turn

    def _user_content(self, user_text: str, attachment: tuple[str, str] | None):
        if attachment is None:
            return user_text
        filename, text = attachment
        return attachment_block(filename, text) + "\n\n" + user_text


class Backend:
    name = "base"

    def __init__(self, model: str, temperature: float | None = None, max_tokens: int = 32000,
                 timeout_s: float = 3600.0, **kwargs: Any):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout_s = timeout_s
        self.options = kwargs

    def describe(self) -> dict[str, Any]:
        return {"backend": self.name, "model": self.model, "temperature": self.temperature,
                "max_tokens": self.max_tokens, **self.options}

    def new_conversation(self) -> Conversation:
        return Conversation(self)

    def _complete(self, messages: list[dict[str, Any]]) -> Turn:  # pragma: no cover
        raise NotImplementedError


# --------------------------------------------------------------------------- OpenAI-compatible
class OpenAICompatBackend(Backend):
    """LM Studio (http://localhost:1234/v1), Ollama's /v1 shim, OpenAI, OpenRouter, etc."""

    name = "openai_compat"

    def __init__(self, model: str, base_url: str = "http://localhost:1234/v1",
                 api_key: str | None = None, reasoning_effort: str | None = None,
                 max_tokens_param: str = "max_tokens", **kwargs: Any):
        super().__init__(model, **kwargs)
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.reasoning_effort = reasoning_effort
        self.max_tokens_param = max_tokens_param
        self.options.update({"base_url": self.base_url, "reasoning_effort": reasoning_effort})

    def _complete(self, messages):
        body: dict[str, Any] = {"model": self.model, "messages": messages, "stream": False,
                                self.max_tokens_param: self.max_tokens}
        if self.temperature is not None:
            body["temperature"] = self.temperature
        if self.reasoning_effort:
            body["reasoning_effort"] = self.reasoning_effort
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        def call():
            t0 = time.time()
            try:
                r = requests.post(f"{self.base_url}/chat/completions", json=body,
                                  headers=headers, timeout=self.timeout_s)
            except requests.ConnectionError as e:
                raise TransientError(str(e)) from e
            if r.status_code == 429 or r.status_code >= 500:
                raise TransientError(f"HTTP {r.status_code}: {r.text[:200]}")
            r.raise_for_status()
            data = r.json()
            choice = data["choices"][0]
            msg = choice["message"]
            text = _THINK_RE.sub("", msg.get("content") or "").strip()
            return Turn(text=text, latency_s=time.time() - t0,
                        finish_reason=choice.get("finish_reason"), usage=data.get("usage") or {},
                        model_reported=data.get("model"),
                        extra={"reasoning_content": msg.get("reasoning_content")})

        return _retry(call, label=self.name)


# --------------------------------------------------------------------------- Ollama native
class OllamaBackend(Backend):
    """Ollama native /api/chat so num_ctx can be set (the /v1 shim ignores context length)."""

    name = "ollama"

    def __init__(self, model: str, base_url: str = "http://localhost:11434",
                 num_ctx: int = 65536, **kwargs: Any):
        super().__init__(model, **kwargs)
        self.base_url = base_url.rstrip("/")
        self.num_ctx = num_ctx
        self.options.update({"base_url": self.base_url, "num_ctx": num_ctx})

    def _complete(self, messages):
        opts: dict[str, Any] = {"num_ctx": self.num_ctx, "num_predict": self.max_tokens}
        if self.temperature is not None:
            opts["temperature"] = self.temperature
        body = {"model": self.model, "messages": messages, "stream": False, "options": opts}

        def call():
            t0 = time.time()
            try:
                r = requests.post(f"{self.base_url}/api/chat", json=body, timeout=self.timeout_s)
            except requests.ConnectionError as e:
                raise TransientError(str(e)) from e
            if r.status_code >= 500:
                raise TransientError(f"HTTP {r.status_code}: {r.text[:200]}")
            r.raise_for_status()
            data = r.json()
            text = _THINK_RE.sub("", data["message"].get("content") or "").strip()
            usage = {k: data.get(k) for k in ("prompt_eval_count", "eval_count",
                                              "total_duration", "prompt_eval_duration",
                                              "eval_duration")}
            return Turn(text=text, latency_s=time.time() - t0, finish_reason=data.get("done_reason"),
                        usage=usage, model_reported=data.get("model"),
                        extra={"thinking": data["message"].get("thinking")})

        return _retry(call, label=self.name)


# --------------------------------------------------------------------------- Gemini REST
class GeminiBackend(Backend):
    name = "gemini"

    def __init__(self, model: str = "gemini-3.6-flash", api_key: str | None = None, **kwargs: Any):
        super().__init__(model, **kwargs)
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise RuntimeError("GEMINI_API_KEY not set")

    def _complete(self, messages):
        contents = [{"role": "model" if m["role"] == "assistant" else "user",
                     "parts": [{"text": m["content"]}]} for m in messages]
        gen: dict[str, Any] = {"maxOutputTokens": self.max_tokens}
        if self.temperature is not None:
            gen["temperature"] = self.temperature
        body = {"contents": contents, "generationConfig": gen}
        url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
               f"{self.model}:generateContent")

        def call():
            t0 = time.time()
            try:
                r = requests.post(url, json=body, params={"key": self.api_key},
                                  timeout=self.timeout_s)
            except requests.ConnectionError as e:
                raise TransientError(str(e)) from e
            if r.status_code == 429 or r.status_code >= 500:
                raise TransientError(f"HTTP {r.status_code}: {r.text[:200]}")
            r.raise_for_status()
            data = r.json()
            cands = data.get("candidates") or []
            if not cands:
                raise RuntimeError(f"Gemini returned no candidates: {json.dumps(data)[:500]}")
            parts = cands[0].get("content", {}).get("parts", [])
            text = "".join(p.get("text", "") for p in parts if not p.get("thought")).strip()
            return Turn(text=text, latency_s=time.time() - t0,
                        finish_reason=cands[0].get("finishReason"),
                        usage=data.get("usageMetadata") or {},
                        model_reported=data.get("modelVersion"))

        return _retry(call, label=self.name)


# --------------------------------------------------------------------------- Anthropic SDK
class AnthropicConversation(Conversation):
    """Sends the package as a native document block instead of inline text."""

    def _user_content(self, user_text, attachment):
        if attachment is None:
            return user_text
        filename, text = attachment
        return [
            {"type": "document",
             "source": {"type": "text", "media_type": "text/plain", "data": text},
             "title": filename,
             "cache_control": {"type": "ephemeral"}},
            {"type": "text", "text": user_text},
        ]


class AnthropicBackend(Backend):
    name = "anthropic"

    def __init__(self, model: str = "claude-opus-5", effort: str | None = None,
                 fallbacks: bool = True, **kwargs: Any):
        super().__init__(model, **kwargs)
        import anthropic  # optional dependency, imported lazily
        self._anthropic = anthropic
        self.client = anthropic.Anthropic(timeout=self.timeout_s)
        self.effort = effort
        self.fallbacks = fallbacks
        self.options.update({"effort": effort, "fallbacks": fallbacks})

    def new_conversation(self) -> Conversation:
        return AnthropicConversation(self)

    def _complete(self, messages):
        anthropic = self._anthropic
        kwargs: dict[str, Any] = {"model": self.model, "max_tokens": self.max_tokens,
                                  "messages": messages}
        if self.effort:
            kwargs["output_config"] = {"effort": self.effort}
        if self.fallbacks:
            kwargs["betas"] = ["server-side-fallback-2026-07-01"]
            kwargs["fallbacks"] = "default"

        def call():
            t0 = time.time()
            try:
                api = self.client.beta.messages if self.fallbacks else self.client.messages
                with api.stream(**kwargs) as stream:
                    resp = stream.get_final_message()
            except anthropic.RateLimitError as e:
                raise TransientError(f"rate limited: {e}") from e
            except anthropic.APIStatusError as e:
                # mid-stream server errors arrive without a status code
                if e.status_code is None or e.status_code >= 500:
                    raise TransientError(f"HTTP {e.status_code}: {e}") from e
                raise
            except anthropic.APIConnectionError as e:
                raise TransientError(str(e)) from e
            except anthropic.APIError as e:
                if "server error" in str(e).lower() or "overloaded" in str(e).lower():
                    raise TransientError(str(e)) from e
                raise
            if resp.stop_reason == "refusal":
                raise RuntimeError(f"refusal: {getattr(resp, 'stop_details', None)}")
            text = "".join(b.text for b in resp.content if b.type == "text").strip()
            usage = resp.usage.to_dict() if hasattr(resp.usage, "to_dict") else dict(resp.usage)
            return Turn(text=text, latency_s=time.time() - t0, finish_reason=resp.stop_reason,
                        usage=usage, model_reported=resp.model)

        return _retry(call, label=self.name)


# --------------------------------------------------------------------------- Mock
class MockBackend(Backend):
    """Deterministic-per-seed fake model for testing the pipeline end to end."""

    name = "mock"

    def __init__(self, model: str = "mock", package: dict[str, Any] | None = None,
                 seed: int = 0, **kwargs: Any):
        super().__init__(model, **kwargs)
        self.package = package or {}
        self.rng = random.Random(seed)
        self.options["seed"] = seed

    def _complete(self, messages):
        n_user = sum(1 for m in messages if m["role"] == "user")
        if n_user < 4:
            text = f"CHECKPOINT {n_user}: mock findings for step {n_user}."
        elif n_user == 4:
            text = self._final_json()
        else:
            text = self._corrected_json()
        return Turn(text=text, latency_s=0.01, finish_reason="stop",
                    usage={"prompt_tokens": len(json.dumps(messages)) // 4})

    def _corrected_json(self) -> str:
        """Simulate the model fixing the flagged section; sometimes it also flips a decision."""
        obj = json.loads(json.dumps(self._last_obj))
        any_change = any(d["decision"] == "change" for d in obj["parameter_decisions"]
                         if d["parameter_key"].startswith("profile."))
        obj["profile_recommendation"]["decision"] = "change" if any_change else "keep"
        if self.rng.random() < 0.3:
            d = self.rng.choice(obj["parameter_decisions"])
            d["decision"] = "keep"
            d["suggested_value"] = d["current_value"]
        self._last_obj = obj
        return json.dumps(obj, indent=1)

    def _final_json(self) -> str:
        inv = self.package.get("decision_inventory", {}).get("items", [])
        steps = [s["key"] for s in self.package.get("analysis_workflow", {}).get("steps", [])]
        decisions = []
        for item in inv:
            choices = ["keep", "keep", "keep", "change"]
            if item["category"] == "aaps" and any(c.get("current_value") is None
                                                  for c in item.get("components", [])):
                choices.append("verify")
            d = self.rng.choice(choices)
            decisions.append({
                "parameter_key": item["parameter_key"], "parameter": item["label"],
                "current_value": item["current_value"],
                "suggested_value": f"{item['current_value']} +10%" if d == "change" else item["current_value"],
                "decision": d, "rationale": "mock rationale",
            })
        obj = {
            "summary": self.rng.choice(["Stable glucose with minor post-meal rises.",
                                        "Glucose is stable; small evening rises seen."]),
            "analysis_steps": [{"key": k, "status": self.rng.choice(["completed", "partial"]),
                                "confidence": self.rng.choice(["low", "medium", "high"]),
                                "findings": "mock", "evidence": "mock", "dependencies": "mock",
                                "data_gaps": "mock"} for k in steps],
            "strengths": ["mock strength"], "issues": ["mock issue"],
            "recommendations": [{"area": self.rng.choice(["basal", "cr", "isf", "smb"]),
                                 "title": "mock primary", "priority": "medium",
                                 "description": "mock", "suggested_change": {}}],
            "profile_recommendation": {"focus": self.rng.choice(["basal", "cr", "isf"]),
                                       "decision": "keep", "recommendation": "mock",
                                       "rationale": "mock", "confidence": "medium",
                                       "next_check": "mock"},
            "parameter_decisions": decisions,
            "meal_strategy_summary": {"suggestion": "mock", "rationale": "mock",
                                      "confidence": "medium", "next_observation": "mock",
                                      "exceptions": []},
            "implementation_steps": ["mock"], "education": ["mock"], "safety_notes": ["mock"],
        }
        self._last_obj = obj
        wrapped = self.rng.random() < 0.3
        s = json.dumps(obj, indent=1)
        return f"```json\n{s}\n```" if wrapped else s


BACKENDS: dict[str, type[Backend]] = {
    "openai": OpenAICompatBackend,
    "lmstudio": OpenAICompatBackend,
    "openai_compat": OpenAICompatBackend,
    "ollama": OllamaBackend,
    "gemini": GeminiBackend,
    "anthropic": AnthropicBackend,
    "mock": MockBackend,
}
