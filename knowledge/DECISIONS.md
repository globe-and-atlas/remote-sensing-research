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

