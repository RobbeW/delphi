#!/bin/bash
set -e
cd "$(dirname "$0")/.."
BUNDLED="$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
PY=""
for candidate in "$PWD/eval_grading/.venv/bin/python" "$BUNDLED" python3; do
  if "$candidate" -c 'import reportlab' >/dev/null 2>&1; then PY="$candidate"; break; fi
done
if [ -z "$PY" ]; then echo 'Python met reportlab ontbreekt. Installeer de vereisten uit eval_grading/requirements.txt.'; read -r -p 'Druk op Enter om te sluiten.'; exit 1; fi
"$PY" -m eval_grading.app prepare
"$PY" -m eval_grading.app serve --open
