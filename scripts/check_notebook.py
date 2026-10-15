#!/usr/bin/env python3
"""Fast, dependency-free structure/syntax check. Does NOT execute Colab training."""
import ast
import json
from pathlib import Path

notebook_path = Path(__file__).resolve().parents[1] / "notebooks/01-the-first-step.ipynb"
data = json.loads(notebook_path.read_text(encoding="utf-8"))
assert data["nbformat"] == 4
assert data["metadata"]["kernelspec"]["name"] == "python3"
assert len(data["cells"]) >= 10
code = []
for i, cell in enumerate(data["cells"], start=1):
    assert cell["cell_type"] in {"markdown", "code"}
    source = cell["source"]
    source = "".join(source) if isinstance(source, list) else source
    assert source.strip(), f"Empty cell {i}"
    if cell["cell_type"] == "code":
        assert cell.get("outputs", []) == [], f"Committed outputs in cell {i}"
        assert cell.get("execution_count") is None, f"Committed execution count in cell {i}"
        # IPython's %pip line isn't Python syntax; everything else should compile.
        valid_python = "\n".join(
            line for line in source.splitlines() if not line.lstrip().startswith("%")
        )
        ast.parse(valid_python, filename=f"cell-{i}")
        code.append(source)
all_code = "\n".join(code)
for required in ('"stories"', '"math"', "RUN_REMIX = False", "run_experiment(", "TinyStories"):
    assert required in all_code, f"Missing {required}"
print(f"OK: {len(data['cells'])} cells; {len(code)} code cells; valid JSON and Python syntax.")
