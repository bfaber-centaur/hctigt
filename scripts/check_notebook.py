#!/usr/bin/env python3
"""Dependency-free notebook structure and Python syntax checks; NOT a Colab runtime test."""

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = {
    "01-the-first-step.ipynb": (
        '"stories"',
        '"math"',
        "RUN_REMIX = False",
        "run_experiment(",
        "TinyStories",
    ),
    "02-from-scratch.ipynb": (
        "RUN_PRETRAINING = False",
        "GPT2LMHeadModel(config)",
        "make_random_gpt2(",
        "pack_blocks(",
        '"TinyStories"',
        '"WikiText-2"',
        '"Arithmetic"',
        "fetch_rows(corpus, \"validation\", 80)",
    ),
}

for name, expected in NOTEBOOKS.items():
    path = ROOT / "notebooks" / name
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["nbformat"] == 4, name
    assert data["metadata"]["kernelspec"]["name"] == "python3", name
    assert len(data["cells"]) >= 10, f"{name}: missing cells"

    code = []
    for cell_number, cell in enumerate(data["cells"], start=1):
        assert cell["cell_type"] in {"markdown", "code"}
        source = cell["source"]
        source = "".join(source) if isinstance(source, list) else source
        assert source.strip(), f"{name}: empty cell {cell_number}"
        if cell["cell_type"] == "code":
            assert cell.get("outputs", []) == [], f"{name}: committed outputs in cell {cell_number}"
            assert cell.get("execution_count") is None, f"{name}: executed cell {cell_number}"
            # IPython %pip is not Python syntax, so remove it before parsing.
            python_source = "\n".join(
                line for line in source.splitlines()
                if not line.lstrip().startswith("%")
            )
            ast.parse(python_source, filename=f"{name}:cell-{cell_number}")
            code.append(source)

    all_code = "\n".join(code)
    for needle in expected:
        assert needle in all_code, f"{name}: missing {needle}"

    if name == "02-from-scratch.ipynb":
        assert "GPT2LMHeadModel.from_pretrained" not in all_code
        assert "AutoModelForCausalLM.from_pretrained" not in all_code
        assert "make_arithmetic(row_count + 80, seed=1)" in all_code

    print(f"OK: {name}: {len(data['cells'])} cells, {len(code)} code cells")

print("Static checks passed. Run Colab GPU smoke tests before publishing.")
