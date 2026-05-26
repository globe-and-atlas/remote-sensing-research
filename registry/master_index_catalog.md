# Global Spectral Index Atlas
### A Public-Good Reference for Novel Satellite Band Combinations

*Version 1.0 — May 2026 | ~130 novel indices across 13 domains*

Free satellite data covers the planet. The physics to read environmental signals from it is well-documented in peer-reviewed literature. What has been missing is one organized place that names the formulas, explains the spectral reasoning, and states the public benefit clearly.

This atlas fills that gap. It covers indices that are operational (used in production tools), proposed (grounded in published physics but awaiting field validation), and newly enabled (known spectral mechanisms now actionable on sensors launched 2019–2024: EMIT, PACE, EnMAP, PRISMA, NISAR).

**How to read the novelty tiers:**

- **T1 — First formula:** The detection purpose exists, but no named, standardized formula has been published. This atlas proposes the first one — use it, adapt it, build on it.
- **T2 — First standardized formula:** The concept appears in the literature, but only as a qualitative description. No formula with a name and defined inputs had been written down. This atlas writes it out.
- **T3 — Newly computable:** The spectral physics has been published for years, but the sensor needed to compute it only launched between 2019 and 2024 (EMIT, PACE, EnMAP, NISAR). These formulas are now operational for the first time.

---

## Master Index Table

| # | Acronym | Full Name | Domain | Platform | Novelty |
|---|---------|-----------|--------|----------|---------|
| 1 | [PWCI](#pwci) | Produced Water Chemical Index | Oilfield | S2 | T1 |
| 2 | [ASAI](#asai) | Arid Salinity Anomaly Index | Oilfield | S2 | T1 |
| 3 | [VSI](#vsi) | Vegetation Stress Index | Oilfield | S2 | T1 |
| 4 | [OBEC](#obec) | Oil-Brine Emulsion Composite | Oilfield | S2 | T1 |
| 5 | [FBC](#fbc) | Ferrugination-Brine Composite | Oilfield | S2 | T1 |
| 6 | [LBI](#lbi) | Liquid Brine Index | Oilfield | S2 | T1 |
| 7 | [TRI](#tri) | Toxic Residue Index | Oilfield | S2 | T1 |
| 8 | [BPI](#bpi) | Brine-Pavement Index | Oilfield | S2 | T1 |
| 9 | [REAI](#reai) | Red Edge Alteration Index | Oilfield | S2 | T1 |
| 10 | [VCBI](#vcbi) | Vegetation-Confirmed Brine Index | Oilfield | S2 | T1 |
| 11 | [CMA](#cma) | Clay-Mineral Alteration | Oilfield | S2 | T1 |
| 12 | [PHI](#phi) | Petro-Hydrocarbon Index | Oilfield | S2 | T1 |
| 13 | [HMI](#hmi) | Heavy Metal Interaction | Oilfield | S2 | T1 |
| 14 | [EHC](#ehc) | Evaporite Halo Composite | Oilfield | S2 | T1 |
| 15 | [SCRI](#scri) | Salt Crust Roughness Index | Oilfield | S1 SAR | T1 |
| 16 | [MVPI](#mvpi) | Methane Venting Plume Index | Oilfield | S2 | T1 |
| 17 | [PBMEI](#pbmei) | Permian Basin Methane Emission Index | Oilfield/Atm | TROPOMI+VIIRS | T1 |
| 18 | [EMIT-BMIN](#emitbmin) | EMIT Brine Mineral Index | Oilfield | EMIT | T1 |
| 19 | [EMIT-HC](#emithc) | EMIT Hydrocarbon Staining Index | Oilfield | EMIT | T1 |
| 20 | [PW-ETA](#pweta) | Produced Water ET Anomaly | Oilfield | ECOSTRESS | T1 |
| 21 | [ASTER-GSI](#astergsi) | ASTER Gypsum Emissivity Index | Oilfield | ASTER TIR | T1 |
| 22 | [GOES-FCI](#goesfci) | GOES Flare Combustion Index | Oilfield | GOES ABI | T1 |
| 23 | [OLCI-PWWCI](#olcipwwci) | OLCI Produced Water Chemistry Index | Oilfield | S3 OLCI | T1 |
| 24 | [GRACE-PWI](#gracepwi) | GRACE Produced Water Injection Index | Oilfield | GRACE-FO | T1 |
| 25 | [PB-CDI](#pbcdi) | Permian Basin Coherence Disturbance Index | Oilfield | S1 InSAR | T1 |
| 26 | [BH-DFSI](#bhdfsi) | Burnt Hillside Debris-Flow Susceptibility Index | Wildfire | S2 | T1 |
| 27 | [SF-EII](#sfeii) | Wildfire Fuel Hazard & Canopy Dehydration Index | Wildfire | S2 | T1 |
| 28 | [LFMPI](#lfmpi) | Live Fuel Moisture Pre-Ignition Index | Wildfire | S2 | T2 |
| 29 | [PSHRI](#pshri) | Post-Fire Soil Hydrophobicity Risk Index | Wildfire | S2+ERA5 | T1 |
| 30 | [BSMTI](#bsmti) | Burn Severity Mineralogy Transition Index | Wildfire | EMIT | T1 |
| 31 | [SACI](#saci) | Smoke Aerosol Composition Index | Wildfire | TROPOMI | T1 |
| 32 | [PCSII](#pcsii) | Pyroconvection Detection Index | Wildfire | GOES+TROPOMI | T1 |
| 33 | [PETI](#peti) | Phycocyanin Eutrophication Toxicity Index | Water Quality | S2 | T2 |
| 34 | [CSRC](#csrc) | Cyanotoxin Scum Risk Composite | Water Quality | S2 | T2 |
| 35 | [SWRI](#swri) | Sewage-Water Release Index | Water Quality | S2 | T2 |
| 36 | [DWCI](#dwci) | Drinking Water Catchment Injury Index | Water Quality | S2 | T1 |
| 37 | [RRFI](#rrfi) | Riparian Refuge Failure Index | Water Quality | S2 | T1 |
| 38 | [EPDI](#epdi) | Erosion Pulse Delivery Index | Water Quality | S2 | T1 |
| 39 | [RDOCI](#rdoci) | River Dissolved Organic Carbon Index | Water Quality | PACE OCI | T1 |
| 40 | [CTPSTI](#ctpsti) | Cyanobacterial Toxin Proxy Spectral Index | Water Quality | PACE, DESIS | T1 |
| 41 | [DTPSI](#dtpsi) | Dam Thermal Plume Stratification Index | Water Quality | Landsat TIRS | T1 |
| 42 | [GMCPI](#gmcpi) | Glacial Meltwater Chemistry Proxy Index | Water Quality | S2, PACE | T1 |
| 43 | [FCLI](#fcli) | Floodplain Contamination Legacy Index | Water Quality | S2 bi-temporal | T1 |
| 44 | [HABSDI](#habsdi) | HAB Species-Level Discrimination Index | Marine/Coastal | PACE, DESIS | T1 |
| 45 | [SMADI](#smadi) | Sargassum vs. Microplastic Discrimination Index | Marine/Coastal | S2, EMIT | T1 |
| 46 | [CBSDI](#cbsdi) | Coral Bleaching Stage Discrimination Index | Marine/Coastal | S2, PRISMA | T1 |
| 47 | [KCDSI](#kcdsi) | Kelp Canopy Density and Stress Index | Marine/Coastal | S2+S3 | T2 |
| 48 | [OWSI](#owsi) | Oil Spill Weathering Stage Index | Marine/Coastal | EMIT, S2 | T2 |
| 49 | [MDSPI](#mdspi) | Mangrove Dieback Spatial Pattern Index | Marine/Coastal | S2+S1 | T1 |
| 50 | [SGDCI](#sgdci) | Submarine Groundwater Discharge Chemistry Index | Marine/Coastal | PACE+ECOSTRESS | T1 |
| 51 | [SPEI](#spei) | Seagrass Photosynthetic Efficiency Index | Marine/Coastal | S2, DESIS | T2 |
| 52 | [CD-UAI](#cduai) | Coastal Dredging & Marine Siltation Plume Index | Marine/Coastal | S2 | T1 |
| 53 | [MP-PDI](#mppdi) | Marine Plastisphere & Polymer Differentiation Index | Marine/Coastal | S2 | T1 |
| 54 | [NPDDI](#npddi) | Nitrogen vs. Phosphorus Deficiency Discrimination Index | Agriculture | S2, EnMAP | T1 |
| 55 | [SCSPI](#scspi) | Soil Compaction Spectral Proxy Index | Agriculture | S2 | T1 |
| 56 | [APRI](#apri) | Aflatoxin Pre-Harvest Risk Index | Agriculture | ECOSTRESS+S2 | T1 |
| 57 | [PDSDI](#pdsdi) | Pesticide vs. Drought Stress Discrimination Index | Agriculture | S2 | T1 |
| 58 | [CCTTI](#cctti) | Cover Crop Termination Timing Index | Agriculture | S2 time series | T2 |
| 59 | [IWUEI](#iwuei) | Irrigation Water Use Efficiency Index | Agriculture | ECOSTRESS+S1 | T2 |
| 60 | [WDA-CSI](#wdacsi) | Wetland Encroachment & Agricultural Intrusion Composite | Agriculture/Wetland | S2 | T1 |
| 61 | [TRSI](#trsi) | Tailings River Shock Index | Mining | S2 | T2 |
| 62 | [TDR-ASI](#tdrasi) | Tailings Dam Runout & Acid Silt Index | Mining | S2 | T1 |
| 63 | [AMDPHI](#amdphi) | Acid Mine Drainage pH Proxy Index | Mining | S2, EMIT | T1 |
| 64 | [TDSII](#tdsii) | Tailings Dam Structural Integrity Index | Mining | S2+S1 InSAR | T1 |
| 65 | [REESAI](#reesai) | Rare Earth Element Surface Anomaly Index | Mining | EnMAP, EMIT | T1 |
| 66 | [CCRBI](#ccrbi) | Coal Combustion Residue Bioaccumulation Index | Mining | S2 | T1 |
| 67 | [HLPII](#hlpii) | Heap Leach Pad Integrity Index | Mining | S2, EMIT | T1 |
| 68 | [IERPI](#ierpi) | Industrial Effluent River Plume Index | Mining | Landsat | T2 |
| 69 | [EC-ACI](#ecaci) | Evapotranspirative Canopy & Asphalt Contrast | Urban | S2+ECOSTRESS | T2 |
| 70 | [HSAI](#hsai) | Heat-Shelter Absence Index | Urban | S2 | T2 |
| 71 | [SPSRI](#spsri) | Solar Panel Soiling Remote Index | Urban | S2, Planet | T1 |
| 72 | [UCIEI](#uciei) | Urban Cool Infrastructure Effectiveness Index | Urban | S2+ECOSTRESS | T1 |
| 73 | [PCADI](#pcadi) | Pavement Condition and Albedo Decay Index | Urban | S2 | T1 |
| 74 | [CSDEI](#csdei) | Construction Site Silica Dust Emission Index | Urban | TROPOMI+GIS | T1 |
| 75 | [LFGVI](#lfgvi) | Landfill Gas Vegetation Intrusion Index | Urban/Waste | S2 | T1 |
| 76 | [LRD-VSI](#lrdvsi) | Landfill Leachate & Runoff Degradation Index | Urban/Waste | S2 | T1 |
| 77 | [TT-API](#ttapi) | Thermokarst Thaw & Anoxic Peat Index | Permafrost | S2 | T1 |
| 78 | [TPERI](#tperi) | Thermokarst Pond Expansion Rate Index | Permafrost | S2 bi-temporal | T1 |
| 79 | [PCEI](#pcei) | Peat Carbon Exposure Index | Permafrost | S2 | T1 |
| 80 | [SABSI](#sabsi) | Snow/Ice Algae Bloom Severity Index | Permafrost | S2, Planet | T2 |
| 81 | [FGDCI](#fgdci) | Frozen Ground Dielectric Change Index | Permafrost | S1 SAR | T1 |
| 82 | [MEPSI](#mepsi) | CH4 Ebullition Pond Spectral Proxy | Permafrost | S2, Planet | T1 |
| 83 | [ALSI](#alsi) | Active Layer Depth Thermal-Spectral Index | Permafrost | ECOSTRESS+S2 | T1 |
| 84 | [PDCSI](#pdcsi) | Pre-Deforestation Canopy Stress Index | Tropical Forest | S2 | T2 |
| 85 | [LISI](#lisi) | Liana Infestation Structural Index | Tropical Forest | S2 | T2 |
| 86 | [UBCDI](#ubcdi) | Understory vs. Canopy Burn Discrimination Index | Tropical Forest | S2 bi-temporal | T1 |
| 87 | [FEDGI](#fedgi) | Forest Edge Degradation Gradient Index | Tropical Forest | S2 | T1 |
| 88 | [SLSDI](#slsdi) | Selective Logging Scar Detection Index | Tropical Forest | S2, Planet | T2 |
| 89 | [ETCSI](#etcsi) | Emergent Tree Crown Stress Index | Tropical Forest | Planet+S2 | T1 |
| 90 | [BSCMCI](#bscmci) | Biological Soil Crust Multi-Condition Index | Dryland | PRISMA, DESIS | T1 |
| 91 | [SBCI](#sbci) | Sabkha Brine Chemistry Index | Dryland | EMIT | T1 |
| 92 | [CSCAI](#cscai) | Caliche Surface Carbonate Accumulation Index | Dryland | EnMAP, PRISMA | T1 |
| 93 | [DEFPI](#defpi) | Dust Emission Flux Proxy Index | Dryland | EMIT+S2+SMAP | T1 |
| 94 | [DLPEHI](#dlpehi) | Desert Locust Pre-Emergence Habitat Index | Dryland | S2+GPM | T1 |
| 95 | [AIBEAI](#aibeai) | Arroyo Incision and Bank Erosion Activity Index | Dryland | S2, Planet | T1 |
| 96 | [PWTDI](#pwtdi) | Peatland Water Table Depth Index | Wetland | S2+S1 | T2 |
| 97 | [MHSSP](#mhssp) | Methane Hotspot Surface Spectral Predictor | Wetland | S2+TROPOMI | T1 |
| 98 | [TFIDI](#tfidi) | Tidal Flat Inundation Dynamics Index | Wetland | S2 monthly | T1 |
| 99 | [WDPTZI](#wdptzi) | Wet-Dry Peatland Transition Zone Index | Wetland | S2 | T1 |
| 100 | [IPVSI](#ipvsi) | Invasive Phragmites vs. Native Vegetation | Wetland | S2 seasonal | T2 |
| 101 | [WVTDI](#wvtdi) | Wetland Vegetation Type Discrimination Index | Wetland | S2 time series | T2 |
| 102 | [CMSTI](#cmsti) | Clay Mineral Stress Transition Index | Hyperspectral | EMIT | T1 |
| 103 | [MPSSFI](#mpssfi) | Methane Plume Spectral Shape Feature Index | Hyperspectral | EMIT | T2 |
| 104 | [AFCDI](#afcdi) | Asbestos Fiber Chrysotile Detection Index | Hyperspectral | EMIT, PRISMA | T1 |
| 105 | [SCFGOSI](#scfgosi) | Soil Carbon Functional Group Oxidation Index | Hyperspectral | EMIT, EnMAP | T1 |
| 106 | [REENBI](#reenbi) | REE Neodymium Band Depth Index | Hyperspectral | EnMAP | T1 |
| 107 | [EPCASE](#epcase) | EnMAP Porphyry Cu Alteration Sequence Index | Hyperspectral | EnMAP | T1 |
| 108 | [DPCCI](#dpcci) | DESIS Phycocyanin Column Concentration Index | Hyperspectral | DESIS, PACE | T2 |
| 109 | [PFTIB](#pftib) | Phytoplankton Functional Type Index Battery | Hyperspectral | PACE OCI | T1 |
| 110 | [TSEAI](#tseai) | TROPOMI–Sentinel-2 Emission Attribution Index | Cross-sensor | S5P+S2 | T1 |
| 111 | [ISSAI](#issai) | ICESat-2+Sentinel-1 Subsidence Attribution Index | Cross-sensor | ICESat-2+S1+S2 | T1 |
| 112 | [GEAWSI](#geawsi) | GRACE-FO+ECOSTRESS Agricultural Water Stress | Cross-sensor | GRACE+ECOSTRESS | T1 |
| 113 | [EMSMMI](#emsmmi) | EMIT Mineral+Sentinel-1 Soil Moisture Index | Cross-sensor | EMIT+S1 | T1 |
| 114 | [NFCAI](#nfcai) | NISAR+Sentinel-2 Forest Carbon Accumulation | Cross-sensor | NISAR+S2 | T3 |
| 115 | [SNUVQI](#snuvqi) | NO2+Sentinel-2 Urban Vegetation Air Quality | Cross-sensor | TROPOMI+S2 | T1 |
| 116 | [PUENPI](#puenpi) | PACE+ECOSTRESS Coastal Wetland NEP Index | Cross-sensor | PACE+ECOSTRESS | T1 |

---

## Section 1: Oilfield & Produced Water (Permian Basin)

*All indices validated against TRRC 27-site spill dataset, 2026-03-28, unless marked "Proposed."*

---

### <a id="pwci"></a>PWCI — Produced Water Chemical Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B02–B12) | **Novelty:** T1

**Problem:** Oilfield produced water contains salt, hydrocarbons, and heavy metals simultaneously. No standard index addresses this three-chemical co-occurrence.

**Formula:**
```
PWCI = NDSI**3 * HCAI * HMRI
```

| Component | Expression | Physical Target |
|-----------|------------|-----------------|
| **NDSI** | `(B08 - B11) / (B08 + B11)` | Salt crust / water-salt interaction (1610 nm) |
| **HCAI** | `(B11 - B12) / (B11 + B12)` | Hydrocarbon absorption shoulder (2190 nm) |
| **HMRI** | `(B03 - B02) / (B03 + B02)` | Heavy metals (Fe/Ba blue-green reflectance shift) |

Where: `NDSI = (B08 - B11) / (B08 + B11)` | `HCAI = (B11 - B12) / (B11 + B12)` | `HMRI = (B03 - B02) / (B03 + B02)`

**Physics:** Three-way AND gate requiring simultaneous salt (NDSI at 1610 nm), hydrocarbon (HCAI SWIR shoulder at 2190 nm vs. 1610 nm), and heavy metal (HMRI blue-green ratio from Fe/Ba reflectance shift). Cubic scaling of NDSI suppresses caliche which produces high NDSI but not HCAI or HMRI.

**Benefit:** Independent satellite screening of 20+ billion barrels of produced water disposed annually in the Permian Basin.

**Validated:** 81.5% detection rate against TRRC 27-site dataset.


---

### <a id="asai"></a>ASAI — Arid Salinity Anomaly Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B03, B11, B12) | **Novelty:** T1

**Problem:** Produced water leaves both wet brine pools and dry evaporated salt crusts. Indices optimized for one mode miss the other.

**Formula:**
```
ASAI = max(NDSI_dry_mode, NDWI_specular_proxy) * (1 - NDVI)
```

| Mode | Expression | Target Feature |
|------|------------|----------------|
| **Dry Mode** | `(B11 - B12) / (B11 + B12)` | Evaporated NaCl/gypsum crust |
| **Specular Mode** | `B03` (Green brightness) | Smooth liquid brine pool reflectance |
| **Vegetation Rejection** | `(1 - NDVI)` | Excludes healthy vegetation false positives |
Dry mode: high B11/B12 absorption ratio. Specular mode: high B03 brightness from brine pond reflectance.

**Physics:** Dry brine evaporation concentrates NaCl/gypsum, elevating SWIR1/SWIR2 ratio relative to background arid soils. Active brine pools produce specular reflectance in green (B03). Taking the maximum of both modes extends detection across the full spill life cycle.

**Benefit:** Catches spill sites in both active-pooling and post-evaporation phases, doubling the detection window.

**Validated:** 77.8% detection rate.


---

### <a id="vsi"></a>VSI — Vegetation Stress Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B05, B07, B8A, B11) | **Novelty:** T1

**Problem:** Brine toxicity stress in surviving vegetation is invisible to NDVI until biomass decline is severe. Red-edge bands capture sub-lethal chlorophyll suppression weeks earlier.

**Formula:**
```
VSI = [(B8A - B07) / (B8A + B07)] - [(B07 - B05) / (B07 + B05)]
```

| Ratio | Expression | Physiological Signal |
|-------|------------|----------------------|
| **Red-Edge Broader** | `(B8A - B07) / (B8A + B07)` | Leaf mesophyll water & cellular structure |
| **Red-Edge Narrow** | `(B07 - B05) / (B07 + B05)` | Sub-lethal chlorophyll suppression |
| **Bare Soil Gate** | `B11` | SWIR1 gate to exclude bare soil false positives |

with B11 gate to exclude dry bare soil.

**Physics:** Brine osmotic stress and sodium toxicity suppress chlorophyll before causing visible yellowing. The red-edge position shifts from ~720 nm toward ~705 nm as chlorophyll declines, detectable as a differential between the B8A/B07 and B07/B05 ratios.

**Benefit:** Earliest warning signal — detects sub-lethal brine impact on scrub vegetation before kill occurs.

**Validated:** 74.1% detection rate.


---

### <a id="obec"></a>OBEC — Oil-Brine Emulsion Composite
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B02–B12) | **Novelty:** T1

**Problem:** Oil-brine emulsions have a mixed spectral signature that neither NDOI (oil) nor NDSI (brine) captures independently.

**Formula:**
```
OBEC = optical_smoothness * NDOI * NDSI
```

| Factor | Expression | Target Property |
|--------|------------|-----------------|
| **Smoothness** | Low spectral variance (B02–B08) | Suppressed scattering from surface oil emulsion |
| **NDOI** | `(B11 - B12) / (B11 + B12)` | Surface crude oil film signature |
| **NDSI** | `(B08 - B11) / (B08 + B11)` | Saturated brine water salinity |
Optical smoothness = low variance across B02–B08.

**Physics:** Oil-brine emulsions create anomalously smooth, low-variance spectrum. NDOI targets oil film signal; NDSI targets brine signal. Three-way product isolates co-occurrence.

**Benefit:** Identifies blowout events where oil and brine are mixed — the most environmentally damaging scenario.

**Validated:** 66.7% detection rate.


---

### <a id="fbc"></a>FBC — Ferrugination-Brine Composite
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B02–B12) | **Novelty:** T1

**Problem:** Deep Permian brine carries elevated Fe²⁺ that oxidizes to Fe³⁺ on surfacing, leaving a rust-brown iron stain distinct from hydrocarbon and salt signals.

**Formula:**
```
FBC = AOI * NDSI * HMRI
```

| Index | Expression | Target Property |
|-------|-----------|-----------------|
| **AOI** | `(B04 - B02) / (B04 + B02)` | Fe³⁺ anoxic iron oxidation (red-blue contrast) |
| **NDSI** | `(B08 - B11) / (B08 + B11)` | Evaporated brine salts |
| **HMRI** | `(B03 - B02) / (B03 + B02)` | Surfacing heavy metal signature |
Where `AOI = (B04 - B02) / (B04 + B02)` encodes Fe³⁺ / anoxic iron oxidation.

**Physics:** Fe²⁺ oxidizes to goethite/hematite producing absorption at 480 nm and 535 nm. AOI captures the red-to-blue contrast; NDSI and HMRI require co-occurrence with salt and heavy metals.

**Benefit:** Detects brine surfacing from legacy wells where the visual signal is iron staining, not free-standing liquid.

**Validated:** 66.7% detection rate.


---

### <a id="lbi"></a>LBI — Liquid Brine Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B03, B08, B11, B12) | **Novelty:** T1

**Problem:** Active standing brine pools must be distinguished from other water bodies.

**Formula:**
```
LBI = NDSI * adj_NDWI * (1 - NDVI) * BSI
```

| Gate | Expression | Operational Purpose |
|------|------------|---------------------|
| **Salinity** | `NDSI` | Confirms salt concentration |
| **Water Saturated** | `adj_NDWI = (B03 - B11) / (B03 + B11)` | Gao (1996) variant sensitive to saline water |
| **Tundra Rejection** | `(1 - NDVI)` | Removes vegetation false positives |
| **Bare Soil Context** | `BSI` | Restricts detection to bare/disturbed soil context |
Where `adj_NDWI = (B03 - B11) / (B03 + B11)` (Gao 1996 variant).

**Physics:** Four-factor product requires: (1) salt signal, (2) liquid water, (3) absence of vegetation, (4) bare/disturbed soil context. Highly specific to industrial brine pools.

**Benefit:** Enables automated counting and area measurement of active produced water impoundments at basin scale.

**Validated:** 63.0% detection rate.


---

### <a id="tri"></a>TRI — Toxic Residue Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B02–B12) | **Novelty:** T1

**Problem:** After brine evaporates, a mineral scar persists for 12+ months. Standard indices return to background when liquid is gone.

**Formula:**
```
TRI = NDSI * HMRI * AOI
```

**Physics:** Evaporated brine leaves co-deposits of halite/gypsum (NDSI), heavy metal hydroxides from Ba/Sr/Fe precipitation (HMRI), and iron oxidation staining (AOI). Forensic evidence that persists in the landscape.

**Benefit:** Forensic detection of historical spill sites. Enables timeline reconstruction from satellite archives.


---

### <a id="bpi"></a>BPI — Brine-Pavement Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B04, B08, B11, B12) | **Novelty:** T1

**Problem:** Brine and hydrocarbon co-located on compacted pad surfaces — pad-level integrity monitoring.

**Formula:** `BPI = NDSI * HCAI * BSI` (brine + hydrocarbon on bare compacted surface)


---

### <a id="reai"></a>REAI — Red Edge Alteration Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B05, B06) | **Novelty:** T1

**Problem:** Iron staining from brine alters the red-edge slope before causing visible stress or SWIR changes.

**Formula:**
```
REAI = (B06 - B05) / (B06 + B05)
```
B05 = 705 nm, B06 = 740 nm.

**Physics:** Iron oxide deposition on leaf surfaces increases absorption in 680–710 nm, compressing the red-edge slope — invisible to all VNIR/SWIR broad-band sensors.

**Benefit:** Earliest vegetation-based signal from oilfield brine exposure.


---

### <a id="vcbi"></a>VCBI — Vegetation-Confirmed Brine Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B04, B08, B11, B12) | **Novelty:** T1

**Problem:** Leading edge of spill migration — vegetation dying + NDSI firing simultaneously.

**Formula:** `VCBI = NDSI * (1 - NDVI_normalized)` with NDVI approaching kill threshold.


---

### <a id="cma"></a>CMA — Clay-Mineral Alteration
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B02, B04, B11, B12) | **Novelty:** T1

**Problem:** Persistent clay lattice disruption from brine exposure survives after surface brine is gone.

**Formula:** SWIR2-to-SWIR1 deviation from local clay mineral baseline.


---

### <a id="phi"></a>PHI — Petro-Hydrocarbon Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B11, B12) | **Novelty:** T1

**Problem:** Isolates oily brine from clean runoff using three-factor gate (HCAI + NDSI).

**Formula:** `PHI = HCAI * NDSI * (1 - NDWI)` — hydrocarbon + brine without fresh water.


---

### <a id="hmi"></a>HMI — Heavy Metal Interaction
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B02, B03, B11, B12) | **Novelty:** T1

**Problem:** Ba/Sr precipitation in soil from evaporating brine — persistent 12+ months.

**Formula:** `HMI = HMRI * NDSI * (1 - NDVI)` with SWIR persistence filter.


---

### <a id="ehc"></a>EHC — Evaporite Halo Composite
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B04, B11, B12) | **Novelty:** T1

**Problem:** False-color composite revealing morphology of blowout events and evaporite halos.

**Formula:** NDOI→Red channel, BSI→Green, NDSI→Blue (false-color mapping).


---

### <a id="scri"></a>SCRI — Salt Crust Roughness Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-1 SAR (VV, VH) | **Novelty:** T1

**Problem:** Optical indices cannot see through dust, smoke, or clouds. SAR penetrates all conditions but general SAR indices don't specifically target salt crystallization.

**Formula:**
```
SCRI = low_variance[(VV - VH) / (VV + VH)] within salt_mask
```

**Physics:** Crystallized halite/gypsum is specularly smooth at C-band wavelengths (5.6 cm), suppressing volume scattering (VH). Low cross-polarization ratio and low spatial variance is distinct from all natural rough soil surfaces.

**Benefit:** Cloud/dust-penetrating verification of chemical indices — the only all-weather oilfield brine indicator.


---

### <a id="mvpi"></a>MVPI — Methane Venting Plume Index
**Domain:** Oilfield / atmospheric | **Platform:** Sentinel-2 (B11, B12) | **Novelty:** T1

**Problem:** Produced water impoundments outgas dissolved methane. MVPI provides a surface context gate for atmospheric detections, not direct methane sensing.

**Formula:**
```
MVPI = high_albedo_pad_gate * (1 - NDVI) * (1 - NDWI) * HCAI_anomaly
```

**Physics:** Operational use is as a surface context filter identifying which pad-level features are co-located with TROPOMI or EMIT methane detections, enabling source attribution below the TROPOMI pixel footprint.

**Benefit:** Source attribution for methane plumes — narrows a 5.5×7 km TROPOMI pixel to specific facility features.


---

### <a id="pbmei"></a>PBMEI — Permian Basin Methane Emission Index
**Domain:** Oilfield / atmospheric | **Platform:** Sentinel-5P TROPOMI + VIIRS | **Novelty:** T1

**Formula:**
```
PBMEI = (XCH4_obs - XCH4_background) / (FRP_VIIRS + 1)
```

**Physics:** High XCH4 with low fire radiative power = fugitive methane (produced water outgassing, equipment leaks). High XCH4 with high FRP = flare-associated combustion.

**Benefit:** Independent cross-check on EPA/RRC methane inventory. Zhang et al. (2020) found Permian emissions 60% above EPA estimates.


---

### <a id="emitbmin"></a>EMIT-BMIN — EMIT Brine Mineral Index
**Domain:** Oilfield | **Platform:** EMIT (60 m, 285 bands) | **Novelty:** T1

**Formula:** Spectral Angle Mapping distance from a brine-altered soil endmember (gypsum + halite + iron oxide mixture) vs. background evaporite desert soil.

**Physics:** Produced water precipitates gypsum (SO4 absorptions at 2160, 2211 nm), halite, and iron hydroxides (480/535 nm). EMIT's 5 nm resolution resolves these features — forensic mineral fingerprinting from orbit.


---

### <a id="emithc"></a>EMIT-HC — EMIT Hydrocarbon Staining Index
**Domain:** Oilfield | **Platform:** EMIT | **Novelty:** T1

**Formula:** Band depth at 2300–2350 nm (C-H overtone) vs. clean soil background.


---

### <a id="pweta"></a>PW-ETA — Produced Water ET Anomaly
**Domain:** Oilfield | **Platform:** ECOSTRESS | **Novelty:** T1

**Formula:** `PW - ETA = ET_observed - ET_predicted_from_vegetation_cover`

**Physics:** Brine-saturated soil produces anomalously high ECOSTRESS latent heat signal from evaporating salts (not vegetation transpiration) — "phantom ET" from salt-driven evaporation.


---

### <a id="astergsi"></a>ASTER-GSI — ASTER Gypsum Emissivity Index
**Domain:** Oilfield | **Platform:** ASTER TIR (90 m) | **Novelty:** T1

**Formula:**
```
ASTER - GSI = (B11 - B12) / (B11 + B12)
```
B11 = ~8.6 µm, B12 = ~9.1 µm.

**Physics:** Gypsum has distinctive thermal emissivity minimum at ~8.6 µm from SO4 vibrational absorption — unique among desert surface minerals.


---

### <a id="goesfci"></a>GOES-FCI — GOES Flare Combustion Index
**Domain:** Oilfield / regulatory | **Platform:** GOES-16/18 ABI | **Novelty:** T1

**Formula:**
```
GOES - FCI = (B7 - B6) / (B7 + B6)
```
B7 = 3.9 µm (mid-wave IR), B6 = 2.25 µm.

**Physics:** Active flares emit strongly at 3.9 µm; the ratio encodes flare temperature and combustion efficiency.

**Benefit:** 5-minute cadence — the only real-time flare accountability tool.


---

### <a id="olcipwwci"></a>OLCI-PWWCI — OLCI Produced Water Chemistry Index
**Domain:** Oilfield | **Platform:** Sentinel-3 OLCI (300 m) | **Novelty:** T1

**Formula:**
```
OLCI - PWWCI = (B4 / B3) * (B8 / B6)
```


---

### <a id="gracepwi"></a>GRACE-PWI — GRACE Produced Water Injection Index
**Domain:** Oilfield / subsurface | **Platform:** GRACE-FO | **Novelty:** T1

**Formula:**
```
GRACE - PWI = TWS_anomaly - (agriculture_signal + precipitation_signal + natural_groundwater_trend)
```


---

### <a id="pbcdi"></a>PB-CDI — Permian Basin Coherence Disturbance Index
**Domain:** Oilfield | **Platform:** Sentinel-1 InSAR | **Novelty:** T1

**Formula:**
```
PB - CDI = coherence_current - coherence_multi - year_baseline
```


---

## Section 2: Wildfire & Post-Fire

---

### <a id="bhdfsi"></a>BH-DFSI — Burnt Hillside Debris-Flow Susceptibility Index
**Domain:** Post-fire hydrological hazard | **Platform:** Sentinel-2 | **Novelty:** T1

**Problem:** Catastrophic mudslides and debris flows occur in burned mountainous terrain 1–3 years post-fire.

**Formula:**
```
BH - DFSI = BurnGate * SoilGate * MoistureSignal * ChromaticSlopeProxy
```
| Component | Expression |
|-----------|------------|
| BurnGate | `clamp((0.15 - NBR) / 0.30, 0, 1)` |
| SoilGate | `clamp((BSI - 0.10) / 0.20, 0, 1)` |
| MoistureSignal | `clamp((NDWI_Gao + 0.35) / 0.50, 0, 1)` |
| ChromaticSlopeProxy | `clamp((B04 - B02) / (B04 + B02) * 2.0, 0, 1)` |

**Physics:** All four must co-occur: severe char (NBR < 0.15), complete canopy loss (BSI elevated), pre-flow moisture (NDWI_Gao), terrain proxy (red-to-blue encodes steep slope sun angle).

**Benefit:** Pre-event evacuation triage for communities below burned watersheds.

> **Claim strength:** High

---

### <a id="sfeii"></a>SF-EII — Wildfire Fuel Hazard & Canopy Dehydration Index
**Domain:** Pre-fire fuel assessment | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:**
```
SF - EII = [(B8A - B11) / (B8A + B11)] * [1 - (B08 / B12)]
```

**Physics:** SWIR1 absorption reflects bulk canopy water content; B12/B08 encodes cell wall integrity.

**Benefit:** Identifies which specific forest patches are in critical pre-ignition condition.

> **Claim strength:** Medium

---

### <a id="lfmpi"></a>LFMPI — Live Fuel Moisture Pre-Ignition Index
**Domain:** Pre-fire | **Platform:** Sentinel-2, Landsat-9 | **Novelty:** T2

**Formula:**
```
LFMPI = 2.5 * [(B8A - B11) / (B8A + B11 + 6 * B4 - 7.5 * B2 + 1)] - (B12 / B11)
```


---

### <a id="pshri"></a>PSHRI — Post-Fire Soil Hydrophobicity Risk Index
**Domain:** Post-fire | **Platform:** Sentinel-2 + ERA5 | **Novelty:** T1

**Formula:**
```
PSHRI = NDWI_post - rain - NDWI_pre - rain
```
Applied in confirmed post-precipitation window from ERA5. Negative PSHRI after rain = hydrophobic soil.

**Physics:** Normal soil wets with rain → NDWI increases post-precipitation. Hydrophobic soil repels water → NDWI unchanged despite rainfall.

**Benefit:** Identifies burned hillslopes where soil will not absorb rain.


---

### <a id="bsmti"></a>BSMTI — Burn Severity Mineralogy Transition Index
**Domain:** Post-fire | **Platform:** EMIT (5 nm resolution) | **Novelty:** T1

**Formula:**
```
BSMTI = depth(535nm) / depth(486nm)
```

**Physics:** Goethite→magnetite→hematite transition encodes fire temperature history. EMIT is the only sensor with spectral resolution for this discrimination.


---

### <a id="saci"></a>SACI — Smoke Aerosol Composition Index
**Domain:** Wildfire | **Platform:** Sentinel-5P TROPOMI | **Novelty:** T1

**Formula:**
```
SACI = AOD_UV340 / AOD_550
```
High ratio (>1.5) = smoldering/OC-dominated. Low ratio (~1.0) = flaming/BC-dominated.

**Benefit:** Distinguishes fire type for public health advisories.


---

### <a id="pcsii"></a>PCSII — Pyroconvection Detection Index
**Domain:** Wildfire / atmosphere | **Platform:** GOES + TROPOMI | **Novelty:** T1

**Formula:**
```
PCSII = (BT_3.7µm - BT_11µm > 0) AND (AOD_TROPOMI > 1.0)
```


---

## Section 3: Water Quality & Freshwater

---

### <a id="peti"></a>PETI — Phycocyanin Eutrophication Toxicity Index
**Domain:** Water quality | **Platform:** Sentinel-2 | **Novelty:** T2

**Formula:**
```
PETI = [(B04 - B05) / (B04 + B05)] * turbidity_gate * persistence_gate
```

**Physics:** Phycocyanin absorbs at 620 nm (between S2's B04=665 nm and B05=705 nm), creating a reduction in red band reflectance relative to red-edge.

**Benefit:** Public health early warning for cyanobacterial blooms.

> **Claim strength:** Medium

---

### <a id="csrc"></a>CSRC — Cyanotoxin Scum Risk Composite
**Domain:** Water quality | **Platform:** Sentinel-2 | **Novelty:** T2

**Formula:**
```
CSRC = NDCI * NIR_scum_boost * (1 - turbidity_rejection) * (1 - floating_veg_rejection) * persistence_gate
```

**Physics:** Dense floating scum elevates NIR from cell clumping while maintaining NDCI signal.

**Benefit:** Identifies specific locations where direct human contact risk is highest.

> **Claim strength:** Very High

---

### <a id="swri"></a>SWRI — Sewage-Water Release Index
**Domain:** Water quality / public health | **Platform:** Sentinel-2 | **Novelty:** T2

**Formula:** `SWRI = turbidity_shock * organic_bloom_proxy * urban_channel_context * persistence`

> **Claim strength:** Very High

---

### <a id="dwci"></a>DWCI — Drinking Water Catchment Injury Index
**Domain:** Water quality / public health | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:**
```
DWCI = turbidity_anomaly * upstream_flow_path_weight * persistence
```

**Benefit:** Early warning system for water treatment facilities.

> **Claim strength:** High

---

### <a id="rrfi"></a>RRFI — Riparian Refuge Failure Index
**Domain:** Water quality / ecology | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:** `RRFI = NDVI_riparian_loss * NDWI_channel_decline * BSI_bank_exposure`

> **Claim strength:** High

---

### <a id="epdi"></a>EPDI — Erosion Pulse Delivery Index
**Domain:** Water quality | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:** `EPDI = BSI_upslope_change * turbidity_downstream * persistence`

> **Claim strength:** High

---

### <a id="rdoci"></a>RDOCI — River Dissolved Organic Carbon Index
**Domain:** Water quality / carbon cycle | **Platform:** PACE OCI | **Novelty:** T1

**Formula:**
```
RDOCI = ln(ρ_320nm / ρ_412nm) / (412 - 320) * ( - 1)
```
Approximating CDOM spectral slope coefficient S275-295 from PACE UV channels.

**Physics:** DOC absorbs strongly in UV-blue with exponential decay. PACE OCI's 320 nm and 412 nm channels make this calculable from orbit for the first time (launched 2024).

**Benefit:** Global river DOC flux monitoring — critical, poorly constrained carbon cycle element.


---

### <a id="ctpsti"></a>CTPSTI — Cyanobacterial Toxin Proxy Spectral Index
**Domain:** Water quality | **Platform:** PACE OCI, DESIS | **Novelty:** T1

**Formula:**
```
CTPSTI = [ρ(560nm) - ρ(620nm)] / [ρ(560nm) + ρ(620nm)]
```

**Physics:** Microcystis (toxic) is phycocyanin-dominant (620 nm). Non-toxic Aphanizomenon has phycoerythrin contribution at 565 nm. The ratio encodes species composition correlating with toxin-producer abundance.


---

### <a id="dtpsi"></a>DTPSI — Dam Thermal Plume Stratification Index
**Domain:** Water quality / ecology | **Platform:** Landsat-9 TIRS | **Novelty:** T1

**Formula:**
```
DTPSI = (LST_downstream_1km - LST_reservoir_surface) / (LST_upstream_1km - LST_reservoir_surface)
```
<0 = cold hypolimnetic release; >0 = warm surface release.


---

### <a id="gmcpi"></a>GMCPI — Glacial Meltwater Chemistry Proxy Index
**Domain:** Water quality | **Platform:** Sentinel-2, PACE | **Novelty:** T1

**Formula:** CDOM ratio and turbidity combination in glacier outflow plumes.


---

### <a id="fcli"></a>FCLI — Floodplain Contamination Legacy Index
**Domain:** Water quality / environmental justice | **Platform:** Sentinel-2 bi-temporal | **Novelty:** T1

**Formula:**
```
FCLI = (B12_post - flood - B12_pre - flood) * (1 - NDVI_next - season)
```

**Physics:** Metal-contaminated sediments alter SWIR2; phytotoxic suppression of next-season vegetation confirms legacy impact.


---

## Section 4: Marine & Coastal

---

### <a id="habsdi"></a>HABSDI — HAB Species-Level Discrimination Index
**Domain:** Marine water quality | **Platform:** PACE OCI, DESIS | **Novelty:** T1

**Formula:**
```
HABSDI_cyano  = PC_index - FX_index     # positive = cyanobacteria dominant
HABSDI_diatom = FX_index - PC_index     # positive = diatom dominant
```
PC_index = (560nm - 705nm); FX_index = (490nm - 560nm).

**Physics:** Cyanobacteria → phycocyanin (620 nm). Diatoms → fucoxanthin (510–540 nm). PACE OCI 5 nm resolution resolves these pigment packages.

**Benefit:** Transforms HAB monitoring from presence/absence to toxin-risk species assessment.


---

### <a id="smadi"></a>SMADI — Sargassum vs. Microplastic Discrimination Index
**Domain:** Marine pollution | **Platform:** Sentinel-2, EMIT | **Novelty:** T1

**Formula:**
```
SMADI = FAI - [(B8A - B11) / (B8A + B11)]
```

**Physics:** Sargassum has active photosynthesis — strong 680 nm chlorophyll absorption. Microplastics (PE/PP) have C-H stretch overtones at 1730 nm, suppressed NIR, and no chlorophyll. FAI/SWIR1 combination isolates the vegetation component absent from plastic.


---

### <a id="cbsdi"></a>CBSDI — Coral Bleaching Stage Discrimination Index
**Domain:** Marine ecology | **Platform:** Sentinel-2 (10–20 m), PRISMA | **Novelty:** T1

**Formula:**
```
CBSDI_pale = (B3 - B4) / (B3 + B4)           # stage 1
CBSDI_full = B2 / (B3 + B4 + B1)             # fully bleached
CBSDI_dead = (B3 / B4) - (B2 / B4)           # algae - colonized dead
```


---

### <a id="kcdsi"></a>KCDSI — Kelp Canopy Density and Stress Index
**Domain:** Marine ecology | **Platform:** Sentinel-2 + Sentinel-3 | **Novelty:** T2


---

### <a id="owsi"></a>OWSI — Oil Spill Weathering Stage Index
**Domain:** Marine pollution | **Platform:** EMIT, Sentinel-2 | **Novelty:** T2


---

### <a id="mdspi"></a>MDSPI — Mangrove Dieback Spatial Pattern Index
**Domain:** Marine ecology | **Platform:** Sentinel-2 + Sentinel-1 | **Novelty:** T1

**Formula:** Spatial pattern of NDVI loss + SAR backscatter change in mangrove zones.


---

### <a id="sgdci"></a>SGDCI — Submarine Groundwater Discharge Chemistry Index
**Domain:** Coastal hydrology | **Platform:** PACE OCI + ECOSTRESS | **Novelty:** T1

**Formula:**
```
SGDCI = (ρ_412 / ρ_550) - CDOM_regional_mean
```
Applied within thermal anomaly mask from ECOSTRESS.


---

### <a id="spei"></a>SPEI — Seagrass Photosynthetic Efficiency Index
**Domain:** Marine ecology | **Platform:** Sentinel-2, DESIS | **Novelty:** T2


---

### <a id="cduai"></a>CD-UAI — Coastal Dredging & Marine Siltation Plume Index
**Domain:** Coastal ecology | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:**
```
CD - UAI = turbidity_ratio * green_red_plume * (1 - cloud_SWIR_mask)
```

> **Claim strength:** Medium

---

### <a id="mppdi"></a>MP-PDI — Marine Plastisphere & Polymer Differentiation Index
**Domain:** Marine pollution | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:**
```
MP - PDI = FDI_base * (1 - Sargassum_rejection) * (1 - vegetation_rejection) * (1 - foam_rejection) * (1 - turbidity_rejection)
```

> **Claim strength:** High

---

## Section 5: Agriculture & Food Security

---

### <a id="npddi"></a>NPDDI — Nitrogen vs. Phosphorus Deficiency Discrimination Index
**Domain:** Precision agriculture | **Platform:** Sentinel-2, EnMAP | **Novelty:** T1

**Formula:**
```
NPDDI = [(B4 - B5) / (B4 + B5)] - [(B12 - B11) / (B12 + B11)]
```
Positive NPDDI = N deficiency. Negative = P deficiency.

**Physics:** N deficiency → chlorophyll degradation → red-edge shift (B5/B4 signal). P deficiency → anthocyanin accumulation → SWIR2 change (B12 signal). Index subtracts P signal from N signal, yielding signed nutrient discriminator.

**Benefit:** Enables precision nutrient prescription from orbit — reduces fertilizer over-application.


---

### <a id="scspi"></a>SCSPI — Soil Compaction Spectral Proxy Index
**Domain:** Agriculture / soil health | **Platform:** Sentinel-2 (bare soil windows) | **Novelty:** T1

**Formula:**
```
SCSPI = [1 - (B11 / B12)] * (B3 / B2)
```
Applied during bare-field windows.


---

### <a id="apri"></a>APRI — Aflatoxin Pre-Harvest Risk Index
**Domain:** Food security | **Platform:** ECOSTRESS + Sentinel-2 + ERA5 | **Novelty:** T1

**Formula:**
```
APRI = (LST_anomaly / σ) * [1 - NDWI] * heat_accumulation_days
```

**Physics:** Aspergillus infection risk peaks when heat stress + moisture deficit + heat accumulation coincide during flowering-to-grain-fill window.

**Benefit:** Pre-harvest aflatoxin risk mapping at field scale. Estimated 25% reduction in aflatoxin burden could prevent millions of cancer cases globally.


---

### <a id="pdsdi"></a>PDSDI — Pesticide vs. Drought Stress Discrimination Index
**Domain:** Precision agriculture | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:**
```
PDSDI = texture_cv(NDVI, 3 * 3 kernel) / [(B5 - B4) / (B5 + B4)]
```
High texture + moderate red-edge stress = pesticide (patchy necrosis). Low texture + uniform stress = drought.


---

### <a id="cctti"></a>CCTTI — Cover Crop Termination Timing Index
**Domain:** Agriculture | **Platform:** Sentinel-2 time series | **Novelty:** T2


---

### <a id="iwuei"></a>IWUEI — Irrigation Water Use Efficiency Index
**Domain:** Agriculture | **Platform:** ECOSTRESS + Sentinel-1 | **Novelty:** T2


---

### <a id="wdacsi"></a>WDA-CSI — Wetland Encroachment & Agricultural Intrusion Composite
**Domain:** Wetland / agriculture interface | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:**
```
WDA - CSI = nitrogen_chlorophyll_spike * peat_drainage_signal * NDWI_loss
```

> **Claim strength:** Medium

---

## Section 6: Mining & Industrial Contamination

---

### <a id="trsi"></a>TRSI — Tailings River Shock Index
**Domain:** Mining contamination | **Platform:** Sentinel-2 | **Novelty:** T2

**Formula:** `TRSI = turbidity_jump * ferric_color_shift * mine_proximity * persistence`

> **Claim strength:** Very High

---

### <a id="tdrasi"></a>TDR-ASI — Tailings Dam Runout & Acid Silt Index
**Domain:** Mining contamination | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:**
```
TDR - ASI = jarosite_signal * sulfate_absorption * mine_proximity_weight
```

> **Claim strength:** Medium-High

---

### <a id="amdphi"></a>AMDPHI — Acid Mine Drainage pH Proxy Index
**Domain:** Mining contamination | **Platform:** Sentinel-2, EMIT | **Novelty:** T1

**Formula:**
```
AMDPHI = [(B4 - B3) / (B4 + B3)] / [(B2 - B3) / (B2 + B3 + 0.001)]
```

**Physics:** AMD iron mineral precipitates are pH-diagnostic: jarosite (pH 2–3.5), schwertmannite (pH 3–4.5), goethite (pH 4.5–6). Ratio encodes iron mineral assemblage → pH range.

**Benefit:** Continental-scale AMD triage without field sampling at every site.


---

### <a id="tdsii"></a>TDSII — Tailings Dam Structural Integrity Index
**Domain:** Mining safety | **Platform:** Sentinel-2 + Sentinel-1 InSAR | **Novelty:** T1

**Formula:**
```
TDSII = w1 * NDWI_anomaly + w2 * ( - InSAR_subsidence_rate) + w3 * NDVI_decline_rate
```

**Physics:** Three precursors: downstream seepage (NDWI increase), structural settling (InSAR), vegetation stress from leachate (NDVI decline).

**Benefit:** Life-safety monitoring for all 14,000+ operational tailings dams globally.


---

### <a id="reesai"></a>REESAI — Rare Earth Element Surface Anomaly Index
**Domain:** Mining prospecting | **Platform:** EnMAP, EMIT | **Novelty:** T1

**Formula:**
```
REESAI = 1 - ρ(803nm) / [ρ(780nm) + (803 - 780) / (830 - 780) * (ρ(830nm) - ρ(780nm))]
```

**Physics:** Nd³⁺ f-f transition absorption at 803 nm in REE carbonate/phosphate minerals.

**Benefit:** Transforms REE exploration from field-campaign to satellite-first screening.


---

### <a id="ccrbi"></a>CCRBI — Coal Combustion Residue Bioaccumulation Index
**Domain:** Mining / environmental justice | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:**
```
CCRBI = [(B4 - B8) / (B4 + B8)] * [B3 / (B11 + 0.01)]
```

**Physics:** Grass over CCR impoundments accumulates As/Se causing anthocyanin stress response (elevated red reflectance). Harkness et al. 2025: "grass is a tattletale."


---

### <a id="hlpii"></a>HLPII — Heap Leach Pad Integrity Index
**Domain:** Mining | **Platform:** Sentinel-2, EMIT | **Novelty:** T1

**Formula:** SWIR2 anomaly from liner failure zone + EMIT mineral alteration in downslope soil.


---

### <a id="ierpi"></a>IERPI — Industrial Effluent River Plume Index
**Domain:** Mining | **Platform:** Landsat | **Novelty:** T2


---

## Section 7: Urban & Infrastructure

---

### <a id="ecaci"></a>EC-ACI — Evapotranspirative Canopy & Asphalt Contrast Index
**Domain:** Urban climate | **Platform:** Sentinel-2 + ECOSTRESS | **Novelty:** T2

> **Claim strength:** Medium

---

### <a id="hsai"></a>HSAI — Heat-Shelter Absence Index
**Domain:** Urban climate | **Platform:** Sentinel-2 | **Novelty:** T2

> **Claim strength:** Medium-High

---

### <a id="spsri"></a>SPSRI — Solar Panel Soiling Remote Index
**Domain:** Renewable energy / infrastructure | **Platform:** Sentinel-2, Planet | **Novelty:** T1

**Formula:**
```
SPSRI = (ρ_B2 - ρ_clean_baseline_B2) / ρ_clean_baseline_B2 * (B11 / B12)
```

**Physics:** Clean PV panels have very low reflectance (~5%). Dust-coated panels show elevated reflectance with dust mineralogy signature. B11/B12 ratio encodes dust mineral type.

**Benefit:** Optimizes cleaning crew deployment. Estimated global PV soiling loss exceeds $5B/year.


---

### <a id="uciei"></a>UCIEI — Urban Cool Infrastructure Effectiveness Index
**Domain:** Urban climate | **Platform:** Sentinel-2 + ECOSTRESS | **Novelty:** T1

**Formula:**
```
UCIEI = (1 - albedo_satellite) * LST_anomaly
```

**Physics:** High UCIEI = hot dark surface (old asphalt). Low UCIEI = effective cool infrastructure. Green roofs have low UCIEI despite low albedo because they convert absorbed energy to ET.

**Benefit:** Parcel-level scorecard for cool infrastructure programs.


---

### <a id="pcadi"></a>PCADI — Pavement Condition and Albedo Decay Index
**Domain:** Urban infrastructure | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:** `PCADI = (ρ_B2 - baseline_B2) / baseline_B2` within road network mask.


---

### <a id="csdei"></a>CSDEI — Construction Site Silica Dust Emission Index
**Domain:** Urban health | **Platform:** TROPOMI + GIS | **Novelty:** T1

**Formula:** `CSDEI = AOD_anomaly * construction_site_proximity * wind_vector`


---

### <a id="lfgvi"></a>LFGVI — Landfill Gas Vegetation Intrusion Index
**Domain:** Urban waste / environmental justice | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:**
```
LFGVI = red_edge_stress * moisture_loss * chlorosis_signal * ring_pattern_score
```

**Physics:** LFG creates characteristic annular NDVI depression around landfill boundary — geometrically distinctive and not mimicked by any natural stress pattern.

**Benefit:** Maps LFG migration extent — identifies properties where buried methane creates fire/explosion hazard.

> **Claim strength:** Very High

---

### <a id="lrdvsi"></a>LRD-VSI — Landfill Leachate & Runoff Degradation Vegetation Index
**Domain:** Environmental justice | **Platform:** Sentinel-2 | **Novelty:** T1

> **Claim strength:** High

---

## Section 8: Permafrost & Arctic

---

### <a id="ttapi"></a>TT-API — Thermokarst Thaw & Anoxic Peat Index
**Domain:** Permafrost / climate | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:**
```
TT - API = PeatExposure * WetAnoxic * EdgeCollapse
```

**Physics:** Dark anoxic peat (high SWIR2, depressed NIR), saturated zone (mid-NDWI signal), edge collapse (abrupt NDVI step at slump margins).

**Benefit:** Maps thermokarst features across circumpolar permafrost where >1,000 Gt carbon is at risk.

> **Claim strength:** Medium-High

---

### <a id="tperi"></a>TPERI — Thermokarst Pond Expansion Rate Index
**Domain:** Permafrost | **Platform:** Sentinel-2 bi-temporal | **Novelty:** T1

**Formula:**
```
TPERI = Δ(B11_t1 - B11_t2) / Δ(B3_t1 - B3_t2)
```

**Physics:** Active thermokarst expansion creates a transitional zone encoding expansion velocity directly.

**Benefit:** Provides the rate signal needed for carbon flux modeling — "how fast is this pond growing."


---

### <a id="pcei"></a>PCEI — Peat Carbon Exposure Index
**Domain:** Permafrost | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:** `PCEI = (1 - NDVI) * high_SWIR2 * (1 - NDWI)` — exposed dark peat without vegetation or water.


---

### <a id="sabsi"></a>SABSI — Snow/Ice Algae Bloom Severity Index
**Domain:** Permafrost / cryosphere | **Platform:** Sentinel-2, Planet | **Novelty:** T2


---

### <a id="fgdci"></a>FGDCI — Frozen Ground Dielectric Change Index
**Domain:** Permafrost | **Platform:** Sentinel-1 SAR | **Novelty:** T1

**Formula:**
```
FGDCI = (VV_dB - VH_dB) - seasonal_mean(VV_dB - VH_dB)
```

**Physics:** Frozen soil dielectric ~4; thawed ~20–30. 3–6 dB shifts in C-band VV. VV-VH difference normalizes vegetation effects; anomaly from seasonal mean isolates the freeze/thaw transition.

**Benefit:** Pan-Arctic freeze/thaw monitoring from Sentinel-1's global coverage.


---

### <a id="mepsi"></a>MEPSI — CH4 Ebullition Pond Spectral Proxy
**Domain:** Permafrost / climate | **Platform:** Sentinel-2, Planet | **Novelty:** T1

**Formula:** Open sediment-covered shallow water zones: high NDWI + low NDVI + low macrophyte chlorophyll index.


---

### <a id="alsi"></a>ALSI — Active Layer Depth Thermal-Spectral Composite Index
**Domain:** Permafrost | **Platform:** ECOSTRESS + Sentinel-2 | **Novelty:** T1

**Formula:**
```
ALSI = 0.6 * (LST_anomaly / σ_LST) + 0.4 * [(B12 - B11) / (B12 + B11)]
```

**Physics:** Deeper active layers → warmer surface temperatures + greater clay mineral exposure from frost churning.

**Benefit:** Satellite proxy for active layer depth — orders of magnitude denser than field probe networks.


---

## Section 9: Tropical Forest

---

### <a id="pdcsi"></a>PDCSI — Pre-Deforestation Canopy Stress Index
**Domain:** Tropical deforestation monitoring | **Platform:** Sentinel-2 red-edge | **Novelty:** T2

**Formula:**
```
PDCSI = [(B6 - B5) / (B6 + B5)] - [(B8A - B8) / (B8A + B8)]
```

**Physics:** Early-stage canopy thinning shifts the red-edge toward 705 nm — detectable 6–18 months before clear-cutting.


---

### <a id="lisi"></a>LISI — Liana Infestation Structural Index
**Domain:** Tropical forest health | **Platform:** Sentinel-2 | **Novelty:** T2

**Formula:**
```
LISI = 2.5 * [(B8 - B11) / (B8 + 6 * B4 - 7.5 * B2 + 1)] * (B8 / B11)
```


---

### <a id="ubcdi"></a>UBCDI — Understory vs. Canopy Burn Discrimination Index
**Domain:** Tropical fire ecology | **Platform:** Sentinel-2 bi-temporal | **Novelty:** T1

**Formula:**
```
UBCDI = (ΔB8 / B8_pre) / (ΔB4 / B4_pre)
```
Near -1 = canopy fire. Near 0 = surface fire.


---

### <a id="fedgi"></a>FEDGI — Forest Edge Degradation Gradient Index
**Domain:** Tropical forest | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:** NDVI gradient magnitude from forest interior toward edge, applied at 100 m buffer increments.


---

### <a id="slsdi"></a>SLSDI — Selective Logging Scar Detection Index
**Domain:** Tropical forest | **Platform:** Sentinel-2, Planet | **Novelty:** T2


---

### <a id="etcsi"></a>ETCSI — Emergent Tree Crown Stress Index
**Domain:** Tropical forest | **Platform:** Planet + Sentinel-2 | **Novelty:** T1

**Formula:** Planet 3 m resolution crown delineation + S2 red-edge stress per crown.


---

## Section 10: Dryland & Arid

---

### <a id="bscmci"></a>BSCMCI — Biological Soil Crust Multi-Condition Index
**Domain:** Dryland ecology | **Platform:** PRISMA, DESIS | **Novelty:** T1

**Formula:**
```
BSCMCI = [(ρ680 - ρ720) / (ρ680 + ρ720)] * [(ρ550 / ρ670) - 1]
```

**Physics:** BSC development stages have distinctive pigment signatures: early cyanobacteria (680 nm), mid-stage green algae (550 nm peak), advanced lichen (usnic acid), disturbed (bright mineral).


---

### <a id="sbci"></a>SBCI — Sabkha Brine Chemistry Index
**Domain:** Dryland / arid geomorphology | **Platform:** EMIT | **Novelty:** T1

**Formula:**
```
SBCI = depth(2217nm) / depth(2175nm)
```
Gypsum-to-anhydrite absorption depth ratio.

**Physics:** Gypsum at 2217 nm; anhydrite at 2175 nm. Anhydrite forms at higher brine concentration — ratio encodes brine concentration history. EMIT only.


---

### <a id="cscai"></a>CSCAI — Caliche Surface Carbonate Accumulation Index
**Domain:** Dryland pedology | **Platform:** EnMAP | **Novelty:** T1

**Formula:**
```
CSCAI = depth(2335nm) / depth(2160nm)
```
Calcite CO3²⁻ at 2335 nm vs. weaker feature at 2160 nm.


---

### <a id="defpi"></a>DEFPI — Dust Emission Flux Proxy Index
**Domain:** Dryland | **Platform:** EMIT + Sentinel-2 + SMAP | **Novelty:** T1

**Formula:** `DEFPI = mineral_erodibility(EMIT) * BSI(S2) * (1 - soil_moisture(SMAP))`


---

### <a id="dlpehi"></a>DLPEHI — Desert Locust Pre-Emergence Habitat Index
**Domain:** Food security / early warning | **Platform:** Sentinel-2 + GPM | **Novelty:** T1

**Formula:**
```
DLPEHI = NDWI * (0.1 < NDVI < 0.3) * (NDTI > - 0.2) * rainfall_binary
```

**Physics:** Logical conjunction: moist sandy soil + sparse greening vegetation + sandy loam texture after rain = oviposition habitat.

**Benefit:** 2–4 week earlier warning of locust outbreak habitat vs. vegetation-flush monitoring.


---

### <a id="aibeai"></a>AIBEAI — Arroyo Incision and Bank Erosion Activity Index
**Domain:** Dryland geomorphology | **Platform:** Sentinel-2, Planet | **Novelty:** T1

**Formula:**
```
AIBEAI = BSI_channel_bottom / NDVI_channel_margin
```

**Physics:** Active incision exposes fresh bright mineral soils (high BSI). Stable channels have established bank vegetation (positive NDVI at margins).


---

## Section 11: Wetland & Peatland

---

### <a id="pwtdi"></a>PWTDI — Peatland Water Table Depth Index
**Domain:** Wetland / carbon | **Platform:** Sentinel-2 + Sentinel-1 | **Novelty:** T2

**Formula:**
```
PWTDI = 0.65 * NDWI_1020 + 0.35 * (VV_dB - VH_dB)
```
Where `NDWI_1020 = (B8A - B9) / (B8A + B9)` (970 nm Sphagnum water feature).

**Physics:** Surface Sphagnum 970 nm absorption + C-band SAR fusion for WTD proxy.

**Benefit:** Global peatland WTD monitoring — the most important unmeasured variable in wetland carbon accounting.


---

### <a id="mhssp"></a>MHSSP — Methane Hotspot Surface Spectral Predictor
**Domain:** Wetland / climate | **Platform:** Sentinel-2 + TROPOMI | **Novelty:** T1

**Formula:**
```
MHSSP = NDWI * (1 - NDVI) * (1 - CI_rededge / max_CI_rededge_local)
```


---

### <a id="tfidi"></a>TFIDI — Tidal Flat Inundation Dynamics Index
**Domain:** Coastal wetland | **Platform:** Sentinel-2 monthly | **Novelty:** T1

**Formula:**
```
TFIDI = (NDWI_p90 - NDWI_p10) / NDWI_mean   [monthly composite]
```

**Physics:** High NDWI percentile spread = full tidal flat habitat; low spread = always-wet or always-dry.


---

### <a id="wdptzi"></a>WDPTZI — Wet-Dry Peatland Transition Zone Index
**Domain:** Peatland carbon | **Platform:** Sentinel-2 | **Novelty:** T1

**Formula:**
```
WDPTZI = spatial_gradient_magnitude[(B11 - B8A) / (B11 + B8A)]
```
Applied as Sobel edge detector to SWIR1/NIR ratio raster.


---

### <a id="ipvsi"></a>IPVSI — Invasive Phragmites vs. Native Vegetation
**Domain:** Wetland | **Platform:** Sentinel-2 seasonal | **Novelty:** T2


---

### <a id="wvtdi"></a>WVTDI — Wetland Vegetation Type Discrimination Index
**Domain:** Wetland | **Platform:** Sentinel-2 time series | **Novelty:** T2


---

## Section 12: Hyperspectral-Enabled Indices

*These indices require EMIT, EnMAP, PRISMA, PACE OCI, or DESIS — operationally impossible before 2019–2024.*

---

### <a id="pftib"></a>PFTIB — Phytoplankton Functional Type Index Battery
**Domain:** Ocean ecology / carbon cycle | **Platform:** PACE OCI | **Novelty:** T1

**Formula:**
```
PFT_diatom  = absorption(490nm) / absorption(440nm)
PFT_hapto   = absorption(453nm) / absorption(490nm)
PFT_prokary = ρ(490nm) / ρ(440nm)
PFT_crypto  = absorption(565nm) / absorption(490nm)
```

**Physics:** Diatoms → fucoxanthin (490–510 nm). Haptophytes → 19'-hex-fucoxanthin (453 nm). Prokaryotes → divinyl chlorophyll a (440 nm shift). Cryptophytes → phycoerythrin (565 nm). PACE OCI 5 nm bands resolve all four.

**Benefit:** Global phytoplankton community monitoring — enables carbon export estimates and HAB species prediction.


---

### <a id="cmsti"></a>CMSTI — Clay Mineral Stress Transition Index
**Domain:** Soil degradation | **Platform:** EMIT only | **Novelty:** T1

**Formula:**
```
CMSTI = position_minimum(2190 - 2220nm) - 2200
```
Negative shift = smectite. Positive = illite.

**Physics:** Smectite Al-OH at 2200 nm; illite at 2208 nm. This 8 nm shift requires EMIT's 5 nm bands — invisible to Sentinel-2, Landsat, or even EnMAP (10 nm).

**Benefit:** Maps irreversible soil degradation (smectite→illite) — permanent loss taking centuries to reverse.


---

### <a id="mpssfi"></a>MPSSFI — Methane Plume Spectral Shape Feature Index
**Domain:** Climate / methane | **Platform:** EMIT | **Novelty:** T2

**Formula:**
```
MPSSFI = 1 - ρ(1667nm) / [0.5 * (ρ(1640nm) + ρ(1700nm))]
```


---

### <a id="afcdi"></a>AFCDI — Asbestos Fiber Chrysotile Detection Index
**Domain:** Environmental health | **Platform:** EMIT, PRISMA | **Novelty:** T1

**Formula:**
```
AFCDI = depth(2317nm) / depth(2387nm)
```

**Physics:** Chrysotile Mg-OH doublet at 2317/2387 nm — discriminated from antigorite (2320/2100 nm) and lizardite (2320/2390 nm). EMIT's 5 nm sampling resolves the 70 nm separation.

**Benefit:** Natural asbestos zone mapping near communities.


---

### <a id="scfgosi"></a>SCFGOSI — Soil Carbon Functional Group Oxidation State Index
**Domain:** Carbon accounting | **Platform:** EMIT, EnMAP | **Novelty:** T1

**Formula:**
```
SCFGOSI = depth(1730nm) / (1 - mean_reflectance_400 - 2500nm)
```

**Physics:** Labile carbon (lipids, proteins) → C-H overtone at 1730 nm. Recalcitrant carbon (aromatic humus, char) → broad spectral darkness without sharp features. Ratio encodes labile vs. recalcitrant proportion.

**Benefit:** Distinguishes stable carbon (char, humus) from labile carbon — critical for understanding which soils store carbon permanently vs. lose it under warming.


---

### <a id="reenbi"></a>REENBI — REE Neodymium Band Depth Index
**Domain:** Critical minerals | **Platform:** EnMAP | **Novelty:** T1

**Formula:**
```
REENBI = 1 - ρ(803nm) / [ρ(780nm) + (803 - 780) / (830 - 780) * (ρ(830nm) - ρ(780nm))]
```

**Physics:** Nd³⁺ f-f transitions at 583, 740, and 803 nm in REE carbonate/phosphate minerals.

**Benefit:** Global REE deposit prospecting from EnMAP — transforms exploration from field-intensive to satellite-first.


---

### <a id="epcase"></a>EPCASE — EnMAP Porphyry Cu Alteration Sequence Index
**Domain:** Mining prospecting | **Platform:** EnMAP | **Novelty:** T1

**Formula:** SAM distance to porphyry alteration sequence endmember (phyllic → potassic → propylitic zones) from EnMAP L2A.


---

### <a id="dpcci"></a>DPCCI — DESIS Phycocyanin Column Concentration Index
**Domain:** Water quality | **Platform:** DESIS, PACE | **Novelty:** T2

**Formula:** `DPCCI = depth(621nm) / continuum` from DESIS 2.55 nm resolution.


---

## Section 13: Cross-Sensor Fusion Indices

---

### <a id="tseai"></a>TSEAI — TROPOMI–Sentinel-2 Emission Attribution Index
**Domain:** Climate / methane accountability | **Platform:** S5P TROPOMI + Sentinel-2 | **Novelty:** T1

**Formula:**
```
TSEAI = XCH4_TROPOMI_anomaly / Σ(source_fraction_i * emission_factor_i)
```
Where source_fraction_i = fractional area of each emission source type within TROPOMI pixel from S2 land cover.

**Physics:** Each emission source type has literature-derived emission factors. S2 maps source type fractions within each 5.5×7 km TROPOMI pixel. Ratio of observed to predicted enhancement identifies unaccounted sources.

**Benefit:** Transforms TROPOMI from "where is methane enhanced" to "what is emitting that methane."


---

### <a id="issai"></a>ISSAI — ICESat-2 + Sentinel-1 Subsidence Attribution Index
**Domain:** Infrastructure / geology | **Platform:** ICESat-2 + Sentinel-1 + Sentinel-2 | **Novelty:** T1

**Formula:**
```
ISSAI = (ICESat2_dZ / dt - InSAR_LOS_vertical) / ICESat2_dZ / dt
```

**Physics:** ICESat-2 measures absolute elevation change; InSAR measures relative deformation. Discrepancy between methods indicates rapid incoherent subsidence or different temporal sampling.

**Benefit:** Subsidence cause attribution for tens of millions in coastal cities.


---

### <a id="geawsi"></a>GEAWSI — GRACE-FO + ECOSTRESS Agricultural Water Stress Index
**Domain:** Food security / water | **Platform:** GRACE-FO + ECOSTRESS + ERA5 | **Novelty:** T1

**Formula:**
```
GEAWSI = (ET_ecostress / PET_estimate) * TWS_anomaly_sign
```

**Physics:** ET/PET < 1 = crop water stress. Negative TWS simultaneously = groundwater drawdown confirming supply-driven stress.

**Benefit:** Identifies irrigation systems where crop stress AND aquifer depletion co-occur — the most urgent water security scenario.


---

### <a id="emsmmi"></a>EMSMMI — EMIT Mineral + Sentinel-1 Soil Moisture Index
**Domain:** Hydrology | **Platform:** EMIT + Sentinel-1 | **Novelty:** T1

**Formula:**
```
EMSMMI = VWC_S1_raw / (1 + clay_fraction_EMIT * clay_dielectric_correction)
```

**Physics:** Clay minerals (especially smectite) have elevated ionic conductivity inflating C-band backscatter-to-moisture retrieval. EMIT mineral fraction maps provide the clay correction enabling mineralogy-specific VWC retrieval.

**Benefit:** Improved soil moisture accuracy at global scale — particularly in agricultural regions with high clay content where standard VWC estimates have systematic 15–25% errors.


---

### <a id="puenpi"></a>PUENPI — PACE + ECOSTRESS Coastal Wetland Net Ecosystem Production Index
**Domain:** Carbon accounting | **Platform:** PACE OCI + ECOSTRESS + ERA5 | **Novelty:** T1

**Formula:**
```
PUENPI = GPP_ECOSTRESS_proxy - NPP_PACE_aquatic - R_temperature_model
```

**Benefit:** Global coastal blue-carbon accounting — enables national carbon inventories to include coastal wetland carbon fluxes.


---

### <a id="nfcai"></a>NFCAI — NISAR + Sentinel-2 Forest Carbon Accumulation Index
**Domain:** Forest carbon | **Platform:** NISAR + Sentinel-2 | **Novelty:** T3

**Formula:**
```
NFCAI = L - band_HV * (1 - canopy_cover_S2) + L - band_HH * age_proxy_NDVI_trend
```

**Physics:** NISAR L-band (24 cm) penetrates canopy, encoding woody volume. NDVI time series provides stand age context.

**Benefit:** NISAR (operational 2024) enables global 10 m L-band SAR for forest carbon monitoring.


---

### <a id="snuvqi"></a>SNUVQI — NO₂ + Sentinel-2 Urban Vegetation Air Quality Index
**Domain:** Urban health | **Platform:** TROPOMI + Sentinel-2 + ERA5 | **Novelty:** T1

**Formula:**
```
SNUVQI = NO2_TROPOMI_downscaled - f(NDVI_S2, wind_ERA5)
```

**Benefit:** Maps which neighborhoods receive NO₂ benefit from urban trees — environmental justice analysis.


---

## Appendix: Standard Baselines (Published — No Claim)

These established indices are used as inputs to the novel composites above.

| Index | Formula | Purpose |
|-------|---------|---------|
| NDVI | `(B08 - B04) / (B08 + B04)` | Vegetation density |
| NDWI | `(B03 - B08) / (B03 + B08)` | Surface water |
| NDMI | `(B08 - B11) / (B08 + B11)` | Soil/canopy moisture |
| BSI | `((B11 + B04) - (B08 + B02)) / ((B11 + B04) + (B08 + B02))` | Bare soil |
| NDSI | `(B08 - B11) / (B08 + B11)` | Saline surface |
| HCAI | `(B11 - B12) / (B11 + B12)` | Hydrocarbon SWIR shoulder |
| HMRI | `(B03 - B02) / (B03 + B02)` | Heavy metal reflectance |
| NDOI | `(B03 - B11) / (B03 + B11)` | Oil slick |
| AOI | `(B04 - B02) / (B04 + B02)` | Fe³⁺ iron oxidation |
| NBR | `(B08 - B12) / (B08 + B12)` | Burn ratio |
| MSI | `B11 / B08` | Moisture stress |
| SAVI | `1.5 * (B08 - B04) / (B08 + B04 + 0.5)` | Vegetation, soil-corrected |
| FAI | Floating Algae Index (NIR - SWIR shoulder) | Floating vegetation |
| NDCI | `(B05 - B04) / (B05 + B04)` | Chlorophyll / algal bloom |
| EVI | `2.5 * (B08 - B04) / (B08 + 6 * B04 - 7.5 * B02 + 1)` | Vegetation, soil+atm corrected |

---

## Authorship Summary

**All novel indices below were originated, named, and formulated by Daniel Bally (Globe & Atlas), May 2026.**

| Project | What Daniel created | Tier | Claim strength |
|---------|---------------------|------|----------------|
| **limn** — PWCI, ASAI, VSI, OBEC, FBC, LBI, TRI, BPI, REAI, VCBI, CMA, PHI, HMI, EHC, SCRI, MVPI | Named the index, wrote the formula, defined the gate logic, validated against 27 TRRC confirmed sites | T1 | Very High — empirically validated |
| **limn platform extensions** — PBMEI, EMIT-BMIN, EMIT-HC, PW-ETA, ASTER-GSI, GOES-FCI, OLCI-PWWCI, GRACE-PWI, PB-CDI | Named the index, wrote the formula, proposed the cross-sensor application | T1 | High — physically grounded, proposed |
| **civic-sentinel** — CSRC, TRSI, LFGVI, SWRI, BH-DFSI, MP-PDI, LRD-VSI, DWCI, RRFI, EPDI, TDR-ASI, PETI, TT-API, HSAI, EC-ACI, SF-EII, WDA-CSI, CD-UAI | Named the index, wrote the gate logic, defined the civic screening workflow | T1/T2 | Very High to Medium (see authorshipClaims.js) |
| **globe-and-atlas global survey** — 79 indices across 12 domains | Named the index, wrote the first standardized formula, proposed the novel sensor application | T1/T2/T3 | High (T1), Medium (T2/T3) |

---

## Publication-Ready Claim Language

For any index when publishing or presenting, substitute the correct tier phrase:

**T1 (Unclaimed):**
> "I originated and named [INDEX NAME] — a [domain] screening index with no equivalent formula in the published literature as of May 2026. The formula [one sentence on what it does]. [Validation if any.]"

**T2 (Underspecified):**
> "I formalized [INDEX NAME] — the detection concept has been described qualitatively, but no standardized formula or acronym had been published. The formula [one sentence on what it does]."

**T3 (Sensor-Enabled):**
> "I wrote the first operational formula for [INDEX NAME], enabled by [SENSOR] launched in [year]. The underlying spectral physics is established; this is the first formula that can actually be computed from open satellite data."

**For all tiers — always include the limit clause:**
> "This index [what it does not measure / what it cannot confirm]. It is a screening tool for triage, not a substitute for [field measurement / lab analysis / regulatory confirmation]."

**Critical rule:** Every published claim must include what the index does NOT do. This is what separates a defensible claim from an overclaim.

---

*PRIVATE — GITIGNORED — Last updated: 2026-05-25*
*Author: Daniel Bally · Globe & Atlas · <dbally@gmail.com>*
*Cross-reference public ATLAS.md for formulas, physics, and public benefit language.*
*Cross-reference civic-sentinel/src/authorshipClaims.js for verbatim civic-sentinel claim language.*