# GSIA preprint version 2 submission manifest

**Prepared:** 21 July 2026  
**Publication boundary:** Global Spectral Index Atlas only. Produced-water Limn formulas, gates, evidence, results, and case studies are excluded.  
**Audited Atlas source:** `e50c2eda5cf405c7693e5210e04894c691e5f2eb`

## Submission and companion files

| File | Purpose | SHA-256 |
|---|---|---|
| `gsia_preprint_v2_submission_2026-07-21.pdf` | Submission manuscript PDF | `98473d6e2c525b87d945078c0e59ff86ab78c87c160242edfe1f03927c863ab1` |
| `gsia_preprint_v2_submission_manuscript_2026-07-21.md` | Editable manuscript source | `8635907398d587c7ae863447578d1701b91bd2fd947acf89b8c9f46fae86f9db` |
| `gsia_preprint_v2_status_supplement_2026-07-21.csv` | Machine-readable 91-record status supplement | `ab3b6df11639e397fb2b7c093595288c5714e61b2be0dd042a5c484933169f8c` |
| `../formulas/gsia-v2-formula-catalog.md` | Human-readable catalog generated from the 91-record supplement | `567a3d1ce6f92b299d1166bc74f7a2795bdee0794949b83d1bc5971719bce3af` |

## Frozen scientific inventory

- 91 unique registry records across 12 domains and 24 capability families.
- Maturity: 37 M3 live screening proxies, 16 M2 executable non-live formulas, and 38 M1 specified concepts or retired formulas.
- Method roles: 15 primary, 10 variant, 12 component, 1 reference, 51 research-model, and 2 retired.
- Provisional contribution classes: 68 C1, 22 C2, and 1 C3.
- Formula schema: version 2.0 for all 91 records.
- Validation status: all 91 remain below V1 independent evaluation.
- Retirements: SF-EII and AMDPHI are M1, non-renderable, and retained only for traceability.
- LFMPI: M3 primary normalized NDMI-deficit screening proxy with live-vegetation and water-rejection gates; not percent LFMC, ignition probability, or fire danger.

## Verification completed

- Atlas formula-schema, retirement, and live-formula reconciliation tests passed.
- Capability-family hierarchy and family-first interface tests passed.
- Focused LFMPI water-rejection and live-vegetation-gate tests passed.
- 37 renderable evalscripts audited; 0 band-declaration or output-shape flags.
- Fresh WMS audit returned 37 nonblank overlays meeting the automated strong-display criterion under the recorded audit settings.
- 42 of 42 live/demo evidence packs met the three-reachable-source rule.
- Submission consistency checker passed: counts, identifiers, family/role metadata, formula versions, retirements, LFMPI formula, snapshot hash, and scope boundary.
- Human-readable catalog regenerated deterministically from the governed CSV: 91 records, 24 capability families, and one unique anchor and proposed formula per record.
- All 19 DOI links resolved without 404, 410, or server-error responses; four publisher endpoints returned access-control 403 after successful DOI resolution.
- PDF text extraction passed on all 16 pages; required claims and snapshot identifier are present and no out-of-scope terms were found.
- All 16 rendered pages were visually inspected. No clipping, overlap, broken tables, missing pages, or unreadable references were observed.

## Interpretation limits preserved

- Formula, schema, rendering, display, and link checks are software or provenance results, not environmental accuracy results.
- A Gold-ready evidence pack documents an event or domain context; it does not provide pixel labels, causal attribution, or a matched control.
- A strong overlay is visually legible under the tested WMS request; it is not evidence of sensitivity, specificity, calibration, transferability, or operational reliability.
- Contribution classes and method roles organize the registry. They do not establish scientific priority.
- The renderable evalscript audit covers 37 live records, not every external workflow represented by the 54 non-live records.

## Author-controlled pre-upload checks

- Confirm author name, affiliation, correspondence address, license, and competing-interest statement.
- Upload the PDF and CSV together as version 2 and retain the Markdown source and readable formula catalog in the project archive.
- Confirm that the ESS Open Archive version selector, date, and citation display identify the upload as version 2.
- Archive or attach this exact supplement and preserve the audited commit link so the reported snapshot remains reproducible.
