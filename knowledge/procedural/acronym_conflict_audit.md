# Procedural Guide: Acronym Conflict Audits & Refactoring

This guide outlines the standard operating procedure for auditing proposed spectral index acronyms against global databases to prevent naming collisions, and how to safely refactor them across the repository.

---

## 1. Triggering an Audit

An acronym audit MUST be conducted whenever:
1. A new index is drafted and named.
2. An index is proposed for submission to a community repository (e.g., *Awesome Spectral Indices*).
3. Preparing a manuscript or preprint for formal publication.

---

## 2. Scholarly Search Protocol

To verify that a proposed acronym is unique and does not overlap with existing literature:

1. **Query Remote Sensing Databases**: Search for the exact acronym in Google Scholar, IEEE Xplore, and MDPI Remote Sensing.
2. **Query the Awesome Spectral Indices Registry**: Search the ASI catalogue (or the active `awesome-spectral-indices` repository) to ensure that the acronym is not already registered.
3. **Cross-reference Environmental Science**: If a match is found in soil science, agricultural monitoring, or oceanography, record the overlapping name even if it is not an optical index.

### Conflict Evaluation Matrix

*   **Identical Match (Optical Index)**: Conflict is **blocking**. The acronym MUST be renamed.
*   **Identical Match (Non-Optical environmental metric)**: Conflict is **blocking**. (e.g. `SMADI` conflicted with *Soil Moisture Agricultural Drought Index*). Acronym MUST be renamed to prevent GEE import confusion.
*   **Identical Match (Unrelated domain, e.g. medicine)**: Conflict is **permissible** but should be avoided if an intuitive alternative exists.

---

## 3. Systematic Refactoring Steps

Once a collision is identified and a replacement acronym is approved (e.g., `SMADI` $\rightarrow$ `SMPDI` and `NPDDI` $\rightarrow$ `NPDefI`), execute the refactoring in the following sequence to preserve repository integrity:

### Step 3.1: Global Text Replacement
Use code-editing tools or python scripts to search and replace all instances of the acronym in:
*   `README.md`
*   `ATLAS.md` (and `ATLAS.private.md` to maintain parity)
*   All registry files (`registry/master_index_catalog.md`, `registry/comparative_analysis.md`, `registry/Awesome_EE_Spectral_Indices_Contribution.md`)
*   Formula quick references (`formulas/formula-quick-reference.md`)
*   Active manuscript or preprint files (`preprint/gsia_preprint_v1.md`)

### Step 3.2: Verification Suite Execution
Immediately run the automated verification script:
```bash
python3 /Users/danielbally/.gemini/antigravity-ide/brain/898abd31-4cc6-4638-825a-e09efd6b9a94/scratch/verify_registry.py
```
Ensure that:
*   All markdown anchor IDs are correctly updated (e.g. `<a id="smpdi"></a>` and `[SMPDI](#smpdi)`).
*   No dead links are introduced.

### Step 3.3: Syncing Private Atlas and Git History
Verify that the `.gitignore` correctly protects `ATLAS.private.md`, commit the public changes, and push to the public remote branch:
```bash
git add .
git commit -m "refactor: rename [OLD] -> [NEW] to resolve registry conflicts"
git push public main
```
