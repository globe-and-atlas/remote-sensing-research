#!/usr/bin/env python3
"""Generate the readable GSIA formula-schema v2 catalog from a governed CSV."""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path


OUT_OF_SCOPE = re.compile(r"produced[ -]water|\bPWCI\b|\bASAI\b|\bOBEC\b|\bTRRC\b", re.I)
EXPECTED_MATURITY = {"M1": 38, "M2": 16, "M3": 37}
EXPECTED_ROLES = {
    "primary": 15,
    "variant": 10,
    "component": 12,
    "reference": 1,
    "research-model": 51,
    "retired": 2,
}


def code_block(value: str, empty: str) -> list[str]:
    text = (value or "").strip() or empty
    if "```" in text:
        raise ValueError("Formula text contains a Markdown fence")
    return ["```text", text, "```"]


def clean(value: str) -> str:
    return " ".join((value or "").split())


def link(label: str, url: str) -> str:
    if not label:
        return "No context source recorded in the governed supplement."
    return f"[{label}]({url})" if url else label


def sentence(value: str) -> str:
    text = clean(value)
    return text if not text or text.endswith((".", "!", "?")) else f"{text}."


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: generate_gsia_v2_formula_catalog.py INPUT.csv OUTPUT.md", file=sys.stderr)
        return 2

    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    with source.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if len(rows) != 91:
        raise ValueError(f"Expected 91 rows, found {len(rows)}")
    if len({row["record_id"] for row in rows}) != 91:
        raise ValueError("Record identifiers are not unique")
    if Counter(row["maturity"] for row in rows) != EXPECTED_MATURITY:
        raise ValueError("Maturity distribution does not match the governed release")
    if Counter(row["method_role"] for row in rows) != EXPECTED_ROLES:
        raise ValueError("Method-role distribution does not match the governed release")
    if any(OUT_OF_SCOPE.search(" ".join(row.values())) for row in rows):
        raise ValueError("Atlas publication boundary violation")

    families: OrderedDict[tuple[str, str], list[dict[str, str]]] = OrderedDict()
    for row in rows:
        key = (row["capability_id"], row["capability_label"])
        families.setdefault(key, []).append(row)
    if len(families) != 24:
        raise ValueError(f"Expected 24 capability families, found {len(families)}")

    source_commit = {row["source_commit"] for row in rows}
    audit_dates = {row["audit_date"] for row in rows}
    if len(source_commit) != 1 or len(audit_dates) != 1:
        raise ValueError("Supplement does not identify one release snapshot")
    commit = next(iter(source_commit))
    audit_date = next(iter(audit_dates))

    lines = [
        "# Global Spectral Index Atlas Method-Specification Catalog (schema v2.0)",
        "",
        f"- **Release audit:** {audit_date}",
        "- **Registry:** 24 capability families comprising 91 governed method specifications across 12 domains",
        "- **Formula schema:** 2.0",
        f"**Audited Atlas source:** commit `{commit}`, since made private; the public Atlas viewer is now maintained at "
        "[globe-and-atlas/limn-atlas](https://github.com/globe-and-atlas/limn-atlas)",
        "",
        "This is the human-readable companion to the machine-readable "
        f"[`{source.name}`](../preprint/{source.name}). "
        "The CSV is authoritative. This file is generated from it so the formulas, maturity states, method roles, and limits remain synchronized.",
        "",
        "GSIA is a registry of governed environmental remote-sensing method specifications. "
        "The 91-record count is inventory, not a claim of 91 unique band combinations, scientifically unprecedented equations, or validated detectors. "
        "A formula can be useful as a screening feature or research hypothesis without establishing target specificity, causal attribution, concentration, risk, or regulatory status.",
        "",
        "## How to read the records",
        "",
        "- **Proposed formula or workflow** states the full research specification, including operators or calibration that may not yet be implemented.",
        "- **Implemented or retained legacy formula** states what currently runs, or what is preserved for traceability after retirement.",
        "- **M1** means formula specified; **M2** means executable but not live; **M3** means demonstrated in the Atlas interface.",
        "- **M3 is not validation.** Every record in this release remains below V1 independent evaluation.",
        "- **Contribution classes are provisional.** C1, C2, and C3 describe the intended contribution; they do not establish scientific priority.",
        "- **Method roles organize families.** Primary, variant, component, reference, research-model, and retired are catalog roles, not performance rankings.",
        "",
        "## Release inventory",
        "",
        "| Dimension | Distribution |",
        "|---|---|",
        "| Maturity | 37 M3; 16 M2; 38 M1 |",
        "| Method roles | 15 primary; 10 variant; 12 component; 1 reference; 51 research-model; 2 retired |",
        "| Contribution classes | 68 C1; 22 C2; 1 C3, all provisional |",
        "| Independent validation | 0 V1; 0 V2 |",
        "",
        "## Record index",
        "",
        "| # | Record | Capability family | Role | Maturity | Formula status |",
        "|---:|---|---|---|---|---|",
    ]

    for number, row in enumerate(rows, start=1):
        lines.append(
            f"| {number} | [{row['record_id']}](#{row['record_id'].lower()}) - {clean(row['record_name'])} "
            f"| {clean(row['capability_label'])} | {row['method_role']} | {row['maturity']} | {clean(row['formula_status'])} |"
        )

    for (family_id, family_label), family_rows in families.items():
        lines.extend(["", f"## {family_label}", ""])
        roles = Counter(row["method_role"] for row in family_rows)
        role_summary = "; ".join(f"{count} {role}" for role, count in roles.items())
        lines.extend(
            [
                f"- **Family ID:** `{family_id}`",
                f"- **Records:** {len(family_rows)} ({role_summary})",
                "",
            ]
        )

        for row in family_rows:
            anchor = row["record_id"].lower()
            lines.extend(
                [
                    f'<a id="{anchor}"></a>',
                    f"### {row['record_id']} - {clean(row['record_name'])}",
                    "",
                    f"- **Domain:** {clean(row['domain_label'])} (`{row['domain_id']}`)",
                    f"- **Capability role:** {row['method_role']} in {clean(row['capability_label'])}",
                    f"- **Contribution:** {row['contribution_class']} - {clean(row['contribution_status'])}",
                    f"- **Maturity:** {row['maturity']} - {clean(row['interactive_state'])}",
                    f"- **Formula status:** {clean(row['formula_status'])}",
                    f"- **Required inputs:** {clean(row['required_inputs'])}",
                    f"- **Formula version:** {row['formula_version']}",
                    "",
                    "**Proposed formula or workflow**",
                    "",
                    *code_block(row["proposed_formula"], "No proposed formula recorded."),
                    "",
                    "**Implemented or retained legacy formula**",
                    "",
                    *code_block(row["implemented_formula"], "Not implemented in the current Atlas release."),
                    "",
                    f"- **Temporal operator:** {clean(row['temporal_operator'])}",
                    f"- **Spatial operator:** {clean(row['spatial_operator'])}",
                    f"- **Units:** {clean(row['units'])}",
                    f"- **Calibration:** {clean(row['calibration_status'])}",
                    "",
                    f"**Physical rationale.** {clean(row['physical_rationale'])}",
                    "",
                    f"**Intended use and inference limit.** {clean(row['intended_use_and_inference_limit'])}",
                    "",
                    f"**Evidence and validation.** {sentence(row['event_evidence_status'])} {sentence(row['validation_status'])}",
                    "",
                    f"**Context source.** {link(clean(row['source_name']), row['source_url'])}",
                    "",
                    "---",
                    "",
                ]
            )

    lines.extend(
        [
            "## Reproducibility",
            "",
            "Regenerate this document from the governed supplement:",
            "",
            "```bash",
            "python3 scripts/generate_gsia_v2_formula_catalog.py \\",
            f"  preprint/{source.name} \\",
            "  formulas/gsia-v2-formula-catalog.md",
            "```",
            "",
            "The generator fails if record counts, maturity counts, method-role counts, capability-family counts, unique identifiers, or the Atlas publication boundary do not match the governed release.",
            "",
        ]
    )

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(lines), encoding="utf-8")
    print(f"{destination}: {len(rows)} records in {len(families)} families")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
