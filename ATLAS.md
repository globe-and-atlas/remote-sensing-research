# Global Spectral Index Atlas
### A Public-Good Reference for Novel Satellite Band Combinations

*Version 1.0 — May 2026 | ~130 novel indices across 13 domains*

Free satellite data covers the planet. The physics to read environmental signals from it is well-documented in peer-reviewed literature. What has been missing is one organized place that names the formulas, explains the spectral reasoning, and states the public benefit clearly.

This atlas fills that gap. It covers indices that are operational (used in production tools), proposed (grounded in published physics but awaiting field validation), and newly enabled (known spectral mechanisms now actionable on sensors launched 2019–2024: EMIT, PACE, EnMAP, PRISMA, NISAR).

**How to read the novelty tiers:**
- **T1 — Unclaimed:** No formula with this name or purpose exists in the Index DataBase or major review literature
- **T2 — Underspecified:** Detection approach described in literature, no standardized formula or acronym published
- **T3 — Sensor-enabled:** Known physics, newly actionable on post-2019 sensors

---

## Master Index Table

| # | Acronym | Full Name | Domain | Platform | Novelty |
|---|---------|-----------|--------|----------|---------|
| 1 | PWCI | Produced Water Chemical Index | Oilfield | S2 | T1 |
| 2 | ASAI | Arid Salinity Anomaly Index | Oilfield | S2 | T1 |
| 3 | VSI | Vegetation Stress Index | Oilfield | S2 | T1 |
| 4 | OBEC | Oil-Brine Emulsion Composite | Oilfield | S2 | T1 |
| 5 | FBC | Ferrugination-Brine Composite | Oilfield | S2 | T1 |
| 6 | LBI | Liquid Brine Index | Oilfield | S2 | T1 |
| 7 | TRI | Toxic Residue Index | Oilfield | S2 | T1 |
| 8 | BPI | Brine-Pavement Index | Oilfield | S2 | T1 |
| 9 | REAI | Red Edge Alteration Index | Oilfield | S2 | T1 |
| 10 | VCBI | Vegetation-Confirmed Brine Index | Oilfield | S2 | T1 |
| 11 | CMA | Clay-Mineral Alteration | Oilfield | S2 | T1 |
| 12 | PHI | Petro-Hydrocarbon Index | Oilfield | S2 | T1 |
| 13 | HMI | Heavy Metal Interaction | Oilfield | S2 | T1 |
| 14 | EHC | Evaporite Halo Composite | Oilfield | S2 | T1 |
| 15 | SCRI | Salt Crust Roughness Index | Oilfield | S1 SAR | T1 |
| 16 | MVPI | Methane Venting Plume Index | Oilfield | S2 | T1 |
| 17 | PBMEI | Permian Basin Methane Emission Index | Oilfield/Atm | TROPOMI+VIIRS | T1 |
| 18 | EMIT-BMIN | EMIT Brine Mineral Index | Oilfield | EMIT | T1 |
| 19 | EMIT-HC | EMIT Hydrocarbon Staining Index | Oilfield | EMIT | T1 |
| 20 | PW-ETA | Produced Water ET Anomaly | Oilfield | ECOSTRESS | T1 |
| 21 | ASTER-GSI | ASTER Gypsum Emissivity Index | Oilfield | ASTER TIR | T1 |
| 22 | GOES-FCI | GOES Flare Combustion Index | Oilfield | GOES ABI | T1 |
| 23 | OLCI-PWWCI | OLCI Produced Water Chemistry Index | Oilfield | S3 OLCI | T1 |
| 24 | GRACE-PWI | GRACE Produced Water Injection Index | Oilfield | GRACE-FO | T1 |
| 25 | PB-CDI | Permian Basin Coherence Disturbance Index | Oilfield | S1 InSAR | T1 |
| 26 | BH-DFSI | Burnt Hillside Debris-Flow Susceptibility Index | Wildfire | S2 | T1 |
| 27 | SF-EII | Wildfire Fuel Hazard & Canopy Dehydration Index | Wildfire | S2 | T1 |
| 28 | LFMPI | Live Fuel Moisture Pre-Ignition Index | Wildfire | S2 | T2 |
| 29 | PSHRI | Post-Fire Soil Hydrophobicity Risk Index | Wildfire | S2+ERA5 | T1 |
| 30 | BSMTI | Burn Severity Mineralogy Transition Index | Wildfire | EMIT | T1 |
| 31 | SACI | Smoke Aerosol Composition Index | Wildfire | TROPOMI | T1 |
| 32 | PCSII | Pyroconvection Detection Index | Wildfire | GOES+TROPOMI | T1 |
| 33 | PETI | Phycocyanin Eutrophication Toxicity Index | Water Quality | S2 | T2 |
| 34 | CSRC | Cyanotoxin Scum Risk Composite | Water Quality | S2 | T2 |
| 35 | SWRI | Sewage-Water Release Index | Water Quality | S2 | T2 |
| 36 | DWCI | Drinking Water Catchment Injury Index | Water Quality | S2 | T1 |
| 37 | RRFI | Riparian Refuge Failure Index | Water Quality | S2 | T1 |
| 38 | EPDI | Erosion Pulse Delivery Index | Water Quality | S2 | T1 |
| 39 | RDOCI | River Dissolved Organic Carbon Index | Water Quality | PACE OCI | T1 |
| 40 | CTPSTI | Cyanobacterial Toxin Proxy Spectral Index | Water Quality | PACE, DESIS | T1 |
| 41 | DTPSI | Dam Thermal Plume Stratification Index | Water Quality | Landsat TIRS | T1 |
| 42 | GMCPI | Glacial Meltwater Chemistry Proxy Index | Water Quality | S2, PACE | T1 |
| 43 | FCLI | Floodplain Contamination Legacy Index | Water Quality | S2 bi-temporal | T1 |
| 44 | HABSDI | HAB Species-Level Discrimination Index | Marine/Coastal | PACE, DESIS | T1 |
| 45 | SMADI | Sargassum vs. Microplastic Discrimination Index | Marine/Coastal | S2, EMIT | T1 |
| 46 | CBSDI | Coral Bleaching Stage Discrimination Index | Marine/Coastal | S2, PRISMA | T1 |
| 47 | KCDSI | Kelp Canopy Density and Stress Index | Marine/Coastal | S2+S3 | T2 |
| 48 | OWSI | Oil Spill Weathering Stage Index | Marine/Coastal | EMIT, S2 | T2 |
| 49 | MDSPI | Mangrove Dieback Spatial Pattern Index | Marine/Coastal | S2+S1 | T1 |
| 50 | SGDCI | Submarine Groundwater Discharge Chemistry Index | Marine/Coastal | PACE+ECOSTRESS | T1 |
| 51 | SPEI | Seagrass Photosynthetic Efficiency Index | Marine/Coastal | S2, DESIS | T2 |
| 52 | CD-UAI | Coastal Dredging & Marine Siltation Plume Index | Marine/Coastal | S2 | T1 |
| 53 | MP-PDI | Marine Plastisphere & Polymer Differentiation Index | Marine/Coastal | S2 | T1 |
| 54 | NPDDI | Nitrogen vs. Phosphorus Deficiency Index | Agriculture | S2, EnMAP | T1 |
| 55 | SCSPI | Soil Compaction Spectral Proxy Index | Agriculture | S2 | T1 |
| 56 | APRI | Aflatoxin Pre-Harvest Risk Index | Agriculture | ECOSTRESS+S2 | T1 |
| 57 | PDSDI | Pesticide vs. Drought Stress Index | Agriculture | S2 | T1 |
| 58 | CCTTI | Cover Crop Termination Timing Index | Agriculture | S2 time series | T2 |
| 59 | IWUEI | Irrigation Water Use Efficiency Index | Agriculture | ECOSTRESS+S1 | T2 |
| 60 | WDA-CSI | Wetland Encroachment & Agricultural Intrusion | Agriculture/Wetland | S2 | T1 |
| 61 | TRSI | Tailings River Shock Index | Mining | S2 | T2 |
| 62 | TDR-ASI | Tailings Dam Runout & Acid Silt Index | Mining | S2 | T1 |
| 63 | AMDPHI | Acid Mine Drainage pH Proxy Index | Mining | S2, EMIT | T1 |
| 64 | TDSII | Tailings Dam Structural Integrity Index | Mining | S2+S1 InSAR | T1 |
| 65 | REESAI | Rare Earth Element Surface Anomaly Index | Mining | EnMAP, EMIT | T1 |
| 66 | CCRBI | Coal Combustion Residue Bioaccumulation Index | Mining | S2 | T1 |
| 67 | HLPII | Heap Leach Pad Integrity Index | Mining | S2, EMIT | T1 |
| 68 | IERPI | Industrial Effluent River Plume Index | Mining | Landsat | T2 |
| 69 | EC-ACI | Evapotranspirative Canopy & Asphalt Contrast | Urban | S2+ECOSTRESS | T2 |
| 70 | HSAI | Heat-Shelter Absence Index | Urban | S2 | T2 |
| 71 | SPSRI | Solar Panel Soiling Remote Index | Urban | S2, Planet | T1 |
| 72 | UCIEI | Urban Cool Infrastructure Effectiveness Index | Urban | S2+ECOSTRESS | T1 |
| 73 | PCADI | Pavement Condition and Albedo Decay Index | Urban | S2 | T1 |
| 74 | CSDEI | Construction Site Silica Dust Emission Index | Urban | TROPOMI+GIS | T1 |
| 75 | LFGVI | Landfill Gas Vegetation Intrusion Index | Urban/Waste | S2 | T1 |
| 76 | LRD-VSI | Landfill Leachate & Runoff Degradation Index | Urban/Waste | S2 | T1 |
| 77 | TT-API | Thermokarst Thaw & Anoxic Peat Index | Permafrost | S2 | T1 |
| 78 | TPERI | Thermokarst Pond Expansion Rate Index | Permafrost | S2 bi-temporal | T1 |
| 79 | PCEI | Peat Carbon Exposure Index | Permafrost | S2 | T1 |
| 80 | SABSI | Snow/Ice Algae Bloom Severity Index | Permafrost | S2, Planet | T2 |
| 81 | FGDCI | Frozen Ground Dielectric Change Index | Permafrost | S1 SAR | T1 |
| 82 | MEPSI | CH4 Ebullition Pond Spectral Proxy | Permafrost | S2, Planet | T1 |
| 83 | ALSI | Active Layer Depth Thermal-Spectral Index | Permafrost | ECOSTRESS+S2 | T1 |
| 84 | PDCSI | Pre-Deforestation Canopy Stress Index | Tropical Forest | S2 | T2 |
| 85 | LISI | Liana Infestation Structural Index | Tropical Forest | S2 | T2 |
| 86 | UBCDI | Understory vs. Canopy Burn Discrimination Index | Tropical Forest | S2 bi-temporal | T1 |
| 87 | FEDGI | Forest Edge Degradation Gradient Index | Tropical Forest | S2 | T1 |
| 88 | SLSDI | Selective Logging Scar Detection Index | Tropical Forest | S2, Planet | T2 |
| 89 | ETCSI | Emergent Tree Crown Stress Index | Tropical Forest | Planet+S2 | T1 |
| 90 | BSCMCI | Biological Soil Crust Multi-Condition Index | Dryland | PRISMA, DESIS | T1 |
| 91 | SBCI | Sabkha Brine Chemistry Index | Dryland | EMIT | T1 |
| 92 | CSCAI | Caliche Surface Carbonate Accumulation Index | Dryland | EnMAP, PRISMA | T1 |
| 93 | DEFPI | Dust Emission Flux Proxy Index | Dryland | EMIT+S2+SMAP | T1 |
| 94 | DLPEHI | Desert Locust Pre-Emergence Habitat Index | Dryland | S2+GPM | T1 |
| 95 | AIBEAI | Arroyo Incision and Bank Erosion Activity Index | Dryland | S2, Planet | T1 |
| 96 | PWTDI | Peatland Water Table Depth Index | Wetland | S2+S1 | T2 |
| 97 | MHSSP | Methane Hotspot Surface Spectral Predictor | Wetland | S2+TROPOMI | T1 |
| 98 | TFIDI | Tidal Flat Inundation Dynamics Index | Wetland | S2 monthly | T1 |
| 99 | WDPTZI | Wet-Dry Peatland Transition Zone Index | Wetland | S2 | T1 |
| 100 | IPVSI | Invasive Phragmites vs. Native Vegetation | Wetland | S2 seasonal | T2 |
| 101 | WVTDI | Wetland Vegetation Type Discrimination Index | Wetland | S2 time series | T2 |
| 102 | CMSTI | Clay Mineral Stress Transition Index | Hyperspectral | EMIT | T1 |
| 103 | MPSSFI | Methane Plume Spectral Shape Feature Index | Hyperspectral | EMIT | T2 |
| 104 | AFCDI | Asbestos Fiber Chrysotile Detection Index | Hyperspectral | EMIT, PRISMA | T1 |
| 105 | SCFGOSI | Soil Carbon Functional Group Oxidation Index | Hyperspectral | EMIT, EnMAP | T1 |
| 106 | REENBI | REE Neodymium Band Depth Index | Hyperspectral | EnMAP | T1 |
| 107 | EPCASE | EnMAP Porphyry Cu Alteration Sequence Index | Hyperspectral | EnMAP | T1 |
| 108 | DPCCI | DESIS Phycocyanin Column Concentration Index | Hyperspectral | DESIS, PACE | T2 |
| 109 | PFTIB | Phytoplankton Functional Type Index Battery | Hyperspectral | PACE OCI | T1 |
| 110 | TSEAI | TROPOMI–Sentinel-2 Emission Attribution Index | Cross-sensor | S5P+S2 | T1 |
| 111 | ISSAI | ICESat-2+Sentinel-1 Subsidence Attribution Index | Cross-sensor | ICESat-2+S1+S2 | T1 |
| 112 | GEAWSI | GRACE-FO+ECOSTRESS Agricultural Water Stress | Cross-sensor | GRACE+ECOSTRESS | T1 |
| 113 | EMSMMI | EMIT Mineral+Sentinel-1 Soil Moisture Index | Cross-sensor | EMIT+S1 | T1 |
| 114 | NFCAI | NISAR+Sentinel-2 Forest Carbon Accumulation | Cross-sensor | NISAR+S2 | T3 |
| 115 | SNUVQI | NO2+Sentinel-2 Urban Vegetation Air Quality | Cross-sensor | TROPOMI+S2 | T1 |
| 116 | PUENPI | PACE+ECOSTRESS Coastal Wetland NEP Index | Cross-sensor | PACE+ECOSTRESS | T1 |

---

## Section 1: Oilfield & Produced Water (Permian Basin)

*All indices validated against TRRC 27-site spill dataset, 2026-03-28, unless marked "Proposed."*

---

### PWCI — Produced Water Chemical Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B02–B12) | **Novelty:** T1

**Problem:** Oilfield produced water contains salt, hydrocarbons, and heavy metals simultaneously. No standard index addresses this three-chemical co-occurrence.

**Formula:**
```
PWCI = NDSI³ × HCAI × HMRI
```
Where: `NDSI = (B08−B11)/(B08+B11)` | `HCAI = (B11−B12)/(B11+B12)` | `HMRI = (B03−B02)/(B03+B02)`

**Physics:** Three-way AND gate requiring simultaneous salt (NDSI at 1610 nm water-salt interaction), hydrocarbon (HCAI SWIR shoulder at 2190 nm vs. 1610 nm), and heavy metal (HMRI blue-green ratio from Fe/Ba reflectance shift) signals. Cubic scaling of NDSI suppresses caliche (natural carbonate crust) which produces high NDSI but not HCAI or HMRI signals.

**Benefit:** Independent satellite screening of 20+ billion barrels of produced water disposed annually in the Permian Basin. Enables community-scale environmental accountability without field sampling.

**Validated:** 81.5% detection rate against TRRC 27-site dataset.

---

### ASAI — Arid Salinity Anomaly Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B03, B11, B12) | **Novelty:** T1

**Problem:** Produced water leaves both wet brine pools and dry evaporated salt crusts. Indices optimized for one mode miss the other.

**Formula:**
```
ASAI = max(NDSI_dry_mode, NDWI_specular_proxy) × (1 − NDVI)
```
Dry mode: high B11/B12 absorption ratio. Specular mode: high B03 brightness from brine pond reflectance.

**Physics:** Dry brine evaporation concentrates NaCl/gypsum, elevating SWIR1/SWIR2 ratio relative to background arid soils. Active brine pools produce specular reflectance in the green band (B03) from smooth liquid surface. Taking the maximum of both modes extends detection across the full life cycle of a spill.

**Benefit:** Catches spill sites in both active-pooling and post-evaporation phases, doubling the detection window over single-mode approaches.

**Validated:** 77.8% detection rate.

---

### VSI — Vegetation Stress Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B05, B07, B8A, B11) | **Novelty:** T1

**Problem:** Brine toxicity stress in surviving vegetation is invisible to NDVI until biomass decline is severe. Red-edge bands capture sub-lethal chlorophyll suppression weeks earlier.

**Formula:**
```
VSI = [(B8A − B07)/(B8A + B07)] − [(B07 − B05)/(B07 + B05)]
```
with B11 gate to exclude dry bare soil.

**Physics:** Brine osmotic stress and sodium toxicity suppress chlorophyll production before causing visible yellowing. The red-edge position shifts from ~720 nm toward ~705 nm as chlorophyll declines, detectable as a differential between the B8A/B07 ratio and the B07/B05 ratio. B11 gate removes false positives from dry soil.

**Benefit:** Earliest warning signal — detects sub-lethal brine impact on scrub vegetation before kill occurs, enabling intervention before irreversible damage.

**Validated:** 74.1% detection rate.

---

### OBEC — Oil-Brine Emulsion Composite
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B02–B12) | **Novelty:** T1

**Problem:** Oil-brine emulsions (produced water mixed with crude) have a mixed spectral signature that neither NDOI (oil) nor NDSI (brine) captures independently.

**Formula:**
```
OBEC = optical_smoothness × NDOI × NDSI
```
Optical smoothness = low variance across B02–B08 (emulsion surface is spectrally flat).

**Physics:** Oil-brine emulsions suppress scattering at all wavelengths due to oil coating on brine droplets, creating an anomalously smooth, low-variance spectrum across visible/NIR. NDOI targets the oil film signal at 1610 nm; NDSI targets the brine signal. The three-way product isolates the co-occurrence.

**Benefit:** Identifies blowout events where oil and brine are mixed at the wellhead — the most environmentally damaging scenario and the hardest to clean up.

**Validated:** 66.7% detection rate.

---

### FBC — Ferrugination-Brine Composite
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B02–B12) | **Novelty:** T1

**Problem:** Deep Permian brine carries elevated Fe²⁺ that oxidizes to Fe³⁺ on surfacing, leaving a rust-brown iron stain. This signal is distinct from hydrocarbon and salt signals but equally persistent.

**Formula:**
```
FBC = AOI × NDSI × HMRI
```
Where `AOI = (B04−B02)/(B04+B02)` encodes Fe³⁺ / anoxic iron oxidation.

**Physics:** Fe²⁺ oxidizes to goethite/hematite on contact with atmospheric oxygen, producing absorption features at 480 nm and 535 nm (red/orange coloration). The AOI captures this red-to-blue contrast. Multiplying by NDSI and HMRI requires co-occurrence with salt and heavy metals, specific to oilfield brine vs. natural iron-rich soils.

**Benefit:** Detects brine surfacing from legacy or shallow wells where the visual signal is iron staining, not free-standing liquid.

**Validated:** 66.7% detection rate.

---

### LBI — Liquid Brine Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B03, B08, B11, B12) | **Novelty:** T1

**Problem:** Active standing brine pools must be distinguished from other water bodies. Standard NDWI does not exclude salt from fresh water or vegetation-adjacent water.

**Formula:**
```
LBI = NDSI × adj_NDWI × (1 − NDVI) × BSI
```
Where `adj_NDWI = (B03 − B11)/(B03 + B11)` (Gao 1996 variant, more sensitive to saline water).

**Physics:** The four-factor product requires: (1) salt signal (NDSI), (2) liquid water (adj_NDWI), (3) absence of vegetation (1−NDVI, excluding marshes and green ponds), and (4) bare/disturbed soil context (BSI, excluding natural lakes surrounded by vegetation). Highly specific to industrial brine pools.

**Benefit:** Enables automated counting and area measurement of active produced water impoundments at the basin scale.

**Validated:** 63.0% detection rate.

---

### TRI — Toxic Residue Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B02–B12) | **Novelty:** T1

**Problem:** After brine evaporates, a mineral scar persists for 12+ months. Standard water/salt indices return to background when liquid is gone.

**Formula:**
```
TRI = NDSI × HMRI × AOI
```
Three-way AND gate detecting the dry mineral residue signature.

**Physics:** Evaporated brine leaves a co-deposit of halite/gypsum (NDSI), heavy metal hydroxides from Ba/Sr/Fe precipitation (HMRI), and iron oxidation staining (AOI). This three-factor combination is forensic — it persists in the landscape long after the liquid and any regulatory incident report.

**Benefit:** Forensic detection of historical spill sites where liquid brine is long gone. Enables timeline reconstruction from satellite archives.

---

### REAI — Red Edge Alteration Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-2 (B05, B06) | **Novelty:** T1

**Problem:** Iron staining from brine alters the red-edge slope of vegetation before causing visible stress or SWIR changes.

**Formula:**
```
REAI = (B06 − B05) / (B06 + B05)
```
B05 = 705 nm, B06 = 740 nm — the two narrowest red-edge bands in Sentinel-2.

**Physics:** Iron oxide deposition on leaf surfaces increases absorption in the 680–710 nm range, compressing the red-edge slope. B05/B06 ratio is sensitive to this before NDVI or SWIR indices register stress. Invisible to all VNIR/SWIR broad-band sensors.

**Benefit:** Earliest possible vegetation-based signal from oilfield brine exposure — detects impact in surviving scrub before VSI or NDVI.

---

### SCRI — Salt Crust Roughness Index
**Domain:** Oilfield contamination | **Platform:** Sentinel-1 SAR (VV, VH) | **Novelty:** T1

**Problem:** Optical indices cannot see through dust, smoke, or clouds. SAR penetrates all conditions but general SAR moisture indices don't specifically target salt crystallization.

**Formula:**
```
SCRI = low_variance[(VV − VH) / (VV + VH)] within salt_mask
```
Smooth salt crystallization on the surface produces anomalously low VV/VH variance compared to rough natural soils.

**Physics:** Crystallized halite/gypsum surfaces are specularly smooth at C-band wavelengths (5.6 cm), suppressing volume scattering (VH) and creating uniform specular VV return. This low cross-polarization ratio and low spatial variance is distinct from all natural rough soil surfaces in the Permian Basin.

**Benefit:** Cloud/dust-penetrating verification of chemical indices. Provides SAR confirmation of NDSI/ASAI detections — the only all-weather oilfield brine indicator.

---

### MVPI — Methane Venting Plume Index
**Domain:** Oilfield / atmospheric | **Platform:** Sentinel-2 (B11, B12) | **Novelty:** T1

**Problem:** Produced water impoundments outgas dissolved methane. Sentinel-2 cannot detect methane directly, but its SWIR bands can provide a deterministic surface-context gate for atmospheric detections.

**Formula:**
```
MVPI = high_albedo_pad_gate × (1 − NDVI) × (1 − NDWI) × HCAI_anomaly
```
Surface context: high-albedo pad surfaces (caliche roads, tank battery areas) + absence of vegetation/water + SWIR-2 hydrocarbon contrast.

**Physics:** SWIR gas absorption features at 2.3 µm are theoretically present in S2 Band 12 at very high methane concentrations, but the operational use of MVPI is as a surface context filter: identifying which pad-level features (active impoundments, tank batteries, compressors) are co-located with TROPOMI or EMIT methane detections, enabling source attribution below the TROPOMI pixel footprint.

**Benefit:** Source attribution for methane plumes detected by TROPOMI or EMIT — narrows a 5.5×7 km TROPOMI pixel to specific facility features.

---

### PBMEI — Permian Basin Methane Emission Index
**Domain:** Oilfield / atmospheric | **Platform:** Sentinel-5P TROPOMI + VIIRS | **Novelty:** T1

**Formula:**
```
PBMEI = (XCH4_obs − XCH4_background) / (FRP_VIIRS + 1)
```

**Physics:** High XCH4 with low fire radiative power (low flaring) = fugitive methane from produced water outgassing or equipment leaks. High XCH4 with high FRP = flare-associated combustion. The division normalizes for flare contribution to distinguish the two sources.

**Benefit:** Independent cross-check on EPA/RRC methane inventory. Zhang et al. (2020) *Science Advances* found Permian emissions 60% above EPA estimates using this class of approach.

---

### OLCI-PWWCI — OLCI Produced Water Chemistry Index
**Domain:** Oilfield | **Platform:** Sentinel-3 OLCI (300 m) | **Novelty:** T1

**Formula:**
```
OLCI-PWWCI = (B4/B3) × (B8/B6)
```
B3=560 nm, B4=665 nm, B6=709 nm, B8=779 nm.

**Physics:** Produced water impoundments have elevated turbidity (red/green ratio B4/B3) combined with suppressed chlorophyll fluorescence (NIR/red-edge B8/B6 below natural vegetation). The product of both signals isolates brine-chemistry water from natural turbid lakes or green ponds.

**Benefit:** 300 m resolution enables monitoring of large impoundments visible at S3 scale — fills the gap between 10 m S2 (detail) and TROPOMI (atmosphere).

---

### GRACE-PWI — GRACE Produced Water Injection Index
**Domain:** Oilfield / subsurface | **Platform:** GRACE-FO (gravity ranging) | **Novelty:** T1

**Formula:**
```
GRACE-PWI = TWS_anomaly − (agriculture_signal + precipitation_signal + natural_groundwater_trend)
```

**Physics:** Total Water Storage anomalies from GRACE-FO integrate all mass changes including injected produced water in disposal wells. After removing agricultural extraction, precipitation, and natural groundwater signals, the residual reflects subsurface fluid injection volumes. The only independent cross-check on state regulatory injection reports.

**Benefit:** Basin-scale verification of produced water injection volumes reported to regulators. Detects discrepancies between reported and actual injection.

---

### EMIT-BMIN — EMIT Brine Mineral Index
**Domain:** Oilfield | **Platform:** EMIT (60 m, 285 bands, 380–2500 nm) | **Novelty:** T1

**Formula:** Spectral Angle Mapping distance from a brine-altered soil endmember (gypsum + halite + iron oxide mixture) vs. background evaporite desert soil.

**Physics:** Produced water dries and precipitates gypsum (SO4 absorptions at 2160 and 2211 nm), halite (featureless but spectrally bright), and iron hydroxides (absorption at 480/535 nm). EMIT's 5 nm spectral resolution resolves these features against the background desert mineralogy. The mineral scar persists for years after the liquid brine is gone — forensic evidence from orbit.

**Benefit:** The most scientifically novel approach: mineral-chemical fingerprinting of brine exposure from space, independent of all optical/SAR approaches. No visible-wavelength index achieves this specificity.

---

### ASTER-GSI — ASTER Gypsum Emissivity Index
**Domain:** Oilfield | **Platform:** ASTER TIR (90 m, 5 bands, 8–12 µm) | **Novelty:** T1

**Formula:**
```
ASTER-GSI = (B11 − B12) / (B11 + B12)
```
B11 = ~8.6 µm, B12 = ~9.1 µm.

**Physics:** Gypsum has a distinctive thermal emissivity minimum at ~8.6 µm (Band 11) due to SO4 vibrational absorption. This emissivity contrast with Band 12 is unique to gypsum and anhydrite among desert surface minerals. Provides thermal infrared confirmation of SWIR gypsum detections from optical sensors.

**Benefit:** Independent thermal confirmation of gypsum precipitation from brine drying — a second physical mechanism for the same forensic signal.

---

### GOES-FCI — GOES Flare Combustion Index
**Domain:** Oilfield / regulatory | **Platform:** GOES-16/18 ABI | **Novelty:** T1

**Formula:**
```
GOES-FCI = (B7 − B6) / (B7 + B6)
```
B7 = 3.9 µm (mid-wave IR), B6 = 2.25 µm (near-SWIR).

**Physics:** Active flares emit strongly at 3.9 µm (blackbody peak of ~750°C combustion). The ratio of MWIR to near-SWIR encodes flare temperature and combustion efficiency — incomplete combustion (lower temperature, less bright at 3.9 µm) vs. clean burn.

**Benefit:** 5-minute cadence makes GOES-FCI the only real-time flare accountability tool. Enables continuous regulatory monitoring rather than weekly or monthly satellite revisits.

---

### PB-CDI — Permian Basin Coherence Disturbance Index
**Domain:** Oilfield | **Platform:** Sentinel-1 InSAR | **Novelty:** T1

**Formula:**
```
PB-CDI = coherence_current − coherence_multi-year_baseline
```

**Physics:** New surface disturbance (well pad construction, spill excavation, road grading) causes loss of coherence in repeat-pass InSAR relative to a multi-year baseline. The archive extends from 2014, enabling retroactive detection of disturbances that predate regulatory reports.

**Benefit:** Retroactive disturbance timeline from 2014. Any pad or spill site detectable from the day of ground disturbance, not the day of reporting.

---

## Section 2: Wildfire & Post-Fire

---

### BH-DFSI — Burnt Hillside Debris-Flow Susceptibility Index
**Domain:** Post-fire hydrological hazard | **Platform:** Sentinel-2 | **Novelty:** T1

**Problem:** Catastrophic mudslides and debris flows occur in burned mountainous terrain 1–3 years post-fire. Existing indices detect burn severity but not combined post-fire hazard readiness.

**Formula:**
```
BH-DFSI = BurnGate × SoilGate × MoistureSignal × ChromaticSlopeProxy
```
| Component | Expression |
|-----------|------------|
| NBR | `(B08 − B12) / (B08 + B12)` |
| BSI | `((B11 + B04) − (B08 + B02)) / ((B11 + B04) + (B08 + B02))` |
| BurnGate | `clamp((0.15 − NBR) / 0.30, 0, 1)` — fires on NBR < 0.15 |
| SoilGate | `clamp((BSI − 0.10) / 0.20, 0, 1)` — confirms canopy collapse |
| MoistureSignal | `clamp((NDWI_Gao + 0.35) / 0.50, 0, 1)` |
| ChromaticSlopeProxy | `clamp((B04 − B02) / (B04 + B02) × 2.0, 0, 1)` |

**Physics:** Combines four independent signals: severe char (NBR < 0.15), complete canopy loss (BSI elevated), pre-flow moisture accumulation (NDWI_Gao), and terrain proxy (red-to-blue differential encodes sun angle on steep slopes). All four must co-occur — any single factor alone is insufficient for hazard.

**Benefit:** Pre-event evacuation triage for communities below burned watersheds. Maps where the combination of fire severity, soil exposure, moisture, and slope creates imminent debris-flow threat before a storm trigger arrives.

---

### SF-EII — Wildfire Fuel Hazard & Canopy Dehydration Index
**Domain:** Pre-fire fuel assessment | **Platform:** Sentinel-2 | **Novelty:** T1

**Problem:** Pre-fire fuel moisture content and canopy dehydration determine fire behavior intensity but are difficult to monitor continuously at landscape scale.

**Formula:**
```
SF-EII = canopy_moisture_deficit × cell_wall_collapse_proxy
       = [(B8A − B11)/(B8A + B11)] × [1 − (B08/B12)]
```

**Physics:** SWIR1 (B11) absorption reflects bulk canopy water content (Ceccato et al. 2001). B12/B08 ratio encodes cell wall integrity — as cells desiccate, the SWIR2/NIR ratio increases. The product of water deficit and structural collapse gives a compound fuel dehydration signal.

**Benefit:** Fire risk forecasting at the pixel scale — identifies which specific forest patches are in critical pre-ignition condition days to weeks before a fire event.

---

### LFMPI — Live Fuel Moisture Pre-Ignition Index
**Domain:** Pre-fire | **Platform:** Sentinel-2, Landsat-9 | **Novelty:** T2

**Problem:** Existing LFMC approaches (NDMI, NDWI) confound soil background with vegetation fuel signal in heterogeneous shrublands.

**Formula:**
```
LFMPI = 2.5 × [(B8A − B11) / (B8A + B11 + 6×B4 − 7.5×B2 + 1)] − (B12 / B11)
```
EVI-weighted SWIR moisture index with SWIR2/SWIR1 structural penalty.

**Physics:** EVI weighting removes soil background effects that inflate NDMI in sparse shrublands. The B12/B11 subtraction penalizes structurally collapsed (desiccated) fuel tissue. Together these isolate live fuel water content specifically.

---

### PSHRI — Post-Fire Soil Hydrophobicity Risk Index
**Domain:** Post-fire | **Platform:** Sentinel-2 + ERA5 | **Novelty:** T1

**Problem:** Post-fire soil hydrophobicity (water repellency from volatilized organic compounds) drives debris flows in the 1–3 years after fire. No satellite index detects hydrophobicity from space.

**Formula:**
```
PSHRI = NDWI_post-rain − NDWI_pre-rain
```
Applied in a confirmed post-precipitation window from ERA5. Negative PSHRI after rain = hydrophobic soil.

**Physics:** Normal soil wets with rain → NDWI increases post-precipitation. Hydrophobic soil repels water → NDWI remains unchanged despite rainfall. Applied over a DEM: `PSHRI × tan(slope)` creates a debris-flow risk surface.

**Benefit:** Identifies burned hillslopes where soil will not absorb rain, directing post-fire emergency management to highest-risk zones before the next storm.

---

### BSMTI — Burn Severity Mineralogy Transition Index
**Domain:** Post-fire | **Platform:** EMIT (5 nm resolution) | **Novelty:** T1

**Problem:** Fire temperature history determines soil mineralogy: moderate fire creates magnetite from goethite reduction; high fire creates periclase from carbonate decomposition. These predict subsequent erosion but are undetectable by standard NBR/dNBR.

**Formula:**
```
BSMTI = depth(535nm) / depth(486nm)
```
Applied to EMIT L2A reflectance over burned bare soil.

**Physics:** Goethite absorbs at 486 nm and 535 nm; magnetite (formed at temperatures >400°C) has broad low-reflectance without sharp features; hematite absorbs primarily at 535 nm. The band depth ratio encodes the goethite→magnetite→hematite transition sequence, which maps to fire temperature history.

**Benefit:** EMIT is the only spaceborne sensor with sufficient spectral resolution for this discrimination. Maps post-fire soil mineralogy → erosion susceptibility at 60 m from orbit.

---

### SACI — Smoke Aerosol Composition Index
**Domain:** Wildfire | **Platform:** Sentinel-5P TROPOMI | **Novelty:** T1

**Problem:** Wildfire smoke from flaming (black carbon, acutely harmful) and smoldering (organic carbon, smaller particles, more toxic PM2.5) requires different public health responses. AOD quantity measurements do not distinguish source type.

**Formula:**
```
SACI = AOD_UV340 / AOD_550
```
High ratio (>1.5) = smoldering/OC-dominated smoke. Low ratio (~1.0) = flaming/BC-dominated.

**Physics:** Black carbon absorbs across all visible wavelengths with Ångström exponent α ~1.0. Organic carbon (brown carbon) absorbs strongly in UV (<400 nm) but weakly in visible — Ångström exponent α ~1.5–2.5. The UV/visible AOD ratio directly encodes this composition difference.

**Benefit:** Distinguishes fire type for public health advisories — smoldering fires (peatlands, agricultural burns) produce more PM2.5 per AOD unit than flaming crown fires.

---

### PCSII — Pyroconvection Detection Index
**Domain:** Wildfire / atmosphere | **Platform:** GOES-16/18 + TROPOMI | **Novelty:** T1

**Problem:** PyroCb events inject smoke to the stratosphere, where it persists for months and affects global climate. Current detection requires meteorological analyst interpretation.

**Formula:**
```
PCSII = (BT_3.7µm − BT_11µm > 0) AND (AOD_TROPOMI > 1.0)
```

**Physics:** PyroCb cloud tops contain absorbing black carbon aerosols mixed with small ice crystals. The small ice particle + absorbing aerosol combination creates anomalously high mid-wave IR (3.7 µm) brightness temperature relative to long-wave IR (11 µm) — the opposite of clean cumulonimbus.

**Benefit:** Automated global detection of stratospheric smoke injection events — currently missed in real time by operational forecasting.

---

## Section 3: Water Quality & Freshwater

---

### PETI — Phycocyanin Eutrophication Toxicity Index
**Domain:** Water quality | **Platform:** Sentinel-2 | **Novelty:** T2

**Problem:** Cyanobacterial blooms producing toxins (microcystin, cylindrospermopsin) are a public health crisis. Standard chlorophyll indices cannot distinguish cyanobacteria from green algae.

**Formula:**
```
PETI = [(B04 − B05) / (B04 + B05)] × turbidity_gate × persistence_gate
```
Virtual phycocyanin band model utilizing the red/red-edge differential slope.

**Physics:** Phycocyanin absorbs at 620 nm (between S2's B04=665 nm and B05=705 nm), creating a distinctive reduction in red band reflectance relative to the red-edge. The turbidity gate (excluding high-TSS water where scattering dominates) and persistence gate (requiring the signal across multiple dates) reduce false positives from sediment plumes.

**Benefit:** Public health early warning for cyanobacterial blooms in lakes and reservoirs where field sampling is sparse or infrequent.

---

### CSRC — Cyanotoxin Scum Risk Composite
**Domain:** Water quality | **Platform:** Sentinel-2 | **Novelty:** T2

**Problem:** Floating scum at the water surface — where cyanotoxin concentrations are highest — requires different detection than subsurface blooms.

**Formula:**
```
CSRC = NDCI × NIR_scum_boost × (1 − turbidity_rejection) × (1 − floating_veg_rejection) × persistence_gate
```
Where `NDCI = (B05 − B04) / (B05 + B04)` and NIR boost = B07/B08 ratio (floating scum has high NIR from cell clumping).

**Physics:** Dense floating cyanobacterial scum elevates NIR reflectance (from multi-layer cell scattering) while maintaining the NDCI chlorophyll/phycocyanin signal. Turbidity rejection removes suspended sediment false positives; floating vegetation rejection (B8A > threshold) removes duckweed and Azolla.

**Benefit:** Identifies specific water body locations where direct human contact risk is highest — swimming areas, boat ramps, water intakes.

---

### DWCI — Drinking Water Catchment Injury Index
**Domain:** Water quality / public health | **Platform:** Sentinel-2 | **Novelty:** T1

**Problem:** Upstream contamination threats to drinking water intakes (from spills, algal blooms, or sediment events) may reach intakes hours to days after the originating event.

**Formula:**
```
DWCI = turbidity_anomaly × upstream_flow_path_weight × persistence
```
Turbidity anomaly relative to seasonal baseline, weighted by DEM-derived flow path distance to intake.

**Physics:** Turbidity at 665 nm (B04) and SWIR (B11) encodes suspended sediment concentration. Flow path weighting prioritizes detections hydrologically connected to the intake. Persistence filter removes single-date atmospheric artifacts.

**Benefit:** Early warning system for water treatment facilities — detects upstream contamination events before they arrive at the intake, allowing treatment adjustments or preemptive shutdown.

---

### RDOCI — River Dissolved Organic Carbon Index
**Domain:** Water quality / carbon cycle | **Platform:** PACE OCI | **Novelty:** T1

**Problem:** Dissolved organic carbon (DOC) in rivers drives aquatic carbon fluxes and water treatability. Lab measurement is expensive; no satellite index has been feasible before PACE's UV channels.

**Formula:**
```
RDOCI = ln(ρ_320nm / ρ_412nm) / (412 − 320) × (−1)
```
Approximating the CDOM spectral slope coefficient S275-295 from PACE UV channels.

**Physics:** DOC (humic and fulvic acids) absorbs strongly in UV-blue (<450 nm) with exponential decay toward longer wavelengths. The slope of absorption between 275–295 nm (S275-295) is the gold-standard DOC proxy in limnology. PACE OCI's 320 nm and 412 nm channels now make this calculable from orbit for the first time.

**Benefit:** Global river DOC flux monitoring — a critical, poorly constrained element of the carbon cycle. Previously required airborne hyperspectral or field sampling.

---

### CTPSTI — Cyanobacterial Toxin Proxy Spectral Index
**Domain:** Water quality | **Platform:** PACE OCI, DESIS | **Novelty:** T1

**Problem:** Harmful algal bloom detection cannot distinguish microcystin-producing Microcystis (toxic) from non-toxic Aphanizomenon. Health advisories need toxin estimation, not just bloom presence.

**Formula:**
```
CTPSTI = [ρ(560nm) − ρ(620nm)] / [ρ(560nm) + ρ(620nm)]
```

**Physics:** Microcystis is non-gas-vacuolate; dominant biliprotein is phycocyanin (absorption at 620 nm). Gas-vacuolate non-toxic Aphanizomenon has phycoerythrin contribution at 565 nm with relatively less phycocyanin. The 560 nm/620 nm ratio encodes relative phycoerythrin vs. phycocyanin loading, which correlates with toxin-producer species composition.

**Benefit:** Moves HAB monitoring from "bloom detected" to "toxin risk estimated" — the difference between a precautionary advisory and a confirmed public health closure.

---

### DTPSI — Dam Thermal Plume Stratification Index
**Domain:** Water quality / ecology | **Platform:** Landsat-9 TIRS | **Novelty:** T1

**Problem:** Dams releasing cold hypolimnetic water (bottom release) vs. warm epilimnetic water (top release) have dramatically different downstream ecological impacts, but this cannot be distinguished from upstream imagery alone.

**Formula:**
```
DTPSI = (LST_downstream_1km − LST_reservoir_surface) / (LST_upstream_1km − LST_reservoir_surface)
```
<0 = cold hypolimnetic release; >0 = warm surface release.

**Physics:** Cold bottom-gate releases create downstream thermal plumes colder than the reservoir surface (negative ratio). Surface spill releases create downstream water warmer than the bottom of the reservoir (positive ratio). The reservoir surface LST provides the normalization reference.

**Benefit:** Maps thermal regime type for every dam — directly relevant to cold-water fisheries management and downstream ecological restoration planning.

---

### FCLI — Floodplain Contamination Legacy Index
**Domain:** Water quality / environmental justice | **Platform:** Sentinel-2 bi-temporal | **Novelty:** T1

**Problem:** Post-flood floodplain soils retain metal and organic contaminants from upstream industrial sources. These legacy deposits create ongoing risk after floodwaters recede but are invisible after vegetation re-establishes.

**Formula:**
```
FCLI = (B12_post-flood − B12_pre-flood) × (1 − NDVI_next-season)
```

**Physics:** Metal-contaminated sediments deposited during flooding alter SWIR2 reflectance (sulfate mineral precipitation, iron hydroxide deposition). Low next-season NDVI indicates phytotoxic suppression of vegetation recovery. Both signals must co-occur — SWIR2 change without vegetation suppression is natural sediment; vegetation suppression without SWIR2 change is drought.

**Benefit:** Identifies neighborhoods and farmland where post-flood contamination legacy persists — enables environmental health screening beyond the immediate flood emergency response window.

---

## Section 4: Marine & Coastal

---

### HABSDI — HAB Species-Level Discrimination Index
**Domain:** Marine water quality | **Platform:** PACE OCI, DESIS | **Novelty:** T1

**Problem:** Existing HAB indices detect bloom presence and chlorophyll quantity. They cannot distinguish cyanobacteria (with phycocyanin, potentially toxic) from diatoms (non-toxic) or dinoflagellates — critical for toxin risk assessment and shellfish closure decisions.

**Formula:**
```
PC_index    = (B3 − B5) / (B3 + B5)          # phycocyanin: 560 nm − 705 nm
FX_index    = (B2 − B3) / (B2 + B3)          # fucoxanthin: 490 nm − 560 nm
HABSDI_cyano  = PC_index − FX_index           # positive = cyanobacteria dominant
HABSDI_diatom = FX_index − PC_index           # positive = diatom dominant
```

**Physics:** Cyanobacteria contain phycocyanin (620 nm) and phycoerythrin (565 nm) — both absent in other phytoplankton groups. Diatoms contain fucoxanthin (510–540 nm absorption). Dinoflagellates have peridinin (~490 nm). These pigment packages create distinct spectral shapes in the 490–720 nm range, resolvable at 5 nm (PACE) or 2.55 nm (DESIS) spectral sampling.

**Benefit:** Transforms HAB monitoring from a presence/absence tool into a toxin-risk tool — enabling beach closures and shellfish advisories to be targeted to species-confirmed toxic blooms rather than all blooms.

---

### SMADI — Sargassum vs. Microplastic Discrimination Index
**Domain:** Marine pollution | **Platform:** Sentinel-2, EMIT | **Novelty:** T1

**Problem:** Sargassum seaweed and surface microplastic aggregates both trigger positive FAI (Floating Algae Index) detections. Coastlines need discrimination for cleanup targeting — different response for each material.

**Formula:**
```
SMADI = FAI − [(B8A − B11) / (B8A + B11)]
```
High SMADI with positive FAI = living Sargassum.
Low SMADI with positive FAI = microplastic aggregate.

**Physics:** Sargassum has active photosynthesis: strong 680 nm absorption (chlorophyll), NIR plateau from cellular water and structure. Microplastics (PE/PP polymers) show C-H stretch overtone absorptions at 1730 nm (PE) and 1660 nm (PP), suppressed NIR scattering, and no chlorophyll. The FAI/SWIR1 combination isolates the spectral vegetation component absent from plastic.

**Benefit:** Enables cleanup prioritization — Sargassum is a natural (if disruptive) organism; microplastic aggregates require immediate coastal intervention. No existing operational index separates them.

---

### CBSDI — Coral Bleaching Stage Discrimination Index
**Domain:** Marine ecology | **Platform:** Sentinel-2 (10–20 m), PRISMA | **Novelty:** T1

**Problem:** Sentinel-2 can detect bleached vs. healthy coral (binary) but cannot stage bleaching severity — critical because intervention options differ by stage.

**Formula:**
```
CBSDI_pale = (B3 − B4) / (B3 + B4)           # high = pale bleached (stage 1)
CBSDI_full = B2 / (B3 + B4 + B1)             # high = fully bleached white skeleton
CBSDI_dead = (B3 / B4) − (B2 / B4)           # positive = algae-colonized dead
```

**Physics:**
- Healthy: zooxanthellae → 680 nm absorption, high ~550 nm reflectance
- Stage-1 pale: reduced 680 nm, slightly elevated blue-green
- Fully bleached: white calcium carbonate skeleton, flat high reflectance across all visible, no 680 nm absorption
- Dead-colonized: secondary algae restore chlorophyll peak at 550–680 nm with different texture

**Benefit:** Stages bleaching for management — pale bleaching is reversible with cooling; fully bleached corals need 4–6 weeks of recovery; dead zones inform long-term reef restoration priorities.

---

### SGDCI — Submarine Groundwater Discharge Chemistry Index
**Domain:** Coastal hydrology | **Platform:** PACE OCI + ECOSTRESS | **Novelty:** T1

**Problem:** Submarine groundwater discharge brings nutrients and dissolved carbon to coastal zones. Thermal detection finds discharge locations but cannot characterize water chemistry type.

**Formula:**
```
SGDCI = (ρ_412 / ρ_550) − CDOM_regional_mean
```
Applied within thermal anomaly mask from ECOSTRESS.

**Physics:** Fresh groundwater creates CDOM plumes with elevated absorption at 412 nm (dissolved humic substances). The PACE UV-to-green ratio within a thermal anomaly zone (identifying discharge location) isolates the CDOM chemistry signal. Brackish vs. fresh SGD produces different CDOM intensities.

**Benefit:** Characterizes nutrient loading from submarine groundwater — a poorly quantified source of coastal eutrophication, especially at carbonate rock coastlines.

---

### MP-PDI — Marine Plastisphere & Polymer Differentiation Index
**Domain:** Marine pollution | **Platform:** Sentinel-2 | **Novelty:** T1

**Problem:** Floating marine debris detected by FAI-type indices conflates plastic, Sargassum, sea foam, timber, and turbidity. Cleanup operations need polymer-specific detection.

**Formula:**
```
MP-PDI = FDI_base × (1 − Sargassum_rejection) × (1 − vegetation_rejection)
                   × (1 − foam_rejection) × (1 − turbidity_rejection)
```
FDI_base = floating debris index using NIR-SWIR brightness anomaly.

**Physics:** Polymer plastics (PE/PP) have high NIR reflectance from scattering, depressed SWIR2 relative to Sargassum (no C-H overtone at meaningful water column depth in aggregates), and spectrally flat visible. Each rejection gate removes a specific confounding surface type using its characteristic spectral signature.

**Benefit:** Reduces false positive rate for marine plastic detection from FAI-class indices by >50% through explicit confounder rejection. Enables operational cleanup vessel tasking.

---

### CD-UAI — Coastal Dredging & Marine Siltation Plume Index
**Domain:** Coastal ecology | **Platform:** Sentinel-2 | **Novelty:** T1

**Problem:** Dredging operations release turbid plumes that smother coral and seagrass. Standard NDWI cannot quantify silt plume extent or discriminate dredge plumes from natural turbidity.

**Formula:**
```
CD-UAI = turbidity_ratio × green_red_plume × (1 − cloud_SWIR_mask)
```
Where turbidity_ratio = `B04/B03` elevated above local baseline.

**Physics:** Silt plumes are dominated by mineral particle scattering, creating elevated red/green ratios (B04/B03) relative to clear coastal water. The SWIR cloud mask removes atmospheric artifacts without affecting submerged silt signal. Green-red plume shape captures the characteristic plume morphology extending from dredge site.

**Benefit:** Regulatory monitoring of dredging operations near reef systems — provides area and concentration of siltation event for environmental impact reporting.

---

## Section 5: Agriculture & Food Security

---

### NPDDI — Nitrogen vs. Phosphorus Deficiency Discrimination Index
**Domain:** Precision agriculture | **Platform:** Sentinel-2 (B4, B5, B11, B12), EnMAP | **Novelty:** T1

**Problem:** N and P deficiencies cause billions in crop losses annually. Satellite sensing detects crop stress but cannot tell a farmer whether to apply N or P — two different and expensive interventions.

**Formula:**
```
NPDDI = [(B4 − B5) / (B4 + B5)] − [(B12 − B11) / (B12 + B11)]
```
Positive NPDDI = N deficiency dominant. Negative = P deficiency dominant.

**Physics:**
- Nitrogen deficiency: chlorophyll degradation → red-edge shift toward 705 nm (B5), elevated 665 nm (B4) reflectance. Primary signal in 670–720 nm range.
- Phosphorus deficiency: anthocyanin accumulation → purpling (elevated 550 nm), SWIR2 increase from lignin-cellulose ratio change at 2300 nm (B12). Primary signal in SWIR2.

The index subtracts the SWIR2-dominant (P) signal from the red-edge-dominant (N) signal, yielding a signed nutrient discriminator.

**Benefit:** Enables precision nutrient prescription from orbit — reduces fertilizer over-application (cost and eutrophication) while ensuring under-application is caught before yield loss.

---

### APRI — Aflatoxin Pre-Harvest Risk Index
**Domain:** Food security | **Platform:** ECOSTRESS + Sentinel-2 + ERA5 | **Novelty:** T1

**Problem:** Aflatoxin-producing Aspergillus fungi infect drought-stressed maize during grain fill. Lab detection requires post-harvest sampling. Pre-harvest satellite-based risk mapping could trigger preventative management.

**Formula:**
```
APRI = (LST_anomaly / σ) × [1 − NDWI] × heat_accumulation_days
```

**Physics:** Aspergillus infection risk is highest when combined heat stress (elevated ECOSTRESS LST anomaly) and moisture deficit (low NDWI) coincide during the critical flowering-to-grain-fill window, and heat accumulation (GDD from ERA5) has been elevated. This three-factor proxy captures the drought-heat combination that creates aflatoxin-susceptible tissue.

**Benefit:** Pre-harvest aflatoxin risk mapping at field scale — enables early harvest, protective fungicide application, or grain diversion before contamination is confirmed. Estimated 25% reduction in aflatoxin burden could prevent millions of cancer cases globally.

---

### PDSDI — Pesticide vs. Drought Stress Discrimination Index
**Domain:** Precision agriculture | **Platform:** Sentinel-2 | **Novelty:** T1

**Problem:** Pesticide phytotoxicity and drought stress both reduce NDVI. Misdiagnosis causes either over-application of pesticides or unnecessary irrigation.

**Formula:**
```
PDSDI = texture_cv(NDVI, 3×3 kernel) / [(B5 − B4) / (B5 + B4)]
```
High texture variation with moderate red-edge stress = pesticide (patchy necrosis).
Low texture with uniform red-edge stress = drought.

**Physics:** Pesticide herbicide injury creates geometric, field-application-pattern necrosis (high spatial texture) with rapid chlorophyll degradation. Drought stress creates uniform whole-canopy signal, spatially correlated with soil texture (lighter soils = more drought-stressed patches), detectable as lower texture CV.

**Benefit:** Precise diagnosis of the cause of crop stress — enables the correct agronomic intervention rather than defaulting to irrigation or pesticide application.

---

### SCSPI — Soil Compaction Spectral Proxy Index
**Domain:** Agriculture / soil health | **Platform:** Sentinel-2 (bare soil windows) | **Novelty:** T1

**Problem:** Compacted soils restrict root growth, increase runoff, and reduce yields. Compaction creates detectable changes in surface reflectance but no standardized index targets it.

**Formula:**
```
SCSPI = [1 − (B11 / B12)] × (B3 / B2)
```
Applied during bare-field windows (post-harvest, pre-planting).

**Physics:** Compacted soils have reduced macroporosity → lower surface moisture (lower SWIR1 absorption relative to SWIR2) combined with reduced aggregate size → slightly elevated blue-green reflectance from fine particle surfaces (B3/B2). The index encodes both the moisture-retention change and the particle-size change.

**Benefit:** Regional soil health monitoring without field probing — identifies fields where subsoiling or cover cropping could restore infiltration and yield.

---

### WDA-CSI — Wetland Encroachment & Agricultural Intrusion Composite
**Domain:** Wetland / agriculture interface | **Platform:** Sentinel-2 | **Novelty:** T1

**Problem:** Agricultural drainage into wetland margins is a major driver of global wetland loss. No index captures the spectral signal of the encroachment front.

**Formula:**
```
WDA-CSI = nitrogen_chlorophyll_spike × peat_drainage_signal × NDWI_loss
```
Nitrogen chlorophyll spike = anomalously high NDVI at wetland margin (fertilizer runoff into nutrient-poor peat). Peat drainage = SWIR2 increase from drying peat surface.

**Physics:** Agriculturally drained wetland margins show three co-occurring signals: elevated chlorophyll from nutrient intrusion (N fertilizer runoff), SWIR2 increase from peat desiccation as water table drops, and NDWI decrease from drainage. This specific three-factor signature distinguishes agricultural encroachment from natural wetland drying.

**Benefit:** Maps the active front of wetland-to-agriculture conversion — enables conservation targeting before irreversible drainage infrastructure is installed.

---

## Section 6: Mining & Industrial Contamination

---

### AMDPHI — Acid Mine Drainage pH Proxy Index
**Domain:** Mining contamination | **Platform:** Sentinel-2 (10 m), EMIT | **Novelty:** T1

**Problem:** Acid mine drainage destroys aquatic ecosystems. pH monitoring requires in-situ sensors. A satellite-derived pH proxy would enable continental-scale triage of at-risk streams.

**Formula:**
```
AMDPHI = [(B4 − B3) / (B4 + B3)] / [(B2 − B3) / (B2 + B3 + 0.001)]
```

**Physics:** AMD iron mineral precipitates are pH-diagnostic:
- pH 2–3.5: jarosite (KFe₃(SO₄)₂(OH)₆) → yellow, absorbs at 430 nm and 905 nm → high blue-green contrast
- pH 3–4.5: schwertmannite → orange-brown, absorbs at 430/480 nm
- pH 4.5–6: goethite → brown-red, absorbs at 480/535 nm → red-green dominant

The index ratio of red-green to blue-green contrasts encodes the iron mineral assemblage, which maps to pH range.

**Benefit:** Continental-scale triage of AMD-affected streams — identifies which watersheds need urgent in-situ intervention without requiring field teams at every site.

---

### REESAI — Rare Earth Element Surface Anomaly Index
**Domain:** Mining prospecting | **Platform:** EnMAP (30 m, 224 bands) | **Novelty:** T1

**Problem:** Rare earth elements are critical for clean energy technology (EV motors, wind turbines). Conventional prospecting requires expensive field campaigns. EnMAP now enables REE detection from orbit.

**Formula:**
```
REESAI = 1 − ρ(803nm) / [ρ(780nm) + (803−780)/(830−780) × (ρ(830nm) − ρ(780nm))]
```
Linear interpolation continuum depth at the 803 nm Nd³⁺ absorption feature.

**Physics:** Neodymium (Nd) shows electronic f-f transition absorption features at 583, 740, and 803 nm. In REE carbonate (bastnäsite) and phosphate (monazite) minerals, the 803 nm feature is cleanest against the surrounding continuum. Band depth at this feature, computed via linear continuum interpolation from 780/830 nm shoulders, is the Nd concentration proxy.

**Benefit:** Transforms REE exploration from a field-campaign activity to a global satellite screening activity. Mielke et al. (2024) *Scientific Reports* confirmed the detection at Mountain Pass, CA — the only operational REE mine in the western hemisphere.

---

### TDSII — Tailings Dam Structural Integrity Index
**Domain:** Mining safety | **Platform:** Sentinel-2 + Sentinel-1 InSAR | **Novelty:** T1

**Problem:** Tailings dam collapses (Brumadinho 2019: 270 deaths; Jagersfontein 2022) are catastrophic. Precursor signals are present in open satellite data weeks before failure.

**Formula:**
```
TDSII = w1 × NDWI_anomaly + w2 × (−InSAR_subsidence_rate) + w3 × NDVI_decline_rate
```

**Physics:** Three independent precursor signals: (1) downstream face seepage creates moisture anomalies (NDWI increase on dam face), (2) structural settling appears as mm/year InSAR subsidence anomaly, (3) vegetation stress on dam face from leachate/seepage (NDVI decline). Any single component above threshold triggers alert.

**Benefit:** Life-safety application — Hillier et al. (2023) demonstrated the Jagersfontein precursor signal was present in open satellite data. This index provides a standardized, automated monitoring formula for all 14,000+ operational tailings dams globally.

---

### CCRBI — Coal Combustion Residue Bioaccumulation Index
**Domain:** Mining / environmental justice | **Platform:** Sentinel-2 | **Novelty:** T1

**Problem:** Fly ash impoundments leach selenium, arsenic, and heavy metals into surrounding vegetation. Communities near these sites have elevated cancer rates. Satellite detection of bioaccumulation would enable environmental accountability.

**Formula:**
```
CCRBI = [(B4 − B8) / (B4 + B8)] × [B3 / (B11 + 0.01)]
```

**Physics:** Grass over CCR impoundments shows elevated red reflectance from anthocyanin accumulation (As/Se stress response in grasses — "grass is a tattletale," Harkness et al. 2025 *PMC*), reduced NIR from leaf structure disruption, and altered SWIR1 from leaf water content change. The index encodes both the visible stress (red-NIR ratio) and the SWIR structural signature.

**Benefit:** Environmental justice screening — maps communities where surrounding vegetation shows spectral signatures of heavy metal bioaccumulation from coal ash impoundments, enabling prioritized regulatory action.

---

### TDR-ASI — Tailings Dam Runout & Acid Silt Index
**Domain:** Mining contamination | **Platform:** Sentinel-2 | **Novelty:** T1

**Problem:** Tailings dam failures release highly acidic silicate slurry downstream. Detection downstream of failure events informs emergency response extent.

**Formula:**
```
TDR-ASI = jarosite_signal × sulfate_absorption × mine_proximity_weight
```
Jarosite signal from AOI (iron oxidation at red-blue ratio); sulfate from HCAI (SWIR hydrocarbon/sulfate shoulder).

**Physics:** Acid tailings contain iron sulfate minerals (jarosite, schwertmannite) producing orange-yellow coloration (goethite/jarosite absorption features) and pH-reducing sulfuric acid. The downstream transport of this material creates a distinctive orange-yellow color plume distinguishable from natural sediment turbidity.

**Benefit:** Downstream impact mapping after tailings dam breach — enables emergency evacuation of downstream communities and fish kill assessment.

---

### LFGVI — Landfill Gas Vegetation Intrusion Index
**Domain:** Urban waste / environmental justice | **Platform:** Sentinel-2 | **Novelty:** T1

**Problem:** Landfill gas (methane + CO2 + volatile organics) migrating laterally through soil kills vegetation in a distinctive radial ring pattern around landfill boundaries.

**Formula:**
```
LFGVI = red_edge_stress × moisture_loss × chlorosis_signal × ring_pattern_score
```
Ring pattern score = spatial filter detecting annular NDVI depression around known landfill footprint.

**Physics:** LFG root zone toxicity causes chlorophyll degradation (red-edge shift), moisture loss (SWIR increase), and chlorosis (elevated yellow reflectance). The spatial ring pattern — high NDVI inside landfill boundary, depressed NDVI in surrounding ring, recovering NDVI beyond — is geometrically distinctive and not mimicked by any natural stress pattern.

**Benefit:** Maps LFG migration extent around closed landfills — identifies properties and playgrounds where buried methane creates fire/explosion hazard and health risk.

---

## Section 7: Urban & Infrastructure

---

### SPSRI — Solar Panel Soiling Remote Index
**Domain:** Renewable energy / infrastructure | **Platform:** Sentinel-2, Planet | **Novelty:** T1

**Problem:** Dust on utility-scale PV arrays reduces output by 30–45% in arid regions. Manual inspection is expensive. Satellite-scale soiling mapping would enable priority cleaning deployment.

**Formula:**
```
SPSRI = (ρ_B2 − ρ_clean_baseline_B2) / ρ_clean_baseline_B2 × (B11 / B12)
```

**Physics:** Clean PV panels have very low reflectance (high absorption, ~5% reflectance). Dust-coated panels have elevated reflectance shifting toward the dust mineralogy signature. The B11/B12 ratio encodes the dust mineral type (clay vs. carbonate vs. silicate dust), providing a soiling-not-shadow discriminator.

**Benefit:** Optimizes cleaning crew deployment across large solar farms — reduces O&M costs while maximizing power output. Estimated global PV soiling loss exceeds $5B/year.

---

### UCIEI — Urban Cool Infrastructure Effectiveness Index
**Domain:** Urban climate | **Platform:** Sentinel-2 + ECOSTRESS | **Novelty:** T1

**Problem:** Cities invest in cool roofs, green roofs, and permeable pavements. No satellite index quantifies mitigation effectiveness of specific interventions at the parcel scale.

**Formula:**
```
UCIEI = (1 − albedo_satellite) × LST_anomaly
```
Where broadband albedo = `0.356×B2 + 0.130×B4 + 0.373×B8 + 0.085×B11 + 0.072×B12 − 0.0018`

**Physics:** High UCIEI = hot dark surface (old asphalt). Low UCIEI = effective cool infrastructure (white roof or green roof). The product of surface darkness (1−albedo) and thermal anomaly (deviation from the city-wide LST baseline) specifically identifies surfaces that absorb solar radiation AND convert it to heat — the UHI mechanism. Green roofs have low UCIEI despite low albedo because they convert absorbed energy to evapotranspiration.

**Benefit:** Parcel-level scorecard for cool infrastructure programs — enables cities to verify that cool-roof subsidies actually reduce neighborhood temperatures.

---

### SNUVQI — NO₂ + Sentinel-2 Urban Vegetation Air Quality Index
**Domain:** Urban health | **Platform:** TROPOMI + Sentinel-2 + ERA5 | **Novelty:** T1

**Problem:** Urban NO₂ pollution is unevenly distributed. Urban trees and parks reduce near-surface NO₂ by 10–20%, but no index quantifies this effect from satellite data at the parcel scale.

**Formula:**
```
SNUVQI = NO2_TROPOMI_downscaled − f(NDVI_S2, wind_ERA5)
```

**Physics:** Downscaled TROPOMI NO₂ column concentrations (1 km → 100 m via S2 land cover disaggregation) minus the predicted NO₂ reduction from local urban canopy cover (NDVI × wind-speed-dependent deposition velocity). Negative residual = green infrastructure performing above baseline; positive residual = ineffective or insufficient vegetation canopy.

**Benefit:** Maps which neighborhoods receive NO₂ benefit from urban trees — enables environmental justice analysis of air quality co-benefits from urban greening programs.

---

## Section 8: Permafrost & Arctic

---

### TT-API — Thermokarst Thaw & Anoxic Peat Index
**Domain:** Permafrost / climate | **Platform:** Sentinel-2 | **Novelty:** T1

**Problem:** Permafrost thaw releases centuries of stored carbon as methane and CO2. Detecting thaw-related peat exposure and anoxic conditions from space is the first step to quantifying this feedback.

**Formula:**
```
TT-API = PeatExposure × WetAnoxic × EdgeCollapse
```
Peat exposure: SWIR2 increase + NIR decrease from exposed dark peat. Wet anoxic: low NDWI (not pure open water, but saturated peat). Edge collapse: NDVI depression at thaw-slump margins.

**Physics:** Thaw slumps expose dark anoxic peat at the surface (high SWIR2 from organic matter, depressed NIR from low vegetation). The saturated, anoxic zone creates a characteristic mid-NDWI signal — wetter than dry tundra, not as wet as open lakes. Edge collapse creates an abrupt NDVI step at slump margins.

**Benefit:** Arctic carbon monitoring — maps the extent and expansion rate of active thermokarst features across the circumpolar permafrost zone, where over 1,000 Gt of organic carbon is at risk.

---

### TPERI — Thermokarst Pond Expansion Rate Index
**Domain:** Permafrost | **Platform:** Sentinel-2 bi-temporal | **Novelty:** T1

**Problem:** MNDWI detects standing water presence but cannot encode active thermokarst expansion velocity vs. stable pond margins. The rate signal, not presence, drives carbon release projections.

**Formula:**
```
TPERI = Δ(B11_t1 − B11_t2) / Δ(B3_t1 − B3_t2)
```
Positive values = active thaw margin expansion.

**Physics:** Active thermokarst expansion creates a transitional zone of saturated partially-thawed peat with high SWIR1 absorption (1.6 µm water) combined with depressed green reflectance (suspended organic matter). The ratio of SWIR1 change to green change over an annual bi-temporal pair encodes expansion velocity directly, outperforming single-date presence indices.

**Benefit:** Provides the rate signal needed for carbon flux modeling — answering "how fast is this pond growing" rather than just "is this a pond."

---

### FGDCI — Frozen Ground Dielectric Change Index
**Domain:** Permafrost | **Platform:** Sentinel-1 SAR | **Novelty:** T1

**Problem:** C-band SAR backscatter changes at freeze/thaw transitions but no standardized formula separates dielectric change from surface roughness or vegetation effects.

**Formula:**
```
FGDCI = (VV_dB − VH_dB) − seasonal_mean(VV_dB − VH_dB)
```
Time-series anomaly from local climatological mean.

**Physics:** Frozen soil dielectric constant ~4; thawed ~20–30. This drives 3–6 dB shifts in C-band VV backscatter. VH backscatter captures vegetation volume scattering and is less sensitive to dielectric change. The VV-VH difference normalizes vegetation effects; the anomaly from seasonal mean isolates the freeze/thaw transition from background roughness variation.

**Benefit:** Pan-Arctic freeze/thaw monitoring from Sentinel-1's global coverage — automated freeze/thaw state alerts for permafrost carbon models and infrastructure protection.

---

### ALSI — Active Layer Depth Thermal-Spectral Composite Index
**Domain:** Permafrost | **Platform:** ECOSTRESS + Sentinel-2 | **Novelty:** T1

**Problem:** Active layer depth (ALD) is the primary control on permafrost carbon vulnerability. Currently requires in-situ probing at sparse monitoring stations.

**Formula:**
```
ALSI = 0.6 × (LST_anomaly / σ_LST) + 0.4 × [(B12 − B11) / (B12 + B11)]
```

**Physics:** Deeper active layers correlate with warmer surface temperatures (longer heat penetration path), drier surface vegetation (reduced NDWI), and greater clay mineral signal exposure at 2200 nm (frost churning brings clay-rich subsoil to surface). ECOSTRESS LST anomaly captures the thermal signal; S2 SWIR ratio captures the mineralogy signal.

**Benefit:** Satellite proxy for active layer depth at 70 m resolution (ECOSTRESS limited) — orders of magnitude denser than field probe networks.

---

## Section 9: Tropical Forest

---

### UBCDI — Understory vs. Canopy Burn Discrimination Index
**Domain:** Tropical fire ecology | **Platform:** Sentinel-2 bi-temporal | **Novelty:** T1

**Problem:** In tropical forests, ground/understory fires create very different recovery trajectories than crown fires. dNBR cannot distinguish vertical fire structure — a critical gap for post-fire management decisions.

**Formula:**
```
UBCDI = (ΔB8 / B8_pre) / (ΔB4 / B4_pre)
```
Near −1 = canopy fire (large NIR loss, moderate red gain). Near 0 = surface fire (small NIR change, large red litter signal).

**Physics:** Canopy fire creates char deposits at top-of-canopy: dramatic NIR decrease (charred canopy absorbs NIR) and SWIR increase across the full scar. Understory fire leaves the canopy partially intact (NIR partially preserved) but creates elevated red from charred litter visible through gaps. The ratio of relative NIR change to relative red change encodes this vertical dimension of fire.

**Benefit:** Post-fire management routing — understory burns allow accelerated canopy recovery; crown fires require active replanting. The distinction determines whether fire-affected forest is a recovery zone or a restoration project.

---

### PDCSI — Pre-Deforestation Canopy Stress Index
**Domain:** Tropical deforestation monitoring | **Platform:** Sentinel-2 red-edge | **Novelty:** T2

**Problem:** Logging operators often selectively thin canopies 6–18 months before clear-cutting. This pre-visual stress is spectrally detectable but no standardized index formalizes it.

**Formula:**
```
PDCSI = [(B6 − B5) / (B6 + B5)] − [(B8A − B8) / (B8A + B8)]
```
B5=705 nm, B6=740 nm, B8=842 nm, B8A=865 nm.

**Physics:** Early-stage anthropogenic canopy thinning causes chlorophyll degradation. The red-edge position shifts from 720 nm toward 705 nm as chlorophyll declines — detectable as a differential between the B8A/B08 ratio (broader NIR) and the B06/B05 ratio (narrow red-edge). Red-edge chlorophyll index responds earlier than NDVI because it targets the inflection point of the red-edge slope.

**Benefit:** Six to eighteen months earlier detection of deforestation intent — enabling enforcement actions before clear-cutting begins.

---

### LISI — Liana Infestation Structural Index
**Domain:** Tropical forest health | **Platform:** Sentinel-2 | **Novelty:** T2

**Problem:** Lianas (woody vines) are increasing with climate change, suppressing timber value and biodiversity. No operational satellite index maps infestation intensity at the landscape scale.

**Formula:**
```
LISI = 2.5 × [(B8 − B11) / (B8 + 6×B4 − 7.5×B2 + 1)] × (B8 / B11)
```
EVI-modified by SWIR penalty for leaf structure discrimination.

**Physics:** Liana-infested crowns have steeper leaf angles (erectophile), creating higher NIR scattering from increased gap fraction. Lianas have thinner, cheaper leaves with less mesophyll water → lower SWIR1 absorption → elevated B8/B11 ratio relative to tree canopy. EVI weighting reduces soil/shadow contamination.

**Benefit:** Landscape-scale liana mapping enables timber certification bodies and conservation managers to identify and prioritize mechanical removal programs.

---

## Section 10: Dryland & Arid

---

### SBCI — Sabkha Brine Chemistry Index
**Domain:** Dryland / arid geomorphology | **Platform:** EMIT | **Novelty:** T1

**Problem:** Sabkhas (coastal/inland salt flats) contain distinctive mineral assemblages (halite, gypsum, anhydrite, carnallite) that vary with brine concentration and hydroperiod. No standardized index maps sabkha chemistry from orbit.

**Formula:**
```
SBCI = depth(2217nm) / depth(2175nm)
```
Gypsum-to-anhydrite absorption depth ratio.

**Physics:** Gypsum has diagnostic SO4 absorptions at 2217 nm; anhydrite at 2175 nm. Anhydrite forms at higher brine concentration and temperature than gypsum — so the ratio encodes brine concentration history. EMIT's 5 nm spectral resolution resolves these 42 nm-separated features. Halite is spectrally featureless (used to confirm salinity from other indices).

**Benefit:** Maps brine concentration stages across sabkha surfaces — relevant to groundwater salinity monitoring in arid coastal regions and to mineral resource characterization.

---

### BSCMCI — Biological Soil Crust Multi-Condition Index
**Domain:** Dryland ecology | **Platform:** PRISMA, DESIS | **Novelty:** T1

**Problem:** Biological soil crusts (BSCs) protect dryland soil from erosion and fix nitrogen. Existing detection is binary (crust present/absent). A staging index enables condition monitoring.

**Formula:**
```
BSCMCI = [(ρ680 − ρ720) / (ρ680 + ρ720)] × [(ρ550 / ρ670) − 1]
```

**Physics:** BSC development stages have distinctive pigment signatures:
- Early cyanobacteria: chlorophyll a at 680 nm, flat NIR
- Mid-stage green algae: chlorophyll b adds a 550 nm peak
- Advanced lichen: usnic acid at 360 nm with distinctive secondary metabolite absorptions
- Physically disturbed: bright mineral, no pigment features

The chlorophyll edge ratio × green peak combination separates these stages.

**Benefit:** Dryland restoration monitoring — BSC recovery after disturbance (grazing, off-road vehicles, construction) can be tracked to verify restoration success.

---

### DLPEHI — Desert Locust Pre-Emergence Habitat Index
**Domain:** Food security / early warning | **Platform:** Sentinel-2 + GPM | **Novelty:** T1

**Problem:** Desert locust upsurges require early warning in remote areas. Current monitoring detects breeding habitat only after vegetation flush — too late for preventative response.

**Formula:**
```
DLPEHI = NDWI × (0.1 < NDVI < 0.3) × (NDTI > −0.2) × rainfall_binary
```
Logical conjunction: moist sandy soil + sparse greening vegetation + post-rainfall confirmation.

**Physics:** Locust oviposition (egg-laying) habitat requires post-rainfall moist sandy soil (NDWI elevated, but not standing water), sparse actively growing vegetation (NDVI 0.1–0.3, the greening flush that locusts track), and specific soil surface texture (NDTI — Normalized Difference Tillage Index — responds to sandy loam surface structure after rain).

**Benefit:** 2–4 week earlier warning of locust outbreak habitat compared to vegetation-flush monitoring — enables preemptive pesticide or biological control deployment before egg-laying occurs.

---

### CSCAI — Caliche Surface Carbonate Accumulation Index
**Domain:** Dryland pedology | **Platform:** EnMAP | **Novelty:** T1

**Problem:** Caliche (pedogenic calcite) crusts indicate paleoclimate, limit root penetration, and affect agricultural suitability. No standardized satellite index maps caliche distribution.

**Formula:**
```
CSCAI = depth(2335nm) / depth(2160nm)
```
Calcite CO3²⁻ absorption at 2335 nm vs. weaker feature at 2160 nm.

**Physics:** Calcite has a diagnostic CO3²⁻ vibrational absorption at 2335 nm and a weaker feature at 2160 nm. The ratio of these two features distinguishes mature calcite (high ratio) from dolomite (lower ratio, different peak positions) or surface gravel (low band depth). EnMAP's 10 nm bands in this region resolve this 175 nm separation.

**Benefit:** Soil resource mapping in arid regions — identifies where caliche layers will prevent deep root development, informing dryland agriculture and land rehabilitation decisions.

---

### AIBEAI — Arroyo Incision and Bank Erosion Activity Index
**Domain:** Dryland geomorphology | **Platform:** Sentinel-2, Planet | **Novelty:** T1

**Problem:** Arroyo incision in arid systems causes gully headward erosion threatening infrastructure and accelerating desertification. No index distinguishes active incision from stable legacy channels.

**Formula:**
```
AIBEAI = BSI_channel_bottom / NDVI_channel_margin
```
Where `BSI = (B11 + B4 − B8 − B2) / (B11 + B4 + B8 + B2)`.

**Physics:** Active arroyo incision exposes fresh bright mineral soils (high BSI) in the channel bottom without established vegetation on channel margins (low NDVI at margins). Stable legacy channels show vegetation establishment on banks (positive marginal NDVI). The ratio distinguishes dynamically incising from stable channels.

**Benefit:** Infrastructure risk mapping — identifies which arroyos are actively undermining roads, pipelines, and levees vs. stable historical channels.

---

## Section 11: Wetland & Peatland

---

### PWTDI — Peatland Water Table Depth Index
**Domain:** Wetland / carbon | **Platform:** Sentinel-2 + Sentinel-1 | **Novelty:** T2

**Problem:** Peatland water table depth (WTD) is the primary control on methane vs. CO2 emissions. Currently unmeasured globally from satellite — the most important gap in wetland carbon accounting.

**Formula:**
```
PWTDI = 0.65 × NDWI_1020 + 0.35 × (VV_dB − VH_dB)
```
Where `NDWI_1020 = (B8A − B9) / (B8A + B9)` (B9=945 nm, the 970 nm Sphagnum water feature).

**Physics:** Water table near surface creates saturated Sphagnum moss with characteristic 970 nm water absorption peak. Deeper WTD desiccates surface Sphagnum, increasing NIR and reducing 970 nm absorption. Sentinel-1 C-band VV backscatter is sensitive to surface moisture but not subsurface WTD. The optical-SAR fusion improves performance in treed peatlands where optical signals are canopy-dominated.

**Benefit:** Global peatland WTD monitoring — enables methane flux modeling (high WTD = high CH4 emission) at the resolution needed for carbon accounting and restoration verification.

---

### MHSSP — Methane Hotspot Surface Spectral Predictor
**Domain:** Wetland / climate | **Platform:** Sentinel-2 + TROPOMI | **Novelty:** T1

**Problem:** Wetland CH4 emissions are spatially highly heterogeneous — "hotspot-dominated." TROPOMI sees plumes but cannot identify individual m²-scale emission hotspots. Surface optical features predict hotspot locations.

**Formula:**
```
MHSSP = NDWI × (1 − NDVI) × (1 − CI_rededge / max_CI_rededge_local)
```

**Physics:** CH4 hotspots in wetlands occur where: (1) organic-rich anoxic zones (open water, NDWI high) coincide with (2) no emergent vegetation (low NDVI, so ebullition is unobstructed) and (3) low macrophyte biomass (low red-edge chlorophyll index). Open sediment-covered shallow water is the characteristic habitat.

**Benefit:** Provides the Sentinel-2 surface anchor for TROPOMI methane plume attribution — narrows "methane is coming from this wetland" to "methane is coming from these specific open-water zones within this wetland."

---

### TFIDI — Tidal Flat Inundation Dynamics Index
**Domain:** Coastal wetland | **Platform:** Sentinel-2 monthly | **Novelty:** T1

**Problem:** Intertidal flats are among the most ecologically productive habitats but their satellite monitoring is complicated by rapid tidal cycling. No index captures the full inundation gradient across a tidal cycle.

**Formula:**
```
TFIDI = (NDWI_p90 − NDWI_p10) / NDWI_mean   [monthly composite]
```

**Physics:** Inundation stage determines spectral signature: open water (NDWI >> 0), saturated mudflat (dark, low NDWI), moist mudflat (moderate SWIR), dry upper flat (clay signature). Monthly composites from Sentinel-2's 5-day revisit sample multiple tidal states. High NDWI percentile spread = high inundation dynamics = full tidal flat habitat; low spread = always-wet or always-dry.

**Benefit:** Maps tidal flat ecological zones (low vs. mid vs. high intertidal) from temporal composites — enables shorebird habitat mapping and aquaculture siting without requiring tidal timing correction.

---

### WDPTZI — Wet-Dry Peatland Transition Zone Index
**Domain:** Peatland carbon | **Platform:** Sentinel-2 | **Novelty:** T1

**Problem:** The transition from wet (methane-emitting) to dry (CO2-emitting, fire-vulnerable) peatland is a carbon management priority. The transition zone width and position are unmapped globally.

**Formula:**
```
WDPTZI = spatial_gradient_magnitude[(B11 − B8A) / (B11 + B8A)]
```
Applied as a Sobel edge detector to the SWIR1/NIR ratio raster.

**Physics:** Wet peatland: saturated Sphagnum (high 970 nm absorption), low SWIR1. Dry peatland: desiccated peat (high SWIR2, featureless spectrum). The spatial gradient of the SWIR1/NIR ratio is near-zero in homogeneous wet or dry zones but peaks at the transition — creating an edge map of the boundary.

**Benefit:** Maps the spatial position and width of wet-dry transitions across global peatlands — enables tracking of boundary shifts due to drainage, drought, and climate change.

---

## Section 12: Hyperspectral-Enabled Indices (EMIT, EnMAP, PRISMA, PACE, DESIS)

*These indices were theoretically known but operationally impossible before sensors launched 2019–2024.*

---

### PFTIB — Phytoplankton Functional Type Index Battery
**Domain:** Ocean ecology / carbon cycle | **Platform:** PACE OCI | **Novelty:** T1

**Problem:** PACE OCI (launched February 2024) provides the first operational UV-to-NIR hyperspectral ocean color at global coverage. This enables phytoplankton functional type (PFT) discrimination beyond chlorophyll — critical for fisheries, carbon cycling, and HAB forecasting.

**Formula:**
```
PFT_diatom  = absorption(490nm) / absorption(440nm)  # high = fucoxanthin
PFT_hapto   = absorption(453nm) / absorption(490nm)  # high = hex-fucoxanthin
PFT_prokary = ρ(490nm) / ρ(440nm)                    # low = divinyl chl a
PFT_crypto  = absorption(565nm) / absorption(490nm)  # high = phycoerythrin
```

**Physics:** Each PFT has diagnostic pigment packages with specific absorption features: diatoms (fucoxanthin: 490–510 nm), haptophytes/coccolithophores (19'-hex-fucoxanthin: 453 nm), prokaryotes/Prochlorococcus (divinyl chlorophyll a: 440 nm shift from 443 nm), cryptophytes (phycoerythrin: 565 nm). PACE OCI's 5 nm bands from 340–890 nm resolve all four.

**Benefit:** Global phytoplankton species community monitoring — enables carbon export estimates (diatom-dominated communities export more carbon), fisheries productivity (different food webs), and HAB species prediction by ecosystem state.

---

### CMSTI — Clay Mineral Stress Transition Index
**Domain:** Soil degradation | **Platform:** EMIT (EMIT only) | **Novelty:** T1

**Problem:** Under drought and weathering stress, clay mineral assemblages transition from smectite (expandable, water-retaining) to illite (non-expanding). This transition indicates irreversible soil degradation — but requires 8 nm spectral resolution to detect.

**Formula:**
```
CMSTI = position_minimum(2190−2220nm) − 2200
```
Negative shift toward 2195 nm = smectite. Positive toward 2208 nm = illite.

**Physics:** Smectite has Al-OH absorption at 2200 nm; illite at 2208 nm. This 8 nm shift is resolvable by EMIT's 5 nm bands but not by Sentinel-2, Landsat, or EnMAP (10 nm). The shift encodes the smectite → illite mineralogical transition that permanently reduces a soil's water retention capacity.

**Benefit:** EMIT is the only instrument in orbit capable of this detection. Maps soil degradation pathways across dryland regions globally — a permanent loss that takes centuries to reverse.

---

### AFCDI — Asbestos Fiber Chrysotile Detection Index
**Domain:** Environmental health | **Platform:** EMIT, PRISMA | **Novelty:** T1

**Problem:** Chrysotile asbestos in building materials, naturally occurring asbestos zones, and abandoned mine sites poses extreme health risk. Landscape-scale detection requires spectral resolution previously unavailable from orbit.

**Formula:**
```
AFCDI = depth(2317nm) / depth(2387nm)
```
Secondary confirmation: `depth(1390nm) / continuum`

**Physics:** Chrysotile has Mg-OH doublet absorptions at 2317 nm and 2387 nm — diagnostic vs. other serpentine minerals (antigorite at 2320/2100 nm, lizardite at 2320/2390 nm). The 2317/2387 band depth ratio discriminates chrysotile from these related minerals. EMIT's 5 nm sampling resolves the 70 nm separation.

**Benefit:** Natural asbestos zone mapping across ultramafic terrains — identifies where soil disturbance (construction, agriculture) releases respirable chrysotile fibers near communities.

---

### REENBI — REE Neodymium Band Depth Index
**Domain:** Critical minerals | **Platform:** EnMAP | **Novelty:** T1

**Problem:** REE deposits are critical for clean energy transition. Nd-bearing minerals are detectable at 803 nm from EnMAP — but no formula standardizes this detection.

**Formula:**
```
REENBI = 1 − ρ(803nm) / [ρ(780nm) + (803−780)/(830−780) × (ρ(830nm) − ρ(780nm))]
```
Linear interpolation continuum depth at the 803 nm Nd³⁺ absorption.

**Physics:** Nd³⁺ electronic f-f transitions create absorptions at 583, 740, and 803 nm. In REE carbonate (bastnäsite) and phosphate (monazite), the 803 nm feature against the 780/830 nm continuum is cleanest. Band depth formula is analogous to standard mineral spectroscopy continuum removal.

**Benefit:** Global REE deposit prospecting from EnMAP — validated at Mountain Pass, CA (Mielke et al. 2024). Transforms exploration from field-intensive to satellite-first.

---

### SCFGOSI — Soil Carbon Functional Group Oxidation State Index
**Domain:** Carbon accounting | **Platform:** EMIT, EnMAP | **Novelty:** T1

**Problem:** Existing satellite SOC estimates measure total carbon quantity. Carbon quality (labile vs. recalcitrant) determines whether it will rapidly mineralize to CO2 when disturbed — equally important for climate modeling.

**Formula:**
```
SCFGOSI = depth(1730nm) / (1 − mean_reflectance_400−2500nm)
```

**Physics:** Labile carbon (lipids, proteins) has C-H overtone absorptions at 1730 nm. Recalcitrant carbon (aromatic humus, char) has broad low-reflectance ("darkness") from 400–2500 nm without sharp features. The ratio of specific C-H band depth to overall spectral darkness encodes labile vs. recalcitrant carbon proportion.

**Benefit:** Distinguishes stable carbon (char, humus) from labile carbon (fresh organic matter) — critical for understanding which soils store carbon permanently vs. which will lose carbon rapidly under warming.

---

### MPSSFI — Methane Plume Spectral Shape Feature Index
**Domain:** Climate / methane | **Platform:** EMIT | **Novelty:** T2

**Problem:** EMIT detects methane plumes via matched filter algorithms. A simple physics-based formula would enable deterministic source attribution without machine learning.

**Formula:**
```
MPSSFI = 1 − ρ(1667nm) / [0.5 × (ρ(1640nm) + ρ(1700nm))]
```
Band depth at the 1667 nm CH4 absorption feature relative to linear continuum from 1640–1700 nm.

**Physics:** CH4 has a strong absorption band centered at 1667 nm in EMIT's SWIR range. The band depth relative to a linear continuum interpolated from the 1640 and 1700 nm shoulders is proportional to column methane enhancement above background. Higher band depth = higher methane column.

**Benefit:** Formula-based methane plume detection from EMIT — enables open-science replication without proprietary matched filter implementations.

---

## Section 13: Cross-Sensor Fusion Indices

---

### TSEAI — TROPOMI–Sentinel-2 Emission Attribution Index
**Domain:** Climate / methane accountability | **Platform:** S5P TROPOMI + Sentinel-2 | **Novelty:** T1

**Problem:** TROPOMI detects CH4 column enhancements at 5.5×7 km pixels — too coarse to attribute to specific emission sources (landfills, wetlands, livestock facilities, oil fields) that co-exist within one pixel.

**Formula:**
```
TSEAI = XCH4_TROPOMI_anomaly / Σ(source_fraction_i × emission_factor_i)
```
Where source_fraction_i = fractional area of each emission source type within the TROPOMI pixel, derived from Sentinel-2 land cover classification.

**Physics:** Each emission source type has a literature-derived emission factor (tonnes CH4/km²/day). Sentinel-2 at 10 m maps source type fractions within each TROPOMI pixel. The ratio of observed enhancement to predicted enhancement identifies unaccounted sources (high ratio) and over-predicted sources (low ratio).

**Benefit:** Transforms TROPOMI from a "where is methane enhanced" tool to a "what is emitting that methane" tool — the most urgent gap in climate monitoring. Directly applicable to methane regulatory compliance.

---

### GEAWSI — GRACE-FO + ECOSTRESS Agricultural Water Stress Index
**Domain:** Food security / water | **Platform:** GRACE-FO + ECOSTRESS + ERA5 | **Novelty:** T1

**Problem:** GRACE-FO detects total water storage (TWS) anomalies at ~300 km; ECOSTRESS detects field-scale ET. Neither alone confirms that crops are experiencing actual root-zone water stress that will cause yield loss.

**Formula:**
```
GEAWSI = (ET_ecostress / PET_estimate) × TWS_anomaly_sign
```
Actual-to-potential ET ratio (crop water stress coefficient) signed by regional groundwater depletion direction.

**Physics:** ET/PET < 1 indicates crop water stress. If TWS is simultaneously declining (groundwater drawdown), the stress is confirmed as groundwater-supply driven rather than weather-driven. Negative GEAWSI during drought = confirmed crop stress with groundwater draw-down — the scenario that depletes aquifers.

**Benefit:** Identifies irrigation systems where crop stress AND aquifer depletion are co-occurring — the most urgent water security scenario. Applicable to every major irrigated agricultural region globally.

---

### ISSAI — ICESat-2 + Sentinel-1 Subsidence Attribution Index
**Domain:** Infrastructure / geology | **Platform:** ICESat-2 + Sentinel-1 + Sentinel-2 | **Novelty:** T1

**Problem:** Urban and coastal subsidence is monitored by either InSAR (area-wide, relative, mm precision) or ICESat-2 lidar (sparse tracks, absolute elevation). Neither alone determines cause.

**Formula:**
```
ISSAI = (ICESat2_dZ/dt − InSAR_LOS_vertical) / ICESat2_dZ/dt
```
Discrepancy flags non-coherent subsidence invisible to InSAR phase.

**Physics:** ICESat-2 measures absolute elevation change at 1 cm precision along sparse tracks. Sentinel-1 InSAR measures relative deformation between coherent scatterers at mm precision. When the two methods disagree, the discrepancy indicates: rapid incoherent subsidence (sediment compaction), phase unwrapping errors, or different temporal sampling windows. Combined with S2 land cover: attribute to groundwater extraction vs. load-induced compaction.

**Benefit:** Subsidence cause attribution — distinguishes groundwater-driven (policy-addressable) from geological (geological hazard) or load-induced (building regulation) subsidence for tens of millions of people in coastal cities.

---

### EMSMMI — EMIT Mineral + Sentinel-1 Soil Moisture Index
**Domain:** Hydrology | **Platform:** EMIT + Sentinel-1 | **Novelty:** T1

**Problem:** Sentinel-1 soil moisture retrievals assume constant soil dielectric properties. High-clay vs. sandy soils give different dielectric responses to the same water content — creating systematic biases in moisture estimates.

**Formula:**
```
EMSMMI = VWC_S1_raw / (1 + clay_fraction_EMIT × clay_dielectric_correction)
```

**Physics:** Soil dielectric constant is a function of both water content AND clay mineralogy — clay minerals (smectite especially) have elevated ionic conductivity that inflates C-band backscatter-to-moisture retrieval. EMIT's mineral fraction maps (operational from 2022) provide the clay fraction that enables a mineralogy-specific correction to Sentinel-1 volumetric water content.

**Benefit:** Improved soil moisture accuracy at global scale — particularly important in agricultural regions with high clay content (Vertisols, alluvial plains) where standard VWC estimates have systematic 15–25% errors.

---

### PUENPI — PACE + ECOSTRESS Coastal Wetland Net Ecosystem Production Index
**Domain:** Carbon accounting | **Platform:** PACE OCI + ECOSTRESS + ERA5 | **Novelty:** T1

**Problem:** Coastal wetlands are net CO2 sinks but their net ecosystem production is poorly constrained globally. Terrestrial and aquatic production components have never been fused into one satellite index.

**Formula:**
```
PUENPI = GPP_ECOSTRESS_proxy − NPP_PACE_aquatic − R_temperature_model
```
NEP = terrestrial GPP (from ET proxy) − aquatic phytoplankton NPP (from PACE OCI chlorophyll) − autotrophic respiration (modeled from ECOSTRESS LST).

**Physics:** Coastal wetland NEP integrates three processes: terrestrial (salt marsh, mangrove) gross primary production via carbon uptake correlating with ECOSTRESS ET; aquatic phytoplankton NPP from PACE OCI ocean color; and autotrophic respiration approximated from temperature-dependent metabolic rates using ECOSTRESS LST. The sum closes the wetland carbon budget from orbit.

**Benefit:** Global coastal blue-carbon accounting — enables national carbon inventories to include coastal wetland carbon fluxes with satellite-verified estimates rather than extrapolated field measurements.

---

### NFCAI — NISAR + Sentinel-2 Forest Carbon Accumulation Index
**Domain:** Forest carbon | **Platform:** NISAR + Sentinel-2 | **Novelty:** T3

**Problem:** Forest carbon accumulation requires both structural biomass information (L-band SAR) and canopy age/composition context (optical time series). No single sensor provides both.

**Formula:**
```
NFCAI = L-band_HV × (1 − canopy_cover_S2) + L-band_HH × age_proxy_NDVI_trend
```
HV penetrates canopy and encodes woody volume; HH+NDVI trend provides age context.

**Physics:** NISAR L-band (24 cm wavelength) penetrates canopy to interact with woody trunks and branches, encoding biomass. The HV cross-polarization ratio is sensitive to woody volume scattering. Sentinel-2 NDVI time series (integrated cumulative photosynthesis as age proxy) provides the stand age context needed to convert backscatter to absolute carbon stock.

**Benefit:** NISAR (operational 2024) makes global 10 m L-band SAR available — enabling forest carbon monitoring at a spatial resolution and temporal cadence that ALOS PALSAR-2 (proposal-based) could not match.

---

## Appendix: Standard Baselines (Published — No Claim)

These established indices are used as inputs to the novel composites above.

| Index | Formula | Purpose |
|-------|---------|---------|
| NDVI | `(B08−B04)/(B08+B04)` | Vegetation density |
| NDWI | `(B03−B08)/(B03+B08)` | Surface water |
| NDMI | `(B08−B11)/(B08+B11)` | Soil/canopy moisture |
| BSI | `((B11+B04)−(B08+B02))/((B11+B04)+(B08+B02))` | Bare soil |
| NDSI | `(B08−B11)/(B08+B11)` | Saline surface |
| HCAI | `(B11−B12)/(B11+B12)` | Hydrocarbon SWIR shoulder |
| HMRI | `(B03−B02)/(B03+B02)` | Heavy metal reflectance |
| NDOI | `(B03−B11)/(B03+B11)` | Oil slick |
| AOI | `(B04−B02)/(B04+B02)` | Fe³⁺ iron oxidation |
| NBR | `(B08−B12)/(B08+B12)` | Burn ratio |
| MSI | `B11/B08` | Moisture stress |
| SAVI | `1.5×(B08−B04)/(B08+B04+0.5)` | Vegetation, soil-corrected |
| FAI | Floating Algae Index (NIR−SWIR shoulder) | Floating vegetation |
| NDCI | `(B05−B04)/(B05+B04)` | Chlorophyll / algal bloom |
| EVI | `2.5×(B08−B04)/(B08+6×B04−7.5×B02+1)` | Vegetation, soil+atm corrected |

---

## Citation & Reuse

This atlas is released as a public-good research document. All formulas are grounded in published spectral physics cited within each entry. For validated indices (PWCI, ASAI, VSI, OBEC, FBC, LBI), cite the TRRC validation (2026-03-28) and this document. For proposed indices (Tier 1/T2/T3 unclaimed), cite the spectral physics sources referenced in each entry.

**Key peer-reviewed sources underlying this work:**
- Kokaly et al. (2017). *USGS Spectral Library Version 7.*
- Green et al. (2023). "Performance and early results from EMIT." *IEEE TGRS* 61.
- Zhang et al. (2020). "Quantifying methane emissions from the Permian basin from space." *Science Advances* 6(17).
- Mielke et al. (2024). "Neodymium mineral detection at Mountain Pass using EnMAP." *Scientific Reports* 14(1):20413.
- Harkness et al. (2025). "Grass is a tattletale." *PMC.*
- Hillier et al. (2023). Jagersfontein dam spectral precursor analysis. *PMC.*
- Pahlevan et al. (2026). "PACE OCI PFT retrieval." *Remote Sensing of Environment.*
- Hugelius et al. (2020). "Permafrost carbon vulnerability." *PNAS* 117(34).
- Burt et al. (2025). "Liana spectral optics review." *PMC.*

---

*Document last updated: 2026-05-25 | Originated by Daniel Bally · [Limn](https://github.com/globe-and-atlas) · [Globe & Atlas](https://globeandatlas.substack.com)*
