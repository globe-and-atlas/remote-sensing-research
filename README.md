# Remote Sensing Research

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20400743.svg)](https://doi.org/10.5281/zenodo.20400743)

**Globe & Atlas** | Open, inspectable environmental remote-sensing research.

This repository is the technical Atlas counterpart to the [Globe & Atlas](https://globeandatlas.substack.com) publication. It documents proposed formulas, implemented screening proxies, required inputs, physical rationales, confounders, maturity, and validation limits.

The Global Spectral Index Atlas version 2 is a registry of **91 proposed specifications across 12 domains and 24 capability families**. It is not a collection of 91 validated detectors, and it does not assert that all 91 formulas are scientifically unprecedented.

## Start here

| Resource | Purpose |
|---|---|
| **[GSIA v2 Formula Catalog](formulas/gsia-v2-formula-catalog.md)** | Human-readable reference for all 91 proposed and implemented formulas, organized by capability family |
| **[Machine-readable supplement](preprint/gsia_preprint_v2_status_supplement_2026-07-21.csv)** | Authoritative 91-record release table with formula, role, maturity, inputs, operators, limits, and audit metadata |
| **[Version 2 preprint PDF](preprint/gsia_preprint_v2_submission_2026-07-21.pdf)** | Submission manuscript |
| **[Version 2 manuscript source](preprint/gsia_preprint_v2_submission_manuscript_2026-07-21.md)** | Editable preprint source |
| **[Submission manifest](preprint/gsia_preprint_v2_submission_manifest_2026-07-21.md)** | Frozen inventory, verification results, and checksums |
| **Audited Atlas source** | Commit `e50c2eda5cf405c7693e5210e04894c691e5f2eb`, since made private; the public Atlas viewer is now maintained at [globe-and-atlas/limn-atlas](https://github.com/globe-and-atlas/limn-atlas) |

The CSV is the governed source for the readable formula catalog. Regenerate the catalog with:

```bash
python3 scripts/generate_gsia_v2_formula_catalog.py \
  preprint/gsia_preprint_v2_status_supplement_2026-07-21.csv \
  formulas/gsia-v2-formula-catalog.md
```

## Release status

| Dimension | Version 2 distribution |
|---|---|
| Registry | 91 records; 12 domains; 24 capability families |
| Maturity | 37 M3 live screening proxies; 16 M2 executable non-live formulas; 38 M1 specified concepts or retired formulas |
| Method roles | 15 primary; 10 variant; 12 component; 1 reference; 51 research-model; 2 retired |
| Contribution classes | 68 C1; 22 C2; 1 C3, all provisional pending entry-level prior-art review |
| Independent evaluation | 0 V1; 0 V2 |

The software release audit found that all 37 renderable evalscripts passed band-declaration and output-shape checks. A fresh WMS audit returned a nonblank display for all 37 under the recorded settings, and 42 of 42 live/demo evidence packs met the repository's source-coverage rule. These are software, display, and provenance results—not environmental accuracy results.

## Status vocabulary

### Maturity

- **M1 - Formula specified:** inputs and an equation or workflow are documented.
- **M2 - Executable:** entry-specific code exists but is not a live Atlas layer.
- **M3 - Demonstrated:** a reviewed Atlas rendering exists with event or domain context.
- **V1 - Independently evaluated:** a locked method has labeled positives, hard negatives, held-out geography or time, uncertainty, and task-appropriate metrics.
- **V2 - Externally replicated:** an independent dataset, analyst, or team reproduces useful performance.

M3 does not imply accuracy. No current GSIA record reaches V1.

### Method roles

- **Primary:** clearest current representative of a capability family; not a validated winner.
- **Variant:** alternate formulation or interpretation in the same family.
- **Component:** useful input or context feature that is weaker as a standalone decision product.
- **Reference:** established sensor product retained for interpretation.
- **Research model:** future retrieval, calibration, temporal, spatial, or cross-sensor workflow.
- **Retired:** legacy formula retained for traceability but removed from live scientific use.

### Contribution classes

- **C1 - Proposed formulation**
- **C2 - Adapted formalization**
- **C3 - Sensor-enabled implementation concept**

These classes are provisional organizational metadata. They do not establish priority, patentability, novelty, or performance.

## Domains

| Domain | Records |
|---|---:|
| Wildfire and post-fire | 7 |
| Water quality and freshwater | 11 |
| Marine and coastal | 10 |
| Agriculture and food | 7 |
| Mining and industrial | 8 |
| Urban and infrastructure | 8 |
| Permafrost and Arctic | 7 |
| Tropical forest | 6 |
| Dryland and arid | 6 |
| Wetland and peatland | 6 |
| Hyperspectral-enabled | 8 |
| Cross-sensor fusion | 7 |
| **Total** | **91** |

## Scientific boundaries

- A formula is not equivalent to the environmental conclusion named in a use case.
- Event documentation and bookmarked views are provenance, not target labels or matched controls.
- Display quality is not sensitivity, specificity, calibration, transferability, or causal attribution.
- Some proposed workflows require atmospheric correction, temporal comparison, spatial operators, inversion, field calibration, or ancillary data not present in a current live script.
- High-consequence decisions require field evidence, domain review, uncertainty analysis, and independent evaluation.

This Atlas publication scope is separate from the original Limn produced-water investigation. Produced-water formulas, evidence, results, and case studies are not part of the 91-record GSIA release or its preprint.

## Historical version 1 documents

The following files are preserved for provenance but use the superseded May 2026 T1/T2/T3 framing and should not be cited as the current scientific status:

- [`ATLAS.md`](ATLAS.md)
- [`registry/master_index_catalog.md`](registry/master_index_catalog.md)
- [`formulas/formula-quick-reference.md`](formulas/formula-quick-reference.md)
- [`preprint/gsia_preprint_v1.md`](preprint/gsia_preprint_v1.md)
- [`preprint/gsia_preprint_v1.pdf`](preprint/gsia_preprint_v1.pdf)

Use the v2 formula catalog and governed CSV for current formulas, maturity, contribution, and validation statements.

## Citation and reuse

Please cite both the Atlas release and the underlying scientific sources identified for the method being used. Reuse of a proposed formula does not convert it into a validated detector; document the exact version, preprocessing, thresholds, calibration data, and domain of applicability.

**Suggested citation:** Bally, D. (2026). *The Global Spectral Index Atlas: An Open Catalog of Proposed Environmental Remote-Sensing Index Specifications Across Twelve Domains*. ESS Open Archive preprint, version 2.

Repository code and third-party data products retain their respective licenses. The manuscript and Atlas documentation are released under CC BY 4.0 unless otherwise noted.

---

*Published by [Globe & Atlas](https://globeandatlas.substack.com) | Version 2 documentation updated July 2026*
