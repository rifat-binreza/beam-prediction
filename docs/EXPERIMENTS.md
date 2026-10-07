# Experiment guide

The root-level notebook filenames are retained so existing links and experiment history remain intact. Names such as “final” identify historical files; they do not certify correspondence to the submitted manuscript.

| Family | Files | Navigation guidance |
| --- | --- | --- |
| Baseline comparison | `beam_predict_final_paper.ipynb` | First stop for saved image/position/height/distance results |
| ConvNeXt temporal fusion | `caformer_convnext_tiny_finetuned_random_split_final (1).ipynb` | Reviewed ConvNeXt encoder, cross-attention, gating and LSTM implementation; read split caveats |
| Other CAFormer variants | `ca_former.ipynb`, `ca_former1.ipynb`, `ca_former_updated.ipynb`, `caformer_convnext_tiny_anti_overfit_fixed.ipynb` | Historical variants; verify configuration in each notebook before comparing |
| Image experiments | `image_advance.ipynb`, `imageadvance1.ipynb` | Image-focused exploration |
| Position / traditional experiments | `position_ungabunga.ipynb`, `traditional_model.ipynb` | Additional baseline exploration |
| Other exploratory notebooks | `intro.ipynb`, `lalal.ipynb`, `ungabunga.ipynb`, `updated12.ipynb`, `seed_changed_88 (1).ipynb`, `new_paper_style.ipynb` | Historical context; not selected as default entry points |
| Tabular utilities | `improve_tabular_models.py` | Residual MLP, train-only imputation/scaling, stratified folds and ensemble evaluation; import from a prepared notebook, not a data-loading CLI |
| Figures | `generate_ieee_comparison_figure.py`, `export_notebook_figures.py` | Render stored metrics and export embedded diagnostics |
| Existing comparison write-up | `IEEE_FINDINGS_COMPARISON.md`, `.tex`, `main.tex` | Comparative baseline report; `main.tex` contains placeholder authors |

## Fusion path

Image sequence → crop or full-image fallback → ConvNeXt-Tiny → projected image tokens. Position sequences → MLP → position tokens. Two bidirectional cross-attention blocks exchange context, position tokens gate image tokens, concatenation feeds a unidirectional LSTM, and its final timestep feeds the beam classifier.

The configured embedding size is 256, attention uses four heads, and the LSTM hidden size is 256. This is a code-grounded overview of the reviewed variant, not a claim that every CAFormer notebook shares this architecture.
