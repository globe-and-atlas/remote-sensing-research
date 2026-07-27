# Sentinel-2 Band-Algebra Audit — Structural Baseline

**Generated:** 2026-07-26  
**Status:** Structural and catalog crosswalk only; no environmental performance claim

## The count changes with the question

The full Sentinel-2 MSI instrument has 13 bands. Its unique unordered 2-, 3-,
and 4-band sets total **1,079**. That is a valid
instrument-level combinatorial count, but it is not automatically a sensible
surface-index search space.

A reflected-surface core that excludes B01 aerosol, B09 water-vapor, and B10
cirrus channels contains 10 bands and **375**
unordered 2-4 band sets.

Applying the six bounded formula families defined for this audit produces:

| Search universe | Signed/role-specific expressions | Direction-neutral structural classes | Information classes |
|---|---:|---:|---:|
| Full 13-band MSI | 15,054 | 7,527 | 7,449 |
| 10-band surface core | 4,770 | 2,385 | 2,340 |

Direction-neutral classes collapse sign-reversed forms and reciprocal simple
ratios. The information-class count additionally merges simple ratios and
normalized differences for the same positive-reflectance band pair because
they are monotonic transforms of one another. It does not claim that their
scales, noise behavior, or operational thresholds are interchangeable.

## Formula-family counts

| Family | Full 13-band expressions | Surface-core expressions |
|---|---:|---:|
| difference | 156 | 90 |
| difference-of-contrasts | 8,580 | 2,520 |
| four-band-balance | 4,290 | 1,260 |
| normalized-difference | 156 | 90 |
| ratio | 156 | 90 |
| three-band-correction | 1,716 | 720 |

## Crosswalk to established spectral indices

The audit compared deterministic numerical fingerprints against the Awesome
Spectral Indices catalog pinned at commit `18147d1726ecfa28fa02510d6f655ae5e6a19ac5`.
The pinned catalog contains **280** entries.
Of the Sentinel-2 entries that use only 2-4 mapped reflectance bands and no
external parameters, **185**
were eligible for this exact-equation check and
**71** matched one of the six bounded
families. Those 71 named catalog entries
resolve to only **48** distinct
signed equations, because different application traditions sometimes publish
the same band algebra under different names.

An exact match identifies prior documented use of the equation. Absence of a
match is not evidence of novelty: the catalog is not exhaustive, formulas may
be algebraically or monotonically related without being exactly equal, and
many published methods use constants, masks, temporal operators, or fitted
models outside these six families.

## Applicability to the 91-record GSIA registry

| Audit class | Records |
|---|---:|
| component-comparison | 33 |
| direct-formula-outside-six-families | 1 |
| direct-six-family-match | 1 |
| manual-review | 1 |
| not-applicable-no-implemented-formula | 52 |
| not-applicable-other-sensor | 2 |
| not-applicable-workflow | 1 |

This is why a band-permutation search does not invalidate or directly evaluate
all 91 GSIA records. It can directly audit only plain band algebra. Composite
records should be tested through component ablations, while temporal, spatial,
SAR, thermal, hyperspectral, and multi-sensor workflows require task-specific
evaluation.

## Reproduction

The reference run used Python **3.13.7** and NumPy
**2.4.3**. From the repository root:

```bash
python3 scripts/audit_band_algebra.py
python3 -m unittest tests/test_band_algebra_audit.py
```

The remote catalog input is pinned by commit and SHA-256 above. Candidate
generation and fingerprints are deterministic; the reflectance sample generator
uses fixed seed `20260726`.

## What this audit establishes

- The difference between band sets, signed equations, structural classes, and
  information-equivalent transformations.
- A reproducible enumeration of the six bounded formula families.
- Exact-equation links to a pinned established-index catalog snapshot.
- A record-level map of where permutation analysis is directly applicable.

## What it does not establish

- Environmental usefulness, accuracy, transferability, or novelty.
- That an unmatched expression is a new spectral index.
- That atmospheric channels should be used as general surface-index inputs.
- That synthetic or catalog-level analysis substitutes for labeled imagery.

The next empirical gate is a target-specific benchmark with locked formulas,
hard negatives, geographic and temporal holdouts, established baselines,
uncertainty, and explicit failure cases.
