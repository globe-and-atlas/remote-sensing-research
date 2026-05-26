# Remote Sensing Research

**Globe & Atlas** | Public-good spectral index research for environmental monitoring.

This repository is the technical **Atlas** counterpart to the [Globe & Atlas](https://globeandatlas.substack.com) publication. It catalogs the electromagnetic physics, raw band formulas, confounder gates, and validation status behind public-good satellite screening workflows.

The focus is novel, newly formalized, or newly sensor-enabled satellite band combinations that can be computed from free, open-access sensors such as Sentinel-2, Sentinel-1, TROPOMI, EMIT, PACE, EnMAP, and Landsat. The goal is to make environmental monitoring formulas inspectable, reusable, and honest about their limits.

---

## 🗺️ The Atlas Index

**[`ATLAS.md`](ATLAS.md)** is the primary reference database — containing 116 named spectral indices across 13 environmental domains. Each entry is documented with:

- **Formula**: Ready to implement in JavaScript, Python, or database engines.
- **Spectral Physics**: Physical explanation of the surface interactions and band mechanics.
- **Confounder Rejection**: Domain gates and masks used to isolate clean anomalies.
- **Validation Status**: Empirically verified metrics against confirmed ground-truth events.
- **Novelty Tier**: Contribution category based on the literature gap and what Globe & Atlas adds (T1 Original Formula / T2 Standardized Formula / T3 Sensor-Enabled Formula).

*This is a living, public-good reference. Validated indices have been run against regional ground truth; proposed indices are grounded in published physics and awaiting field verification.*

---

## 🧭 Novelty & Contribution Tiers

The tier labels describe the specific contribution made here. They do not claim invention of the underlying electromagnetic physics, individual spectral bands, satellite sensors, or environmental phenomena.

- **T1 entries are original Globe & Atlas formulations**: named indices with formulas and workflows originated here.
- **T2 entries are formalization contributions**: the concept existed, but this atlas turns it into a named, reproducible formula.
- **T3 entries are sensor-enabled operationalizations**: the physics or approach may have been written about before, but newer open sensors make the workflow practical from orbit.

| Tier | What it means | Daniel Bally / Globe & Atlas contribution |
|------|---------------|----------------------------|
| **T1 — Original Formula** | No equivalent named, standardized formula for this screening purpose was found in the surveyed literature. | Originated the index name, wrote the formula, defined the workflow, and documented the public-good use case. |
| **T2 — Standardized Formula** | The detection concept exists in papers, reports, or practice, but remains qualitative, fragmented, unnamed, or lacking a clear reproducible formula. | Formalized the concept into a named index with explicit inputs, formula logic, gates, limitations, and decision context. |
| **T3 — Sensor-Enabled Formula** | The physics or analytic approach has been written about before, but it was not previously practical as an open, operational satellite index until newer sensors made the needed bands, cadence, or resolution available. | Translates the known physics into a computable open-sensor workflow and names the operational formula. |

In short: **T1 is original formulation, T2 is formalization, and T3 is operationalization made possible by new sensor capability.**

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

## 🏆 Top 25 Priority Novel Indices

This priority list is a qualitative triage, not a validation leaderboard.

**Selection criteria:** the ordering favors indices that combine four traits: likely unclaimed or under-formalized novelty, global applicability, policy-actionable output, and feasibility on currently available open sensors. In practice, the highest-priority indices are the ones that could turn existing satellite physics into a named, replicable public-good workflow with near-term operational value.

| Rank | Acronym | Name | Operational Significance |
|------|---------|------|--------------------------|
| 1 | **[TSEAI](ATLAS.md#tseai)** | TROPOMI–Sentinel-2 Emission Attribution Index | CH₄ source attribution at field scale — climate monitoring's most urgent gap |
| 2 | **[HABSDI](ATLAS.md#habsdi)** | HAB Species-Level Discrimination Index | Toxic vs. non-toxic cyanobacteria — PACE OCI UV bands make this globally possible |
| 3 | **[NPDefI](ATLAS.md#npdefi)** | N vs. P Deficiency Discrimination Index | Precision fertilizer prescription and runoff management from orbit |
| 4 | **[SMPDI](ATLAS.md#smpdi)** | Sargassum vs. Microplastic Discrimination Index | Disentangles global marine debris crises; current indices conflate them |
| 5 | **[FGDCI](ATLAS.md#fgdci)** | Frozen Ground Dielectric Change Index | Pan-Arctic freeze/thaw dynamics from Sentinel-1 SAR |
| 6 | **[CBSDI](ATLAS.md#cbsdi)** | Coral Bleaching Stage Discrimination Index | Classifies bleaching severity stages vs. binary surface detection |
| 7 | **[REESAI](ATLAS.md#reesai)** | Rare Earth Element Surface Anomaly Index | EnMAP bastnäsite/monazite Nd detection for clean energy supply chains |
| 8 | **[BSMTI](ATLAS.md#bsmti)** | Burn Severity Mineralogy Transition Index | Post-fire debris flow risk via EMIT soil mineralogy changes |
| 9 | **[PWTDI](ATLAS.md#pwtdi)** | Peatland Water Table Depth Index | Critical unmeasured variable in wetland carbon accounting |
| 10 | **[RDOCI](ATLAS.md#rdoci)** | River Dissolved Organic Carbon Index | PACE OCI UV channels make this orbital for the first time |
| 11 | **[AMDPHI](ATLAS.md#amdphi)** | Acid Mine Drainage pH Proxy Index | Mine-drainage acidity triage from open optical and hyperspectral data |
| 12 | **[TPERI](ATLAS.md#tperi)** | Thermokarst Pond Expansion Rate Index | Permafrost pond expansion velocity for carbon-release risk models |
| 13 | **[MEPSI](ATLAS.md#mepsi)** | CH₄ Ebullition Pond Spectral Proxy | Screens thaw ponds for methane ebullition risk where field flux data is sparse |
| 14 | **[ALSI](ATLAS.md#alsi)** | Active Layer Depth Thermal-Spectral Index | Active-layer depth proxy for Arctic infrastructure and carbon vulnerability |
| 15 | **[PSHRI](ATLAS.md#pshri)** | Post-Fire Soil Hydrophobicity Risk Index | Post-rain hydrophobic soil screening for debris-flow and runoff hazards |
| 16 | **[UBCDI](ATLAS.md#ubcdi)** | Understory vs. Canopy Burn Discrimination Index | Separates hidden understory burns from canopy-level fire damage |
| 17 | **[ISSAI](ATLAS.md#issai)** | ICESat-2 + Sentinel-1 Subsidence Attribution Index | Cross-checks lidar and InSAR deformation for infrastructure risk triage |
| 18 | **[GEAWSI](ATLAS.md#geawsi)** | GRACE-FO + ECOSTRESS Agricultural Water Stress Index | Links basin groundwater depletion to crop water stress and food-security alerts |
| 19 | **[SCFGOSI](ATLAS.md#scfgosi)** | Soil Carbon Functional Group Oxidation State Index | Hyperspectral soil-carbon quality proxy for degradation and accounting workflows |
| 20 | **[AFCDI](ATLAS.md#afcdi)** | Asbestos Fiber Chrysotile Detection Index | Public-health mineral hazard screening using diagnostic SWIR absorptions |
| 21 | **[CCRBI](ATLAS.md#ccrbi)** | Coal Combustion Residue Bioaccumulation Index | Coal ash exposure screening for wetlands, rivers, and nearby communities |
| 22 | **[SPSRI](ATLAS.md#spsri)** | Solar Panel Soiling Remote Index | Utility-scale solar soiling triage for clean-energy operations |
| 23 | **[SBCI](ATLAS.md#sbci)** | Sabkha Brine Chemistry Index | Hyperspectral arid-brine chemistry mapping in salt-flat environments |
| 24 | **[CSCAI](ATLAS.md#cscai)** | Caliche Surface Carbonate Accumulation Index | Dryland carbonate accumulation proxy for soil, water, and restoration planning |
| 25 | **[DLPEHI](ATLAS.md#dlpehi)** | Desert Locust Pre-Emergence Habitat Index | Early-warning habitat screen for locust emergence and food-security response |

---

## 🧪 Ground-Truth Validation

This section is separate from the priority list above: these are the indices already tested against a specific ground-truth dataset. The following indices have been tested against the Texas Railroad Commission (TRRC) 27-site Permian Basin produced water spill dataset:

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

All indices in this atlas are built from published spectral physics. The contribution is the named formula, the multi-gate workflow, the confounder rejection, and the public-good decision framing. To establish defensive prior art for the community and protect these composites from predatory patenting, the claim for each novel composite is structured as:

> *A named, transparent, decision-ready composite built from established spectral mechanisms, domain gates, and confounder rejection — applied to a specific public-good screening workflow.*

- **We Claim**: The index name, formula/workflow, multi-gate logic, confounder rejection, limitations, and civic framing described for each T1/T2/T3 contribution.
- **We Do Not Claim**: Invention of the underlying band physics, individual spectral ratios, satellite sensors, or environmental problem itself.

---

## 📚 Registry & Reference Files

The former `surveys/` and `catalogs/` documents have been consolidated into the current `registry/` files below.

| Resource | Contents |
|----------|----------|
| [Master Index Catalog](registry/master_index_catalog.md) | Unified 116-index registry with formulas, physics, novelty tiers, and claim posture. |
| [Spectral Index Comparative Analysis](registry/comparative_analysis.md) | Detailed technical comparison and scientific rationale of novel indices vs established baselines. |
| [Sensor Platforms Reference](registry/sensor_platforms.md) | Consolidated 31-platform open-sensor guide with public-benefit rankings and integration notes. |
| [Remote Sensing Science & Policy Guide](registry/scholarly_synthesis.md) | Scholarly synthesis, prior-art posture, ethical safeguards, and validation roadmap. |
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
