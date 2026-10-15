# HCTiGT

**Hill Climb Till It's Go Time.** Small invitations to take a first step into learning, experimenting, and research.

This repository is the **authoring source of truth**. LessWrong is the primary publishing surface; its typography, images, and layout can differ without becoming the canonical text. A personal site may follow.

## First installment

- [Manuscript](posts/01-the-first-step.md) — deliberately almost blank; the author writes the invitation.
- [Colab notebook](notebooks/01-the-first-step.ipynb) — Part A runs unchanged; Part B invites an intentional choice.
- [Assets](assets/README.md) — illustrations and other publication material.

When this branch reaches upstream main, the notebook can be opened directly at:

https://colab.research.google.com/github/bubskee/hctigt/blob/main/notebooks/01-the-first-step.ipynb

**Readers shouldn't need GitHub:** send them straight to the Colab notebook from the LessWrong post.

## Working convention

- `bubskee/hctigt`: authoritative manuscript, notebook, and asset revisions.
- `bfaber-centaur/hctigt`: collaborative work and proposed changes.
- LessWrong: the published edition and discussion; don't chase pixel-perfect formatting parity.
- Record a published edition with a Git tag or commit reference and its LessWrong URL.

## Test before sharing

Static checks: `python scripts/check_notebook.py` (JSON structure and Python syntax, **not** a runtime test).

Manual Colab acceptance, on a **fresh GPU runtime**:

1. Open the notebook from GitHub in Colab and **Run all**. Part A trains, reports a before/after loss, and plots the curve; Part B should only display instructions.
2. In Part B, check `RUN_REMIX`, choose **math**, and run that cell. It must use a fresh GPT-2 and finish without errors.
3. Repeat Part B with **stories**, and confirm the control values really affect the run.
4. Confirm the notebook works with only its own cells and public downloads. Do not call it Colab-tested until someone has performed these steps.

Both tracks **fine-tune pretrained GPT-2**. The notebook shows training and memorization pressure; it does not prove arithmetic generalization.
