# Getting started

## 1. Select an experiment

Use `beam_predict_final_paper.ipynb` for the documented image and position-family baselines. Use `caformer_convnext_tiny_finetuned_random_split_final (1).ipynb` to inspect ConvNeXt–CAFormer–LSTM fusion. These are research notebooks with external inputs, not standalone inference packages.

Review the repository's proprietary LICENSE before using its materials. Dependency installation does not grant permission to use the project or dataset.

## 2. Prepare the environment

Create a Python environment and install `requirements/base.txt`. For fusion, install `requirements/fusion.txt`, which includes the base requirements. Choose PyTorch/torchvision builds appropriate for your device from their official installation instructions. The saved fusion runtime reports PyTorch 2.5.1+cu121 on an NVIDIA GeForce RTX 3050 Laptop GPU; that is an observed environment, not a universal requirement.

Requirements are inferred from imports and unpinned because a complete original environment lockfile is unavailable. No clean-environment training reproduction is claimed. Save `python -m pip freeze` with any new experiment.

## 3. Obtain external inputs

Request data through [DeepSense Scenario 23](https://www.deepsense6g.net/scenarios/Scenarios%2020-29/scenario-23). Keep the original file hierarchy and dataset terms. This repository does not distribute raw data, trained checkpoints or a complete set of prepared split files.

### Baseline notebook

| Setting or input | Expected content |
| --- | --- |
| `zip_path` / extraction paths | Local Scenario 23 archive and writable extraction destination |
| `AUTHOR_ROOT` | Image split CSVs: `scenario23_img_beam_train.csv`, `_val.csv`, `_test.csv` |
| Image CSV columns | `index`, `unit1_rgb`, `unit1_beam`; existing loaders depend on column order |
| `AUTHOR_POS_ROOT` | Position split CSVs: `scenario23_pos_beam_train.csv`, `_val.csv`, `_test.csv` |
| Position CSV columns | `index`, `unit2_pos` (serialized coordinate pair), `unit1_beam`; check loader order |
| `DATA_ROOT` | Extracted scenario root, including `unit2/height` and `unit2/distance` |
| `/content/...` outputs | Writable checkpoint and derived-CSV paths; change for local execution |

The notebook checks for external author resources such as `build_net.py`, `data_feed.py`, `main_beam.py` and `main_beam_eval.py`; these are not in this repository. Resolve the expected inputs before a full run. The Colab drive-mount cell is Colab-specific: skip it locally and replace drive paths with local paths.

Run cells in order: data preparation → image training/evaluation → optional image refinement → position baseline → height/distance preparation → sensor baselines → plots. Later cells depend on earlier variables and generated checkpoints.

### Fusion notebook

Set `AUTHOR_ROOT`, `POSITION_ROOT`, `EXTRACT_ROOT`, `YOLO_CROP_ROOT` and `FINAL_MODEL_PATH` for your machine. Define `ZIP_PATH` if using archive extraction; the saved notebook contains a `NameError` at that cell because it is undefined. If using an already extracted dataset, deliberately skip archive extraction after verifying the files.

Inputs include:

- `scenario23_img_beam.csv` with `index`, `unit1_rgb`, `unit1_beam`.
- `X_train_seq.npy`, `X_val_seq.npy`, `X_test_seq.npy` and matching `y_train_seq.npy`, `y_val_seq.npy`, `y_test_seq.npy`.
- Saved initial shape assertions expect `(7968, 4, 21)`, `(2276, 4, 21)`, `(1139, 4, 21)`. These describe that prepared sequence dataset; different data require reviewing the assertions and alignment logic.
- Raw images and a writable crop cache; pretrained YOLO and timm model downloads may require network access.

Review `SPLIT_MODE` before execution and record it with your results. Use a clean kernel and rerun through final evaluation so source, output and saved weights describe the same experiment. Sequence-disjoint evaluation is needed to assess generalization beyond overlapping temporal windows; changing split mode produces a new experiment.

The crop function selects the largest detection with padding, falling back to the full image. It does not explicitly filter detections to the transmitting drone class; inspect crop quality before interpreting it as target localization.

## 4. Save a traceable run

Save the commit SHA, package versions, seed, split membership, class mapping, preprocessing statistics, checkpoint hash and per-sample predictions. Keep model selection on validation data and reserve test data for final evaluation. Report Top-k with sample counts and split mode. Do not compare remapped 29-class fusion outputs directly with 64/65-output baseline configurations.

## 5. Troubleshooting

| Symptom | Check |
| --- | --- |
| Missing CSV or image | Dataset roots, column order, path rewriting and index alignment |
| `ZIP_PATH` undefined | Define the local archive path or skip extraction for verified extracted data |
| Missing checkpoint | Run the corresponding training stage first; weights are not shipped |
| CUDA memory error | Reduce batch size and record the change in the run configuration |
| Figure exporter fails | Confirm saved PNG outputs exist; exporter identifies plot cells by source markers |
| Notebook filename or source says random, output says sequence | Outputs are stale relative to source; rerun the chosen protocol |
