# HCTiGT

**Hill Climb Till It's Go Time.** Small invitations to take a first step into learning, experimenting, and research.

This repository is the **authoring source of truth**. LessWrong is the primary publishing surface; its typography, images, and layout can differ without becoming the canonical text. A personal site may follow.

## First installment

- [Manuscript](posts/01-the-first-step.md) — deliberately almost blank; the author writes the invitation.
- [First-step Colab notebook](notebooks/01-the-first-step.ipynb) — Part A runs unchanged; Part B invites an intentional choice.
- [From-scratch rabbit hole](notebooks/02-from-scratch.ipynb) — optional: choose a corpus, initialize a GPT-2 architecture with random weights, and run bounded pretraining.
- [Assets](assets/README.md) — illustrations and other publication material.

When this branch reaches upstream main, the notebook can be opened directly at:

- First step: https://colab.research.google.com/github/bubskee/hctigt/blob/main/notebooks/01-the-first-step.ipynb
- From scratch: https://colab.research.google.com/github/bubskee/hctigt/blob/main/notebooks/02-from-scratch.ipynb

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
4. In the optional **from-scratch** notebook, run setup; confirm **Run all** does not start training until the opt-in box is checked. With **TinyStories / tiny / 20 steps**, verify random parameter initialization, updates, and *training plus validation* loss reporting.
5. Repeat the scratch run with **Arithmetic** or **WikiText-2** and verify corpus selection works. The 124M-model option is not part of the minimal smoke test.
6. Confirm both notebooks work with only their own cells and public downloads. Do not call either Colab-tested until someone has performed these steps.

The first notebook **fine-tunes pretrained GPT-2**. The optional second one trains GPT-2 architecture **from random weights**, reusing GPT-2's tokenizer. A short demo is not complete pretraining; loss changes alone do not establish generalization.
