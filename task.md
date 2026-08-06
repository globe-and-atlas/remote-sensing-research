# Tasks — Unification of Catalogs and Surveys

- [x] Create the `registry/` directory inside `remote-sensing-research`
- [x] Build `registry/sensor_platforms.md` by merging the 31 satellite platforms survey and integration roadmaps
- [x] Build `registry/master_index_catalog.md` by unifying the 53 Limn indices, the 18 Sentinel-2 composites, and the 91 global novel indices into a single indexed master database
- [x] Build `registry/scholarly_synthesis.md` by unifying prior art analysis, validation roadmaps, ethical safeguards, and claims policies
- [x] Write and run `verify_registry.py` to automatically validate registry integrity (clean math operators, zero duplicates, no broken links)
- [x] Delete/cleanup the redundant `surveys/` and `catalogs/` directories
- [x] Verify repository Git status (ensuring untracked files are correct and `ATLAS.private.md` remains gitignored)

## Sentinel-2 Band-Algebra Audit

- [x] Separate the 13-band full-instrument count from a 10-band reflected-surface core
- [x] Enumerate six bounded 2–4 band formula families with deterministic role ordering
- [x] Canonicalize direction/sign variants and ratio/normalized-difference information classes
- [x] Crosswalk exact equations against a pinned Awesome Spectral Indices snapshot
- [x] Classify all 91 GSIA records by direct, component, manual, or non-applicable permutation scope
- [x] Generate a technical report, full candidate table, GSIA applicability table, known-index crosswalk, G&A article draft, LinkedIn draft, and publication graphic
- [ ] Run a target-specific empirical benchmark with independent labels, hard negatives, and geographic or temporal holdouts

## GSIA v3 Submission and Closeout

Package frozen at tag `gsia-v3-submission` (commit `0d79cd1`). Checksums in
`preprint/gsia_preprint_v3_submission_manifest_2026-07-26.md`.

### Completed 2026-07-30

- [x] Repository carries a LICENSE file detectable by GitHub
- [x] Content is licensed CC BY 4.0
- [x] First-party code is licensed MIT in LICENSE-CODE
- [x] The v1.0.1 draft release is removed from GitHub
- [x] The tag `v1.0.1` remains present on the public remote
- [x] A GitHub release exists on tag `gsia-v3-submission`
- [x] Zenodo concept DOI `10.5281/zenodo.20400743` resolves to the v3 snapshot
- [x] The Zenodo update guide names `...20400743` as the concept DOI

### Phase B — ESS Open Archive v3 (manual, essopenarchive.org)

- [x] The submission is filed as a revision to record `007f7377-d063-474f-9ba0-d776c927729e`
- [x] `gsia_preprint_v3_submission_2026-07-26.pdf` is uploaded
- [x] `gsia_preprint_v3_status_supplement_2026-07-25.csv` is uploaded
- [x] `gsia_preprint_v2_erratum_2026-07-25.md` is uploaded
- [x] `analysis/band-algebra/audit_summary.json` is uploaded
- [x] `analysis/band-algebra/candidate_formula_space.csv` is uploaded
- [x] `analysis/band-algebra/known_index_crosswalk.csv` is uploaded
- [x] `analysis/band-algebra/gsia_registry_applicability.csv` is uploaded
- [x] The license field is set to CC BY 4.0
- [x] The author name is reviewed
- [x] The affiliation is reviewed
- [x] The correspondence address is reviewed
- [x] The competing-interest statement is reviewed
- [x] The AI-assistance disclosure is reviewed
- [x] Submitted 2026-07-31; in moderation. Preprint DOI `10.22541/essoar.15004217/v3` minted
- [x] The record displays as version 3 once moderation clears — confirmed live 2026-08-05, posted date "5 August 2026"

### Phase C — Closeout (after v3 is live)

- [x] `preprint/README.md` states the v3 record is deposited
- [x] `preprint/README.md` carries the live v3 record link
- [x] `README.md` persistent-identifier table lists the v3 preprint DOI
- [x] The GitHub homepage field points at the v3 preprint DOI
- [x] `knowledge/SESSION.md` records the v3 submission checkpoint
- [x] `knowledge/DECISIONS.md` records the dual-license decision
- [x] `python3 /Users/danielbally/Git/.agent/scripts/session_capture.py` has been run
- [x] The submission manifest is left unmodified

**Do not amend the manifest.** It is the frozen checksummed record of what was
submitted; correcting it after the fact defeats its purpose.
