---
generated_by: "Claude Code CLI (Claude Opus 5)"
timestamp: "2026-07-30T22:14:00-05:00"
---

# Persistent identifiers: ESS Open Archive and Zenodo

Platform behavior verified 2026-07-30 against Crossref, DataCite, and the live
records. Two defects reached the frozen v3 submission PDF because this was not
written down earlier. Both were accepted rather than corrected; see
`DECISIONS.md`.

## ESS Open Archive

**Each version carries its own DOI. There is no version-agnostic preprint DOI.**

| Version | DOI | Posted |
|---|---|---|
| v1 | `10.22541/essoar.15004217/v1` | 2026-06-02 |
| v2 | `10.22541/essoar.15004217/v2` | 2026-07-30 |

The unversioned base `10.22541/essoar.15004217` returns **404 at doi.org** — it
is not registered. Never cite it. This differs from Zenodo, where a concept DOI
does exist and always resolves to the latest version.

**`essopenarchive.org/doc/<uuid>` URLs are working links, not identifiers.**
They change between revisions. Observed directly: the record was
`007f7377-d063-474f-9ba0-d776c927729e`, and clicking "create new version" for v3
produced a different working ID, `e4eb3b76-5960-40af-9520-6ef6f991e099`. Cite
the versioned DOI instead.

**Moderation takes days, so submission date is not posting date.** v2 was
submitted 2026-07-21 and posted 2026-07-30 — a nine-day gap. Do not write a
posting date into a manuscript until the record is live and the date is
confirmed against Crossref:

```bash
curl -s "https://api.crossref.org/works/10.22541/essoar.15004217/v2" \
  | python3 -c "import sys,json; m=json.load(sys.stdin)['message']; print(m['posted'])"
```

**The title has changed every version.** v1 "A Systematic Framework of Novel
Spectral Indices…", v2 "An Open Catalog of Proposed … Index Specifications…",
v3 "An Open Registry of … Method Specifications…". Always update the title field
on the submission form; never assume it carries over.

**Crossref recorded no license for v1 or v2.** v3 is the first version deposited
under an explicit license (CC BY 4.0).

## Zenodo

| DOI | Role |
|---|---|
| `10.5281/zenodo.20400743` | **Concept DOI** — always resolves to the current edition |
| `10.5281/zenodo.20400744` | Version DOI, v1.0.0 |
| `10.5281/zenodo.20401605` | Version DOI, v1.0.1 |

Cite the concept DOI for the current archived edition. Confirm which is which
through DataCite; a version record declares `IsVersionOf` against the concept
DOI. See [procedural/zenodo_update.md](../procedural/zenodo_update.md).

## GitHub blob links and large files

A `blob/` link to a file above GitHub's preview limit still returns HTTP 200,
but the page renders "Sorry about that, but we can't show files that are this
big right now" instead of the file. The link is not broken; only the preview is
suppressed. Verified 2026-07-31 for the 4.2 MB
`analysis/band-algebra/candidate_formula_space.csv`, which returned 200 in 0.88s
while serving GitHub's size-limit page. Neighbouring files render normally.

An HTTP status check therefore does **not** prove a `blob/` link is readable.
For files over roughly 1 MB, either cite the raw form, which serves the bytes
directly:

```text
https://raw.githubusercontent.com/<owner>/<repo>/<tag>/<path>
```

or rely on the archive copy. The same CSV is attached to the version 3 ESS Open
Archive record as a supplement, so a reader blocked by the preview limit can
download it from the record instead. Attaching supporting files to the deposit
is what makes the GitHub preview limit harmless.

## Rules for the next edition

1. Cite versioned ESSOAr DOIs, never `doc/` URLs, and never the base DOI.
2. Cite the Zenodo concept DOI for archived code.
3. Do not state a posting date in the manuscript until confirmed via Crossref.
4. Update the title field on every submission.
5. Set the license explicitly on every deposit.
6. Cite files over roughly 1 MB by raw URL, not `blob/`, and attach them to the
   deposit as well.
7. Freeze and tag only after 1–6 are satisfied. Once a Zenodo release is
   published against a tag, re-rendering the PDF invalidates the manifest
   checksums and desyncs the archive, so late corrections are expensive.
