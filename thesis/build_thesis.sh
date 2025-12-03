#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 generate_thesis.py
echo "thesis.md rebuilt successfully."
