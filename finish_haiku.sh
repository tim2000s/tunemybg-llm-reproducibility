#!/bin/zsh
# Finish the Haiku batch, replay its repair-class runs with the app's wording, re-validate.
cd /Users/tims/llm-endo
export ANTHROPIC_API_KEY="$(tr -d '[:space:]' < ~/Downloads/Claude-API-Key.txt)"
echo "=== finish_haiku.sh start $(date +%H:%M:%S)" >> results/replay_haiku.log
python3 run_experiment.py --backend anthropic --model claude-haiku-4-5 --runs 50 --workers 2 --max-tokens 32000 --max-repairs 1 --experiment real_haiku45_50 >> results/real_haiku45_50.log 2>&1
python3 rerun_corrections.py results/real_haiku45_50 --backend anthropic --model claude-haiku-4-5 --max-tokens 32000 >> results/replay_haiku.log 2>&1
python3 revalidate.py results/real_haiku45_50 >> results/replay_haiku.log 2>&1
echo "HAIKU-ALL-DONE $(date +%H:%M:%S)" >> results/replay_haiku.log
