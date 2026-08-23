"""Load the prompt sequence and the analysis package exactly as the app sends them."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

_PROMPT_HEADER = re.compile(r"^Prompt\s+(\d+):\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Inputs:
    package_path: Path
    package_text: str          # raw bytes of the uploaded JSON, untouched
    package_sha256: str
    prompts_path: Path
    prompts: list[str]         # prompt 1..4 in order
    prompts_sha256: str


def parse_prompts(text: str) -> list[str]:
    """Split a 'Prompt N:' delimited file into an ordered list of prompt bodies."""
    matches = list(_PROMPT_HEADER.finditer(text))
    if not matches:
        raise ValueError("No 'Prompt N:' headers found in prompts file")
    prompts: list[tuple[int, str]] = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        prompts.append((int(m.group(1)), text[start:end].strip()))
    prompts.sort(key=lambda p: p[0])
    numbers = [n for n, _ in prompts]
    if numbers != list(range(1, len(numbers) + 1)):
        raise ValueError(f"Prompt numbers are not contiguous from 1: {numbers}")
    return [body for _, body in prompts]


def load_inputs(package_path: str | Path, prompts_path: str | Path) -> Inputs:
    package_path = Path(package_path)
    prompts_path = Path(prompts_path)
    package_text = package_path.read_text(encoding="utf-8")
    prompts_text = prompts_path.read_text(encoding="utf-8")
    return Inputs(
        package_path=package_path,
        package_text=package_text,
        package_sha256=hashlib.sha256(package_text.encode("utf-8")).hexdigest(),
        prompts_path=prompts_path,
        prompts=parse_prompts(prompts_text),
        prompts_sha256=hashlib.sha256(prompts_text.encode("utf-8")).hexdigest(),
    )


# The app's repair prompt, as observed on its "Paste AI result" screen (2026-08-22). It is
# composed of a fixed opening line, one clause per error type, and a fixed closing line.
CORRECTION_OPEN = ("Correct the previous final response using the originally attached TuneMyBG package. "
                   "Do not repeat the analysis and do not ask for the package again.")
CORRECTION_CLOSE = ("Return the complete final strict JSON again, including every original section and "
                    "exactly one parameter_decisions row for every decision_inventory item.")
CLAUSE_SECTIONS = "Correct these sections according to required_output_schema: {items}."
CLAUSE_MISSING = "Add exactly these missing parameter_key values: {items}."
CLAUSE_EXTRA = "Remove these keys because they are not in decision_inventory: {items}."
CLAUSE_CURRENT = "Copy current_value exactly from decision_inventory for: {items}."

# Legacy single-clause template kept for --correction-prompt overrides ({sections} placeholder).
CORRECTION_TEMPLATE = CORRECTION_OPEN + "\n" + CLAUSE_SECTIONS.replace("{items}", "{sections}") + "\n" + CORRECTION_CLOSE

# Assumed wording when the response did not parse at all. The real app offers no prompt in that
# case ("Paste a valid JSON response from AI."); this is only used with --correct-unparseable.
UNPARSEABLE_SECTIONS = "entire response (it was not one valid strict JSON object)"


def correction_prompt(sections: list[str], template: str = CORRECTION_TEMPLATE,
                      validation: dict | None = None) -> str:
    """Build the app's repair prompt. With a validation dict the per-error clauses are used;
    otherwise (or with a custom template) the single-clause template is filled with sections."""
    if validation is None or template != CORRECTION_TEMPLATE:
        return template.format(sections=", ".join(sections) if sections else UNPARSEABLE_SECTIONS)
    # Only the three error types the app actually repairs (observed 2026-08-22).
    d = validation.get("details") or {}
    clauses = []
    if d.get("missing_keys"):
        clauses.append(CLAUSE_MISSING.format(items=", ".join(d["missing_keys"])))
    if d.get("extra_keys") or d.get("duplicate_keys"):
        clauses.append(CLAUSE_EXTRA.format(items=", ".join(d.get("extra_keys", []) + d.get("duplicate_keys", []))))
    if d.get("current_value_mismatch"):
        clauses.append(CLAUSE_CURRENT.format(items=", ".join(d["current_value_mismatch"])))
    if d.get("focus_invalid"):
        clauses.append(CLAUSE_SECTIONS.format(items="profile_recommendation.focus"))
    if not clauses:
        clauses.append(CLAUSE_SECTIONS.format(items=", ".join(sections) if sections else UNPARSEABLE_SECTIONS))
    return "\n".join([CORRECTION_OPEN, *clauses, CORRECTION_CLOSE])


def attachment_block(filename: str, package_text: str) -> str:
    """Plain-text rendering of a file attachment for backends without native documents."""
    return f"[Attached file: {filename}]\n{package_text}\n[End of attached file]"
