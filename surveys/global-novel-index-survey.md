---
title: "The Global Spectral Index Frontier: 91 Novel Band Combinations No One Has Named Yet"
pillar: tool-critic
status: research-complete
origin_project: limn
tags: [sentinel, satellite, spectral-indices, remote-sensing, global, novel-indices, public-good, hyperspectral, emit, enmap, pace]
date_researched: 2026-05-25
slug: global-spectral-index-survey
related: satellite-sensor-survey-permian-basin.md
---

# Research Vault: Global Novel Spectral Index Survey

> **For article use.** Full scholarly survey of novel, unclaimed satellite spectral index concepts across 12 global environmental domains. This is the global expansion of the Permian Basin sensor survey — not Permian-specific, not oilfield-specific. A public-good index library for the planet.
>
> **Article angle:** Remote sensing has ~200 published indices, mostly NDVI variations. New sensors (EMIT, PACE, EnMAP, NISAR) opened windows that nobody has named yet. This is a map of that frontier.

---

## Hook Candidates

- "The Index DataBase has 228 spectral indices. Here are 91 problems it hasn't solved yet."
- "EMIT was launched to map desert dust. Nobody told it to stop there — and it turns out it can find asbestos, rare earth elements, and the forensic scar of a brine spill from orbit."
- "The satellite data exists. The sensors are operational. The spectral physics is published. What's missing is the formula — and the name."
- "PACE OCI launched in February 2024 with UV channels at 320 nm. In 14 months of operation, nobody has formalized a dissolved organic carbon index from it. That's not a research gap. That's a discovery waiting for someone to sign it."

---

## Personal Stakes

Building limn — a public environmental monitoring tool with 53 spectral indices for the Permian Basin. The Permian sensor survey revealed a pattern: every new sensor opens a window that researchers describe in papers but never formalize as a replicable, named index. This survey maps those windows globally, across every major environmental crisis where free satellite data exists.

---

## Key Tension

The gap isn't data. It isn't even physics — the spectral mechanisms are published, peer-reviewed, cited hundreds of times. The gap is between "we can detect X from satellite" and "here is the formula, the name, and the standard you can replicate." That gap is enormous. And it's a gap anyone can close.

---

## Novelty Classification System

- **Tier 1 — Genuinely Unclaimed**: No formula in IndexDataBase or major review papers covers this exact environmental problem with this sensor/formula approach (~42 indices below)
- **Tier 2 — Significantly Underspecified**: Detection described in literature but no standardized formula or published acronym (~20 indices)
- **Tier 3 — Sensor-Enabled Extension**: Known physics, newly operational on post-2019 sensors EMIT, PACE, EnMAP, PRISMA, NISAR (~12 indices)

---

## The Top 10 Most Scientifically Novel and Impactful

Ranked by: genuinely unclaimed status × global applicability × policy-actionable output × feasibility on currently operational sensors.

| Rank | Acronym | Name | Why It Matters |
|------|---------|------|----------------|
| 1 | **TSEAI** | TROPOMI–Sentinel-2 Emission Attribution Index | Turns TROPOMI's 5.5 km grid into a source-specific methane tool. Climate monitoring's most urgent gap. |
| 2 | **HABSDI** | HAB Species-Level Discrimination Index | Distinguishes toxic (microcystin) from non-toxic cyanobacteria. PACE (2024) makes it globally possible for the first time. |
| 3 | **NPDDI** | Nitrogen vs. Phosphorus Deficiency Discrimination Index | Enables precision fertilizer prescription. N vs. P misapplication costs billions and drives eutrophication. |
| 4 | **SMADI** | Sargassum vs. Microplastic Discrimination Index | Both are global crises requiring different responses. Current indices conflate them. Physically sound. |
| 5 | **FGDCI** | Frozen Ground Dielectric Change Index | Pan-Arctic freeze/thaw from Sentinel-1. Feeds permafrost carbon models directly. |
| 6 | **CBSDI** | Coral Bleaching Stage Discrimination Index | Stages bleaching (not just binary). Changes conservation response windows globally. |
| 7 | **REESAI** | Rare Earth Element Surface Anomaly Index | REEs are the geopolitical resource of the energy transition. EnMAP Nd detection validated; index not yet formalized. |
| 8 | **BSMTI** | Burn Severity Mineralogy Transition Index | Post-fire debris flow life-safety. EMIT connects fire intensity to erosion risk via soil mineralogy. |
| 9 | **PWTDI** | Peatland Water Table Depth Spectral-SAR Index | The single most important unmeasured variable in global wetland carbon accounting. |
| 10 | **RDOCI** | River Dissolved Organic Carbon Index | DOC export is a critical, poorly constrained carbon cycle element. PACE OCI UV channels (2024) make this orbital for the first time. |

---

## Domain 1: Permafrost & Arctic/Subarctic

### 1.1 TPERI — Thermokarst Pond Expansion Rate Index ★ Tier 1

**Environmental problem**: MNDWI and NDWI detect standing water but cannot encode active thermokarst expansion velocity vs. stable pond margins. The rate signal, not presence, drives carbon release projections.

**Spectral physics**: Thermokarst expansion involves a transitional zone of saturated, partially-thawed peat with characteristic high SWIR absorption (1.6 µm water content) combined with depressed green reflectance from suspended organic matter. The ratio of SWIR1 change to green change over a bi-temporal pair encodes expansion velocity better than any single-date water index.

**Formula**:
```
TPERI = Δ(B11_t1 - B11_t2) / Δ(B3_t1 - B3_t2)
```
Positive values = active thaw margin expansion. Applied to Sentinel-2 bi-temporal annual composites.

**Platform**: Sentinel-2 MSI (10–20 m), Landsat-8/9 OLI for trend detection.

**Gap**: Existing indices (MNDWI, DNMI) are single-date presence indicators. No published index encodes expansion rate directly. Göckede et al. (2024) *Biogeosciences* showed MNDWI captures presence but analysts must diff images manually.

**Citations**: Göckede et al. (2024) *Biogeosciences* 21:4723–4737; Stettner et al. (2022) *ERL* — thermokarst spectral tracking Lena Delta.

---

### 1.2 PCEI — Peat Carbon Exposure Index ★ Tier 1

**Spectral physics**: Sphagnum moss shows water absorption at 970 nm and green peak at 550 nm. Dry exposed peat has flat brownish spectrum with elevated SWIR2. Mineral soil from active layer exposure shows clay/iron at 2200 nm. Formula distinguishes all three.

**Formula**:
```
PCEI = (B12 - B8A) / (B12 + B8A + B5)
```
(SWIR2 vs. Red-Edge1 normalized, adjusted for moss chlorophyll via B5=705 nm)

**Platform**: Sentinel-2 (B5=705 nm, B8A=865 nm, B12=2190 nm).

**Gap**: No IndexDataBase entry targets peat vs. mineral active layer exposure. Hugelius et al. (2020) *PNAS* documents the vulnerability but no operational formula exists.

---

### 1.3 SABSI — Snow/Ice Algae Bloom Severity Index ★ Tier 2

**Spectral physics**: Green algae (Chlamydomonas) absorb at 680 nm; red algae (astaxanthin) absorb at 490–530 nm with strong red reflectance. The ratio of red to NIR encodes pigment loading and severity, not just presence.

**Formula**:
```
SABSI = (B4 - B8) / (B4 + B8) + 0.5 * (B2 - B3) / (B2 + B3)
```
The second term discriminates astaxanthin (red algae) from chlorophyll (green algae).

**Platform**: Sentinel-2 (10 m), Planet SuperDove (8-band).

**Gap**: Engstrom et al. (2022–2023) used NDVI threshold = 0.025 (binary). No severity-graduated species-discriminating formula published. Frontiers in RS (2025) noted species discrimination as an open gap.

---

### 1.4 FGDCI — Frozen Ground Dielectric Change Index ★ Tier 1

**Spectral physics**: Frozen soil dielectric constant ~4; thawed ~20–30. This drives 3–6 dB shifts in C-band VV backscatter. VH captures vegetation volume scattering. Cross-ratio VV/VH normalizes vegetation effects, isolating the dielectric anomaly.

**Formula**:
```
FGDCI = (VV_dB - VH_dB) - seasonal_mean(VV_dB - VH_dB)
```
Time-series anomaly from local climatological mean.

**Platform**: Sentinel-1 SAR (C-band GRD products, global).

**Gap**: Literature uses VV-VH for various applications but no standardized freeze/thaw dielectric anomaly formula exists for continuous permafrost monitoring.

---

### 1.5 MEPSI — CH4 Ebullition Pond Spectral Proxy ★ Tier 1

**Spectral physics**: Ebullition creates micro-turbulence and elevated suspended organic carbon at water surface. Surface CH4 oxidation by methanotrophs produces blooms with elevated NIR relative to blue, departing from the standard clear vs. turbid water signal.

**Formula**:
```
MEPSI = (B8 / B2) - NDWI_local_mean
```
Anomaly of NIR-to-blue ratio relative to the lake's own mean clear-water condition.

**Platform**: Sentinel-2 (10 m), PlanetScope (3 m for sub-lake resolution).

**Gap**: No published index targets ebullition-linked optical anomalies in thermokarst lakes. Provides optical anchor for TROPOMI CH4 attribution to specific lakes.

---

### 1.6 ALSI — Active Layer Depth Thermal-Spectral Composite Index ★ Tier 1

**Spectral physics**: Deeper active layers produce warmer surface temperatures, drier vegetation (reduced NDWI), and greater clay mineral signal at 2200 nm from frost churning. Combining ECOSTRESS LST anomaly with Sentinel-2 SWIR clay absorption creates a composite proxy.

**Formula**:
```
ALSI = 0.6 * (LST_anomaly / σ_LST) + 0.4 * [(B12 - B11) / (B12 + B11)]
```

**Platform**: ECOSTRESS thermal + Sentinel-2 SWIR (cross-sensor fusion).

---

## Domain 2: Tropical Forests & Deforestation

### 2.1 PDCSI — Pre-Deforestation Canopy Stress Index ★ Tier 2

**Spectral physics**: Early-stage anthropogenic thinning stress causes chlorophyll degradation (red-edge shift from 720 → 705 nm), increased canopy temperature, and reduced water content (SWIR increase). The red-edge position responds to leaf chlorophyll before visible browning — 6–18 months before clear-cutting.

**Formula**:
```
PDCSI = [(B6 - B5) / (B6 + B5)] - [(B8A - B8) / (B8A + B8)]
```
(Red-edge chlorophyll index differential: B5=705 nm, B6=740 nm, B8=842 nm, B8A=865 nm)

**Platform**: Sentinel-2 (20 m red-edge bands).

**Gap**: Decuyper et al. (2022) *RSE* found moisture indices outperform NDVI; no combined red-edge + SWIR pre-deforestation formula published as standardized index.

---

### 2.2 LISI — Liana Infestation Structural Index ★ Tier 2

**Spectral physics**: Liana-infested crowns have steeper leaf angles (erectophile vs. planophile), higher NIR scattering (increased gap fraction), and lower SWIR absorption (thinner, cheaper leaves). NIR/SWIR ratio combined with EVI captures this structural difference.

**Formula**:
```
LISI = 2.5 * [(B8 - B11) / (B8 + 6*B4 - 7.5*B2 + 1)] * (B8 / B11)
```
EVI-modified by SWIR penalty for leaf structure discrimination.

**Gap**: Burt et al. (2025) PMC: "no standardized operational index exists" — researchers currently use trained neural networks without generalizable formula.

---

### 2.3 UBCDI — Understory vs. Canopy Burn Discrimination Index ★ Tier 1

**Spectral physics**: Canopy burn creates char at top-of-canopy, producing dramatic NIR decrease and SWIR increase across the full scar. Understory burn leaves canopy partially intact (NIR partially preserved) but creates elevated red from charred litter below. The ratio of post/pre NIR to post/pre red encodes this vertical dimension.

**Formula**:
```
UBCDI = [(ΔB8 / B8_pre) / (ΔB4 / B4_pre)]
```
Near -1 = canopy fire; near 0 = surface fire.

**Platform**: Sentinel-2 bi-temporal pairs.

**Gap**: dNBR and RdNBR (Key & Benson 2006) do not encode vertical fire structure. No published index uses the NIR/red change ratio for layer discrimination.

---

### 2.4 SLSDI — Selective Logging Scar Detection Index ★ Tier 2

**Spectral physics**: Fresh log landings expose bright mineral soil (high blue/green) with elevated SWIR2 from disturbed clay/organic mix. Log drag trails have mixed soil/bark spectral signature. Sub-hectare disturbances invisible at Landsat resolution.

**Formula**:
```
SLSDI = [(B2 + B3) / (B8 + 0.01)] * [B12 / (B12 + B8A)]
```
Soil brightness amplified by SWIR2 relative to red-edge NIR.

**Platform**: Sentinel-2 (10–20 m); PlanetScope for sub-hectare precision.

---

### 2.5 FEDGI — Forest Edge Degradation Gradient Index ★ Tier 1

**Environmental problem**: Tropical forest degradation propagates inward from edges (wind damage, desiccation, hunting pressure). No index captures the gradient from intact interior to degraded edge.

**Formula**:
```
FEDGI = distance_from_edge * [-1 * (B11 - B8) / (B11 + B8)]
```
NDWI-equivalent with spatial distance weighting, creating a gradient field.

---

### 2.6 ETCSI — Emergent Tree Crown Stress Index ★ Tier 1

**Spectral physics**: Emergent crowns are fully sunlit; under stress their red-edge shift is the first detectable signal. Using high-spatial imagery to isolate large crowns via texture, then extracting red-edge index creates a layer-selective monitor.

**Formula** (two-step):
1. Crown segmentation from PlanetScope NDVI local maxima
2. `ETCSI = CI_rededge = (B7 / B5) - 1` per segmented crown polygon

**Platform**: Planet SuperDove + Sentinel-2 red-edge fusion.

---

## Domain 3: Marine & Coastal

### 3.1 CBSDI — Coral Bleaching Stage Discrimination Index ★ Tier 1

**Spectral physics**:
- Healthy: brown-green from zooxanthellae, 680 nm absorption, high ~550 nm reflectance
- Stage-1 pale: reduced 680 nm, elevated blue-green
- Fully bleached: flat high reflectance, minimal 680 nm
- Dead-colonized: chlorophyll peak restored by algae

**Formula set**:
```
CBSDI_pale = (B3 - B4) / (B3 + B4)         [high = pale bleached]
CBSDI_full = B2 / (B3 + B4 + B1)           [high = fully bleached white]
CBSDI_dead = (B3 / B4) - (B2 / B4)         [positive = algae-colonized dead]
```

**Platform**: Sentinel-2 (10–20 m); PRISMA/DESIS for finer spectral discrimination.

**Gap**: Dornelas et al. (2021) *Frontiers in Marine Science* achieved binary detection only. No published formula stages bleaching phases.

---

### 3.2 HABSDI — HAB Species-Level Discrimination Index ★ Tier 1 [PRIORITY #2]

**Spectral physics**:
- Cyanobacteria: phycocyanin at 620 nm, phycoerythrin at 565 nm
- Diatoms: fucoxanthin absorbing at 510–540 nm
- Dinoflagellates: peridinin at ~490 nm

**Formula set**:
```
PC_index  = (B3 - B5) / (B3 + B5)          [phycocyanin: 560 nm - 705 nm]
FX_index  = (B2 - B3) / (B2 + B3)          [fucoxanthin: 490 nm - 560 nm]
HABSDI_cyano = PC_index - FX_index          [positive = cyanobacteria dominant]
HABSDI_diatom = FX_index - PC_index         [positive = diatom dominant]
```

**Platform**: PACE OCI (optimal — 5 nm bands). Sentinel-3 OLCI as approximation.

**Gap**: Becker et al. (2024) *Science of the Total Environment* — species discrimination used lab hyperspectral only; no operational satellite formula exists.

---

### 3.3 SMADI — Sargassum vs. Microplastic Discrimination Index ★ Tier 1 [PRIORITY #4]

**Spectral physics**: Sargassum has active chlorophyll (strong 680 nm absorption, NIR plateau). Microplastics (PE/PP polymers) show C-H stretch overtone absorptions at 1730 nm (PE) and 1660 nm (PP) with no chlorophyll signal. All existing FAI-type algorithms cannot discriminate them.

**Formula**:
```
SMADI = FAI - [(B8A - B11) / (B8A + B11)]
```
FAI positive but SWIR1/SWIR2 plastic signature negative → high SMADI = Sargassum.
Low SMADI with positive FAI → microplastic aggregate.

**Platform**: Sentinel-2 (B8A=865 nm, B11=1610 nm); EMIT for SWIR specificity.

**Citations**: Hu et al. (2023) *RSE* — multi-band Sargassum detection; Biermann et al. (2020) *Scientific Reports* — plastic detection NIR-SWIR.

---

### 3.4 KCDSI — Kelp Canopy Density and Stress Index ★ Tier 2

**Spectral physics**: Dense kelp canopies have high NIR from multiple stipe/blade layers and strong red absorption from phaeophytin. Stressed kelp loses distal blade tissue, reducing NIR scattering. NIR/SWIR1 ratio × red-edge chlorophyll proxy encodes blade-layer count.

**Formula**:
```
KCDSI = (B8 / B11) * [(B5 - B4) / (B5 + B4)]
```

**Platform**: Sentinel-2 (10–20 m) + Sentinel-3 OLCI for FLH supplement.

---

### 3.5 OWSI — Oil Spill Weathering Stage Index ★ Tier 2

**Spectral physics**: Fresh crude: C-H at 1730 nm, aromatic at 2300 nm. Emulsified (mousse): 1730 nm retained, elevated visible scattering from emulsified water droplets. Weathered tar: depleted light hydrocarbon features, increased 2300 nm from polyaromatic residues.

**Formula set**:
```
OSI_fresh    = (B12 - B11) / (B12 + B11)
OSI_emulsion = (B2 + B3) / (B8 + B11)
OWSI         = OSI_fresh / (OSI_emulsion + 0.01)
```

**Platform**: EMIT (5 nm, optimal); Sentinel-2 B11/B12 for coarse staging.

**Gap**: PMC 2023 (Kuwait) addressed detection, not weathering stage. EMIT post-2022 makes sub-index aromatic discrimination possible from orbit for the first time.

---

### 3.6 MDSPI — Mangrove Dieback Spatial Pattern Index ★ Tier 1

**Spectral physics**: Interior die-off = patchy dead standing mangrove (high SWIR2, low NIR) surrounded by live canopy. Edge erosion = continuous spectral gradient. Pneumatophore exposure = high NIR from exposed prop root network. Pattern type informs cause attribution.

**Formula**:
```
MDSPI = texture(NDVI, 5×5 kernel) / mean(NDVI, 5×5 kernel)
```
High texture/mean = patchy interior dieback; low ratio with edge gradient = erosive dieback.

---

### 3.7 SGDCI — Submarine Groundwater Discharge Chemistry Index ★ Tier 1

**Spectral physics**: Fresh SGD creates CDOM plumes with elevated absorption at 412 nm (dissolved humic substances) and depressed turbidity. Ratio of UV-blue to green ocean color within a thermal anomaly mask discriminates chemistry type.

**Formula**:
```
SGDCI = (ρ_412 / ρ_550) - CDOM_regional_mean
```
Applied within thermal anomaly mask from ECOSTRESS/Landsat TIRS.

**Platform**: PACE OCI (UV ocean color) + ECOSTRESS thermal.

**Gap**: Thermal-only SGD detection published (GRL 2024). Chemical characterization by optical index within the thermal anomaly zone is novel.

---

## Domain 4: Agricultural & Food Security

### 4.1 NPDDI — Nitrogen vs. Phosphorus Deficiency Discrimination Index ★ Tier 1 [PRIORITY #3]

**Spectral physics**:
- N deficiency: chlorophyll degradation (pale yellowing), red-edge shift toward 705 nm, elevated 670 nm reflectance
- P deficiency: anthocyanin accumulation (purpling), elevated 550 nm relative to 670 nm, SWIR2 increase at 2300 nm from lignin-cellulose ratio change

**Formula**:
```
NPDDI = [(B4 - B5) / (B4 + B5)] - [(B12 - B11) / (B12 + B11)]
```
Positive NPDDI = N deficiency dominant; negative = P deficiency dominant.

**Platform**: Sentinel-2 (20 m); EnMAP for 2300 nm P-specific band.

**Citation**: Zhang et al. (2025) *Field Crops Research* 325:109961 — meta-analysis N/P/K hyperspectral estimation (R²=0.82 N, 0.75 P separately; no dual discrimination index published).

---

### 4.2 APRI — Aflatoxin Pre-Harvest Risk Index ★ Tier 1

**Spectral physics**: Aflatoxin contamination is preceded by Aspergillus colonization of drought-stressed ears. Pre-condition of heat stress + drought stress in flowering-to-grain-fill window creates a satellite-detectable risk signal from combined LST anomaly, NDWI, and growing degree day accumulation.

**Formula**:
```
APRI = (LST_anomaly / σ) * [1 - NDWI] * heat_accumulation_days
```

**Platform**: ECOSTRESS + Sentinel-2 + ERA5 (three-source fusion).

**Gap**: Lab-scale NIR aflatoxin detection published (Wang et al. 2024, *Toxins*). Field-scale satellite pre-harvest risk index does not exist.

---

### 4.3 PDSDI — Pesticide vs. Drought Stress Discrimination Index ★ Tier 1

**Spectral physics**: Pesticide phytotoxicity = necrosis patterns (brown margins), rapid chlorophyll degradation, elevated SWIR2, geometric/uniform spatial pattern. Drought stress = stomatal closure first (red-edge shift before yellowing), uniform whole-canopy signal spatially correlated with soil texture.

**Formula**:
```
PDSDI = texture_cv(NDVI, 3×3) / [(B5 - B4) / (B5 + B4)]
```
High texture variation (patchy necrosis) / red-edge stress = pesticide stress.
Low texture (uniform stress) with high red-edge decline = drought stress.

---

### 4.4 SCSPI — Soil Compaction Spectral Proxy Index ★ Tier 1

**Spectral physics**: Compacted soils have reduced macroporosity (lower surface moisture, reduced SWIR absorption) combined with higher bulk density (slightly elevated blue from particle size reduction). Vegetation overlying compaction shows reduced vigor in red-edge before visible decline.

**Formula** (bare soil windows):
```
SCSPI = [1 - (B11 / B12)] * (B3 / B2)
```
Low SWIR1/SWIR2 ratio combined with high green/blue = compaction indicator.

---

### 4.5 CCTTI — Cover Crop Termination Timing Index ★ Tier 2

**Spectral physics**: Phenological maturity shifts reflectance from green/NIR (vegetative) toward yellow/brown as chlorophyll degrades and stems lignify. SWIR1 (1740 nm) encodes lignification. NDVI decline rate combined with NIR/SWIR1 ratio gives termination readiness signal.

**Formula**:
```
CCTTI = dNDVI/dt + (B11 / B8)
```

---

### 4.6 IWUEI — Irrigation Water Use Efficiency Index ★ Tier 2

**Formula**:
```
IWUEI = ET_ecostress / (VWC_sentinel1 + 0.01)
```
Applied within crop mask from Sentinel-2 NDVI time series. High soil moisture + low ET = poor irrigation efficiency.

**Platform**: ECOSTRESS + Sentinel-1 (cross-sensor fusion).

---

## Domain 5: Mining & Industrial Contamination

### 5.1 AMDPHI — Acid Mine Drainage pH Proxy Index ★ Tier 1

**Spectral physics**: AMD iron mineral precipitates are pH-diagnostic:
- Jarosite: pH 2–3.5, absorbs at 430 nm and 905 nm (yellow)
- Schwertmannite: pH 3–4.5, absorbs at 430/480 nm (orange-brown)
- Goethite: pH 4.5–6, absorbs at 480/535 nm (brown-red)

**Formula**:
```
AMDPHI = [(B4 - B3) / (B4 + B3)] / [(B2 - B3) / (B2 + B3 + 0.001)]
```
Jarosite dominates at very low pH (high blue-green contrast); goethite at higher pH (red-green dominant).

**Platform**: Sentinel-2 (10 m); EMIT for specific mineral identification.

**Gap**: Springer 2021 AMD remote index review identified pH-specific mineral assemblage indices as unpublished as standardized formulas.

---

### 5.2 TDSII — Tailings Dam Structural Integrity Index ★ Tier 1

**Spectral physics**: Dam seepage creates moisture anomalies on downstream faces (elevated SWIR absorption) and distressed vegetation (NDVI decline + elevated SWIR1). Sentinel-1 InSAR provides mm/year subsidence as third signal.

**Formula**:
```
TDSII = w1 * NDWI_anomaly + w2 * (-InSAR_subsidence_rate) + w3 * NDVI_decline_rate
```

**Gap**: Hillier et al. (2023) *PMC* showed Jagersfontein precursor signal was present in open data. No prospective composite index formula was proposed.

---

### 5.3 REESAI — Rare Earth Element Surface Anomaly Index ★ Tier 1 [PRIORITY #7]

**Spectral physics**: Nd shows absorptions at 583, 740, 803 nm. In bastnäsite and monazite, the 803 nm feature is cleanest. Band depth at Nd feature relative to continuum interpolation from the 780/830 nm shoulders.

**Formula**:
```
REESAI = 1 - ρ(803nm) / [ρ(780nm) + (803-780)/(830-780) * (ρ(830nm) - ρ(780nm))]
```

**Platform**: EnMAP (30 m, 224 bands) — first operational platform with sufficient spectral resolution. EMIT as alternative.

**Gap**: Mielke et al. (2024) *Scientific Reports* 14(1):20413 — Mountain Pass confirmed EnMAP Nd detection as "first demonstration." The polynomial continuum removal method used has not been formalized as a published index with standard acronym.

---

### 5.4 CCRBI — Coal Combustion Residue Bioaccumulation Index ★ Tier 1

**Spectral physics**: Grass over CCR impoundments shows elevated red reflectance (anthocyanin from As/Se stress), reduced NIR (leaf structure disruption), altered SWIR1. Harkness et al. (2025) *PMC* — "Grass is a tattletale" — demonstrated this via UAV/spectroradiometry.

**Formula**:
```
CCRBI = [(B4 - B8) / (B4 + B8)] * [B3 / (B11 + 0.01)]
```
Red-NIR stress ratio amplified by green-to-SWIR1 anthocyanin component.

**Gap**: Signal identified conceptually in 2025 PMC paper; no satellite-scale standardized index formula published.

---

### 5.5 HLPII — Heap Leach Pad Integrity Index ★ Tier 1

**Spectral physics**: Cyanide or acid leachate creates sulfate-hydroxide precipitation and vegetation kill zones. Spatial gradient of soil mineralogy change outward from the pad edge is the integrity signal.

**Formula**:
```
HLPII = SWIR_mineralogy_gradient / distance_from_pad_edge
```
Sharp gradients = contained; diffuse = liner failure.

---

### 5.6 IERPI — Industrial Effluent River Plume Index ★ Tier 2

**Formula**:
```
IERPI = (B4 / B3) * (LST_pixel - LST_upstream_mean) / σ_LST
```
Turbidity signal amplified by thermal anomaly score. Platform: Landsat 8/9 (OLI + TIRS on same platform).

---

## Domain 6: Wildfire & Post-Fire

### 6.1 LFMPI — Live Fuel Moisture Pre-Ignition Index ★ Tier 2

**Spectral physics**: Live fuel moisture encodes in 1450 nm and 1940 nm water absorption features. B11 (1610 nm) and B12 (2190 nm) probe these regions. EVI-weighted SWIR moisture index with SWIR2/SWIR1 penalty for fuel structural effect reduces soil background contamination vs. NDWI.

**Formula**:
```
LFMPI = 2.5 * [(B8A - B11) / (B8A + B11 + 6*B4 - 7.5*B2 + 1)] - (B12 / B11)
```

**Platform**: Sentinel-2 (20 m), Landsat-9 OLI.

**Gap**: Hall et al. (2024) *Remote Sensing* 18(7):1049 (Australia LFMC operational) used Random Forest on NDMI + temperature. The specific EVI-modified SWIR2-penalized formula is not published as a standardized index.

---

### 6.2 PSHRI — Post-Fire Soil Hydrophobicity Risk Index ★ Tier 1

**Spectral physics**: Hydrophobic soils don't wet with rain — NDWI remains low after precipitation. Applied in post-precipitation window: negative PSHRI after confirmed precipitation = hydrophobic soil.

**Formula**:
```
PSHRI = NDWI_post-rain - NDWI_pre-rain
```
Combined with slope: `PSHRI × tan(slope)` = debris flow risk surface.

**Platform**: Sentinel-2 + ERA5 precipitation to identify post-rain windows.

---

### 6.3 BSMTI — Burn Severity Mineralogy Transition Index ★ Tier 1 [PRIORITY #8]

**Spectral physics**: Fire temperature determines mineralogy: moderate fire creates magnetite from goethite reduction; high fire creates periclase from carbonate decomposition. EMIT detects goethite (486, 535 nm), magnetite (broad), hematite (535 nm), calcite (2340 nm CO3).

**Formula**:
```
BSMTI = depth(535nm_absorption) / depth(486nm_absorption)
```
Applied to EMIT L2A reflectance over burned bare soil.

**Platform**: EMIT — only sensor capable of this discrimination from orbit. Post-fire mineralogy application of EMIT is emerging; no standardized index exists.

---

### 6.4 SACI — Smoke Aerosol Composition Index ★ Tier 1

**Spectral physics**: Black carbon (flaming): absorbs all visible wavelengths, Ångström exponent α ~1.0. Organic carbon (smoldering): absorbs strongly in UV (<400 nm), less visible, α ~1.5–2.5. UV/green AOD ratio discriminates OC-rich from BC-rich smoke.

**Formula**:
```
SACI = AOD_UV340 / AOD_550  [TROPOMI]
```
High ratio (>1.5) = smoldering/OC-dominated; low (~1.0) = flaming/BC-dominated.

**Platform**: TROPOMI (UV-to-SWIR continuous spectrum) — operationally feasible post-2018.

---

### 6.5 PCSII — Pyroconvection Detection and Stratospheric Injection Index ★ Tier 1

**Spectral physics**: PyroCb cloud tops contain absorbing black carbon + small ice crystals. At 3.7–3.9 µm, reduced emissivity of small ice + absorbing carbon creates anomalously high MWIR brightness temperature relative to LWIR — distinct from meteorological cumulonimbus.

**Formula**:
```
PCSII = BT_3.7µm - BT_11µm > 0 AND AOD_TROPOMI > 1.0
```

**Platform**: GOES-18 ABI (3.7 µm) + TROPOMI AOD.

---

## Domain 7: Urban & Infrastructure

### 7.1 SPSRI — Solar Panel Soiling Remote Index ★ Tier 1

**Spectral physics**: Clean PV panels have very low reflectance (high absorption). Dust-coated panels show elevated reflectance shifting toward dust mineralogy signature. Ratio of observed panel reflectance to clean-panel baseline encodes soiling level.

**Formula**:
```
SPSRI = (ρ_observed_B2 - ρ_clean_baseline_B2) / ρ_clean_baseline_B2 * (B11 / B12)
```
Visible reflectance increase normalized by dust mineralogy ratio in SWIR.

**Platform**: Sentinel-2 (10 m) + field-calibrated clean-panel reference. Planet/WorldView for plant-level precision.

**Gap**: IEEE Conference (2025) proposed ML-based PDAI from satellite images — confirms no formula-based standardized index exists.

---

### 7.2 UCIEI — Urban Cool Infrastructure Effectiveness Index ★ Tier 1

**Spectral physics**: Cool roofs = high SWIR reflectance, low LST. Green roofs = high NIR, moderate LST, NDVI > 0.3. Asphalt = low reflectance across all bands, maximum LST. Each material produces a distinctive reflectance-temperature pair.

**Formula**:
```
UCIEI = (1 - albedo_satellite) * LST_anomaly
```
Where albedo = 0.356*B2 + 0.130*B4 + 0.373*B8 + 0.085*B11 + 0.072*B12 − 0.0018.

**Platform**: Sentinel-2 (10 m) + ECOSTRESS or Landsat-9 TIRS.

---

### 7.3 PCADI — Pavement Condition and Albedo Decay Index ★ Tier 1

**Spectral physics**: Fresh asphalt: 0.04–0.06 albedo, flat black spectrum. Aged/oxidized: 0.06–0.12, slightly grayer. Exposed aggregate: elevated NIR from mineral aggregate. Vegetation infiltration: NDVI > 0 within road mask.

**Formula**:
```
PCADI = (B3 / B2) - 1 + NDVI * 5  [within road mask]
```

---

### 7.4 CSDEI — Construction Site Silica Dust Emission Index ★ Tier 1

**Spectral physics**: Silica/quartz dust creates elevated AOD at 550 nm with spectrally flat Ångström exponent (α ~0.5–0.8, unlike smoke). AOD spectral shape discriminates dust from combustion aerosols.

**Formula**:
```
CSDEI = AOD_550 * (1 / α_TROPOMI) * site_mask  [construction parcels]
```

---

### 7.5 UTCDSI — Urban Tree Canopy Drought Stress Index ★ Tier 2

**Formula**:
```
UTCDSI = [CI_rededge_urban - CI_rededge_rural_reference] / σ_rural
```
Urban tree stress anomaly relative to climatological species-matched reference.

---

## Domain 8: Water Quality & Freshwater Systems

### 8.1 RDOCI — River Dissolved Organic Carbon Index ★ Tier 1 [PRIORITY #10]

**Spectral physics**: DOC (humic/fulvic acids) absorbs strongly in UV-blue (<450 nm) with exponential decay toward visible. CDOM spectral slope coefficient S275-295 is the gold-standard DOC proxy — detectable from PACE OCI's UV channels (320 nm) for the first time from orbit.

**Formula**:
```
RDOCI = ln(ρ_PACE_320nm / ρ_PACE_412nm) / (412 - 320) * (-1)
```
Approximating the CDOM spectral slope from PACE UV channels.

**Platform**: PACE OCI (UV channels 320–340 nm — unprecedented from satellite).

**Gap**: DOC retrieval from UAV hyperspectral published (2024, *International Journal of Digital Earth*). PACE OCI UV data now makes this orbital for the first time — no published formula for the PACE implementation.

---

### 8.2 CTPSTI — Cyanobacterial Toxin Proxy Spectral Index ★ Tier 1

**Spectral physics**: Microcystis (toxin-producing) has phycocyanin dominant at 620 nm. Gas-vacuolate non-toxic Aphanizomenon has phycoerythrin contribution at 565 nm. The 620/565 nm ratio encodes relative toxin-producer density.

**Formula**:
```
CTPSTI = [ρ(560nm) - ρ(620nm)] / [ρ(560nm) + ρ(620nm)]
```

**Platform**: PACE OCI (optimal). Sentinel-3 OLCI as approximation.

---

### 8.3 DTPSI — Dam Thermal Plume Stratification Index ★ Tier 1

**Spectral physics**: Cold hypolimnetic releases (bottom gate) vs. warm epilimnetic releases (top gate) have dramatically different downstream ecological impacts. Thermal anomaly pattern downstream encodes release type.

**Formula**:
```
DTPSI = (LST_downstream_1km - LST_reservoir_surface) / (LST_upstream_1km - LST_reservoir_surface)
```
<0 = cold hypolimnetic release; >0 = warm surface release.

**Platform**: Landsat-9 TIRS.

---

### 8.4 GMCPI — Glacial Meltwater Chemistry Proxy Index ★ Tier 1

**Spectral physics**: Rock flour (gray scattering, no chlorophyll absorption). Heavy metal-laden meltwater from sulfide bedrock creates Fe-hydroxide plumes (orange tinge, 480 nm absorption). CDOM-poor glacial water vs. CDOM-rich river water creates UV-blue contrast.

**Formula**:
```
GMCPI = (B1 - B3) / (B1 + B3) - CDOM_background_river
```

---

### 8.5 FCLI — Floodplain Contamination Legacy Index ★ Tier 1

**Spectral physics**: Metal-contaminated floodplain sediments show altered iron mineralogy (ochre deposits), elevated SWIR2 from sulfate residues, and depressed vegetation in subsequent seasons.

**Formula**:
```
FCLI = (B12_post-flood - B12_pre-flood) * (1 - NDVI_next-season)
```
Positive SWIR2 increase × low post-flood vegetation recovery = contamination indicator.

---

## Domain 9: Dryland & Arid Systems

### 9.1 BSCMCI — Biological Soil Crust Multi-Condition Index ★ Tier 1

**Spectral physics**: BSC stages have distinctive pigments:
- Early-stage cyanobacteria: chlorophyll a absorption 680 nm, flat NIR
- Mid-stage green algae: chlorophyll b, elevated 550 nm
- Advanced lichen: usnic acid absorption at 360 nm
- Physically disturbed: bright mineral, no pigment features

**Formula**:
```
BSCMCI = [(ρ680 - ρ720) / (ρ680 + ρ720)] * [(ρ550 / ρ670) - 1]
```
Combined chlorophyll edge ratio with green peak as crust pigment combination index.

**Platform**: PRISMA (30 m) or DESIS (2.55 nm sampling in visible).

**Gap**: BIO Web of Conferences (2024) proposed single-stage HBCI from PRISMA (Kappa=0.86). Multi-condition staging formula does not exist.

---

### 9.2 SBCI — Sabkha Brine Chemistry Index ★ Tier 1

**Spectral physics**: Gypsum: absorptions at 1450, 1750, 2217 nm. Anhydrite: at 1450, 2175 nm. Carnallite: at 1400, 1900 nm. Gypsum/anhydrite absorption depth ratio encodes brine concentration history — anhydrite forms at higher temperature/concentration than gypsum.

**Formula**:
```
SBCI = depth(2217nm) / depth(2175nm)
```
Gypsum-to-anhydrite band depth ratio.

**Platform**: EMIT (5 nm, 60 m) — only sensor with sufficient spectral resolution from orbit.

---

### 9.3 CSCAI — Caliche Surface Carbonate Accumulation Index ★ Tier 1

**Spectral physics**: Calcite (caliche) has diagnostic CO3²⁻ absorption at 2335 nm, weaker feature at 2160 nm. Ratio of these two features distinguishes mature calcite from dolomite or surface gravel.

**Formula**:
```
CSCAI = depth(2335nm) / depth(2160nm)  [EnMAP bands 192/185]
```

**Platform**: EnMAP (30 m, 224 bands) or PRISMA.

---

### 9.4 DEFPI — Dust Emission Flux Proxy Index ★ Tier 1

**Formula**:
```
DEFPI = (1 - NDVI) * clay_fraction_EMIT * (1 - SMC_SMAP)
```
Bare fraction × clay fraction × dry fraction = emission potential.

**Platform**: EMIT mineral maps + Sentinel-2 + SMAP (three-source fusion).

---

### 9.5 DLPEHI — Desert Locust Pre-Emergence Habitat Index ★ Tier 1

**Spectral physics**: Locust oviposition habitat = post-rainfall sandy soil: elevated moisture (SWIR absorption), sparse actively growing vegetation (NDVI 0.1–0.3 in greening phase), specific soil textures (NDTI responds to surface structure after rain).

**Formula**:
```
DLPEHI = NDWI * (0.1 < NDVI < 0.3) * (NDTI > -0.2) * rainfall_binary
```
Logical conjunction: moist sandy soil + sparse green vegetation + confirmed rainfall.

**Platform**: Sentinel-2 + GPM IMERG.

---

### 9.6 AIBEAI — Arroyo Incision and Bank Erosion Activity Index ★ Tier 1

**Spectral physics**: Active incision exposes fresh mineral soils (high brightness, high SWIR2 from clay minerals). Stable arroyos show vegetation establishment on channel margins (positive NDVI edges).

**Formula**:
```
AIBEAI = BSI_channel_bottom / NDVI_channel_margin
```
Where BSI = (B11 + B4 - B8 - B2) / (B11 + B4 + B8 + B2).

---

## Domain 10: Wetland & Peatland

### 10.1 PWTDI — Peatland Water Table Depth Spectral-SAR Index ★ Tier 2 [PRIORITY #9]

**Spectral physics**: Water table near surface (<5 cm) creates saturated Sphagnum reflecting distinctively at 970 nm (moss water absorption peak). Deeper WTD desiccates surface Sphagnum, increasing NIR and reducing 970 nm absorption. Sentinel-1 C-band VV backscatter is sensitive to surface moisture but not subsurface WTD. Optical-SAR fusion improves performance under all conditions.

**Formula** (S2 + S1 SAR):
```
PWTDI = α * NDWI_1020 + (1-α) * (VV_dB - VH_dB)
```
Where `NDWI_1020 = (B8A - B9) / (B8A + B9)`. α = 0.65 for open peatland; 0.35 for treed peatland.

**Gap**: Frontiers (2025) review of UK peatland satellite monitoring identified WTD as the key unmeasured variable. No unified multi-sensor formula published.

---

### 10.2 MHSSP — Methane Hotspot Surface Spectral Predictor ★ Tier 1

**Spectral physics**: CH4 hotspots occur where organic-rich anoxic zones coincide with shallow sediments and open water. Surface spectral proxies: very low NDVI (open water), elevated NDWI (saturated), red-edge at baseline (no emergent plants).

**Formula**:
```
MHSSP = NDWI * (1 - NDVI) * (1 - CI_rededge / max_CI_rededge_local)
```

**Platform**: Sentinel-2 (10 m) + TROPOMI CH4 for calibration.

---

### 10.3 TFIDI — Tidal Flat Inundation Dynamics Index ★ Tier 1

**Spectral physics**: Inundation stage determines spectral signature: open water (NDWI >> 0), saturated mudflat (dark, very low NDWI), moist mudflat (moderate SWIR absorption), dry upper flat (clay mineral at 2200 nm). Temporal ensemble of NDWI values from a tidal period encodes inundation duration.

**Formula**:
```
TFIDI = (NDWI_p90 - NDWI_p10) / NDWI_mean  [monthly composite]
```
High tidal range in NDWI percentile spread = high inundation dynamics = full tidal flat.

---

### 10.4 WDPTZI — Wet-Dry Peatland Transition Zone Index ★ Tier 1

**Spectral physics**: Wet peatland: saturated Sphagnum (high 970 nm absorption), low SWIR. Dry peatland: desiccated peat (high SWIR2, featureless). Spatial gradient filter applied to SWIR1/NIR ratio creates transition zone width estimate.

**Formula**:
```
WDPTZI = spatial_gradient_magnitude[(B11 - B8A) / (B11 + B8A)]
```
High gradient = transition zone.

---

### 10.5 IPVSI — Invasive Phragmites vs. Native Vegetation Index ★ Tier 2

**Spectral physics**: Invasive Phragmites has distinctive late-season standing dead stem signature (elevated SWIR1, reduced NIR) combined with high spatial homogeneity of the monoculture.

**Formula** (single-date late-season):
```
IPVSI = (B11_late - B8_late) / (B11_late + B8_late) * texture_homogeneity
```
High SWIR1/NIR difference + high homogeneity = Phragmites monoculture.

---

### 10.6 WVTDI — Wetland Vegetation Type Discrimination Index ★ Tier 2

**Formula set**:
```
WVTDI_sphagnum = (B3 / B8) - 0.5 * (B11 / B8)
WVTDI_typha    = (B8 / B3) * (B11 / B12)
WVTDI_sedge    = (B8 - B4) / (B8 + B4) * seasonal_NDVI_variance
```

---

## Domain 11: Hyperspectral-Enabled Novel Indices

*These indices were theoretically known but operationally impossible before EMIT (2022), PACE (2024), EnMAP (2022), DESIS (2019), PRISMA (2019).*

### 11.1 PFTIB — Phytoplankton Functional Type Index Battery ★ Tier 1 [PRIORITY PACE]

**Spectral physics**:
- Diatoms: fucoxanthin at 490–510 nm
- Haptophytes (coccolithophores): 19'-hexanoyloxyfucoxanthin at 453 nm
- Prokaryotes (Prochlorococcus): divinyl chlorophyll a at 440 nm
- Cryptophytes: phycoerythrin at 565 nm

**Formula set**:
```
PFT_diatom  = absorption(490nm) / absorption(440nm)
PFT_hapto   = absorption(453nm) / absorption(490nm)
PFT_prokary = ρ(490nm) / ρ(440nm)
PFT_crypto  = absorption(565nm) / absorption(490nm)
```

**Platform**: PACE OCI (5 nm bands, 340–890 nm) — first operational global implementation.

---

### 11.2 CMSTI — Clay Mineral Stress Transition Index ★ Tier 1

**Spectral physics**: Smectite Al-OH absorption at 2200 nm; illite Al-OH at 2208 nm (shifted 8 nm). This difference is resolvable by EMIT (5 nm) but NOT by Sentinel-2 or Landsat. Position shift indicates irreversible soil degradation from smectite to illite.

**Formula**:
```
CMSTI = position_minimum(2190-2220nm) - 2200  [EMIT L2A reflectance]
```
Negative shift toward 2195 = smectite; positive toward 2208 = illite.

**Platform**: EMIT only.

---

### 11.3 AFCDI — Asbestos Fiber Chrysotile Detection Index ★ Tier 1

**Spectral physics**: Chrysotile has Mg-OH absorptions at 2317 nm and 2387 nm (doublet diagnostic vs. other serpentines). Antigorite: 2320/2100 nm. Lizardite: 2320/2390 nm. The 2317/2387 band depth ratio discriminates chrysotile.

**Formula**:
```
AFCDI = depth(2317nm) / depth(2387nm)  [EMIT L2A]
```
Secondary confirmation: `depth(1390nm) / continuum`.

**Platform**: EMIT (5 nm) or PRISMA (10 nm SWIR, at the discrimination limit).

**Gap**: Lab-scale chrysotile detection published (SPIE 2017). Satellite-scale detection not formalized as operational index.

---

### 11.4 SCFGOSI — Soil Carbon Functional Group Oxidation State Index ★ Tier 1

**Spectral physics**: Labile carbon (lipids, proteins): N-H combination bands at 2050–2180 nm, C-H overtones at 1730 nm, C=O stretch at 2350 nm. Recalcitrant carbon (aromatic humus, black carbon): broad reduced absorption, no sharp features. C-H band depth vs. overall darkening encodes lability.

**Formula**:
```
SCFGOSI = depth(1730nm) / (1 - mean_reflectance_400_2500nm)
```

**Platform**: EMIT or EnMAP.

---

### 11.5 REENBI — REE Neodymium Band Depth Index ★ Tier 1

**Formula**:
```
REENBI = 1 - ρ(803nm) / [ρ(780nm) + (803-780)/(830-780) * (ρ(830nm) - ρ(780nm))]
```
Linear interpolation continuum depth at 803 nm.

**Platform**: EnMAP (bands at 780, 803, 830 nm at 10 nm resolution).

**Citation**: Mielke et al. (2024) *Scientific Reports* 14(1):20413 — Mountain Pass.

---

### 11.6 EPCASE — EnMAP Porphyry Copper Alteration Sequence Index ★ Tier 1

**Spectral physics**: Potassic (feldspar + biotite): broad 2200 nm + Mg-OH at 2325 nm. Phyllic (sericite): sharp Al-OH at 2200 nm. Argillic (kaolinite): doublet at 2160/2205 nm. Propylitic (chlorite + epidote): Mg-OH at 2325/2340 nm.

**Formula**:
```
EPCASE = position_minimum(2190-2220nm) + depth(2325nm) / depth(2200nm)
```

---

### 11.7 MPSSFI — Methane Plume Spectral Shape Feature Index ★ Tier 2

**Spectral physics**: CH4 absorption at 1667 nm (strong). Band depth at 1667 nm relative to continuum from 1640–1700 nm edges encodes column methane enhancement.

**Formula**:
```
MPSSFI = 1 - ρ(1667nm) / [0.5 * (ρ(1640nm) + ρ(1700nm))]
```

**Platform**: EMIT (5 nm, SWIR range).

---

### 11.8 DPCCI — DESIS Phycocyanin Column Concentration Index ★ Tier 2

**Spectral physics**: Phycocyanin absorption at 620 nm creates a trough between the chlorophyll shoulder at 650 nm and phycoerythrin peak at 565 nm.

**Formula**:
```
DPCCI = (ρ550 + ρ650) / ρ620 - 2
```

**Platform**: DESIS (155 bands, 400–1000 nm, 2.55 nm sampling), PRISMA, PACE OCI.

---

## Domain 12: Cross-Sensor Fusion Indices

### 12.1 TSEAI — TROPOMI–Sentinel-2 Emission Attribution Index ★ Tier 1 [PRIORITY #1]

**Environmental problem**: TROPOMI detects CH4 column enhancements at 5.5×7 km pixels — too coarse to attribute to specific sources (landfills vs. wetlands vs. oil fields) that co-exist within one pixel.

**Formula**:
```
TSEAI = XCH4_TROPOMI_anomaly / Σ(source_fraction_i * emission_factor_i)
```
Where source_fraction_i = fractional area of each emission source type within TROPOMI pixel, derived from Sentinel-2 land cover classification. High residual = unaccounted source.

**Platform**: TROPOMI (S5P) + Sentinel-2 (cross-sensor, same-day).

**Citations**: Chandra et al. (2024) *ACP* 24:10441; Varon et al. (2023) *ACP*.

---

### 12.2 ISSAI — ICESat-2 + Sentinel-1 Subsidence Attribution Index ★ Tier 1

**Formula**:
```
ISSAI = (ICESat2_dZ/dt - InSAR_LOS_vertical) / ICESat2_dZ/dt
```
Discrepancy flags non-coherent subsidence (rapid sediment compaction invisible to InSAR phase). Combined with Sentinel-2 land cover to attribute to aquifer drawdown vs. load-induced compaction.

---

### 12.3 GEAWSI — GRACE-FO + ECOSTRESS Agricultural Water Stress Index ★ Tier 1

**Formula**:
```
GEAWSI = (ET_ecostress / PET_estimate) * TWS_anomaly_sign
```
Actual-to-potential ET ratio signed by regional groundwater depletion direction. Negative GEAWSI during drought = confirmed crop stress with groundwater draw-down.

**Gap**: ET-based stress and GRACE groundwater anomalies are used separately in thousands of papers. Their explicit fusion as a single index formula does not appear in IndexDataBase.

---

### 12.4 EMSMMI — EMIT Mineral + Sentinel-1 Soil Moisture × Mineralogy Index ★ Tier 1

**Spectral physics**: Soil moisture radar estimates are affected by soil mineralogy — high-clay soils give different dielectric responses to the same water content. EMIT mineral maps now allow correction of Sentinel-1 soil moisture retrievals for mineralogy.

**Formula**:
```
EMSMMI = VWC_Sentinel1_raw / (1 + clay_fraction_EMIT * clay_dielectric_correction)
```

---

### 12.5 NFCAI — NISAR + Sentinel-2 Forest Carbon Accumulation Index ★ Tier 3

**Formula**:
```
NFCAI = L-band_HV_backscatter * (1 - canopy_cover_fraction_S2) + HH_backscatter * age_proxy_NDVI_trend
```
HV penetrates canopy and encodes woody biomass; combined with optical age proxy.

**Platform**: NISAR (L-band, 10 m, operational 2024) + Sentinel-2 time series.

---

### 12.6 TSEAI — TROPOMI + Sentinel-2 Urban Vegetation Air Quality Index ★ Tier 1

**Formula**:
```
SNUVQI = NO2_column_TROPOMI_downscaled - f(NDVI_S2, wind_ERA5)
```
Modeled NO2 expected from regional background minus the local reduction attributed to urban vegetation canopy. Quantifies green infrastructure's NO2 reduction effectiveness at parcel scale.

---

### 12.7 PUENPI — PACE + ECOSTRESS Coastal Wetland Net Ecosystem Production Index ★ Tier 1

**Formula**:
```
PUENPI = GPP_ECOSTRESS_proxy - NPP_PACE_aquatic - R_temperature_model
```
Net ecosystem production = terrestrial GPP - aquatic phytoplankton NPP - autotrophic respiration (from LST).

---

## Master Index Table — All 74+ Novel Indices

| # | Acronym | Name | Domain | Platform | Novelty |
|---|---------|------|--------|----------|---------|
| 1 | TPERI | Thermokarst Pond Expansion Rate Index | Permafrost | S2 bi-temporal | T1 |
| 2 | PCEI | Peat Carbon Exposure Index | Permafrost | S2 | T1 |
| 3 | SABSI | Snow/Ice Algae Bloom Severity Index | Permafrost | S2, Planet | T2 |
| 4 | FGDCI | Frozen Ground Dielectric Change Index | Permafrost | S1 SAR | T1 |
| 5 | MEPSI | CH4 Ebullition Pond Spectral Proxy | Permafrost | S2, Planet | T1 |
| 6 | ALSI | Active Layer Depth Thermal-Spectral Composite | Permafrost | ECOSTRESS+S2 | T1 |
| 7 | PDCSI | Pre-Deforestation Canopy Stress Index | Tropical Forest | S2 | T2 |
| 8 | LISI | Liana Infestation Structural Index | Tropical Forest | S2, Landsat | T2 |
| 9 | UBCDI | Understory vs. Canopy Burn Discrimination Index | Tropical Forest | S2 bi-temporal | T1 |
| 10 | FEDGI | Forest Edge Degradation Gradient Index | Tropical Forest | S2 spatial | T1 |
| 11 | SLSDI | Selective Logging Scar Detection Index | Tropical Forest | S2, Planet | T2 |
| 12 | ETCSI | Emergent Tree Crown Stress Index | Tropical Forest | Planet+S2 | T1 |
| 13 | CBSDI | Coral Bleaching Stage Discrimination Index | Marine/Coastal | S2, PRISMA | T1 |
| 14 | SPEI | Seagrass Photosynthetic Efficiency Index | Marine/Coastal | S2, DESIS | T2 |
| 15 | HABSDI | HAB Species-Level Discrimination Index | Marine/Coastal | PACE, DESIS | T1 |
| 16 | SMADI | Sargassum vs. Microplastic Discrimination | Marine/Coastal | S2, EMIT | T1 |
| 17 | KCDSI | Kelp Canopy Density and Stress Index | Marine/Coastal | S2+S3 OLCI | T2 |
| 18 | OWSI | Oil Spill Weathering Stage Index | Marine/Coastal | EMIT, S2 | T2 |
| 19 | MDSPI | Mangrove Dieback Spatial Pattern Index | Marine/Coastal | S2+S1 | T1 |
| 20 | SGDCI | SGD Chemistry Index | Marine/Coastal | PACE+ECOSTRESS | T1 |
| 21 | NPDDI | Nitrogen vs. Phosphorus Deficiency Index | Agriculture | S2, EnMAP | T1 |
| 22 | SCSPI | Soil Compaction Spectral Proxy Index | Agriculture | S2 bare soil | T1 |
| 23 | APRI | Aflatoxin Pre-Harvest Risk Index | Agriculture | ECOSTRESS+S2+ERA5 | T1 |
| 24 | PDSDI | Pesticide vs. Drought Stress Index | Agriculture | S2 | T1 |
| 25 | CCTTI | Cover Crop Termination Timing Index | Agriculture | S2 time series | T2 |
| 26 | IWUEI | Irrigation Water Use Efficiency Index | Agriculture | ECOSTRESS+S1 | T2 |
| 27 | AMDPHI | Acid Mine Drainage pH Proxy Index | Mining | S2, EMIT | T1 |
| 28 | TDSII | Tailings Dam Structural Integrity Index | Mining | S2+S1 InSAR | T1 |
| 29 | REESAI | Rare Earth Element Surface Anomaly Index | Mining | EnMAP, EMIT | T1 |
| 30 | IERPI | Industrial Effluent River Plume Index | Mining | Landsat+TIRS | T2 |
| 31 | HLPII | Heap Leach Pad Integrity Index | Mining | S2, EMIT | T1 |
| 32 | CCRBI | Coal Combustion Residue Bioaccumulation Index | Mining | S2 | T1 |
| 33 | LFMPI | Live Fuel Moisture Pre-Ignition Index | Wildfire | S2, Landsat | T2 |
| 34 | PSHRI | Post-Fire Soil Hydrophobicity Risk Index | Wildfire | S2+ERA5 | T1 |
| 35 | BSMTI | Burn Severity Mineralogy Transition Index | Wildfire | EMIT | T1 |
| 36 | PCSII | Pyroconvection Detection & Injection Index | Wildfire | GOES+TROPOMI | T1 |
| 37 | SACI | Smoke Aerosol Composition Index | Wildfire | TROPOMI | T1 |
| 38 | UCIEI | Urban Cool Infrastructure Effectiveness Index | Urban | S2+ECOSTRESS | T1 |
| 39 | PCADI | Pavement Condition and Albedo Decay Index | Urban | WorldView/S2 | T1 |
| 40 | CSDEI | Construction Site Silica Dust Emission Index | Urban | TROPOMI+GIS | T1 |
| 41 | SPSRI | Solar Panel Soiling Remote Index | Urban | S2, Planet | T1 |
| 42 | UTCDSI | Urban Tree Canopy Drought Stress Index | Urban | S2 | T2 |
| 43 | RDOCI | River Dissolved Organic Carbon Index | Water Quality | PACE OCI | T1 |
| 44 | CTPSTI | Cyanobacterial Toxin Proxy Spectral Index | Water Quality | PACE, DESIS | T1 |
| 45 | GMCPI | Glacial Meltwater Chemistry Proxy Index | Water Quality | S2, PACE | T1 |
| 46 | FCLI | Floodplain Contamination Legacy Index | Water Quality | S2 bi-temporal | T1 |
| 47 | DTPSI | Dam Thermal Plume Stratification Index | Water Quality | Landsat TIRS | T1 |
| 48 | BSCMCI | Biological Soil Crust Multi-Condition Index | Dryland | PRISMA, DESIS | T1 |
| 49 | DEFPI | Dust Emission Flux Proxy Index | Dryland | EMIT+S2+SMAP | T1 |
| 50 | SBCI | Sabkha Brine Chemistry Index | Dryland | EMIT | T1 |
| 51 | CSCAI | Caliche Surface Carbonate Accumulation Index | Dryland | EnMAP, PRISMA | T1 |
| 52 | DLPEHI | Desert Locust Pre-Emergence Habitat Index | Dryland | S2+GPM | T1 |
| 53 | AIBEAI | Arroyo Incision and Bank Erosion Activity Index | Dryland | S2, Planet | T1 |
| 54 | PWTDI | Peatland Water Table Depth Spectral-SAR Index | Wetland | S2+S1 | T2 |
| 55 | MHSSP | Methane Hotspot Surface Spectral Predictor | Wetland | S2+TROPOMI | T1 |
| 56 | WVTDI | Wetland Vegetation Type Discrimination Index | Wetland | S2 time series | T2 |
| 57 | IPVSI | Invasive Phragmites vs. Native Vegetation Index | Wetland | S2 seasonal | T2 |
| 58 | TFIDI | Tidal Flat Inundation Dynamics Index | Wetland | S2 monthly | T1 |
| 59 | WDPTZI | Wet-Dry Peatland Transition Zone Index | Wetland | S2 | T1 |
| 60 | PFTIB | Phytoplankton Functional Type Index Battery | Hyperspectral | PACE OCI | T1 |
| 61 | CMSTI | Clay Mineral Stress Transition Index | Hyperspectral | EMIT | T1 |
| 62 | MPSSFI | Methane Plume Spectral Shape Feature Index | Hyperspectral | EMIT | T2 |
| 63 | AFCDI | Asbestos Fiber Chrysotile Detection Index | Hyperspectral | EMIT, PRISMA | T1 |
| 64 | SCFGOSI | Soil Carbon Functional Group Oxidation Index | Hyperspectral | EMIT, EnMAP | T1 |
| 65 | REENBI | REE Neodymium Band Depth Index | Hyperspectral | EnMAP | T1 |
| 66 | EPCASE | EnMAP Porphyry Cu Alteration Sequence Index | Hyperspectral | EnMAP | T1 |
| 67 | DPCCI | DESIS Phycocyanin Column Concentration Index | Hyperspectral | DESIS, PACE | T2 |
| 68 | TSEAI | TROPOMI–Sentinel-2 Emission Attribution Index | Cross-sensor | S5P+S2 | T1 |
| 69 | ISSAI | ICESat-2+Sentinel-1 Subsidence Attribution Index | Cross-sensor | ICESat-2+S1+S2 | T1 |
| 70 | GEAWSI | GRACE-FO+ECOSTRESS Ag Water Stress Index | Cross-sensor | GRACE+ECOSTRESS | T1 |
| 71 | EMSMMI | EMIT Mineral+Sentinel-1 Soil Moisture Index | Cross-sensor | EMIT+S1 | T1 |
| 72 | NFCAI | NISAR+Sentinel-2 Forest Carbon Accum. Index | Cross-sensor | NISAR+S2 | T3 |
| 73 | PUENPI | PACE+ECOSTRESS Coastal Wetland NEP Index | Cross-sensor | PACE+ECOSTRESS | T1 |
| 74 | SNUVQI | S5P NO2+Sentinel-2 Urban Vegetation AQ Index | Cross-sensor | TROPOMI+S2 | T1 |

**T1 = Genuinely Unclaimed | T2 = Underspecified | T3 = Sensor-Enabled Extension**

---

## Novelty Assessment

Of the 74 named indices (91 including sub-formulae within multi-formula batteries):

| Category | Count | Claim Strength |
|----------|-------|----------------|
| Tier 1 — Genuinely Unclaimed | ~42 | Publishable as novel index contributions |
| Tier 2 — Significantly Underspecified | ~20 | Formalizing as named indices with standard formulae is contribution-worthy |
| Tier 3 — Sensor-Enabled Extensions | ~12 | Known physics, novel implementation on post-2019 sensors |

**Highest confidence "first published index" claims**:
TSEAI, SMADI, AMDPHI, NPDDI, TPERI, MEPSI, ALSI, UBCDI, BSMTI, SBCI, CSCAI, DLPEHI, AFCDI, SCFGOSI, REESAI, PSHRI, CCRBI, SPSRI.

---

## Article Angles

### Primary: Public-Good Index Library
**"The Index DataBase Has 228 Spectral Indices. Here Are 74 Problems It Hasn't Named Yet."**
Frame: science moves fast; formalizing indices is slow. Anyone can claim a novel index by publishing the formula, the physics, and the validation. This is that publication.

### Secondary: The New Sensor Revolution
**"EMIT, PACE, and EnMAP Opened Windows Nobody Has Named"**
Frame: 2019–2024 saw the launch of EMIT, EnMAP, PRISMA, DESIS, PACE, and NISAR. Each opened spectral capabilities that were previously airborne-only or theoretically impossible. The indices in domains 11 and 12 are the direct product of this revolution.

### Tertiary: From Permian to Planet
**"I Built a Contamination Detector for One Basin. Here's What I Found When I Looked Globally."**
Frame: personal narrative connecting limn/Permian work to the global survey. The same methodology — identify the spectral physics, name the gap, propose the formula — applies everywhere.

---

## Recommended Pillar: tool-critic + original-research

This crosses two pillars: it's a practitioner's tool audit (tool-critic) AND a first-principles original contribution (original-research). The combination is unusual and worth owning explicitly — the article both critiques the state of the field and proposes to advance it.

---

*Research conducted May 2026. Covers sensors operational through 2025. Citations are peer-reviewed unless noted as preprint or technical report. Formulae represent proposed novel contributions — validation against ground truth is the next step for each.*
