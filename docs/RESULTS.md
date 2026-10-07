# Results and reproducibility

## Evidence available in this repository

| Result | Source | Interpretation |
| --- | --- | --- |
| Position Top-1 57.594381% | Main notebook, saved `Position Test metrics` output | Recorded baseline run |
| Position + height Top-1 69.710272% | Main notebook, saved sensor evaluation | Recorded baseline run |
| Position + height + distance Top-1 74.187884% | Main notebook, saved sensor evaluation | Recorded baseline run |
| Initial image Top-1 87.620720% | Main notebook, saved image evaluation | Pre-refinement checkpoint |
| Refined image Top-1 88.3231% | `generate_ieee_comparison_figure.py` and existing `IEEE_FINDINGS_COMPARISON.md` | Reported refinement value; not newly recomputed from weights |
| Final ConvNeXt fusion scores | No completed final evaluation output in the reviewed fusion notebook | Not promoted as a verified benchmark |

The README summary is also available as [CSV](../results/baseline_metrics.csv). Summary plots draw from recorded numbers; diagnostic plots are extracted from saved notebook outputs without rerunning training. The gallery's initial image plot remains explicitly labelled as pre-refinement.

## Comparability

The existing baseline report records 6,832 training, 3,416 validation and 1,139 test samples for the position family, with 617 missing height/distance file pairs filled using training medians. The reference study used a different split and a 32-beam problem, while existing baseline output heads have 64 or 65 units. Do not label the difference between their accuracies as a controlled gain or state-of-the-art result.

The reviewed ConvNeXt notebook uses a remapped label space (29 classes in saved preparation output) and length-four sequences with 21 position features. Its source currently selects `random_stratified` but the saved output reports `sequence`. It also contains an extraction error and lacks completed final training/evaluation outputs. Do not infer a completed random-split result from its filename.

Randomly splitting overlapping windows can place shared context across train, validation and test sets. Disjoint row indices alone do not establish temporal independence. Preserve sequence identities and audit shared observations when evaluating generalization.

## What the metrics do and do not show

Top-k accuracy measures ground-truth beam membership in the k highest-ranked predictions. Candidate ranking is useful for studying search reduction, but accuracy alone does not establish measured beam-training overhead savings, throughput, field robustness or deployment latency. No statistical superiority or cross-scenario generalization claim is made here.

The baseline metrics are saved single-run observations; confidence intervals and repeated-seed summaries are not included. The submitted manuscript was not available during this documentation pass, so its exact title, author list, method naming and final result tables have not been inferred from notebook filenames.

## Documentation pass validation

This update preserves experimental notebook contents and the inherited license. It repairs diagnostic export matching, commits previously missing figure assets, and adds navigation, architecture documentation and setup notes. Summary figure generation and all ten saved diagnostic exports are checked locally. Full model training is not rerun; data and checkpoints are external.
