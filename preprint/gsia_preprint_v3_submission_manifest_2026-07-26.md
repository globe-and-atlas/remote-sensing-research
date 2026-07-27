# GSIA preprint version 3 submission manifest

**Prepared:** 27 July 2026<br>
**Status:** Pre-submission package; final immutable repository tag not yet created  
**Publication boundary:** Global Spectral Index Atlas only. Produced-water Limn formulas, gates, evidence, results, and case studies are excluded.  
**Audited Atlas source:** `fd00b890c16105d2e011f85d9e182ec5b709ab57`, tagged `gsia-v3-audit` in the implementation repository  
**Public audited-source copy:** `dd12f3c8e2e987480e2811599da0a11e6a23ec24`, tag `gsia-v3-audit`, in `globe-and-atlas/limn-atlas`

## Submission and companion files

| File | Purpose | SHA-256 |
|---|---|---|
| `gsia_preprint_v3_submission_2026-07-26.pdf` | Rendered pre-submission manuscript | `98d42716d210f7c338e8697f6a0a22ead564e5a96a23107f313ff07f0f5a02e0` |
| `gsia_preprint_v3_submission_manuscript_2026-07-25.md` | Editable manuscript source | `04199f3ca0c25521cbb93dccd9d411f3f5bb646f307c4408a24ac741d2a1b524` |
| `gsia_preprint_v3_status_supplement_2026-07-25.csv` | Machine-readable 91-record status supplement | `250ca9a220a8b577e78731c372cc5e55882eab9a520e10a520a38eae73ff10e5` |
| `gsia_preprint_v2_erratum_2026-07-25.md` | Version 2 correction ledger carried into version 3 | `aeceeec7634a42a0387d44e6c72ba0ac5b74ed306914f2dd45d9f56ef0179471` |
| `../formulas/gsia-v2-formula-catalog.md` | Human-readable formula-schema v2.0 catalog generated from the version 3 supplement | `974bfc731b80c347921c6580f63a08c6b01d559689ea9b7aa391986a539536ea` |
| `../scripts/audit_band_algebra.py` | Reproducible structural-audit script | `2ad849e723233c3e4b8814bf496d78ee36a81f2b9f3682e5b022dfca5c01dd59` |
| `../scripts/render_gsia_preprint.py` | Reproducible Markdown-to-PDF renderer | `33f62727ba2104e3af8b5324edc1cfd3d4a66aefb56e94402e85bb08207a469e` |
| `../tests/test_band_algebra_audit.py` | Seven structural-audit regression tests | `d5944e52eb7a1c9277bef1095bdb90eff4b999ade859a6b74a899669d4778eef` |
| `../analysis/band-algebra/audit_report.md` | Human-readable structural methods, results, and limits | `314fad8cb8a6cbc65d63e9440cb0751d4ac5c230963c556e020957278dbeef3c` |
| `../analysis/band-algebra/audit_summary.json` | Machine-readable counts, environment, and pinned-source metadata | `c7bd179f668714ac5b29de3230c98dafdff2e6a5263c42bd148ad7f1e68dd622` |
| `../analysis/band-algebra/candidate_formula_space.csv` | 19,824 enumerated full-instrument and surface-core expressions | `ea1c250b97daed290d6da6746c01e2a3fe57b2205f0644460f6e13ead5f22a60` |
| `../analysis/band-algebra/known_index_crosswalk.csv` | 71 exact named matches representing 48 signed equations | `1f6d992a28a9ed8bd87faaef8bc67825f66a90023e1b149cc39b73e40a93d8d3` |
| `../analysis/band-algebra/gsia_registry_applicability.csv` | Applicability classification for all 91 GSIA records | `1c90d93dd4bc13c257bacb4984fd5cc717fbc6a2e253c3c6dc92177e2a99b5df` |
| `../analysis/band-algebra/requirements.txt` | Reference NumPy environment | `d322e88b2f6367f38a2e81d44d4aff471f0f8d14bb04aa5b9d0ddd6c9a5f7694` |

## Frozen scientific inventory

- 24 capability families comprising 91 governed method-specification records across 12 domains.
- Maturity: 37 M3 live screening proxies, 16 M2 executable non-live formulas, and 38 M1 specified concepts or retired formulas.
- Method roles: 15 primary, 10 variant, 12 component, 1 reference, 51 research-model, and 2 retired.
- Provisional contribution classes: 68 C1, 22 C2, and 1 C3.
- Validation status: all 91 remain below V1 independent evaluation.
- Full Sentinel-2 MSI search: 1,079 unordered two- to four-band sets; 15,054 role-specific expressions; 7,527 direction-neutral classes; 7,449 information classes.
- Ten-band reflected-surface core: 375 sets; 4,770 expressions; 2,385 direction-neutral classes; 2,340 information classes.
- Established-index crosswalk: 280 catalog records; 185 eligible pure-band Sentinel-2 entries; 71 exact named matches; 48 distinct signed equations.
- GSIA applicability: 1 direct six-family match; 1 direct formula outside the six families; 33 component or ablation comparisons; 1 manual review; 55 not directly applicable.

## Verification completed

- Seven structural-audit unit tests passed.
- The formula catalog regenerated successfully from the version 3 supplement: 91 records in 24 capability families.
- All 91 records contain an intended-use/inference-limit field, but its specificity varies; confounders are addressed mainly at domain and study-design levels rather than through a dedicated field for every record.
- The candidate table contains 19,824 data rows, the established-index crosswalk 71 data rows, the GSIA applicability table 91 data rows, and the status supplement 91 data rows.
- Crossref metadata was checked for all 20 DOI-bearing bibliography entries; the two Zenodo records were checked through DataCite and the Zenodo API.
- Twenty-one Atlas source, audit, and test files were confirmed byte-identical between the private audited snapshot and the public `limn-atlas` tag. The private COG renderer and offset regression test are absent from that public copy, and the manuscript now states that reproducibility limit explicitly.
- PDF text extraction contains the version 3 citation, structural counts, applicability findings, and new references, with no template or tool tokens.
- The 19-page letter-size PDF was rendered to PNG and visually inspected across complete and focused review passes. No clipping, overlap, broken tables, missing pages, or unreadable references were observed.
- PDF metadata identifies version 3 and Daniel Bally.

## Interpretation limits preserved

- Enumeration and exact-equation matching do not establish environmental usefulness, scientific novelty, or performance.
- The 91-record count is registry inventory, not a count of unique band sets, unique equations, or established inventions.
- The six formula families are deliberately bounded and do not represent all spectral-index algebra.
- The Awesome Spectral Indices snapshot is pinned but not exhaustive; absence of a match is not evidence of novelty.
- Ratio and normalized-difference information classes share monotonic information for positive reflectance but do not have interchangeable scales, noise behavior, or thresholds.
- The ten-band reflected-surface core is a search-design choice, not a universal exclusion rule for B01, B09, or B10.
- Formula, schema, rendering, display, and link checks remain software, structural, or provenance results rather than environmental accuracy results.

## Final pre-upload actions

- Review the author name, affiliation, correspondence address, license, competing-interest statement, and AI-assistance disclosure.
- Commit the complete version 3 package and create a new immutable submission tag; do not move or overwrite the earlier `gsia-v3-preprint` tag.
- Update the pre-submission structural-audit links to the new immutable tag and confirm each resolves publicly.
- Recompute this manifest if any hashed file changes.
- Upload the PDF, 91-record supplement, audit summary, formula-space table, established-index crosswalk, and GSIA applicability table together.
- Confirm that ESS Open Archive displays the revision as version 3.
