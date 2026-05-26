# Remote Sensing Research

**Globe & Atlas** | Public-good spectral index research for environmental monitoring.

This repository documents novel satellite band combinations that can be computed from free, open-access sensors — Sentinel-2, Sentinel-1, TROPOMI, EMIT, PACE, EnMAP, and others — and applied to environmental problems where satellite data can serve as an independent accountability layer.

---

## The Atlas

**[`ATLAS.md`](ATLAS.md)** is the primary document — 116 named spectral indices across 13 environmental domains, each with:

- Formula (ready to implement)
- Spectral physics explanation
- Public benefit
- Novelty tier (T1 Unclaimed / T2 Underspecified / T3 Sensor-Enabled)
- Validation status

This is a living reference. Indices marked *Validated* have been tested against ground-truth datasets. Indices marked *Proposed* are grounded in published spectral physics and awaiting field validation.

---

## Domains Covered

| Domain | Indices | Key Sensors |
|--------|---------|-------------|
| Oilfield & Produced Water | 25 | S2, S1, TROPOMI, EMIT, ECOSTRESS, GOES |
| Wildfire & Post-Fire | 7 | S2, EMIT, TROPOMI, GOES |
| Water Quality & Freshwater | 11 | S2, PACE OCI, Landsat TIRS |
| Marine & Coastal | 10 | S2, EMIT, PACE OCI, DESIS |
| Agriculture & Food Security | 7 | S2, EnMAP, ECOSTRESS, ERA5 |
| Mining & Industrial | 8 | S2, S1, EnMAP, EMIT, Landsat |
| Urban & Infrastructure | 8 | S2, TROPOMI, ECOSTRESS |
| Permafrost & Arctic | 7 | S2, S1, ECOSTRESS |
| Tropical Forest | 6 | S2, Planet |
| Dryland & Arid | 6 | S2, EMIT, EnMAP, PRISMA |
| Wetland & Peatland | 6 | S2, S1, TROPOMI |
| Hyperspectral-Enabled | 8 | EMIT, EnMAP, PRISMA, PACE, DESIS |
| Cross-Sensor Fusion | 7 | TROPOMI+S2, GRACE+ECOSTRESS, ICESat-2+S1, NISAR+S2 |

---

## Top 10 Priority Novel Indices

| Rank | Acronym | Name | Why It Matters |
|------|---------|------|----------------|
| 1 | TSEAI | TROPOMI–Sentinel-2 Emission Attribution Index | CH₄ source attribution at field scale — climate monitoring's most urgent gap |
| 2 | HABSDI | HAB Species-Level Discrimination Index | Toxic vs. non-toxic cyanobacteria — PACE (2024) makes it globally possible |
| 3 | NPDDI | N vs. P Deficiency Discrimination Index | Precision fertilizer prescription from orbit |
| 4 | SMADI | Sargassum vs. Microplastic Discrimination Index | Both global crises; current indices conflate them |
| 5 | FGDCI | Frozen Ground Dielectric Change Index | Pan-Arctic freeze/thaw from Sentinel-1 |
| 6 | CBSDI | Coral Bleaching Stage Discrimination Index | Stages bleaching severity vs. binary detection |
| 7 | REESAI | Rare Earth Element Surface Anomaly Index | EnMAP Nd detection — clean energy supply chain |
| 8 | BSMTI | Burn Severity Mineralogy Transition Index | Post-fire debris flow risk via EMIT soil mineralogy |
| 9 | PWTDI | Peatland Water Table Depth Index | Most important unmeasured variable in wetland carbon accounting |
| 10 | RDOCI | River Dissolved Organic Carbon Index | PACE OCI UV channels (2024) make this orbital for the first time |

---

## Validated Indices

The following indices have been tested against the TRRC 27-site Permian Basin spill dataset (2026-03-28):

| Index | Full Name | Detection Rate |
|-------|-----------|----------------|
| PWCI | Produced Water Chemical Index | **81.5%** |
| ASAI | Arid Salinity Anomaly Index | **77.8%** |
| VSI | Vegetation Stress Index | **74.1%** |
| OBEC | Oil-Brine Emulsion Composite | **66.7%** |
| FBC | Ferrugination-Brine Composite | **66.7%** |
| LBI | Liquid Brine Index | **63.0%** |

*TRRC = Texas Railroad Commission. Validation against confirmed spill sites, threshold=0.01.*

---

## Novelty Tiers

| Tier | Meaning |
|------|---------|
| **T1 — Unclaimed** | No formula with this name or purpose exists in the Index DataBase or major review literature |
| **T2 — Underspecified** | Detection approach described in literature; no standardized formula or acronym published |
| **T3 — Sensor-Enabled** | Known spectral physics, newly actionable on sensors launched 2019–2024 |

---

## Supporting Documents

| File | Contents |
|------|----------|
| [`surveys/global-novel-index-survey.md`](surveys/global-novel-index-survey.md) | Deep research document covering 74 global novel indices with citations |
| [`surveys/permian-basin-platform-survey.md`](surveys/permian-basin-platform-survey.md) | 31-platform free satellite survey with integration roadmap |
| [`surveys/global-public-good-atlas.md`](surveys/global-public-good-atlas.md) | Scholarly synthesis of public-good band combinations |
| [`catalogs/limn-index-catalog.md`](catalogs/limn-index-catalog.md) | 53-index catalog with TRRC validation rates |
| [`catalogs/civic-sentinel-composite-slate.md`](catalogs/civic-sentinel-composite-slate.md) | 24-composite civic sentinel slate |
| [`catalogs/civic-sentinel-composite-atlas.md`](catalogs/civic-sentinel-composite-atlas.md) | 18 ranked composites with full formulas |
| [`formulas/formula-quick-reference.md`](formulas/formula-quick-reference.md) | Every formula across all projects, one file |

---

## Claim Philosophy

All indices in this atlas are built from published spectral physics. The defensible claim for each novel composite is:

> *A named, transparent, decision-ready composite built from established spectral mechanisms, domain gates, and confounder rejection — applied to a specific public-good screening workflow.*

**Claim:** the named workflow, the gate logic, the confounder rejection, the civic framing.  
**Do not claim:** invention of the underlying band physics, the individual ratios, or the environmental problem itself.

---

## Citation & Reuse

Formulas in this atlas are grounded in peer-reviewed spectral physics. They are released as public-good research. For validated indices (PWCI, ASAI, VSI, OBEC, FBC, LBI), cite the TRRC validation dataset and this repository. For proposed indices, cite the underlying spectral physics referenced in each entry.

**Key sources:**

- Kokaly et al. (2017). *USGS Spectral Library Version 7.*
- Green et al. (2023). "Performance and early results from EMIT." *IEEE TGRS* 61.
- Zhang et al. (2020). "Quantifying methane emissions from the Permian Basin from space." *Science Advances* 6(17).
- Mielke et al. (2024). "Neodymium mineral detection at Mountain Pass using EnMAP." *Scientific Reports* 14(1):20413.
- Pahlevan et al. (2026). "PACE OCI PFT retrieval." *Remote Sensing of Environment.*
- Hugelius et al. (2020). "Permafrost carbon vulnerability." *PNAS* 117(34).

---

*Published by [Globe & Atlas](https://globeandatlas.substack.com) | Last updated: 2026-05-25*
