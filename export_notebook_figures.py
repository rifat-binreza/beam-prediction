"""Export recorded diagnostic PNGs; never execute or train the notebook."""
import base64
import json
from pathlib import Path

NOTEBOOK = Path("beam_predict_final_paper.ipynb")
OUTPUT_DIR = Path("figures/notebook_diagnostics")
# Match distinctive code rather than cell numbers, which drift after edits.
PLOT_MARKERS = {
    "initial_image_model_test_accuracy": 'image_topk_labels =',
    "position_training_loss": 'hist_pos_df = pd.DataFrame(history_pos)',
    "position_validation_accuracy": 'plt.plot(hist_pos_df["epoch"], hist_pos_df["top1"]',
    "position_test_accuracy": 'pos_metrics = {',
    "position_confusion_matrix": 'y_true_pos = []',
    "position_height_training_validation_test": 'axes[0].plot(history_pos_h["epoch"]',
    "position_height_confusion_matrix": 'y_true_pos_h, y_pred_pos_h = [], []',
    "position_height_distance_training_validation_test": 'axes[0].plot(history_pos_h_d["epoch"]',
    "position_height_distance_confusion_matrix": 'y_true_pos_h_d, y_pred_pos_h_d = [], []',
    "position_modality_test_accuracy_comparison": 'position_modality_results = pd.concat(',
}


def main():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    images = {}
    for name, marker in PLOT_MARKERS.items():
        matches = [cell for cell in notebook["cells"]
                   if cell.get("cell_type") == "code"
                   and marker in "".join(cell.get("source", []))]
        if len(matches) != 1:
            raise ValueError(f"{name}: expected one matching code cell, found {len(matches)}")
        pngs = [output.get("data", {}).get("image/png")
                for output in matches[0].get("outputs", [])
                if output.get("data", {}).get("image/png")]
        if len(pngs) != 1:
            raise ValueError(f"{name}: expected one saved PNG, found {len(pngs)}")
        encoded = "".join(pngs[0]) if isinstance(pngs[0], list) else pngs[0]
        images[name] = base64.b64decode(encoded)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, image in images.items():
        path = OUTPUT_DIR / f"{name}.png"
        path.write_bytes(image)
        print(f"Saved {path}")
    print(f"Exported {len(images)} saved diagnostics; no model execution.")


if __name__ == "__main__":
    main()
