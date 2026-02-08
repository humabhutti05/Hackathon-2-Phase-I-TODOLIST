#!/bin/bash
cd "$(dirname "$0")"
PYTHONPATH=. ~/.local/bin/uv run python src/main.py "$@"
