# Remote Sensing Research

**Globe & Atlas** | Public-good spectral index research for environmental monitoring.

This repository serves as the high-resolution, granular **Atlas** counterpart to the [Globe & Atlas](https://globeandatlas.substack.com) publication. While the *Globe* provides a high-altitude macro scope of where spatial value is shifting, this *Atlas* zooms all the way in to the micro scale: cataloging the electromagnetic physics, raw band formulas, and empirical calibrations that prove a spatial workflow actually works.

Here, we document novel satellite band combinations that can be computed from free, open-access sensors — Sentinel-2, Sentinel-1, TROPOMI, EMIT, PACE, EnMAP, and others — and applied to environmental problems where satellite data can serve as an independent accountability layer.

---

## 🗺️ The Atlas Index

**[`ATLAS.md`](ATLAS.md)** is the primary reference database — containing 116 named spectral indices across 13 environmental domains. Each entry is documented with:

- **Formula**: Ready to implement in JavaScript, Python, or database engines.
- **Spectral Physics**: Physical explanation of the surface interactions and band mechanics.
- **Confounder Rejection**: Domain gates and masks used to isolate clean anomalies.
- **Validation Status**: Empirically verified metrics against confirmed ground-truth events.
- **Novelty Tier**: Demarcated based on literature gaps (T1 Unclaimed / T2 Underspecified / T3 Sensor-Enabled).

*This is a living, public-good reference. Validated indices have been run against regional ground truth; proposed indices are grounded in published physics and awaiting field verification.*

---

## 📡 Domains Covered

| Domain | Indices | Key Earth Observation Sensors |
|--------|---------|-----------------------------|
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

## 🏆 Top 10 Priority Novel Indices

| Rank | Acronym | Name | Operational Significance |
|------|---------|------|--------------------------|
| 1 | **TSEAI** | TROPOMI–Sentinel-2 Emission Attribution Index | CH₄ source attribution at field scale — climate monitoring's most urgent gap |
| 2 | **HABSDI** | HAB Species-Level Discrimination Index | Toxic vs. non-toxic cyanobacteria — PACE OCI UV bands make this globally possible |
| 3 | **NPDDI** | N vs. P Deficiency Discrimination Index | Precision fertilizer prescription and runoff management from orbit |
| 4 | **SMADI** | Sargassum vs. Microplastic Discrimination Index | Disentangles global marine debris crises; current indices conflate them |
| 5 | **FGDCI** | Frozen Ground Dielectric Change Index | Pan-Arctic freeze/thaw dynamics from Sentinel-1 SAR |
| 6 | **CBSDI** | Coral Bleaching Stage Discrimination Index | Classifies bleaching severity stages vs. binary surface detection |
| 7 | **REESAI** | Rare Earth Element Surface Anomaly Index | EnMAP bastnäsite/monazite Nd detection for clean energy supply chains |
| 8 | **BSMTI** | Burn Severity Mineralogy Transition Index | Post-fire debris flow risk via EMIT soil mineralogy changes |
| 9 | **PWTDI** | Peatland Water Table Depth Index | Critical unmeasured variable in wetland carbon accounting |
| 10 | **RDOCI** | River Dissolved Organic Carbon Index | PACE OCI UV channels make this orbital for the first time |

---

## 🧪 Ground-Truth Validation

The following indices have been tested against the Texas Railroad Commission (TRRC) 27-site Permian Basin produced water spill dataset:

| Index | Full Name | Detection Rate |
|-------|-----------|----------------|
| **PWCI** | Produced Water Chemical Index | **81.5%** |
| **ASAI** | Arid Salinity Anomaly Index | **77.8%** |
| **VSI** | Vegetation Stress Index | **74.1%** |
| **OBEC** | Oil-Brine Emulsion Composite | **66.7%** |
| **FBC** | Ferrugination-Brine Composite | **66.7%** |
| **LBI** | Liquid Brine Index | **63.0%** |

*Validation threshold: anomalous pixel deviation > 0.01 above regional known-clean baseline.*

---

## 🛡️ Claim Philosophy

All indices in this atlas are built from published spectral physics. To establish defensive prior art for the community and protect these composites from predatory patenting, the claim for each novel composite is structured as:

> *A named, transparent, decision-ready composite built from established spectral mechanisms, domain gates, and confounder rejection — applied to a specific public-good screening workflow.*

- **We Claim**: The specific workflow, the multi-gate logic, the confounder rejection, and the civic framing.  
- **We Do Not Claim**: Invention of the underlying band physics, the individual ratios, or the environmental problem itself.

---

## 📚 Supporting Research & Data

| Resource | Contents |
|----------|----------|
| [Global Novel Index Survey](surveys/global-novel-index-survey.md) | Deep research document covering 74 global novel indices with full citations. |
| [Permian Basin Platform Survey](surveys/permian-basin-platform-survey.md) | 31-platform free satellite survey with integration roadmap. |
| [Global Public Good Atlas](surveys/global-public-good-atlas.md) | Scholarly synthesis of public-good band combinations. |
| [Limn Index Catalog](catalogs/limn-index-catalog.md) | 53-index catalog with TRRC validation rates. |
| [Civic Sentinel Composite Slate](catalogs/civic-sentinel-composite-slate.md) | 24-composite civic sentinel slate. |
| [Civic Sentinel Composite Atlas](catalogs/civic-sentinel-composite-atlas.md) | 18 ranked composites with full formulas. |
| [Formula Quick Reference](formulas/formula-quick-reference.md) | Every formula across all projects, consolidated into a single file. |

---

## 🎓 Citation & Reuse

Formulas in this atlas are released as public-good research. 
- **For validated indices** (PWCI, ASAI, VSI, OBEC, FBC, LBI), please cite the TRRC validation dataset and this repository. 
- **For proposed indices**, please cite the underlying spectral physics referenced in each entry.

**Key Scholarly Sources:**
- Kokaly et al. (2017). *USGS Spectral Library Version 7.*
- Green et al. (2023). "Performance and early results from EMIT." *IEEE TGRS* 61.
- Zhang et al. (2020). "Quantifying methane emissions from the Permian Basin from space." *Science Advances* 6(17).
- Mielke et al. (2024). "Neodymium mineral detection at Mountain Pass using EnMAP." *Scientific Reports* 14(1):20413.
- Pahlevan et al. (2026). "PACE OCI PFT retrieval." *Remote Sensing of Environment.*
- Hugelius et al. (2020). "Permafrost carbon vulnerability." *PNAS* 117(34).

---

*Published by [Globe & Atlas](https://globeandatlas.substack.com) | Last updated: May 2026*
