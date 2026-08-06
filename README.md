# Remote Sensing Research

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20400743.svg)](https://doi.org/10.5281/zenodo.20400743)

**Globe & Atlas** | Open, inspectable environmental remote-sensing research.

This repository is the technical Atlas counterpart to the [Globe & Atlas](https://globeandatlas.substack.com) publication. It documents proposed formulas, implemented screening proxies, required inputs, physical rationales, implementation maturity, calibration and validation status, and intended-use/inference-limit statements. Confounders are addressed mainly at the domain and study-design levels rather than exhaustively itemized for every record.

The Global Spectral Index Atlas version 3 is a registry of **24 capability families comprising 91 governed method-specification records across 12 domains**. The record count is an inventory measure, not a claim of 91 unique band combinations, scientifically unprecedented equations, or validated detectors.

## Start here

| Resource | Purpose |
|---|---|
| **[Version 3 preprint PDF](preprint/gsia_preprint_v3_submission_2026-07-26.pdf)** | Rendered pre-submission manuscript |
| **[Version 3 manuscript source](preprint/gsia_preprint_v3_submission_manuscript_2026-07-25.md)** | Current pre-submission manuscript, including implementation corrections and the structural band-algebra audit |
| **[Version 3 submission manifest](preprint/gsia_preprint_v3_submission_manifest_2026-07-26.md)** | Package checksums, completed verification, claim limits, and final upload actions |
| **[Version 3 machine-readable supplement](preprint/gsia_preprint_v3_status_supplement_2026-07-25.csv)** | Authoritative 91-record table with formula, role, maturity, inputs, operators, limits, and audit metadata |
| **[GSIA method-specification catalog](formulas/gsia-v2-formula-catalog.md)** | Human-readable reference for all 91 proposed methods and their implementation status, organized by capability family |
| **[Structural band-algebra audit](analysis/band-algebra/audit_report.md)** | Reproducible Sentinel-2 formula-space counts, established-index crosswalk, GSIA applicability, and claim limits |
| **[Version 2 to version 3 erratum](preprint/gsia_preprint_v2_erratum_2026-07-25.md)** | Corrections to declared sensors, formulas, rationale, radiometry, and provenance |
| **Audited Atlas source** | Version 3 commit `fd00b890c16105d2e011f85d9e182ec5b709ab57`, since made private; a byte-identical public Atlas-only copy of 21 relevant registry, evalscript, evidence, audit, and test files is tagged [`gsia-v3-audit`](https://github.com/globe-and-atlas/limn-atlas/tree/gsia-v3-audit) at commit `dd12f3c8e2e987480e2811599da0a11e6a23ec24` |

The CSV is the governed source for the readable formula catalog. Regenerate the catalog with:

```bash
python3 scripts/generate_gsia_v2_formula_catalog.py \
  preprint/gsia_preprint_v3_status_supplement_2026-07-25.csv \
  formulas/gsia-v2-formula-catalog.md
```

## Version 3 pre-submission status

| Dimension | Version 3 distribution |
|---|---|
| Registry | 91 records; 12 domains; 24 capability families |
| Maturity | 37 M3 live screening proxies; 16 M2 executable non-live formulas; 38 M1 specified concepts or retired formulas |
| Method roles | 15 primary; 10 variant; 12 component; 1 reference; 51 research-model; 2 retired |
| Contribution classes | 68 C1; 22 C2; 1 C3, all provisional pending entry-level prior-art review |
| Independent evaluation | 0 V1; 0 V2 |

The software release audit found that all 37 renderable evalscripts passed band-declaration and output-shape checks. A fresh WMS audit returned a nonblank display for all 37 under the recorded settings, and 42 of 42 live/demo evidence packs met the repository's source-coverage rule. These are software, display, and provenance results—not environmental accuracy results.

The version 3 structural audit enumerates six bounded formula families. The full 13-band Sentinel-2 MSI space contains 1,079 unordered two- to four-band sets and 15,054 role-specific expressions; a ten-band reflected-surface core contains 375 sets, 4,770 expressions, and 2,340 information classes after direction and monotonic-equivalence rules. A pinned established-index catalog produced 71 exact named matches representing 48 distinct equations. These are structural and provenance results—not index-discovery, novelty, or environmental-performance results.

Reproduce the structural audit with:

```bash
python3 -m pip install -r analysis/band-algebra/requirements.txt
python3 scripts/audit_band_algebra.py
python3 -m unittest tests/test_band_algebra_audit.py
```

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
- The 91-record count is registry inventory, not a count of unique band sets, unique equations, or established inventions.
- Event documentation and bookmarked views are provenance, not target labels or matched controls.
- Display quality is not sensitivity, specificity, calibration, transferability, or causal attribution.
- Some proposed workflows require atmospheric correction, temporal comparison, spatial operators, inversion, field calibration, or ancillary data not present in a current live script.
- High-consequence decisions require field evidence, domain review, uncertainty analysis, and independent evaluation.

This Atlas publication scope is separate from the original Limn produced-water investigation. Produced-water formulas, evidence, results, and case studies are not part of the 91-record GSIA release or its preprint.

## Historical version 1 documents

The following files are preserved for provenance but use the superseded May 2026 T1/T2/T3 framing and should not be cited as the current scientific status:

- [`ATLAS.md`](ATLAS.md)
- [`registry/master_index_catalog.md`](registry/master_index_catalog.md)
- [`registry/comparative_analysis.md`](registry/comparative_analysis.md)
- [`formulas/formula-quick-reference.md`](formulas/formula-quick-reference.md)
- [`preprint/gsia_preprint_v1.md`](preprint/gsia_preprint_v1.md)
- [`preprint/gsia_preprint_v1.pdf`](preprint/gsia_preprint_v1.pdf)

Use the current v3 status supplement and governed formula catalog for formulas, maturity, contribution, and validation statements.

## Citation and reuse

Please cite both the Atlas release and the underlying scientific sources identified for the method being used. Reuse of a proposed formula does not convert it into a validated detector; document the exact version, preprocessing, thresholds, calibration data, and domain of applicability.

**Suggested citation:** Bally, D. (2026). *The Global Spectral Index Atlas: An Open Registry of Environmental Remote-Sensing Method Specifications Across Twelve Domains*. ESS Open Archive preprint, version 3.

### Persistent identifiers

| Resource | Identifier |
|---|---|
| Preprint, version 3 (current published) | [10.22541/essoar.15004217/v3](https://doi.org/10.22541/essoar.15004217/v3) |
| Preprint, version 2 | [10.22541/essoar.15004217/v2](https://doi.org/10.22541/essoar.15004217/v2) |
| Preprint, version 1 | [10.22541/essoar.15004217/v1](https://doi.org/10.22541/essoar.15004217/v1) |
| Archived code and registry (current edition) | [10.5281/zenodo.20400743](https://doi.org/10.5281/zenodo.20400743) |
| Archived code, version 1.0.0 | [10.5281/zenodo.20400744](https://doi.org/10.5281/zenodo.20400744) |
| Archived code, version 1.0.1 | [10.5281/zenodo.20401605](https://doi.org/10.5281/zenodo.20401605) |

Cite the DOIs rather than `essopenarchive.org/doc/...` URLs, which are working
links that change between revisions. Each preprint version carries its own DOI;
there is no version-agnostic preprint DOI. The Zenodo concept DOI
`10.5281/zenodo.20400743` always resolves to the current archived edition.

## License

This repository is dual-licensed:

| Material | License | File |
|---|---|---|
| Manuscript, ATLAS catalog, registry, formula catalog, and documentation | CC BY 4.0 | [`LICENSE`](LICENSE) |
| First-party source code, including `scripts/` and `tests/` | MIT | [`LICENSE-CODE`](LICENSE-CODE) |

Both require attribution. Third-party data products, satellite imagery, and
referenced catalogs retain their own licenses and are not relicensed here.

Reuse of a proposed formula does not convert it into a validated detector. No
record in this registry has completed independent held-out accuracy assessment.

---

*Published by [Globe & Atlas](https://globeandatlas.substack.com) | Version 3 submission documentation updated July 2026*
