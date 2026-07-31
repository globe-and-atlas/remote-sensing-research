# GSIA preprint files

## Current version 3 submission package

Frozen, checksummed, and pinned to the immutable tag `gsia-v3-submission`
(commit `0d79cd1`). Version 3 is the current edition of the Atlas.

| File | Purpose | In deposit |
|---|---|---|
| [`gsia_preprint_v3_submission_2026-07-26.pdf`](gsia_preprint_v3_submission_2026-07-26.pdf) | Rendered submission manuscript | yes |
| [`gsia_preprint_v3_status_supplement_2026-07-25.csv`](gsia_preprint_v3_status_supplement_2026-07-25.csv) | Authoritative machine-readable status and method-specification supplement for all 91 records | yes |
| [`gsia_preprint_v2_erratum_2026-07-25.md`](gsia_preprint_v2_erratum_2026-07-25.md) | Version 2 to version 3 correction record | yes |
| [`../analysis/band-algebra/audit_summary.json`](../analysis/band-algebra/audit_summary.json) | Machine-readable audit summary and pinned source metadata | yes |
| [`../analysis/band-algebra/candidate_formula_space.csv`](../analysis/band-algebra/candidate_formula_space.csv) | Enumerated six-family candidate space | yes |
| [`../analysis/band-algebra/known_index_crosswalk.csv`](../analysis/band-algebra/known_index_crosswalk.csv) | Exact-equation established-index crosswalk | yes |
| [`../analysis/band-algebra/gsia_registry_applicability.csv`](../analysis/band-algebra/gsia_registry_applicability.csv) | Record-level applicability classification | yes |
| [`gsia_preprint_v3_submission_manuscript_2026-07-25.md`](gsia_preprint_v3_submission_manuscript_2026-07-25.md) | Current editable manuscript source | repo |
| [`gsia_preprint_v3_submission_manifest_2026-07-26.md`](gsia_preprint_v3_submission_manifest_2026-07-26.md) | Frozen package inventory, checksums, verification results, limits, and upload checklist | repo |
| [`../analysis/band-algebra/audit_report.md`](../analysis/band-algebra/audit_report.md) | Structural Sentinel-2 band-algebra methods, results, applicability, and limits | repo |
| [`../formulas/gsia-v2-formula-catalog.md`](../formulas/gsia-v2-formula-catalog.md) | Human-readable method-specification presentation of the same 91 governed records | repo |
| [`../scripts/audit_band_algebra.py`](../scripts/audit_band_algebra.py) | Reproducible structural-audit script | repo |
| [`../scripts/render_gsia_preprint.py`](../scripts/render_gsia_preprint.py) | Reproducible Markdown-to-PDF renderer | repo |
| [`../tests/test_band_algebra_audit.py`](../tests/test_band_algebra_audit.py) | Seven structural-audit regression tests | repo |
| [`../analysis/band-algebra/requirements.txt`](../analysis/band-algebra/requirements.txt) | Reference NumPy environment | repo |

The seven files marked `yes` belong in the archive deposit and are uploaded
together. Those marked `repo` are hosted here and cited from the manuscript
against the pinned tag. SHA-256 checksums for all fifteen are recorded in the
submission manifest.

The version 3 PDF has been rendered and visually verified. Every registry and structural-audit link in the manuscript is pinned to the immutable tag `gsia-v3-submission`, and all twelve resolve. The earlier `gsia-v3-preprint` tag predates corrections to the formula catalog and erratum and is retained unmoved for provenance only.

## Archival record and citation

Cite the archived code and registry through the Zenodo concept DOI
[10.5281/zenodo.20400743](https://doi.org/10.5281/zenodo.20400743), which always
resolves to the current edition. The version 1 record
[10.5281/zenodo.20400744](https://doi.org/10.5281/zenodo.20400744) is a permanent
version DOI and is retained as the historical pointer.

## Superseded version 2 package

The version 2 PDF, manuscript, supplement, and manifest are retained for provenance. Version 3 folds in the 25 July implementation corrections and 26 July structural audit, and supersedes version 2 as the current edition.

## Historical version 1

`gsia_preprint_v1.md` and `gsia_preprint_v1.pdf` are retained for provenance. Their catalog-wide novelty framing, T1/T2/T3 taxonomy, index count, formula names, and scientific status have been superseded and should not be cited as current.

## Publication boundary

This preprint package covers only the 91-record Global Spectral Index Atlas. Original Limn produced-water formulas, evidence, results, and case studies are outside scope.
