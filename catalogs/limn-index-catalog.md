---
title: "Limn Spectral Index Catalog"
project: limn
last_updated: 2026-05-25
total_indices: 53
validation: TRRC 27-site validation run, 2026-03-28, threshold=0.01
sources: [Sentinel-2 L2A, Sentinel-1 GRD]
---

# Limn Spectral Index Catalog

Complete catalog of all 53 spectral indices implemented in limn as of 2026-05-25. Organized into three tiers by novelty and specificity.

---

## Tier 0: Baselines — Standard Remote Sensing (No Claim)

These are established published indices used as inputs to novel composites or as visual reference layers.

| Index | Full Name | Key Bands | Purpose |
|-------|-----------|-----------|---------|
| True Color | — | B04, B03, B02 | Visual reference |
| False Color (NIR) | — | B08, B04, B03 | Vegetation/bare soil contrast |
| NDVI | Normalized Difference Vegetation Index | B04, B08 | Vegetation density |
| NDWI | Normalized Difference Water Index | B03, B08 | Surface water presence |
| NDMI | Moisture Index | B08, B11 | General soil/canopy moisture |
| SAVI | Soil Adjusted Vegetation Index | B04, B08 | NDVI + soil brightness correction |
| MSI | Moisture Stress Index | B08, B11 | Canopy water stress |
| BSI | Bare Soil Index | B02, B04, B08, B11 | Bare/exposed soil |
| SI | Salinity Index | B02, B04 | General surface salinity |
| NDSI | Saline Content Index | B08, B11 | Brine salt surface signal |
| Clay Ratio | Contaminated Soil / Clay Ratio | B11, B12 | Clay mineralogy shift |
| HCAI | Hydrocarbon Absorption Index | B11, B12 | SWIR hydrocarbon absorption shoulder |
| HMRI | Heavy Metal Reflectance Index | B02, B03 | Metal-toxicity reflectance shift |
| NDOI | Oil Slick Index | B03, B11 | Surface oil film |
| CRSI | Chloride Root Stress Index | B04, B08 | Osmotic stress on vegetation from chloride |
| AOI | Anoxic Oxidation Index | B02, B04 | Fe³⁺ / anoxic iron oxidation |

**Count: 16**

---

## Tier 1A: Novel Composites — Produced Water / Permian Basin ★★

Globe & Atlas / Limn Originals. Detection rates from TRRC 27-site validation, 2026-03-28.

| Index | Full Name | Bands | Detection Rate | What It Detects |
|-------|-----------|-------|----------------|-----------------|
| **PWCI** | Produced Water Chemical Index | B02–B12 | **81.5%** | Three-way AND gate: NDSI + HCAI + HMRI; cubic scaling suppresses caliche noise |
| **ASAI** | Arid Salinity Anomaly Index | B03, B11, B12 | **77.8%** | Dry-brine mode + wet specular proxy; fires on both active pools and evaporated salt crusts |
| **VSI** | Vegetation Stress Index | B05, B07, B8A, B11 | **74.1%** | Sub-lethal brine toxicity in surviving scrub before kill — earliest warning signal |
| **OBEC** | Oil-Brine Emulsion Composite | B02–B12 | **66.7%** | Physical-chemical consensus: optical smoothness + NDOI + NDSI |
| **FBC** | Ferrugination-Brine Composite | B02–B12 | **66.7%** | Fe²⁺→Fe³⁺ iron oxidation: rust-brown staining from deep Permian brine surfacing |
| **LBI** | Liquid Brine Index | B03, B08, B11, B12 | **63.0%** | Active standing pools: NDSI × adjusted NDWI × (1−NDVI) × BSI |
| **TRI** | Toxic Residue Index | B02–B12 | high specificity | Forensic: mineral scar post-evaporation; NDSI × HMRI × AOI three-way gate |
| **BPI** | Brine-Pavement Index | B04, B08, B11, B12 | — | Pad-level integrity: brine + hydrocarbon co-located on compacted BSI surface |
| **REAI** | Red Edge Alteration Index | B05, B06 | — | Early-stage iron staining via Red Edge B06/B05 ratio; invisible to VNIR/SWIR indices |
| **VCBI** | Vegetation-Confirmed Brine Index | B04, B08, B11, B12 | — | Leading edge of spill migration: vegetation dying + NDSI firing simultaneously |
| **CMA** | Clay-Mineral Alteration | B02, B04, B11, B12 | — | Persistent clay lattice disruption from brine exposure; survives after surface brine gone |
| **PHI** | Petro-Hydrocarbon Index | B11, B12 | — | Isolates oily brine from clean runoff: three-factor gate (HCAI + NDSI) |
| **HMI** | Heavy Metal Interaction | B02, B03, B11, B12 | — | Ba/Sr precipitation in soil from evaporating brine; persistent 12+ months |
| **EHC** | Evaporite Halo Composite | B04, B11, B12 | — | False-color: NDOI→Red, BSI→Green, NDSI→Blue; morphology of blowout events |
| **SCRI** | Salt Crust Roughness Index | S1 VV, VH | — | SAR: smooth salt crystallization on surface; penetrates dust/cloud; verifies chemical signals |

**Count: 15 optical + 1 SAR = 16**

---

## Tier 1B: Novel Composites — SAR-Based ★★

| Index | Full Name | Sensor | What It Detects |
|-------|-----------|--------|-----------------|
| **SAR Moisture** | Sentinel-1 SAR Moisture (VV/VH) | S1 GRD | General soil moisture / surface roughness |

---

## Tier 2: Novel Composites — Environmental / Civic Atlas ★★

Globe & Atlas Originals. Global-applicable environmental screening indices.

| Index | Full Name | Primary Application | Claim Basis |
|-------|-----------|---------------------|-------------|
| **MVPI** | Methane Venting Plume Index | Permian super-emitter detection | Deterministic S2 SWIR gas-absorption ratios + high-albedo pad gate + veg/water rejection |
| **CSRC** | Cyanotoxin Scum Risk Composite | Harmful algal blooms | NDCI + NIR scum boost + turbidity rejection + floating-veg rejection + persistence gate |
| **TRSI** | Tailings River Shock Index | Mining contamination | Turbidity jump + ferric color shift + mine proximity + persistence |
| **LFGVI** | Landfill Gas Vegetation Intrusion Index | Landfill LFG migration | Radial red-edge stress + moisture loss + chlorosis + ring-pattern scoring |
| **SWRI** | Sewage-Water Release Index | Urban sanitation | Turbidity shock + organic bloom proxy + context + persistence |
| **DWCI** | Drinking Water Catchment Injury Index | Water security | Upstream contamination threat to drinking water intakes |
| **RRFI** | Riparian Refuge Failure Index | Ecosystem health | Riparian habitat loss / vegetation corridor failure |
| **EPDI** | Erosion Pulse Delivery Index | Sediment transport | Sediment pulse from erosion events into water bodies |
| **HSAI** | Heat-Shelter Absence Index | Urban heat | Urban heat vulnerability: absence of shade/cooling vegetation |
| **BH-DFSI** | Burnt Hillside Debris-Flow Susceptibility Index | Post-fire hazard | Post-fire debris flow risk from bare slope + moisture signal |
| **PETI** | Phycocyanin Eutrophication Toxicity Index | Water quality | Phycocyanin (blue-green algae) bloom detection |
| **MP-PDI** | Marine Plastisphere & Polymer Differentiation Index | Ocean pollution | Surface polymer aggregates in marine/coastal settings |
| **TT-API** | Thermokarst Thaw & Anoxic Peat Index | Arctic/permafrost | Permafrost thaw + anoxic peat exposure |
| **EC-ACI** | Evapotranspirative Canopy & Asphalt Contrast Index | Urban heat | Heat island / ET contrast between vegetation and impervious surfaces |
| **LRD-VSI** | Landfill Leachate & Runoff Degradation Vegetation Index | Environmental justice | Leachate plume vegetation stress downslope of landfills |
| **TDR-ASI** | Tailings Dam Runout & Acid Silt Index | Mining disaster | Acid silt / tailings runout mapping |
| **SF-EII** | Wildfire Fuel Hazard & Canopy Dehydration Index | Fire risk | Pre-fire canopy dehydration and fuel hazard |
| **WDA-CSI** | Wetland Encroachment & Agricultural Intrusion Composite | Wetland loss | Wetland loss to agriculture / drainage intrusion |
| **CD-UAI** | Coastal Dredging & Marine Siltation Plume Index | Coastal health | Dredge plume dispersion in coastal waters |

**Count: 19** (MVPI is shared with Permian Tier 1)

---

## Total Index Count: 53

| Tier | Category | Count |
|------|----------|-------|
| Tier 0 | Standard baselines | 16 |
| Tier 1A | Novel Permian Basin composites (optical) | 15 |
| Tier 1B | Novel SAR-based | 1 + 1 baseline = 2 |
| Tier 2 | Environmental / Civic Atlas | 19 |

---

## Limn Integration Roadmap — Near-Term Platform Expansions

### Tier A: Same CDSE WMS Endpoint (No New Credentials)

| Index | Platform | Formula Concept | What It Adds |
|-------|----------|----------------|--------------|
| S5P-CH4 | Sentinel-5P TROPOMI | XCH4 column above background | Atmospheric methane overlay at 3.5 km |
| S5P-SO2 | Sentinel-5P TROPOMI | SO2 vertical column | Flare combustion efficiency |
| PBMEI-Light | S5P + VIIRS static | `(XCH4_obs − XCH4_bg)` normalized | Fugitive methane anomaly |
| OLCI-PWWCI | Sentinel-3 OLCI | `(B4/B3)×(B8/B6)` | Large impoundment water chemistry at 300 m |
| OLCI-Turbidity | Sentinel-3 OLCI | `B08/B06` ratio | Turbidity in ponds, rivers, plume visibility |
| Landsat-PBSI | Landsat 8/9 OLI | `(SWIR2−SWIR1)/(SWIR2+SWIR1) − NDVI` | Brine salt crust cross-validation |
| Landsat-ThermalAnomaly | Landsat 8/9 TIRS | Band 10 deviation from seasonal mean | Thermal inertia anomaly from brine-saturated soil |

### Tier B: New API (GIBS / EARTHDATA)

| Index | Platform | Access | Role |
|-------|----------|--------|------|
| VIIRS-FRP | VIIRS FIRMS | NASA GIBS TMS (no auth) | Real-time active flare overlay |
| VIIRS-SWIR | VIIRS 375m I-bands | NASA GIBS | Daily SWIR screening |
| EMIT-Mineral | EMIT L2B | EARTHDATA LP DAAC | Static mineral alteration forensics overlay |

### Tier C: Link-Out Documentation Only

| Index | Platform | Portal |
|-------|----------|--------|
| EMIT-BMIN (mineral SAM) | EMIT | EARTHDATA LP DAAC |
| EnMAP-EVI (evaporite ratio) | EnMAP | eoweb.geoservice.dlr.de |
| PRISMA-BSAI (hyperspectral SAM) | PRISMA | prisma.asi.it |
| PW-ETA (phantom ET) | ECOSTRESS | EARTHDATA LP DAAC |
| ASTER-GSI (gypsum emissivity) | ASTER TIR | EARTHDATA LP DAAC |
| GRACE-PWI (subsurface fluid mass) | GRACE-FO | EARTHDATA Earthdata Search |
| ICESat2-PBSE (elevation change) | ICESat-2 | EARTHDATA OpenAltimetry |
| NISAR-SFMI (injection subsidence) | NISAR | NASA/ISRO (future) |
| GOES-FCI (real-time flare) | GOES-16 ABI | NOAA AWS / GIBS |
| IASI-PSI (NH3+SO2 composite) | IASI Metop | EUMETSAT portal |
| PBDI (PS-InSAR subsidence) | Sentinel-1 | ASF Vertex / COMET LiCSAR |

---

*Validation: TRRC 27-site Permian Basin spill dataset, 2026-03-28. Sensor sources: Sentinel-2 L2A and Sentinel-1 GRD via CDSE WMS.*
