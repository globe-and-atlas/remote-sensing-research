# Procedural Guide: Validating the Spectral Index Registry

This guide outlines how to execute the automated validation suite to check for duplication, mathematical operators, and internal links across the registry files.

## Overview

To prevent runtime crashes, broken links, or redundant definitions, all documents inside the `registry/` folder must adhere to three core integrity checks:
1.  **Code-Safe Mathematical Operators**: No non-ASCII characters (such as unicode minus `−`, multiplication cross `×`, or superscripts `²`, `³`) are allowed inside backticks or code blocks. They must use standard ASCII operators (`-`, `*`, `**2`, `**3`).
2.  **No Header/Anchor Duplicates**: Every index section must have a unique acronym and anchor (e.g. `### <a id="pwci"></a>PWCI`).
3.  **Link Integrity**: All internal cross-reference markdown links (e.g. `[PWCI](#pwci)`) must resolve to a valid local anchor or section header.

---

## How to Run Validation

To validate the registry, execute the validation script via the terminal:

```bash
python3 /Users/danielbally/.gemini/antigravity-ide/brain/898abd31-4cc6-4638-825a-e09efd6b9a94/scratch/verify_registry.py
```

### Expected Output

When all checks pass, the script will output:

```text
Found 4 registry files to validate.

Validating master_index_catalog.md:
  ✅ Math operators are clean (ASCII code-safe).
  ✅ No duplicate headers found.
  ✅ No broken internal markdown links.

...

🎉 ALL REGISTRY FILES VALIDATED PERFECTLY! 🎉
```

If errors are found, they will be printed in detail with corresponding line numbers. Correct the file contents before staging or committing changes.
