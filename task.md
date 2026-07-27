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
