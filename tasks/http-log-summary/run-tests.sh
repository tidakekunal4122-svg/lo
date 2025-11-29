#!/bin/bash
set -euo pipefail

cd "$TEST_DIR"
python -m pip install --quiet pytest
pytest -q
