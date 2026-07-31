# Architecture & Design Decisions

This document records key structural, governance, and mathematical decisions made during the evolution of the Global Spectral Index Atlas (GSIA) repository.

---

## 1. Registry Unification Structure
* **Decision**: Consolidate disparate surveys, lists, and catalog files (e.g., `surveys/`, `catalogs/`) into a single, cohesive `registry/` directory with a standardized naming structure.
* **Date**: May 25, 2026
* **Rationale**: Prior to consolidation, indices and satellite specifications were scattered across redundant markdown sheets, leading to diverging definitions. By creating a unified `registry/` folder, we establish:
  * `master_index_catalog.md`: The single source of truth indexing all 116 formulas.
  * `comparative_analysis.md`: Detailed baseline comparative reviews for the Top 25 priority indices.
  * `sensor_platforms.md`: Core orbital band specs and integration roadmaps.
  * `scholarly_synthesis.md`: Governance, validation methods, and scientific claims.
* **Alternatives Considered**: Keeping domain directories separate. Rejected because of the high maintenance overhead of synchronized band names across files.

---

## 2. Public vs. Private Atlas Segregation
* **Decision**: Maintain a public `ATLAS.md` file for the repository open-source community, while retaining a private `ATLAS.private.md` file containing private coordinates, draft indices, and proprietary authorship details. Keep `ATLAS.private.md` strictly gitignored.
* **Date**: May 26, 2026
* **Rationale**: Daniel Bally's primary authorship details, sensitive validation sites in the Permian Basin, and early-stage experimental formulas must not leak into the public domain before they are patented or formally peer-reviewed.
* **Rule**: Ensure absolute parity of the core formulas and names between public and private files. Run automated verification to verify that no private data is accidentally committed.

---

## 3. Global Acronym Renaming (SMADI & NPDDI Conflicts)
* **Decision**: Globally rename `SMADI` (Sargassum vs. Microplastic Discrimination Index) to `SMPDI` and `NPDDI` (Nitrogen vs. Phosphorus Deficiency Discrimination Index) to `NPDefI` across all code, directories, index catalogs, and preprint drafts.
* **Date**: May 26, 2026
* **Rationale**: A comprehensive scholarly audit revealed naming collisions in established remote sensing catalogs:
  * `SMADI` conflicted with the *Soil Moisture Agricultural Drought Index*.
  * `NPDDI` conflicted with the *Normalized Polarization Degree Difference Index* (used in atmospheric cloud-masking).
  To ensure seamless integration with the Google Earth Engine *Awesome Spectral Indices* library, unique acronyms are mandatory.
* **Impact**: All YAML, markdown reference files, and formula cheat sheets have been systematically updated to `SMPDI` and `NPDefI`.

---

## 4. GEE-Compatible ASCII-Only Code Blocks
* **Decision**: Mandate strict ASCII operators in all mathematical code blocks (`-`, `*`, `**2`, `**3`) instead of unicode characters (`−`, `×`, `²`, `³`).
* **Date**: May 26, 2026
* **Rationale**: Although unicode looks cleaner in visual documents, it crashes typical programmatic Earth Engine and Python parsers. In addition, regex formatting pipelines often misinterpret exponents if they are not explicitly represented in standard programming notation.


---

## 5. Dual License: CC BY 4.0 for Content, MIT for Code
* **Decision**: Add `LICENSE` (CC BY 4.0) covering the manuscript, ATLAS catalog, registry, formula catalog, and documentation, and `LICENSE-CODE` (MIT) covering first-party code in `scripts/` and `tests/`. Deposit version 3 to ESS Open Archive under Attribution (CC-BY 4.0).
* **Date**: July 31, 2026
* **Rationale**: The repository had no `LICENSE` file, so GitHub reported no license and the default was all rights reserved — contradicting the open-registry framing and the README's own claim that documentation was CC BY 4.0. Crossref recorded no license for preprint v1 or v2. The gap blocked both the ESS Open Archive license field and the Zenodo deposit.
* **Alternatives considered**: Apache-2.0 for code, rejected because its express patent grant would extend to code published here while patent threads remain open elsewhere in the workshop; CC BY 4.0 for the whole repository, rejected because Creative Commons advises against CC licenses for software.
* **Impact**: GitHub now detects `cc-by-4.0`. Version 3 is the first edition of the preprint deposited under an explicit license. MIT grants no express patent license.

---

## 6. Accept Two Frozen Defects in the Version 3 PDF
* **Decision**: Submit version 3 without re-rendering the PDF, despite two known defects in it: the text states version 2 was "posted 21 July 2026" when Crossref records 30 July (21 July was the submission date), and it cites the working URL `essopenarchive.org/doc/007f7377-...` rather than the DOI.
* **Date**: July 31, 2026
* **Rationale**: The Zenodo release is already published against tag `gsia-v3-submission`. Re-rendering changes the PDF hash, invalidates the frozen submission manifest, and desyncs the archive, or forces a duplicate v3 tag and deposit. Neither defect affects a result, count, class, or conclusion. The doc URL is a self-reference, so a reader holding the PDF has already reached the record; every outward-facing identifier in the paper is stable.
* **Mitigations applied**: The ESS Open Archive version note states the correct posting date. The record's Data Availability Statement was rebuilt from the version 3 manuscript, replacing the doc URL with the DOI and repointing all repository links from the mutable `main` branch to the immutable tag.
* **Impact**: Both are recorded in `knowledge/domain/persistent_identifiers.md` as rules for the next edition rather than corrected in place.
