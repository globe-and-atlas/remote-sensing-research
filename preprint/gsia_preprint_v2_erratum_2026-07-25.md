---
generated_by: "Claude Code CLI (Claude Opus 5)"
timestamp: "2026-07-25T12:27:52-05:00"
---

# GSIA preprint v2 — erratum and post-snapshot corrections

**Applies to:** *The Global Spectral Index Atlas*, ESS Open Archive v2 (July 2026)
**Record:** https://essopenarchive.org/doc/007f7377-d063-474f-9ba0-d776c927729e
**Snapshot audited in v2:** commit `e50c2eda5cf405c7693e5210e04894c691e5f2eb` (2026-07-21)
**Correction date:** 2026-07-25

A deep scientific review of the Limn Atlas deployment and the Sentinel processing
chain on 2026-07-25 found defects that the v2 audit did not test for. The v2 audit
checked band declarations, output shape, schema completeness, and display
visibility. It did not check whether a record's *stated inputs matched the sensors
its evalscript actually samples*, whether the *implemented formula matched the
executing code*, or whether the *reflectance conversion was radiometrically
correct*. All corrections below move claims toward the registry's own standard.

Reproduce the current divergence at any time with:

```bash
python3 execution/reconcile_preprint_supplement.py
```

---

## 1. Counts and structural claims are UNAFFECTED

Every headline number in the v2 abstract and Tables 1–3 still holds against the
corrected registry:

| Claim | v2 value | Current | Status |
|---|---|---|---|
| Total records | 91 | 91 | unchanged |
| Live M3 / M2 / M1 | 37 / 16 / 38 | 37 / 16 / 38 | unchanged |
| Method roles (primary/variant/component/reference/research-model/retired) | 15/10/12/1/51/2 | identical | unchanged |
| Capability families | 24 | 24 | unchanged |
| Renderable evalscripts passing static band/output audit | 37, zero flags | 37, zero flags | unchanged |

No record changed maturity, method role, contribution class, or render state.
The corrections are to record *descriptions*, not to the registry's structure.

---

## 2. Radiometric defect in the COG rendering path (not covered by v2)

**Defect.** `execution/render_cog_tile.py` converted Earth Search
`sentinel-2-l2a` digital numbers to reflectance with a bare `DN / 10000`. Since
ESA processing baseline 04.00 (operational 2022-01-25), L2A carries
`BOA_ADD_OFFSET = -1000`, so physical reflectance is `(DN - 1000) / 10000`.

**Consequence — narrower and stranger than a uniform bias.** Earth Search exposes
`earthsearch:boa_offset_applied`. For most items it is `true`: the archive has
already spent the offset, and `DN / 10000` is correct. The defect is the subset
where it is `false` on a baseline >= 04.00 item. Measured over the Permian test
area on 2026-07-25, that subset is **38 of 589 items (6.5%)**, concentrated in
2022 and 2025 with none in 2023 or 2024.

Those scenes read **0.1 reflectance too high** while their neighbours read
correctly. Because an additive offset does not cancel in `(a-b)/(a+b)`, the error
propagates to normalized ratios as well as absolute thresholds: NDVI computed
from DN 3000/1500 returns 0.33 uncorrected versus 0.60 corrected, a 0.27 error.

The scene-dependent character is the substantive problem. A uniform bias would at
least be internally consistent; this makes two dates of the same site differ by
0.1 reflectance with nothing in the rendered output to indicate which convention
applied, so any multi-date comparison built on the raw expression is silently
inconsistent. A date rule cannot fix it — the flag must be read per item.

**Scope.** The COG path is the configured default for map rendering. The Sentinel
Hub WMS path was never affected (`harmonizeValues` defaults to true). The Google
Earth Engine path was never affected (`COPERNICUS/S2_SR_HARMONIZED` is
pre-harmonized). The v2 display audit used the public WMS path, so **the "nonblank
overlay for all 37" result is not invalidated.**

**Net position.** The defect is real and would have silently corrupted any future
multi-date product rendered through this path, but it did not reach a published or
recorded GSIA result. It is reported here as a latent defect found and closed,
which is the outcome the registry's correction pathway is meant to produce.

**Correction.** Offset now resolved per scene, preferring
`earthsearch:boa_offset_applied` (guards against double-correction), then
`s2:processing_baseline`, then acquisition date. Regression test:
`tests/test_cog_boa_offset.py`. The STAC item cache schema was bumped so items
cached under the old logic are not reused.

**Bearing on v2 conclusions.** None of the reported results depended on the COG
path. Any *future* entry-level validation study that uses COG rendering must use
the corrected conversion.

---

## 3. Records whose stated inputs named sensors they never sampled

Seven live records advertised multi-sensor inputs while executing pure
Sentinel-2 evalscripts. Because `required_inputs` defaulted to the platform
string, the supplement's `required_inputs` column carried the same overstatement.

| Record | v2 `required_inputs` | Corrected | Evalscript actually samples |
|---|---|---|---|
| SMPDI | Sentinel-2 + EMIT | Sentinel-2 L2A | B03 B04 B08 B8A B11 B12 |
| OWSI | EMIT + Sentinel-2 | Sentinel-2 L2A | B02 B11 B12 |
| NPDefI | Sentinel-2 + EnMAP | Sentinel-2 L2A | B04 B05 B08 B11 B12 |
| SABSI | Sentinel-2 + Planet | Sentinel-2 L2A | B02 B03 B04 |
| MEPSI | Sentinel-2 + Planet | Sentinel-2 L2A | B03 B04 B05 B08 |
| DLPEHI | Sentinel-2 + GPM | Sentinel-2 L2A | B02 B03 B04 B08 B11 |
| MHSSP | Sentinel-2 + TROPOMI | Sentinel-2 L2A | B03 B04 B05 B08 |

In each case the additional sensor is now stated in `proposed_formula`, where it
belongs: it describes the experiment required to promote the record, not the
current live layer. SACI is unaffected — it genuinely renders a TROPOMI product.

---

## 4. Implemented formulas that did not match the executing code

The v2 schema separates proposed from implemented formulas. Four records had an
`implemented_formula` that did not describe what the code computes.

**LISI.** Published denominator `B08 + 6B04 − 7.5B02 + 1`; the code computes
`B08 + B11 + 6B04 − 7.5B02 + 1`. The extra B11 term means the expression is not
the EVI denominator despite its shape. Corrected to match the code.

**DLPEHI.** The published formula advertised an `NDTI > −0.2` term. NDTI requires
B12, which the script never loaded — **the term was never implemented**, and a
bare-soil index stood in for it. The published NDVI window (0.1–0.3) was coded as
0.05–0.35, and NDWI acted as a gate rather than a multiplicative factor. The
implemented formula now states the executing expression; the locust-habitat model
moved to `proposed_formula`.

**IPVSI and WVTDI** published prose descriptions in the `implemented_formula`
field ("Red-edge structural proxy for dense monoculture…"), which is not
reproducible. Both now carry explicit equations.

---

## 5. Physical rationale corrections

**NPDefI** stated that phosphorus deficiency produces anthocyanin accumulation
detectable at SWIR2 (B12). This is incorrect: anthocyanins absorb near 500–550 nm
and have no SWIR2 absorption feature; the B12/B11 contrast responds to canopy
water and dry-matter (cellulose/lignin) absorption. The nitrogen-versus-phosphorus
separation is therefore hypothesized, not mechanistically supported by the stated
physics. Rationale rewritten; the record is renamed to a contrast proxy.

**SMPDI** described its baseline residual as FAI. The implementation interpolates
the baseline B04→B12, whereas common Sentinel-2 FAI implementations use B04→B11.
It is an FAI variant and is now labelled as such — relevant to §5.3, which
recommends evaluating SMPDI against FDI-based classification (Biermann et al.,
2020).

**MEPSI** described its third term as a macrophyte index; the code computes NDCI,
a chlorophyll-a water index, used as a bare-water proxy.

**MHSSP** advertised normalization of the red-edge term against a local maximum;
the code applies a fixed threshold.

---

## 6. Internal consistency corrections

**Bare Soil Index** had three incompatible definitions across evalscripts. DLPEHI
used B03 where seven other records used B02 — an unintended deviation, now
corrected (B02 added to its `setup()` input list; the static band audit still
passes 37/37). EPDI's binary gate variable named `bsi` was renamed; no arithmetic
changed. LFMPI's B8A-based NDVI is intentional (B08 is not loaded) and is now
named to reflect that.

Because the DLPEHI correction changed rendered output, its display QC was re-run on
2026-07-25 under the same settings as the 2026-07-21 audit (same public endpoint and
layer, 512x512 tile, 15-day window ending on the bookmark date, 30% max cloud cover)
rather than carried forward:

| Metric | 2026-07-21 (pre-fix) | 2026-07-25 (corrected) |
|---|---|---|
| Verdict | strong | strong |
| Visible coverage | 58.800% | 57.392% |
| High-signal coverage | 57.658% | 55.602% |
| p99 luminance | 0.666 | 0.666 |

The verdict is unchanged, so the v3 supplement carries a display verdict for all 37
live records. A `--keys` filter was added to `execution/qc_atlas_bookmarks.py` so a
targeted re-audit writes to a `-partial` file and cannot overwrite the full-catalog
report.

---

## 7. Provenance data correction

`src/verifiedBookmarks.js` held 90 source-reviewed event references, of which
**21 carried dates preceding the Sentinel-2 mission** (earliest 1998-04-25;
Sentinel-2A reached orbit 2015-06-23). No Sentinel-2 observation of those events
can exist at any processing level. These rows now separate `eventDate` from the
Sentinel search-window `date`, which is `null` with `sentinelObservable: false`
where the event predates the mission. Nine further rows falling between 2015-06-23
and the dense L2A archive are flagged `sentinelObservable: "sparse"`. Regression
test: `tests/test_verified_bookmark_dates.mjs`.

This file was not imported by application code at the time of the v2 audit, so no
published result depended on it, and no user was ever shown an unsatisfiable date.

---

## 8. Interface change supporting §2.3

The v2 paper states (§2.3, §7.1) that every entry should publish paired observable
and inference-limit clauses. The deployment labelled these "Physics" and
"Benefit"; they are now labelled **Observable** and **Intended use & inference
limit**.

The Atlas interface additionally now renders an **Authorship & priority** block.
Records with an explicit claim show it alongside their contribution class and
`contributionStatus`; the remaining records show the registry-wide default that
priority is not established. The author's private `level`/`strength` confidence
notes are deliberately **not** rendered, since a "strongly defensible" badge would
contradict §4.5.

---

## 9. Recommended action on the archive record

None of the corrections invalidate a reported result, and all reported counts
still hold. The affected material is the per-record content of the status
supplement. Recommended: publish a v2.1 supplement CSV regenerated from the
corrected registry, with this erratum attached, rather than revising the
manuscript text. The 37 field-level differences are enumerated in
`.tmp/preprint_supplement_reconciliation.md`.

One row in the published supplement is *stale in the opposite direction*: EC-ACI
was corrected in the deployment on 2026-07-23, after the v2 snapshot. The
supplement carries its pre-correction name, formula, and ECOSTRESS input claim.
That row should be updated from the current registry, not treated as authoritative.
