# Project Context

## Identity

- Name: `remote-sensing-research`
- Profile: `hybrid-geospatial`
- Deploy: Local Obsidian vault integration
- Runtime: Static Markdown / Python-assisted authoring

## Purpose

A high-fidelity registry/atlas of novel satellite band combinations (spectral indices) for environmental monitoring, agriculture, oilfield forensic analysis, and disaster tracking. Combines public-domain descriptions with private claim boundaries, authorship parameters, and research context.

## Constraints

- **ATLAS.private.md Isolation:** The private edition (`ATLAS.private.md`) contains private authorship declarations and claim boundaries. It must remain strictly gitignored and never be pushed to the public repository.
- **Formula Integrity:** All formulas inside code blocks must use ASCII operators (`-`, `*`, `**2`, `**3`) to be safe for interpreters (Sentinel Hub JS, Pandas, NumPy) and avoid Unicode crashes.
- **Parity:** Maintain strict structural parity between ATLAS.md and ATLAS.private.md except for specific private metadata, claims, and avoid sections.

## Out of Scope

- Automated satellite pipeline integrations (this repo acts solely as the reference registry and validation source).
