# Beam Prediction

> **Research fork maintained by Rifat Bin Reza.** I contributed to the collaborative beam-prediction research associated with this project. The related manuscript has been submitted to **IEEE Transactions on Vehicular Technology**.
>
> **Upstream:** [shovo896/beam-prediction](https://github.com/shovo896/beam-prediction). This fork preserves the original code, commit history, and license. Submission status does not imply acceptance or publication.

Experiments for beam prediction using camera images, positional/tabular
features, and deep-learning models.

## Contents

- `beam_predict_final_paper.ipynb`: main end-to-end experiment notebook
- `FIGURE_GALLERY.md`: all final result figures in one place
- `IEEE_FINDINGS_COMPARISON.md`: IEEE-style comparison with the reference paper
- `improve_tabular_models.py`: reusable tabular preprocessing, training, and
  evaluation utilities
- `ca_former*.ipynb`: CAFormer experiments
- `traditional_model.ipynb`: traditional model experiments
- `image*.ipynb`: image-based experiments

## Environment

The notebooks are designed for a Python/Jupyter environment with the project
dataset available locally or in Google Colab. Core dependencies include
NumPy, pandas, PyTorch, torchvision, scikit-learn, Matplotlib, Seaborn, and
Jupyter.

Dataset paths used by the notebooks may need to be updated for your
environment before execution.

## Usage

Open a notebook in Jupyter or Google Colab and run its cells in order. For the
main workflow, start with `beam_predict_final_paper.ipynb`.

Generated datasets, model checkpoints, notebook checkpoints, and Python cache
files are excluded from Git.

## Final Results

The final result figures, including the refined image model and all implemented
position-family modalities, are available in [FIGURE_GALLERY.md](FIGURE_GALLERY.md).
Regenerate the summary figures with `python generate_ieee_comparison_figure.py`
and export the notebook diagnostic plots with `python export_notebook_figures.py`.
