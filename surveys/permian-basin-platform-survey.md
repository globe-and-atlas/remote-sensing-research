---
title: "Beyond Sentinel-2: Every Free Satellite That Can See Oilfield Contamination"
pillar: tool-critic
status: outline
origin_project: limn
tags: [sentinel, satellite, permian-basin, produced-water, remote-sensing, environmental-monitoring]
date_researched: 2026-05-24
slug: satellite-sensor-survey-permian-basin
---

# Research Vault: Free Satellite Sensor Survey — Permian Basin Environmental Monitoring

> **For article use.** This is a developed research note — full academic survey of open/free satellite platforms suitable for novel spectral index development around produced water contamination, brine spills, oilfield disturbance, and subsurface fluid migration in the Permian Basin.
>
> **Article angle:** The practitioner's honest guide to what else is out there beyond Sentinel-2. What each sensor actually sees, what it can't, and which ones are worth your time.

---

## Hook Candidates

- "I built my whole environmental monitoring stack on Sentinel-2. Then I found out there are 30 other free satellites I wasn't looking at."
- "The brine spill I was trying to detect had already been invisible for months before the liquid disappeared. The mineral scar was still there — I just didn't have the sensor to read it."
- "EMIT was designed to track desert dust. Nobody told it to stop there."

---

## Personal Stakes

Building limn — a public environmental monitoring tool for the Permian Basin. Already have novel composite indices (PWCI, PWI, PWFI, HPWI, APEX). This research came from asking: what else could I be missing? What contamination signals are currently invisible to my stack?

---

## Key Tension

The Permian Basin produces over 20 billion barrels of produced water per year. The contamination is real. The satellite data is free. But no practitioner has mapped which sensor sees which part of the problem — so most people stick to what they know (Sentinel-2, NDVI, NDWI) and miss the full picture.

This article is about the full picture.

---

## The 31-Platform Survey (Ordered by Public Benefit)

### Tier 1 — The Top Four (Highest Public Benefit)

#### #1: EMIT — Earth Surface Mineral Dust Source Investigation
**NASA JPL | 60m | ISS opportunistic | 380–2500 nm, 285 channels | FREE (EARTHDATA)**

The most compelling platform for this application. Designed to map desert dust sources but its hyperspectral capability is directly applicable to brine-induced mineral alteration:

- **Gypsum (SO4):** diagnostic absorption at 2160 nm and 2211 nm — produced water dries and precipitates gypsum on the surface
- **Halite (NaCl):** overtone features detectable at concentration
- **Iron oxidation:** goethite/hematite at 900 nm and 480 nm — brine iron content oxidizes to persistent iron mineral stain
- **Clay cation exchange:** Al-OH 2200 nm, Mg-OH 2310 nm, Fe-OH 2250 nm — brine changes clay mineralogy
- **Hydrocarbon staining:** C-H stretch features at 1700–1730 nm and 2300–2350 nm

**The key insight:** These mineral signals persist in the landscape *after* the liquid brine is gone. It's forensic evidence — a geochemical scar that survives for years.

**Key citations:**
- Green et al. (2023). "Performance and early results from EMIT." *IEEE TGRS*, 61, 1–16.
- Thompson et al. (2024). "Airborne methane plume measurements using EMIT." NASA JPL preprint.
- Swayze et al. (2014). "Using Imaging Spectroscopy to Map Acidic Mine Waste." *Environmental Science & Technology*, 34(1), 37–45.
- Kokaly et al. (2017). *USGS Spectral Library Version 7.* USGS Data Series 1035.

**Proposed index — EMIT-BMIN:** Spectral angle mapping (SAM) distance from a brine-altered soil endmember (gypsum + halite + iron oxide mixture) vs. background evaporite desert soil. Requires EMIT L2B mineral identification product as input.

**Proposed index — EMIT-HC:** `(R_1730 − R_1750) / (R_1730 + R_1750)` — aliphatic C-H stretch feature for hydrocarbon soil staining.

**Access:** search.earthdata.nasa.gov → EMIT → search Permian Basin area. L2B Mineralogy product is the one to get.

---

#### #2 (tied): NISAR — NASA/ISRO SAR Mission
**NASA/ISRO | 3–10m | 12-day | L + S dual band | FREE (upon operational data release)**

The most transformative *future* platform. First space mission with simultaneous L-band + S-band SAR. L-band penetrates to 5–20 cm depth; the L/S difference isolates subsurface moisture and dielectric properties.

- **InSAR subsidence from produced water injection** at millimeter precision
- **L-band soil moisture** sensitive to brine dielectric constant (not just freshwater)
- The original LBSMI concept `(L_VV − S_VV) / (L_VV + S_VV)` becomes implementable from a single free platform

**Key citation:** Rosen et al. (2017). "The NASA-ISRO SAR (NISAR) mission dual-band radar instrument." *IEEE Radar Conference*, 283–284.

**Status:** Launched 2024; expect operational data in 2025–2026.

---

#### #2 (tied): Sentinel-5P / TROPOMI
**ESA | 3.5×5.5 km | Daily | UV–SWIR 270–2385 nm | FREE (Copernicus)**

The atmospheric accountability layer. Column-integrated methane (XCH4) via SWIR at 2305–2385 nm. Produced water impoundments outgas dissolved methane — a signal visible from space.

Also detects: SO2 (flare combustion efficiency), NO2 (diesel engine load proxy), CO (incomplete combustion), HCHO.

**Key citations:**
- Zhang et al. (2020). "Quantifying methane emissions from the largest oil-producing basin in the United States from space." *Science Advances*, 6(17), eaaz5120. — Permian emissions 60% above EPA inventory.
- Irakulis-Loitxate et al. (2021). "Satellite-based survey of extreme methane emissions in the Permian basin." *ACS Earth and Space Chemistry*, 5(9), 2164–2178.

**Proposed index — PBMEI:** `(XCH4_obs − XCH4_background) / (FRP_VIIRS + 1)`. High = fugitive methane (produced water outgassing); Low = flare-associated combustion.

---

#### #4: EnMAP — Environmental Mapping and Analysis Program
**DLR/GFZ Germany | 30m | 27-day (4-day priority mode) | 420–2450 nm, 243 bands | FREE (DLR portal)**

Launched April 2022. Designed explicitly for environmental monitoring. Better spectral sampling than PRISMA in the 1300–1500 nm window. Detects the full Permian evaporite mineral suite: gypsum, anhydrite, halite, polyhalite, carnallite.

**Key citations:**
- Guanter et al. (2015). "The EnMAP spaceborne imaging spectroscopy mission." *Remote Sensing*, 7(7), 8830–8857.
- Spengler & Förster (2023). "EnMAP data for environmental applications: early results." *Remote Sensing of Environment*, 287, 113456.
- Mielke et al. (2016). "Spaceborne mine waste mineralogy monitoring in South Africa." *Remote Sensing*, 8(5), 392.

**Proposed index — EnMAP-EVI:** `B_2163 / B_2211` absorption depth ratio. Background Permian soils → characteristic range; brine spill zones → sulfate dominance.

---

### Tier 2 — High Value Platforms

#### #5: PRISMA (Italy)
**ASI | 30m | 29-day | 400–2505 nm, 240 bands | FREE (prisma.asi.it)**

240 bands across the full spectral range. Free for registered international researchers. Similar capability to EnMAP but older mission (2019). 29-day repeat is limiting but quality is excellent.

**Key citations:**
- Loizzo et al. (2019). "PRISMA: The Italian Hyperspectral Mission." *IGARSS 2019*, 4814–4817.
- Cogliati et al. (2021). "The PRISMA imaging spectroscopy mission: overview and first performance analysis." *Remote Sensing of Environment*, 262, 112499.

**Proposed index — PRISMA-BSAI:** SAM distance to lab-derived brine-altered Permian soil endmember (from USGS Spectral Library v7).

---

#### #6: Sentinel-1 InSAR (PS-InSAR)
**ESA | 5–20m | 6–12 day | C-band 5.6 cm | FREE (Copernicus)**

Already in the limn stack as a backscatter source. The **coherence and phase** data for Persistent Scatterer InSAR is a qualitatively different product. Full Permian Basin deformation time series is available from 2014–present — it just needs processing.

**Key citations:**
- Bekaert et al. (2020). "Spaceborne SAR Survey of Subsidence in the Permian Basin." *The Leading Edge*, 39(11), 813–819.
- Ferretti et al. (2001). "Permanent scatterers in SAR interferometry." *IEEE TGRS*, 39(1), 8–20.

**Proposed index — PB-CDI:** Coherence deviation from multi-year baseline. New surface disturbance (well pads, spill sites) → coherence loss event, retroactively detectable from 2014.

---

#### #7: GRACE-FO
**NASA/GFZ | 300–400 km | Monthly | Microwave gravity ranging | FREE (EARTHDATA)**

Terrestrial Water Storage anomalies at basin scale. Combined with MODIS ET, precipitation, and runoff → GRACE-FO residuals isolate groundwater storage change including subsurface fluid from injection. The only independent check on EPA/RRC injection volume reports.

**Key citation:** Scanlon et al. (2012). "Groundwater depletion and sustainability of irrigation in the US High Plains and Central Valley." *PNAS*, 109(24), 9320–9325.

---

#### #8: AVIRIS-NG (Airborne — Campaign-Based)
**NASA JPL | 0.3–8m | Campaign | 380–2510 nm, 432 channels | FREE >3 years old (EARTHDATA)**

The gold standard hyperspectral sensor. Multiple Permian Basin methane campaigns are archived. Best for method development and validating satellite-scale indices. Sub-5 kg/hr methane detection limit demonstrated.

**Key citations:**
- Duren et al. (2019). "California's methane super-emitters." *Nature*, 575(7781), 180–184.
- Frankenberg et al. (2016). "Airborne methane remote measurements reveal heavy-tail flux distribution in Four Corners region." *Science*, 354(6316), 1269–1273.

---

#### #9: ECOSTRESS
**NASA JPL | ~70×38m | ISS variable (diurnal sampling) | 5 TIR bands 8–12 µm | FREE (EARTHDATA)**

Unique: ISS overpass times vary, so ECOSTRESS captures the same location at different times of day — enabling thermal inertia computation from a single sensor.

- **Phantom ET:** brine pond evaporation shows up as ET uncorrelated with vegetation
- **Brine-killed vegetation:** near-zero WUE despite water availability
- **PW-ETA:** `ET_observed / ET_expected` — ponds → PW-ETA > 2.0; killed vegetation → < 0.2

**Key citations:**
- Fisher et al. (2020). "ECOSTRESS: NASA's next generation mission to measure evapotranspiration from the ISS." *Water Resources Research*, 56, e2019WR026058.
- Hulley et al. (2021). "ECOSTRESS for studying links between the water cycle and plant health." *Remote Sensing*, 13(6), 1245.

---

### Tier 3 — Workhorse and Specialist Platforms

#### #10: Landsat 8/9 OLI + TIRS Collection 2
**NASA/USGS | 30m/100m | 8-day effective | VNIR+SWIR+Thermal | FREE**

Three detection pathways: (1) salt efflorescence alters SWIR-1/SWIR-2 via clay mineralogy; (2) TIRS diurnal thermal inertia for brine-saturated soil; (3) OLI Band 1+2 VOC haze from impoundments. 40-year archive enables contamination timeline reconstruction.

Proposed indices: **PBSI** `(SWIR2−SWIR1)/(SWIR2+SWIR1) − NDVI` | **PW-ATI** `(1−Albedo)/(T_day−T_night)`

#### #10 (tied): ASTER TIR
**NASA/METI (Terra) | 90m | On-demand | 8–12 µm, 5 TIR bands | FREE (EARTHDATA)**

The emissivity spectroscopy angle. 5 TIR bands resolve gypsum emissivity at ~8.6 µm (Band 11) — a surface gypsum precipitation marker from brine drying. Complementary to hyperspectral SWIR for independent confirmation.

**Proposed index — ASTER-GSI:** `(B11 − B12) / (B11 + B12)`. High = gypsum precipitation.

#### #10 (tied): ICESat-2 ATLAS
**NASA | 13m photon footprint | 91-day | 532 nm lidar | FREE (EARTHDATA)**

1 cm vertical precision along transects. Subsidence profiles over injection well fields. Surface water elevation in produced water impoundments.

#### #13: GOES-16/18 ABI
**NOAA | 2 km | 5 minutes | 16 channels 0.47–13.3 µm | FREE (NOAA/AWS)**

5-minute cadence is unmatched for real-time flare monitoring and regulatory accountability. **GOES-FCI:** `(B7 − B6) / (B7 + B6)` at 5-min refresh.

---

### Tier 4 — Atmospheric Context

| Platform | What it adds | Key index concept |
|----------|-------------|-------------------|
| IASI (Metop A/B/C) | NH3 from impoundments + SO2 from flares | IASI-PSI: NH3+SO2+CO composite per facility |
| GOSAT/GOSAT-2 | 15-year CH4 baseline trend | GOSAT-CEB: XCH4/XCO2 decomposition |
| OCO-2/OCO-3 | CO2 enhancement downwind of flares; vegetation SIF | OCO3-FCI: CO2 enhancement downwind |
| CrIS/ATMS | CO + NH3 complement to TROPOMI | Regional combustion chemistry context |

---

### Tier 5 — Soil, Radar, Gravity

| Platform | What it adds | Note |
|----------|-------------|------|
| ALOS-2 PALSAR-2 (JAXA) | L-band InSAR; subsurface brine dielectric | Proposal-based; NISAR will supersede |
| SAOCOM-1 (CONAE) | L-band soil moisture | ESA Third Party; complements ALOS-2 |
| TanDEM-X / TSX (DLR) | DEM baseline for subsidence differencing | Proposal-based |
| SMAP (NASA) | Soil moisture baseline (36 km) | Brine-specific detection unvalidated but theoretically sound |
| SMOS (ESA) | L-band brine dielectric (ocean salinity physics adapted) | Research hypothesis |
| VIIRS (all bands) | Daily SWIR screening + flare FRP | 375m I-band fills S2/MODIS temporal gap |
| MODIS LST | 20-year thermal baseline | 1 km, too coarse for attribution but essential for context |
| Sentinel-3 OLCI | 300m water color for large impoundments | 21 bands incl. fluorescence at 681/709 nm |
| PACE OCI | UV–NIR at 5 nm, daily global | Aerosol chemistry + impoundment water color |

---

## Full Ranked Table (Public Benefit Score /40)

| Rank | Platform | Score | Key Reason |
|------|----------|-------|------------|
| 1 | EMIT | 37 | Only free tool for chemically-specific brine mineral fingerprinting |
| 2 | NISAR | 36 | Transformative — free global L-band InSAR; subsidence = direct community damage |
| 2 | Sentinel-5P TROPOMI | 36 | Daily CH4; ozone/public health; only independent EPA inventory check |
| 4 | EnMAP | 35 | Best systematic free hyperspectral; designed for environment |
| 5 | PRISMA | 33 | 30m hyperspectral free |
| 6 | Sentinel-1 InSAR | 33 | Free, systematic; PS-InSAR stack from 2014 immediately actionable |
| 7 | GRACE-FO | 32 | Only check on injection volumes; subsurface fluid mass balance |
| 8 | AVIRIS-NG | 32 | Highest scientific value for method development |
| 9 | ECOSTRESS | 31 | Phantom ET genuinely invisible to all other tools |
| 10 | Landsat 8/9 | 29 | 40-year archive + thermal + SWIR |
| 10 | ASTER TIR | 29 | Emissivity spectroscopy: gypsum detection not achievable elsewhere free |
| 10 | ICESat-2 | 29 | 1 cm vertical precision subsidence |
| 13 | GOES-16/18 | 28 | 5-min flare monitoring for regulatory accountability |
| 14 | IASI | 29 | NH3 from impoundments |
| 15 | ALOS-2 | 27 | L-band InSAR superior; proposal-based |
| 16 | OCO-2/3 | 27 | CO2/SIF flare validation |
| 17 | VIIRS | 26 | Daily SWIR + flare FRP |
| 18 | TanDEM-X | 26 | DEM baseline |
| 19 | GOSAT | 25 | 15-yr CH4 trend |
| 20 | Planet Dove | 25 | 3m daily (conditional free) |
| 21–31 | MODIS, CrIS, SAOCOM, DESIS, S-3, PACE, SMOS, HISUI, SMAP, CopDEM, MODIS Aqua | 15–24 | Supplemental / enabling |

---

## Novel Index Master List

| Index | Formula Concept | Platform |
|-------|----------------|----------|
| PBMEI | `(XCH4_obs − XCH4_bg) / (FRP_VIIRS + 1)` | TROPOMI + VIIRS |
| PBSI | `(SWIR2−SWIR1)/(SWIR2+SWIR1) − NDVI` | Landsat OLI |
| PW-ATI | `(1−Albedo)/(T_day−T_night)` | Landsat TIRS |
| EMIT-BMIN | SAM distance to brine mineral endmember | EMIT |
| EMIT-HC | `(R_1730−R_1750)/(R_1730+R_1750)` | EMIT |
| PW-ETA | `ET_observed / ET_expected` | ECOSTRESS |
| FARI | `FRP_VIIRS / Well_area` | VIIRS + registry |
| PBDI | InSAR LOS velocity (ASC + DESC decomposed) | ALOS-2 / Sentinel-1 |
| LBDA | ΔL-band VV/VH vs. precip-removed baseline | ALOS-2 / SAOCOM |
| PRISMA-BSAI | SAM vs. brine-altered Permian soil endmember | PRISMA |
| EnMAP-EVI | `B_2163 / B_2211` absorption depth ratio | EnMAP |
| DESIS-BVSI | Red-edge index − chlorophyll ratio | DESIS |
| ASTER-GSI | `(B11−B12)/(B11+B12)` TIR ratio | ASTER TIR |
| PB-CDI | Coherence deviation from multi-yr baseline | Sentinel-1 |
| TDX-SSDI | TanDEM-X DEM − ICESat-2 elevation diff | TDX + ICESat-2 |
| NISAR-SFMI | ASC − DESC vertical deformation | NISAR |
| ICESat2-PBSE | Elevation rate of change (cm/yr) | ICESat-2 |
| GOSAT-CEB | XCH4/XCO2 decomposition time series | GOSAT |
| OCO3-FCI | XCO2 enhancement downwind of flares | OCO-3 |
| IASI-PSI | NH3 + SO2 + CO composite per facility | IASI + CrIS |
| GOES-FCI | `(B7−B6)/(B7+B6)` | GOES ABI |
| SMAP-BSA | TB residual after moisture model removal | SMAP |
| OLCI-PWWCI | `(B4/B3)×(B8/B6)` | Sentinel-3 OLCI |
| GRACE-PWI | TWS anomaly − (ag + precip signal) | GRACE-FO |
| PBMEI-Comp | Multi-sensor anomaly overlay (stacked) | Multi-sensor |

---

## Synthesis: The Core Finding

The Permian Basin contamination detection problem is a **multi-sensor fusion challenge**. No single platform addresses all four mechanisms:
- **Surface spill → soil geochemistry** → hyperspectral (EMIT, EnMAP, PRISMA)
- **Subsurface injection → surface deformation** → InSAR (Sentinel-1, NISAR)
- **Atmospheric emissions → health exposure** → gas columns (TROPOMI, IASI)
- **Groundwater → water security** → gravity (GRACE-FO)

The most scientifically novel contribution available *today* is using **EMIT to map brine-induced mineral alteration** as a **persistent geochemical record** — a forensic scar that survives for years after the liquid brine is gone. No visible-wavelength index achieves this.

The most transformative future platform: **NISAR** — free L-band InSAR at global 12-day cadence, making injection-well subsidence publicly legible.

---

## Recommended Pillar: tool-critic

This is the "here's what the full toolkit actually looks like" piece — honest about what each sensor can and can't do, grounded in the author's own monitoring problem. Fits the practitioner voice.

**Possible titles:**
- "The Satellite Stack I Should Have Built First" (before I built limn on Sentinel-2 alone)
- "31 Free Satellites. Here's What Each One Actually Sees."
- "Beyond NDVI: The Complete Free Satellite Stack for Environmental Monitoring"
- "EMIT Was Built for Desert Dust. It's Perfect for Finding Brine Spills."

---

## Limn Existing Index Catalog (as of 2026-05-25)

> Complete reference of all indices currently implemented in limn. Detection rates from 2026-03-28 validation run against 27 TRRC (Texas Railroad Commission) documented spill sites, threshold=0.01.

### Data Sources Currently Active
- **Sentinel-2 L2A** — CDSE WMS (sh.dataspace.copernicus.eu), VNIR + SWIR
- **Sentinel-1 GRD** — CDSE WMS, C-band SAR (VV, VH)

---

### Tier 0: Baselines (Standard Remote Sensing — No Claim)

| Index | Key Bands | Purpose |
|-------|-----------|---------|
| True Color | B04, B03, B02 | Visual reference |
| False Color (NIR) | B08, B04, B03 | Vegetation/bare soil contrast |
| Moisture Index (NDMI) | B08, B11 | General soil/canopy moisture |
| Wetness Index (NDWI) | B03, B08 | Surface water presence |
| Vegetation Index (NDVI) | B04, B08 | Vegetation density |
| Arid Vegetation (SAVI) | B04, B08 | NDVI + soil brightness correction |
| Moisture Stress Index (MSI) | B08, B11 | Canopy water stress |
| Salinity Index (SI) | B02, B04 | General surface salinity |
| Bare Soil Index (BSI) | B02, B04, B08, B11 | Bare/exposed soil |
| Saline Content NDSI | B08, B11 | Brine salt surface signal |
| Contaminated Soil / Clay Ratio | B11, B12 | Clay mineralogy shift |
| Hydrocarbons (HCAI) | B11, B12 | SWIR hydrocarbon absorption shoulder |
| Heavy Metals (HMRI) | B02, B03 | Metal-toxicity reflectance shift |
| Oil Slicks (NDOI) | B03, B11 | Surface oil film |
| Salt Stress (CRSI) | B04, B08 | Osmotic stress on vegetation from chloride |
| Anoxic Oxidation (AOI) | B02, B04 | Fe³⁺ / anoxic iron oxidation |

---

### Tier 1: Novel Composites — Produced Water / Permian Basin ★★ (Globe & Atlas / Limn Originals)

Detection rates from TRRC 27-site validation, 2026-03-28.

| Index | Full Name | Bands | Detection | What It Detects |
|-------|-----------|-------|-----------|-----------------|
| **PWCI** | Produced Water Chemical Index | B02–B12 | **81.5%** | Three-way AND gate: NDSI + HCAI + HMRI; cubic scaling suppresses caliche noise |
| **ASAI** | Arid Salinity Anomaly Index (ex-PWOI/APEX) | B03, B11, B12 | **77.8%** | Dry-brine mode + wet specular proxy; fires on both active pools and evaporated salt crusts |
| **VSI** | Vegetation Stress Index | B05, B07, B8A, B11 | **74.1%** | Sub-lethal brine toxicity in surviving scrub before kill — earliest warning signal |
| **OBEC** | Oil-Brine Emulsion Composite (ex-HPWI) | B02–B12 | **66.7%** | Physical-chemical consensus: optical smoothness + NDOI + NDSI |
| **FBC** | Ferrugination-Brine Composite | B02–B12 | **66.7%** | Fe²⁺→Fe³⁺ iron oxidation: rust-brown staining from deep Permian brine surfacing |
| **LBI** | Liquid Brine Index | B03, B08, B11, B12 | **63.0%** | Active standing pools: NDSI × adjusted NDWI × (1−NDVI) × BSI |
| **TRI** | Toxic Residue Index | B02–B12 | High specificity | Forensic: mineral scar post-evaporation; NDSI × HMRI × AOI three-way gate |
| **BPI** | Brine-Pavement Index | B04, B08, B11, B12 | — | Pad-level integrity: brine + hydrocarbon co-located on compacted BSI surface |
| **REAI** | Red Edge Alteration Index | B05, B06 | — | Early-stage iron staining via Red Edge B06/B05 ratio; invisible to VNIR/SWIR indices |
| **VCBI** | Vegetation-Confirmed Brine Index | B04, B08, B11, B12 | — | Leading edge of spill migration: vegetation dying + NDSI firing simultaneously |
| **CMA** | Clay-Mineral Alteration | B02, B04, B11, B12 | — | Persistent clay lattice disruption from brine exposure; survives after surface brine gone |
| **PHI** | Petro-Hydrocarbon Index | B11, B12 + HCAI + NDSI | — | Isolates oily brine from clean runoff: three-factor gate |
| **HMI** | Heavy Metal Interaction | B02, B03, B11, B12 | — | Ba/Sr precipitation in soil from evaporating brine; persistent 12+ months |
| **EHC** | Evaporite Halo Composite | B04, B11, B12 | — | False-color: NDOI→Red, BSI→Green, NDSI→Blue; morphology of blowout events |
| **SCRI** | Salt Crust Roughness Index | S1 VV, VH | — | SAR: smooth salt crystallization on surface; penetrates dust/cloud; verifies chemical signals |

---

### Tier 1: Novel Composites — SAR-Based ★★

| Index | Full Name | Sensor | What It Detects |
|-------|-----------|--------|-----------------|
| **SAR Moisture (VV/VH)** | Sentinel-1 SAR Moisture | S1 GRD | General soil moisture / surface roughness |

---

### Tier 2: Novel Composites — Environmental / Civic Atlas ★★ (Globe & Atlas Originals)

| Index | Full Name | Primary Claim |
|-------|-----------|---------------|
| **MVPI** | Methane Venting Plume Index | Deterministic Permian super-emitter workflow: S2 SWIR gas-absorption ratios + high-albedo pad gate + veg/water rejection |
| **CSRC** | Cyanotoxin Scum Risk Composite | Cyanotoxin scum risk: NDCI + NIR scum boost + turbidity rejection + floating-veg rejection + persistence gate |
| **TRSI** | Tailings River Shock Index | Tailings emergency signal: turbidity jump + ferric color shift + mine proximity + persistence |
| **LFGVI** | Landfill Gas Vegetation Intrusion Index | Radial LFG migration: red-edge stress + moisture loss + chlorosis + ring-pattern scoring around landfill boundary |
| **SWRI** | Sewage-Water Release Index | Suspicious urban-channel discharge: turbidity shock + organic bloom proxy + context + persistence |
| **DWCI** | Drinking Water Catchment Injury Index | Upstream contamination threat to drinking water intakes |
| **RRFI** | Riparian Refuge Failure Index | Riparian habitat loss / vegetation corridor failure |
| **EPDI** | Erosion Pulse Delivery Index | Sediment pulse from erosion events into water bodies |
| **HSAI** | Heat-Shelter Absence Index | Urban heat vulnerability: absence of shade/cooling vegetation |
| **BH-DFSI** | Burnt Hillside Debris-Flow Susceptibility Index | Post-fire debris flow risk from bare slope + moisture signal |
| **PETI** | Phycocyanin Eutrophication Toxicity Index | Phycocyanin (blue-green algae) bloom detection |
| **MP-PDI** | Marine Plastisphere & Polymer Differentiation Index | Surface polymer aggregates in marine/coastal settings |
| **TT-API** | Thermokarst Thaw & Anoxic Peat Index | Permafrost thaw + anoxic peat exposure |
| **EC-ACI** | Evapotranspirative Canopy & Asphalt Contrast Index | Heat island / ET contrast between vegetation and impervious surfaces |
| **LRD-VSI** | Landfill Leachate & Runoff Degradation Vegetation Index | Leachate plume vegetation stress downslope of landfills |
| **TDR-ASI** | Tailings Dam Runout & Acid Silt Index | Acid silt / tailings runout mapping |
| **SF-EII** | Wildfire Fuel Hazard & Canopy Dehydration Index | Pre-fire canopy dehydration and fuel hazard |
| **WDA-CSI** | Wetland Encroachment & Agricultural Intrusion Composite | Wetland loss to agriculture / drainage intrusion |
| **CD-UAI** | Coastal Dredging & Marine Siltation Plume Index | Dredge plume dispersion in coastal waters |

---

### Total Index Count: 53 (as of 2026-05-25)

| Category | Count |
|----------|-------|
| Standard baselines (Tier 0) | 16 |
| Novel produced water / Permian composites (Tier 1) | 15 + 1 SAR = 16 |
| Novel environmental / Civic Atlas (Tier 2) | 20 |
| Other specialized (BH-DFSI, MVPI, EC-ACI) | included above |

---

## Limn Integration Roadmap — From the Survey Findings

### Tier A: Same CDSE WMS Endpoint — Zero New API (Write Evalscript Only)

CDSE natively hosts these alongside S2/S1. Same WMS endpoint, different `DATASOURCE` string.

| New Index | Source | Formula Concept | What It Adds to Limn |
|-----------|--------|----------------|----------------------|
| **S5P-CH4** | Sentinel-5P TROPOMI | XCH4 column above background | Atmospheric methane overlay at 3.5 km; atmospheric context layer category |
| **S5P-SO2** | Sentinel-5P TROPOMI | SO2 vertical column | Flare combustion efficiency; pairs with SCRI for multi-signal confirmation |
| **PBMEI-Light** | S5P + (VIIRS FRP from static table) | `(XCH4_obs − XCH4_bg)` normalized | Standalone fugitive methane anomaly without VIIRS live feed |
| **OLCI-PWWCI** | Sentinel-3 OLCI | `(B4/B3)×(B8/B6)` | Chemistry of large produced water impoundments at 300m |
| **OLCI-Turbidity** | Sentinel-3 OLCI | `B08/B06` ratio | Turbidity in ponds, rivers, plume visibility |
| **Landsat-PBSI** | Landsat 8/9 OLI | `(SWIR2−SWIR1)/(SWIR2+SWIR1) − NDVI` | Brine salt crust signature via Landsat SWIR — redundant cross-validation of S2 NDSI |
| **Landsat-ThermalAnomaly** | Landsat 8/9 TIRS | Band 10 deviation from seasonal mean | Thermal inertia anomaly from brine-saturated soil; adds thermal dimension not in S2 |

**Effort:** ~1 day per index to write and validate evalscript. No new credentials.

---

### Tier B: New API, High Value (GIBS / EARTHDATA)

| New Index | Source | Access | Limn Role |
|-----------|--------|--------|-----------|
| **VIIRS-FRP** | VIIRS FIRMS tiles | NASA GIBS public TMS tiles (no auth) | Real-time active flare overlay — plug into Leaflet as tile layer |
| **VIIRS-SWIR** | VIIRS 375m I-bands | NASA GIBS or EARTHDATA | Daily SWIR screening at 375m; faster cadence than S2's 5-day revisit |
| **EMIT-Mineral** | EMIT L2B Mineralogy | EARTHDATA LP DAAC (free, no key needed for public data) | Static scene overlay for known Permian Basin EMIT acquisitions; mineral alteration forensics |

**Effort:** VIIRS FIRMS tiles = ~1 day (Leaflet tile layer, public TMS). EMIT = moderate — requires scene search, download, and GeoTIFF overlay registration.

---

### Tier C: Documented in Help.html, External Data Portal (Link-Out)

These get entries in limn's help.html documenting the index concept, but render as "Available via external portal" rather than live map layers. Users can follow the link and run the analysis themselves.

| Index | Platform | Portal Link |
|-------|----------|------------|
| EMIT-BMIN (mineral SAM) | EMIT | EARTHDATA LP DAAC |
| EnMAP-EVI (evaporite ratio) | EnMAP | eoweb.geoservice.dlr.de |
| PRISMA-BSAI (hyperspectral SAM) | PRISMA | prisma.asi.it |
| PW-ETA (phantom ET) | ECOSTRESS | EARTHDATA LP DAAC |
| ASTER-GSI (gypsum emissivity) | ASTER TIR | EARTHDATA LP DAAC |
| GRACE-PWI (subsurface fluid mass) | GRACE-FO | EARTHDATA Earthdata Search |
| ICESat2-PBSE (elevation change) | ICESat-2 | EARTHDATA OpenAltimetry |
| NISAR-SFMI (injection subsidence) | NISAR | Future — NASA/ISRO |
| GOES-FCI (real-time flare) | GOES-16 ABI | NOAA AWS / GIBS |
| IASI-PSI (NH3+SO2 composite) | IASI Metop | EUMETSAT portal |
| PBDI (PS-InSAR subsidence) | Sentinel-1 | ASF Vertex / COMET LiCSAR |

---

### Priority Order (Highest Value × Lowest Effort)

1. **VIIRS FIRMS flare overlay** — public TMS, no auth, 1 day, immediate operational value
2. **S5P CH4 + SO2 layers** — same WMS, ~1 day each, adds the atmospheric dimension nobody else has in a Permian Basin tool
3. **Landsat PBSI + Thermal** — same WMS, adds redundant cross-platform validation + thermal
4. **S3 OLCI water chemistry** — same WMS, adds impoundment chemistry for large ponds
5. **EMIT static overlay** — moderate effort, highest scientific novelty (mineral forensics)
6. **Help.html documentation of all Tier C indices** — low effort, big value for the article/public science angle

---

*Index catalog last updated: 2026-05-25. Integration roadmap based on CDSE platform capabilities and GIBS/EARTHDATA public tile availability.*
