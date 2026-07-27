#!/usr/bin/env python3
"""Audit the GSIA registry against a bounded Sentinel-2 band-algebra space.

This script is intentionally a structural audit, not a performance study. It:

1. Enumerates six transparent 2-4 band formula families.
2. Separates the full 13-band MSI instrument from a 10-band reflected-surface
   core that excludes aerosol, water-vapor, and cirrus channels.
3. Collapses direction/sign variants into structural classes.
4. Crosswalks exact equations against a pinned Awesome Spectral Indices
   catalog snapshot using deterministic numerical fingerprints.
5. Classifies which GSIA records are directly amenable to band algebra,
   component-level comparisons, or require broader workflows.

It does not rank environmental usefulness. That requires labeled observations,
hard negatives, held-out geography/time, and established baselines.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import math
import re
import sys
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Iterator

import numpy as np


ASI_COMMIT = "18147d1726ecfa28fa02510d6f655ae5e6a19ac5"
ASI_URL = (
    "https://raw.githubusercontent.com/awesome-spectral-indices/"
    f"awesome-spectral-indices/{ASI_COMMIT}/output/spectral-indices-dict.json"
)

MSI_BANDS = (
    "B01",
    "B02",
    "B03",
    "B04",
    "B05",
    "B06",
    "B07",
    "B08",
    "B8A",
    "B09",
    "B10",
    "B11",
    "B12",
)

# General-purpose reflected-surface channels commonly used for land and water
# indices. B01 (aerosol), B09 (water vapor), and B10 (cirrus) remain in the
# full-instrument enumeration but are excluded from this core search.
SURFACE_CORE_BANDS = (
    "B02",
    "B03",
    "B04",
    "B05",
    "B06",
    "B07",
    "B08",
    "B8A",
    "B11",
    "B12",
)

ASI_TO_MSI = {
    "A": "B01",
    "B": "B02",
    "G": "B03",
    "R": "B04",
    "RE1": "B05",
    "RE2": "B06",
    "RE3": "B07",
    "N": "B08",
    "N2": "B8A",
    "WV": "B09",
    "S1": "B11",
    "S2": "B12",
}

INDEX_ALIASES = (
    "NBR",
    "BSI",
    "NDVI",
    "NDMI",
    "NDWI",
    "NDCI",
    "NDRE",
    "MSI",
    "FAI",
)


@dataclass(frozen=True)
class Candidate:
    universe: str
    family: str
    arity: int
    bands: tuple[str, ...]
    roles: tuple[str, ...]
    expression: str
    signed_key: str
    direction_neutral_key: str
    information_key: str


def _pair_key(a: str, b: str) -> str:
    return "|".join(sorted((a, b)))


def _candidate(
    universe: str,
    family: str,
    roles: tuple[str, ...],
    expression: str,
    signed_key: str,
    direction_neutral_key: str,
    information_key: str,
) -> Candidate:
    return Candidate(
        universe=universe,
        family=family,
        arity=len(set(roles)),
        bands=tuple(sorted(set(roles), key=MSI_BANDS.index)),
        roles=roles,
        expression=expression,
        signed_key=signed_key,
        direction_neutral_key=direction_neutral_key,
        information_key=information_key,
    )


def enumerate_candidates(bands: tuple[str, ...], universe: str) -> Iterator[Candidate]:
    for a, b in itertools.permutations(bands, 2):
        pair = _pair_key(a, b)

        signed = f"difference:{a}-{b}"
        reverse = f"difference:{b}-{a}"
        yield _candidate(
            universe,
            "difference",
            (a, b),
            f"{a} - {b}",
            signed,
            min(signed, reverse),
            f"pair-difference:{pair}",
        )

        signed = f"ratio:{a}/{b}"
        reciprocal = f"ratio:{b}/{a}"
        yield _candidate(
            universe,
            "ratio",
            (a, b),
            f"{a} / {b}",
            signed,
            min(signed, reciprocal),
            f"pair-normalized-information:{pair}",
        )

        signed = f"normalized-difference:{a}-{b}"
        reverse = f"normalized-difference:{b}-{a}"
        yield _candidate(
            universe,
            "normalized-difference",
            (a, b),
            f"({a} - {b}) / ({a} + {b})",
            signed,
            min(signed, reverse),
            f"pair-normalized-information:{pair}",
        )

    for a, b, c in itertools.permutations(bands, 3):
        signed = f"three-band-correction:{a}-{b}|{c}"
        reverse = f"three-band-correction:{b}-{a}|{c}"
        yield _candidate(
            universe,
            "three-band-correction",
            (a, b, c),
            f"({a} - {b}) / ({a} + {b} + {c})",
            signed,
            min(signed, reverse),
            f"three-band-correction:{min(signed, reverse)}",
        )

    for combo in itertools.combinations(bands, 4):
        for positives in itertools.combinations(combo, 2):
            negatives = tuple(band for band in combo if band not in positives)
            pos = tuple(sorted(positives, key=MSI_BANDS.index))
            neg = tuple(sorted(negatives, key=MSI_BANDS.index))
            signed = f"four-band-balance:{'+'.join(pos)}-{'+'.join(neg)}"
            reverse = f"four-band-balance:{'+'.join(neg)}-{'+'.join(pos)}"
            yield _candidate(
                universe,
                "four-band-balance",
                (*pos, *neg),
                f"({pos[0]} + {pos[1]} - {neg[0]} - {neg[1]}) / "
                f"({pos[0]} + {pos[1]} + {neg[0]} + {neg[1]})",
                signed,
                min(signed, reverse),
                f"four-band-balance:{min(signed, reverse)}",
            )

        exact_seen: set[tuple[tuple[str, str], tuple[str, str]]] = set()
        for a, b, c, d in itertools.permutations(combo):
            raw = ((a, b), (c, d))
            equivalent = ((d, c), (b, a))
            exact = min(raw, equivalent)
            if exact in exact_seen:
                continue
            exact_seen.add(exact)
            (a1, b1), (c1, d1) = exact
            signed = f"double-nd:{a1}-{b1}|{c1}-{d1}"
            neg_raw = ((c1, d1), (a1, b1))
            neg_equivalent = ((b1, a1), (d1, c1))
            negative_exact = min(neg_raw, neg_equivalent)
            reverse = (
                f"double-nd:{negative_exact[0][0]}-{negative_exact[0][1]}|"
                f"{negative_exact[1][0]}-{negative_exact[1][1]}"
            )
            yield _candidate(
                universe,
                "difference-of-contrasts",
                (a1, b1, c1, d1),
                f"(({a1} - {b1}) / ({a1} + {b1})) - "
                f"(({c1} - {d1}) / ({c1} + {d1}))",
                signed,
                min(signed, reverse),
                f"difference-of-contrasts:{min(signed, reverse)}",
            )


def deterministic_reflectance_samples() -> dict[str, np.ndarray]:
    rng = np.random.default_rng(20260726)
    return {band: rng.uniform(0.01, 0.8, 64) for band in MSI_BANDS}


def candidate_values(candidate: Candidate, samples: dict[str, np.ndarray]) -> np.ndarray:
    values = [samples[band] for band in candidate.roles]
    if candidate.family == "difference":
        return values[0] - values[1]
    if candidate.family == "ratio":
        return values[0] / values[1]
    if candidate.family == "normalized-difference":
        return (values[0] - values[1]) / (values[0] + values[1])
    if candidate.family == "three-band-correction":
        return (values[0] - values[1]) / (values[0] + values[1] + values[2])
    if candidate.family == "four-band-balance":
        return (values[0] + values[1] - values[2] - values[3]) / sum(values)
    if candidate.family == "difference-of-contrasts":
        first = (values[0] - values[1]) / (values[0] + values[1])
        second = (values[2] - values[3]) / (values[2] + values[3])
        return first - second
    raise ValueError(f"Unsupported family: {candidate.family}")


def fingerprint(values: np.ndarray) -> str:
    rounded = np.round(values.astype(np.float64), 10)
    return hashlib.sha256(rounded.tobytes()).hexdigest()


def fetch_json(url: str) -> tuple[dict, str]:
    with urllib.request.urlopen(url, timeout=30) as response:
        payload = response.read()
    return json.loads(payload), hashlib.sha256(payload).hexdigest()


def safe_known_values(
    formula: str,
    band_tokens: list[str],
    samples: dict[str, np.ndarray],
) -> np.ndarray | None:
    if not band_tokens or not set(band_tokens).issubset(ASI_TO_MSI):
        return None
    if not re.fullmatch(r"[A-Za-z0-9_+\-*/().\s]+", formula):
        return None
    identifiers = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", formula))
    if not identifiers.issubset(ASI_TO_MSI):
        return None
    env = {token: samples[MSI] for token, MSI in ASI_TO_MSI.items()}
    try:
        with np.errstate(all="ignore"):
            values = eval(compile(formula, "<known-index>", "eval"), {"__builtins__": {}}, env)
    except (ArithmeticError, NameError, SyntaxError, TypeError, ValueError):
        return None
    array = np.asarray(values, dtype=np.float64)
    if array.shape != (64,) or not np.all(np.isfinite(array)):
        return None
    return array


def safe_msi_formula_values(
    formula: str,
    samples: dict[str, np.ndarray],
) -> np.ndarray | None:
    normalized = (
        formula.replace("−", "-")
        .replace("×", "*")
        .replace("[", "(")
        .replace("]", ")")
    )
    normalized = re.sub(
        r"(?<![\w.])(\d+(?:\.\d+)?)\s*(B(?:0[1-9]|1[0-2]|8A))\b",
        r"\1*\2",
        normalized,
    )
    if not re.fullmatch(r"[A-Za-z0-9_+\-*/().\s]+", normalized):
        return None
    identifiers = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", normalized))
    if not identifiers or not identifiers.issubset(MSI_BANDS):
        return None
    try:
        with np.errstate(all="ignore"):
            values = eval(
                compile(normalized, "<gsia-formula>", "eval"),
                {"__builtins__": {}},
                samples,
            )
    except (ArithmeticError, NameError, SyntaxError, TypeError, ValueError):
        return None
    array = np.asarray(values, dtype=np.float64)
    if array.shape != (64,) or not np.all(np.isfinite(array)):
        return None
    return array


def known_index_crosswalk(
    candidates: list[Candidate],
    samples: dict[str, np.ndarray],
) -> tuple[list[dict[str, str]], dict[str, object]]:
    payload, source_sha = fetch_json(ASI_URL)
    catalog = payload["SpectralIndices"]
    lookup: defaultdict[str, list[Candidate]] = defaultdict(list)
    for candidate in candidates:
        if candidate.universe != "full-13":
            continue
        lookup[fingerprint(candidate_values(candidate, samples))].append(candidate)

    eligible = 0
    crosswalk: list[dict[str, str]] = []
    unmatched: list[str] = []
    for short_name, record in sorted(catalog.items()):
        if "Sentinel-2" not in record.get("platforms", []):
            continue
        tokens = record.get("bands", [])
        distinct = {token for token in tokens if token in ASI_TO_MSI}
        if not (2 <= len(distinct) <= 4):
            continue
        values = safe_known_values(record["formula"], tokens, samples)
        if values is None:
            continue
        eligible += 1
        matches = lookup.get(fingerprint(values), [])
        if not matches:
            unmatched.append(short_name)
            continue
        for match in matches:
            crosswalk.append(
                {
                    "known_index": short_name,
                    "known_name": record["long_name"],
                    "application_domain": record["application_domain"],
                    "known_formula": record["formula"],
                    "known_bands": "|".join(tokens),
                    "candidate_family": match.family,
                    "candidate_expression": match.expression,
                    "candidate_signed_key": match.signed_key,
                    "reference": record["reference"],
                }
            )

    metadata = {
        "source_url": ASI_URL,
        "source_commit": ASI_COMMIT,
        "source_sha256": source_sha,
        "catalog_entries": len(catalog),
        "eligible_pure_band_sentinel2_indices": eligible,
        "exact_family_matches": len({row["known_index"] for row in crosswalk}),
        "distinct_matched_equations": len(
            {row["candidate_signed_key"] for row in crosswalk}
        ),
        "unmatched_eligible_indices": unmatched,
    }
    return crosswalk, metadata


def registry_audit(
    registry_path: Path,
    candidates: list[Candidate],
    samples: dict[str, np.ndarray],
) -> tuple[list[dict[str, str]], Counter]:
    rows: list[dict[str, str]] = []
    counts: Counter = Counter()
    candidate_lookup: defaultdict[str, list[Candidate]] = defaultdict(list)
    for candidate in candidates:
        if candidate.universe == "full-13":
            candidate_lookup[fingerprint(candidate_values(candidate, samples))].append(
                candidate
            )
    with registry_path.open(newline="", encoding="utf-8") as source:
        for record in csv.DictReader(source):
            formula = record["implemented_formula"].strip()
            required = record["required_inputs"]
            temporal = record["temporal_operator"]
            spatial = record["spatial_operator"]
            bands = sorted(
                set(re.findall(r"\bB(?:0[1-9]|1[0-2]|8A)\b", formula)),
                key=MSI_BANDS.index,
            )
            aliases = [alias for alias in INDEX_ALIASES if re.search(rf"\b{alias}\b", formula)]
            gate_terms = sorted(
                set(
                    re.findall(
                        r"\b(?:[A-Za-z]+Gate|[A-Za-z]+Reject|clip|max|min|mean|I)\b",
                        formula,
                    )
                )
            )
            direct_values = safe_msi_formula_values(formula, samples)
            direct_matches = (
                candidate_lookup.get(fingerprint(direct_values), [])
                if direct_values is not None
                else []
            )
            match_labels = sorted(
                {
                    f"{match.family}:{match.expression}"
                    for match in direct_matches
                }
            )

            if not formula:
                applicability = "not-applicable-no-implemented-formula"
                reason = "No implemented formula is recorded."
            elif not re.search(r"Sentinel-2|\bS2\b", required, re.IGNORECASE):
                applicability = "not-applicable-other-sensor"
                reason = "The implemented or proposed workflow is not Sentinel-2 based."
            elif not temporal.startswith("Single-scene") or not spatial.startswith("Per-pixel"):
                applicability = "not-applicable-workflow"
                reason = "Temporal or spatial operators extend beyond per-pixel band algebra."
            elif aliases or gate_terms or len(bands) > 4:
                applicability = "component-comparison"
                reason = (
                    "A single-scene Sentinel-2 composite can be compared at the component "
                    "or ablation level, but is not itself a plain 2-4 band permutation."
                )
            elif direct_matches:
                applicability = "direct-six-family-match"
                reason = "The complete implemented expression exactly matches a bounded family."
            elif direct_values is not None and 2 <= len(bands) <= 4:
                applicability = "direct-formula-outside-six-families"
                reason = (
                    "The expression is direct 2-4 band algebra but is not an exact member "
                    "of the six bounded families."
                )
            else:
                applicability = "manual-review"
                reason = "The expression requires manual expansion or interpretation."

            counts[applicability] += 1
            rows.append(
                {
                    "record_id": record["record_id"],
                    "record_name": record["record_name"],
                    "domain": record["domain_label"],
                    "capability_family": record["capability_label"],
                    "method_role": record["method_role"],
                    "maturity": record["maturity"],
                    "formula_status": record["formula_status"],
                    "implemented_formula": formula,
                    "required_inputs": required,
                    "band_references": "|".join(bands),
                    "band_reference_count": str(len(bands)),
                    "index_aliases": "|".join(aliases),
                    "gate_or_clip_terms": "|".join(gate_terms),
                    "six_family_exact_match": "|".join(match_labels),
                    "permutation_applicability": applicability,
                    "reason": reason,
                }
            )
    return rows, counts


def write_csv(path: Path, rows: Iterable[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as target:
        writer = csv.DictWriter(target, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def family_counts(candidates: list[Candidate], universe: str) -> dict[str, int]:
    return dict(
        sorted(Counter(c.family for c in candidates if c.universe == universe).items())
    )


def write_report(
    path: Path,
    summary: dict[str, object],
    registry_counts: Counter,
    asi_metadata: dict[str, object],
) -> None:
    full = summary["universes"]["full-13"]
    core = summary["universes"]["surface-core-10"]
    report = f"""# Sentinel-2 Band-Algebra Audit — Structural Baseline

**Generated:** {date.today().isoformat()}  
**Status:** Structural and catalog crosswalk only; no environmental performance claim

## The count changes with the question

The full Sentinel-2 MSI instrument has 13 bands. Its unique unordered 2-, 3-,
and 4-band sets total **{full['unordered_band_sets']:,}**. That is a valid
instrument-level combinatorial count, but it is not automatically a sensible
surface-index search space.

A reflected-surface core that excludes B01 aerosol, B09 water-vapor, and B10
cirrus channels contains 10 bands and **{core['unordered_band_sets']:,}**
unordered 2-4 band sets.

Applying the six bounded formula families defined for this audit produces:

| Search universe | Signed/role-specific expressions | Direction-neutral structural classes | Information classes |
|---|---:|---:|---:|
| Full 13-band MSI | {full['signed_expressions']:,} | {full['direction_neutral_classes']:,} | {full['information_classes']:,} |
| 10-band surface core | {core['signed_expressions']:,} | {core['direction_neutral_classes']:,} | {core['information_classes']:,} |

Direction-neutral classes collapse sign-reversed forms and reciprocal simple
ratios. The information-class count additionally merges simple ratios and
normalized differences for the same positive-reflectance band pair because
they are monotonic transforms of one another. It does not claim that their
scales, noise behavior, or operational thresholds are interchangeable.

## Formula-family counts

| Family | Full 13-band expressions | Surface-core expressions |
|---|---:|---:|
"""
    families = sorted(set(full["families"]) | set(core["families"]))
    for family in families:
        report += (
            f"| {family} | {full['families'].get(family, 0):,} | "
            f"{core['families'].get(family, 0):,} |\n"
        )

    report += f"""
## Crosswalk to established spectral indices

The audit compared deterministic numerical fingerprints against the Awesome
Spectral Indices catalog pinned at commit `{asi_metadata['source_commit']}`.
The pinned catalog contains **{asi_metadata['catalog_entries']:,}** entries.
Of the Sentinel-2 entries that use only 2-4 mapped reflectance bands and no
external parameters, **{asi_metadata['eligible_pure_band_sentinel2_indices']:,}**
were eligible for this exact-equation check and
**{asi_metadata['exact_family_matches']:,}** matched one of the six bounded
families. Those {asi_metadata['exact_family_matches']:,} named catalog entries
resolve to only **{asi_metadata['distinct_matched_equations']:,}** distinct
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
"""
    for key, value in sorted(registry_counts.items()):
        report += f"| {key} | {value} |\n"

    report += f"""
This is why a band-permutation search does not invalidate or directly evaluate
all 91 GSIA records. It can directly audit only plain band algebra. Composite
records should be tested through component ablations, while temporal, spatial,
SAR, thermal, hyperspectral, and multi-sensor workflows require task-specific
evaluation.

## Reproduction

The reference run used Python **{summary['environment']['python']}** and NumPy
**{summary['environment']['numpy']}**. From the repository root:

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
"""
    path.write_text(report, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--registry",
        type=Path,
        default=Path("preprint/gsia_preprint_v3_status_supplement_2026-07-25.csv"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("analysis/band-algebra"),
    )
    args = parser.parse_args()

    full_candidates = list(enumerate_candidates(MSI_BANDS, "full-13"))
    core_candidates = list(
        enumerate_candidates(SURFACE_CORE_BANDS, "surface-core-10")
    )
    candidates = full_candidates + core_candidates
    samples = deterministic_reflectance_samples()
    crosswalk, asi_metadata = known_index_crosswalk(candidates, samples)
    registry_rows, registry_counts = registry_audit(
        args.registry,
        candidates,
        samples,
    )

    candidate_rows = [
        {
            "universe": c.universe,
            "family": c.family,
            "arity": c.arity,
            "bands": "|".join(c.bands),
            "roles": "|".join(c.roles),
            "expression": c.expression,
            "signed_key": c.signed_key,
            "direction_neutral_key": c.direction_neutral_key,
            "information_key": c.information_key,
        }
        for c in candidates
    ]
    write_csv(
        args.output_dir / "candidate_formula_space.csv",
        candidate_rows,
        list(candidate_rows[0]),
    )
    write_csv(
        args.output_dir / "known_index_crosswalk.csv",
        crosswalk,
        list(crosswalk[0]) if crosswalk else [
            "known_index",
            "known_name",
            "application_domain",
            "known_formula",
            "known_bands",
            "candidate_family",
            "candidate_expression",
            "candidate_signed_key",
            "reference",
        ],
    )
    write_csv(
        args.output_dir / "gsia_registry_applicability.csv",
        registry_rows,
        list(registry_rows[0]),
    )

    universes: dict[str, dict[str, object]] = {}
    for name, band_set, group in (
        ("full-13", MSI_BANDS, full_candidates),
        ("surface-core-10", SURFACE_CORE_BANDS, core_candidates),
    ):
        universes[name] = {
            "bands": list(band_set),
            "unordered_band_sets": sum(
                math.comb(len(band_set), arity) for arity in (2, 3, 4)
            ),
            "signed_expressions": len(group),
            "direction_neutral_classes": len(
                {candidate.direction_neutral_key for candidate in group}
            ),
            "information_classes": len(
                {candidate.information_key for candidate in group}
            ),
            "families": family_counts(candidates, name),
        }

    summary = {
        "generated": date.today().isoformat(),
        "scope": "structural audit; no environmental performance claim",
        "environment": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
        },
        "universes": universes,
        "awesome_spectral_indices": asi_metadata,
        "gsia_registry_applicability": dict(sorted(registry_counts.items())),
    }
    (args.output_dir / "audit_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    write_report(
        args.output_dir / "audit_report.md",
        summary,
        registry_counts,
        asi_metadata,
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
