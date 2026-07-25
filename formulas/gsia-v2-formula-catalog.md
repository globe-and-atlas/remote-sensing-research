# Global Spectral Index Atlas v2 Formula Catalog

- **Release audit:** 2026-07-21
- **Records:** 91 across 12 domains and 24 capability families
- **Formula schema:** 2.0
**Audited Atlas source:** commit `e50c2eda5cf405c7693e5210e04894c691e5f2eb`, since made private; the public Atlas viewer is now maintained at [globe-and-atlas/limn-atlas](https://github.com/globe-and-atlas/limn-atlas)

This is the human-readable companion to the machine-readable [`gsia_preprint_v2_status_supplement_2026-07-21.csv`](../preprint/gsia_preprint_v2_status_supplement_2026-07-21.csv). The CSV is authoritative. This file is generated from it so the formulas, maturity states, method roles, and limits remain synchronized.

GSIA is a registry of proposed environmental remote-sensing specifications, not a collection of 91 validated detectors. A formula can be useful as a screening feature or research hypothesis without establishing target specificity, causal attribution, concentration, risk, or regulatory status.

## How to read the records

- **Proposed formula or workflow** states the full research specification, including operators or calibration that may not yet be implemented.
- **Implemented or retained legacy formula** states what currently runs, or what is preserved for traceability after retirement.
- **M1** means formula specified; **M2** means executable but not live; **M3** means demonstrated in the Atlas interface.
- **M3 is not validation.** Every record in this release remains below V1 independent evaluation.
- **Contribution classes are provisional.** C1, C2, and C3 describe the intended contribution; they do not establish scientific priority.
- **Method roles organize families.** Primary, variant, component, reference, research-model, and retired are catalog roles, not performance rankings.

## Release inventory

| Dimension | Distribution |
|---|---|
| Maturity | 37 M3; 16 M2; 38 M1 |
| Method roles | 15 primary; 10 variant; 12 component; 1 reference; 51 research-model; 2 retired |
| Contribution classes | 68 C1; 22 C2; 1 C3, all provisional |
| Independent validation | 0 V1; 0 V2 |

## Formula index

| # | Record | Capability family | Role | Maturity | Formula status |
|---:|---|---|---|---|---|
| 1 | [BH-DFSI](#bh-dfsi) - Burned Hillside Surface Context Score | Fire Effects & Recovery | primary | M3 | Live screening proxy |
| 2 | [SF-EII](#sf-eii) - Canopy Moisture Deficit Calibration Specification | Fuel Moisture Context | retired | M1 | Rebuild required |
| 3 | [LFMPI](#lfmpi) - Live Fuel Moisture Deficit Proxy | Fuel Moisture Context | primary | M3 | Live screening proxy |
| 4 | [PSHRI](#pshri) - Post-Fire Soil Hydrophobicity Risk Index | Fire Effects & Recovery | research-model | M1 | Formula specified; not implemented in Atlas |
| 5 | [BSMTI](#bsmti) - Burn Severity Mineralogy Transition Index | Fire Effects & Recovery | research-model | M1 | Formula specified; not implemented in Atlas |
| 6 | [SACI](#saci) - UV Absorbing Aerosol Context | Smoke & Extreme Fire Behavior | reference | M3 | Live screening proxy |
| 7 | [PCSII](#pcsii) - Pyroconvection Detection Index | Smoke & Extreme Fire Behavior | research-model | M1 | Formula specified; not implemented in Atlas |
| 8 | [PETI](#peti) - Phytoplankton Bloom Context Proxy | Aquatic Blooms & Pigments | primary | M3 | Live screening proxy |
| 9 | [CSRC](#csrc) - Surface Scum Context Composite | Aquatic Blooms & Pigments | variant | M3 | Live screening proxy |
| 10 | [SWRI](#swri) - Sewage-Water Release Index | Water Condition & Plumes | research-model | M2 | Executable but non-live |
| 11 | [DWCI](#dwci) - Drinking Water Catchment Injury Index | Water Condition & Plumes | research-model | M2 | Executable but non-live |
| 12 | [RRFI](#rrfi) - Riparian Dry-Bare Context Composite | Riparian & Floodplain Condition | variant | M3 | Live screening proxy |
| 13 | [EPDI](#epdi) - Bare-Surface and Water-Turbidity Context | Water Condition & Plumes | primary | M3 | Live screening proxy |
| 14 | [RDOCI](#rdoci) - CDOM Spectral-Slope Research Specification | Water Condition & Plumes | research-model | M1 | Retrieval workflow required |
| 15 | [CTPSTI](#ctpsti) - Phytoplankton Pigment Contrast Feature | Aquatic Blooms & Pigments | component | M1 | Formula specified; not implemented in Atlas |
| 16 | [DTPSI](#dtpsi) - Dam Thermal Plume Stratification Index | Water Condition & Plumes | research-model | M1 | Formula specified; not implemented in Atlas |
| 17 | [GMCPI](#gmcpi) - Glacial Meltwater Chemistry Proxy Index | Water Condition & Plumes | research-model | M2 | Executable but non-live |
| 18 | [FCLI](#fcli) - Floodplain SWIR-Vegetation Context | Riparian & Floodplain Condition | primary | M3 | Live screening proxy |
| 19 | [HABSDI](#habsdi) - HAB Species-Level Discrimination Index | Aquatic Blooms & Pigments | research-model | M1 | Formula specified; not implemented in Atlas |
| 20 | [SMPDI](#smpdi) - Floating-Material Spectral Contrast | Floating & Surface Material | primary | M3 | Live screening proxy |
| 21 | [CBSDI](#cbsdi) - Coral Brightness Context Proxy | Coastal Habitat Condition | primary | M3 | Live screening proxy |
| 22 | [KCDSI](#kcdsi) - Floating or Shallow-Water Vegetation Context | Floating & Surface Material | variant | M3 | Live screening proxy |
| 23 | [OWSI](#owsi) - Oil Spill Weathering Stage Index | Floating & Surface Material | variant | M3 | Live screening proxy |
| 24 | [MDSPI](#mdspi) - Mangrove Dieback Spatial Pattern Index | Coastal Habitat Condition | research-model | M2 | Executable but non-live |
| 25 | [SGDCI](#sgdci) - Submarine Groundwater Discharge Chemistry Index | Water Condition & Plumes | research-model | M1 | Formula specified; not implemented in Atlas |
| 26 | [SPEI](#spei) - Seagrass Photosynthetic Efficiency Index | Coastal Habitat Condition | research-model | M2 | Executable but non-live |
| 27 | [CD-UAI](#cd-uai) - Coastal Water Turbidity Context | Water Condition & Plumes | variant | M3 | Live screening proxy |
| 28 | [MP-PDI](#mp-pdi) - Floating-Debris Candidate Feature | Floating & Surface Material | variant | M3 | Live screening proxy |
| 29 | [NPDefI](#npdefi) - Nitrogen vs. Phosphorus Deficiency Discrimination Index | Crop & Soil Stress | primary | M3 | Live screening proxy |
| 30 | [SCSPI](#scspi) - Soil Compaction Spectral Proxy Index | Crop & Soil Stress | research-model | M2 | Executable but non-live |
| 31 | [APRI](#apri) - Aflatoxin Pre-Harvest Risk Index | Crop & Soil Stress | research-model | M1 | Formula specified; not implemented in Atlas |
| 32 | [PDSDI](#pdsdi) - Crop Red-Edge and Dryness Context | Crop & Soil Stress | variant | M3 | Live screening proxy |
| 33 | [CCTTI](#cctti) - Cover Crop Termination Timing Index | Agricultural Management | primary | M3 | Live screening proxy |
| 34 | [IWUEI](#iwuei) - Irrigation Water Use Efficiency Index | Agricultural Management | research-model | M1 | Formula specified; not implemented in Atlas |
| 35 | [WDA-CSI](#wda-csi) - Wetland-Agriculture Edge Context | Riparian & Floodplain Condition | variant | M3 | Live screening proxy |
| 36 | [TRSI](#trsi) - Tailings River Shock Index | Water Condition & Plumes | research-model | M2 | Executable but non-live |
| 37 | [TDR-ASI](#tdr-asi) - Mining Iron-SWIR Context Proxy | Mining Surfaces & Risk | primary | M3 | Live screening proxy |
| 38 | [AMDPHI](#amdphi) - AMD Iron-Mineral Calibration Specification | Mining Surfaces & Risk | retired | M1 | Rebuild required |
| 39 | [TDSII](#tdsii) - Tailings Change-Risk Calibration Model | Mining Surfaces & Risk | research-model | M1 | Calibrated model required |
| 40 | [REESAI](#reesai) - Rare Earth Element Surface Anomaly Index | Mining Surfaces & Risk | research-model | M1 | Formula specified; not implemented in Atlas |
| 41 | [CCRBI](#ccrbi) - Coal Combustion Residue Bioaccumulation Index | Mining Surfaces & Risk | research-model | M2 | Executable but non-live |
| 42 | [HLPII](#hlpii) - Heap Leach Pad Integrity Index | Mining Surfaces & Risk | research-model | M1 | Formula specified; not implemented in Atlas |
| 43 | [IERPI](#ierpi) - Industrial Effluent River Plume Index | Water Condition & Plumes | research-model | M2 | Executable but non-live |
| 44 | [EC-ACI](#ec-aci) - Evapotranspirative Canopy & Asphalt Contrast Index | Urban Surface Condition | primary | M3 | Live screening proxy |
| 45 | [HSAI](#hsai) - Low-Vegetation Bare-Surface Context | Urban Surface Condition | component | M3 | Live screening proxy |
| 46 | [SPSRI](#spsri) - Solar Panel Soiling Remote Index | Urban Surface Condition | research-model | M2 | Executable but non-live |
| 47 | [UCIEI](#uciei) - Urban Cool Infrastructure Effectiveness Index | Urban Surface Condition | research-model | M1 | Formula specified; not implemented in Atlas |
| 48 | [PCADI](#pcadi) - Dark Paved-Surface Context | Urban Surface Condition | component | M3 | Live screening proxy |
| 49 | [CSDEI](#csdei) - Construction Site Silica Dust Emission Index | Urban Surface Condition | research-model | M1 | Formula specified; not implemented in Atlas |
| 50 | [LFGVI](#lfgvi) - Landfill Vegetation-Stress Context | Landfill Surface Context | component | M3 | Live screening proxy |
| 51 | [LRD-VSI](#lrd-vsi) - Vegetation-Moisture Anomaly Context | Landfill Surface Context | component | M3 | Live screening proxy |
| 52 | [TT-API](#tt-api) - Wet Exposed-Peat Context | Permafrost & Peat Change | component | M3 | Live screening proxy |
| 53 | [TPERI](#tperi) - Thermokarst Pond-Edge Context | Permafrost & Peat Change | component | M3 | Live screening proxy |
| 54 | [PCEI](#pcei) - Peat Carbon Exposure Index | Permafrost & Peat Change | primary | M3 | Live screening proxy |
| 55 | [SABSI](#sabsi) - Bright-Snow Red-Green Context | Snow Pigment Context | primary | M3 | Live screening proxy |
| 56 | [FGDCI](#fgdci) - Frozen Ground Dielectric Change Index | Permafrost & Peat Change | research-model | M2 | Executable but non-live |
| 57 | [MEPSI](#mepsi) - CH₄ Ebullition Pond Spectral Proxy | Wetland Gas Surface Context | component | M3 | Live screening proxy |
| 58 | [ALSI](#alsi) - Active Layer Depth Thermal-Spectral Composite | Permafrost & Peat Change | research-model | M1 | Formula specified; not implemented in Atlas |
| 59 | [PDCSI](#pdcsi) - Pre-Deforestation Canopy Stress Index | Forest Canopy Condition | primary | M3 | Live screening proxy |
| 60 | [LISI](#lisi) - Liana Infestation Structural Index | Forest Canopy Condition | variant | M3 | Live screening proxy |
| 61 | [UBCDI](#ubcdi) - Understory vs. Canopy Burn Discrimination Index | Fire Effects & Recovery | research-model | M2 | Executable but non-live |
| 62 | [FEDGI](#fedgi) - Forest Edge Degradation Gradient Index | Forest Disturbance & Carbon | research-model | M2 | Executable but non-live |
| 63 | [SLSDI](#slsdi) - Selective Logging Scar Detection Index | Forest Disturbance & Carbon | research-model | M2 | Executable but non-live |
| 64 | [ETCSI](#etcsi) - Emergent Tree Crown Stress Index | Forest Canopy Condition | research-model | M1 | Formula specified; not implemented in Atlas |
| 65 | [BSCMCI](#bscmci) - Biological Soil Crust Multi-Condition Index | Dryland Surface Processes | research-model | M1 | Formula specified; not implemented in Atlas |
| 66 | [SBCI](#sbci) - Sabkha Brine Chemistry Index | Dryland Surface Processes | research-model | M1 | Formula specified; not implemented in Atlas |
| 67 | [CSCAI](#cscai) - Caliche Surface Carbonate Accumulation Index | Dryland Surface Processes | research-model | M1 | Formula specified; not implemented in Atlas |
| 68 | [DEFPI](#defpi) - Dust Emission Flux Proxy Index | Dryland Surface Processes | research-model | M1 | Formula specified; not implemented in Atlas |
| 69 | [DLPEHI](#dlpehi) - Desert Locust Pre-Emergence Habitat Index | Dryland Surface Processes | component | M3 | Live screening proxy |
| 70 | [AIBEAI](#aibeai) - Arroyo Incision and Bank Erosion Activity Index | Dryland Surface Processes | research-model | M2 | Executable but non-live |
| 71 | [PWTDI](#pwtdi) - Peatland Water-Table Calibration Model | Wetland Hydrology | research-model | M2 | Field calibration required |
| 72 | [MHSSP](#mhssp) - Open Anoxic-Surface Context Proxy | Wetland Gas Surface Context | component | M3 | Live screening proxy |
| 73 | [TFIDI](#tfidi) - Single-Date Tidal-Zone Wetness Context | Wetland Hydrology | component | M3 | Live screening proxy |
| 74 | [WDPTZI](#wdptzi) - Peat Moisture Transition Proxy | Wetland Hydrology | component | M3 | Live screening proxy |
| 75 | [IPVSI](#ipvsi) - Invasive Phragmites vs. Native Vegetation Discrimination | Wetland Vegetation Structure | primary | M3 | Live screening proxy |
| 76 | [WVTDI](#wvtdi) - Wetland Vegetation Type Discrimination Index | Wetland Vegetation Structure | variant | M3 | Live screening proxy |
| 77 | [CMSTI](#cmsti) - Clay-Mineral Absorption-Position Model | Hyperspectral Materials | research-model | M1 | Spectral fitting required |
| 78 | [MPSSFI](#mpssfi) - Methane Matched-Filter Research Specification | Atmospheric Methane & Carbon | research-model | M1 | Atmospheric retrieval required |
| 79 | [AFCDI](#afcdi) - Asbestos Fiber Chrysotile Detection Index | Hyperspectral Materials | research-model | M1 | Formula specified; not implemented in Atlas |
| 80 | [SCFGOSI](#scfgosi) - Soil Carbon Functional Group Oxidation State Index | Hyperspectral Materials | research-model | M1 | Formula specified; not implemented in Atlas |
| 81 | [REENBI](#reenbi) - REE Neodymium Band-Depth Feature | Hyperspectral Materials | research-model | M1 | Continuum-removal specification |
| 82 | [EPCASE](#epcase) - EnMAP Porphyry Cu Alteration Sequence Index | Hyperspectral Materials | research-model | M1 | Formula specified; not implemented in Atlas |
| 83 | [DPCCI](#dpcci) - DESIS Phycocyanin Column Concentration Index | Aquatic Blooms & Pigments | research-model | M1 | Formula specified; not implemented in Atlas |
| 84 | [PFTIB](#pftib) - Phytoplankton Functional Type Index Battery | Aquatic Blooms & Pigments | research-model | M1 | Formula specified; not implemented in Atlas |
| 85 | [TSEAI](#tseai) - Methane Inventory Residual Research Model | Atmospheric Methane & Carbon | research-model | M1 | Transport inversion required |
| 86 | [ISSAI](#issai) - ICESat-2 + Sentinel-1 Subsidence Attribution Index | Cross-Sensor Decision Models | research-model | M1 | Formula specified; not implemented in Atlas |
| 87 | [GEAWSI](#geawsi) - GRACE-FO + ECOSTRESS Agricultural Water Stress Index | Cross-Sensor Decision Models | research-model | M1 | Formula specified; not implemented in Atlas |
| 88 | [EMSMMI](#emsmmi) - EMIT Mineral + Sentinel-1 Soil Moisture Index | Cross-Sensor Decision Models | research-model | M1 | Formula specified; not implemented in Atlas |
| 89 | [NFCAI](#nfcai) - NISAR-Optical Biomass Calibration Model | Forest Disturbance & Carbon | research-model | M1 | Field calibration required |
| 90 | [SNUVQI](#snuvqi) - NO₂ + Sentinel-2 Urban Vegetation Air Quality Index | Cross-Sensor Decision Models | research-model | M1 | Formula specified; not implemented in Atlas |
| 91 | [PUENPI](#puenpi) - Coastal Wetland Carbon-Budget Research Model | Cross-Sensor Decision Models | research-model | M1 | Carbon-budget model required |

## Fire Effects & Recovery

- **Family ID:** `fire-effects`
- **Records:** 4 (1 primary; 3 research-model)

<a id="bh-dfsi"></a>
### BH-DFSI - Burned Hillside Surface Context Score

- **Domain:** Wildfire & Post-Fire (`wildfire`)
- **Capability role:** primary in Fire Effects & Recovery
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 L2A
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Calibrated debris-flow model f(ΔNBR, slope, flow accumulation, soil, rainfall intensity and duration)
```

**Implemented or retained legacy formula**

```text
max(0, 0.15 − NBR) × max(0, BSI + 0.1) × max(0, 0.35 − NDVI)
```

- **Temporal operator:** Single-scene live proxy; proposed model requires pre/post fire and rainfall windows
- **Spatial operator:** Per-pixel live proxy; proposed model requires terrain and flow-network context
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live layer combines low NBR, exposed-soil context, and low vegetation cover in one Sentinel-2 scene. It does not compute slope, rainfall, soil moisture, drainage, or debris-flow susceptibility.

**Intended use and inference limit.** Post-fire surface-context screening. Debris-flow or evacuation decisions require terrain, rainfall, soils, inventories, and held-out watershed evaluation.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [USGS Montecito debris-flow release (2018)](https://www.usgs.gov/data/debris-flow-inundation-and-damage-data-9-january-2018-montecito-debris-flow-event)

---

<a id="pshri"></a>
### PSHRI - Post-Fire Soil Hydrophobicity Risk Index

- **Domain:** Wildfire & Post-Fire (`wildfire`)
- **Capability role:** research-model in Fire Effects & Recovery
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** S2+ERA5
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
NDWI_post_rain − NDWI_pre_rain (in ERA5-confirmed precipitation window)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Normal soil wets after rain → NDWI rises. Hydrophobic burned soil repels water → NDWI unchanged despite rainfall.

**Intended use and inference limit.** Identifies slopes where rain will not absorb, flagging runoff and debris-flow risk.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="bsmti"></a>
### BSMTI - Burn Severity Mineralogy Transition Index

- **Domain:** Wildfire & Post-Fire (`wildfire`)
- **Capability role:** research-model in Fire Effects & Recovery
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** EMIT
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
depth(535nm) / depth(486nm)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Goethite→magnetite→hematite transition encodes fire temperature history. Requires EMIT 5 nm spectral resolution.

**Intended use and inference limit.** Maps fire temperature gradients in burn scars — links to revegetation prognosis.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="ubcdi"></a>
### UBCDI - Understory vs. Canopy Burn Discrimination Index

- **Domain:** Tropical Forest (`tropicalforest`)
- **Capability role:** research-model in Fire Effects & Recovery
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-2 context; proof target pending
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
NBR × SWIR2_elevation proxy (single-date)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Canopy burns cause NIR collapse (no green canopy). Understory fires leave canopy mostly intact but alter SWIR2. Single-date: low NBR + elevated SWIR2 indicates understory fire.

**Intended use and inference limit.** Distinguishes fire type for tropical forest carbon accounting and recovery prognosis.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [NASA Fire Information for Resource Management System (FIRMS)](https://firms.modaps.eosdis.nasa.gov/)

---


## Fuel Moisture Context

- **Family ID:** `fuel-moisture`
- **Records:** 2 (1 retired; 1 primary)

<a id="sf-eii"></a>
### SF-EII - Canopy Moisture Deficit Calibration Specification

- **Domain:** Wildfire & Post-Fire (`wildfire`)
- **Capability role:** retired in Fuel Moisture Context
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Retired record; not live
- **Formula status:** Rebuild required
- **Required inputs:** Sentinel-2 L2A | seasonal reference distribution | field LFMC for stronger inference
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
FuelMask × clip[(NDMI_reference − NDMI_t) / scale_reference, 0, 1]
```

**Implemented or retained legacy formula**

```text
Legacy [(B8A−B11)/(B8A+B11)] × [1−(B08/B12)] retained in source history only
```

- **Temporal operator:** Seasonal anomaly
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The prior multiplicative expression has an unstable physical direction because 1−B08/B12 is commonly negative over vegetation. A seasonal NDMI deficit is the defensible starting feature; LFMC requires field calibration.

**Intended use and inference limit.** Defines a canopy-moisture calibration experiment rather than a pre-ignition hazard product.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [US Drought Monitor — California drought context](https://droughtmonitor.unl.edu/)

---

<a id="lfmpi"></a>
### LFMPI - Live Fuel Moisture Deficit Proxy

- **Domain:** Wildfire & Post-Fire (`wildfire`)
- **Capability role:** primary in Fuel Moisture Context
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Field-calibrated LFMC = f(Sentinel-2 moisture features, vegetation type, season)
```

**Implemented or retained legacy formula**

```text
FuelGate × WaterReject × (1 − NDMI) / 2
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Dimensionless moisture-deficit proxy
- **Calibration:** Uncalibrated

**Physical rationale.** The live layer displays a normalized NDMI deficit over live vegetation after water rejection. It is not calibrated in percent LFMC.

**Intended use and inference limit.** Canopy-moisture context for selecting field-calibration targets.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [Drought.gov California-Nevada October 2021 drought update](https://www.drought.gov/drought-status-updates/drought-status-update-california-nevada-2021-10-15)

---


## Smoke & Extreme Fire Behavior

- **Family ID:** `fire-atmosphere`
- **Records:** 2 (1 reference; 1 research-model)

<a id="saci"></a>
### SACI - UV Absorbing Aerosol Context

- **Domain:** Wildfire & Post-Fire (`wildfire`)
- **Capability role:** reference in Smoke & Extreme Fire Behavior
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** TROPOMI
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Aerosol-composition classifier f(UVAI, AOD, absorption AOD, Ångström exponent, plume height, meteorology)
```

**Implemented or retained legacy formula**

```text
clip(AER_AI_340_380 / 3.5, 0, 1)
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Scaled native UV aerosol-index value
- **Calibration:** Uncalibrated

**Physical rationale.** The live layer displays the TROPOMI 340/380 nm UV Absorbing Aerosol Index. It does not calculate AOD340/AOD550 or distinguish smoldering from flaming combustion.

**Intended use and inference limit.** Documents absorbing-aerosol plume context; composition and fire-type inference require additional aerosol products and labels.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [NOAA GML long-range smoke from Bootleg and Dixie fires](https://gml.noaa.gov/aero/net/bld/2021_fires.html)

---

<a id="pcsii"></a>
### PCSII - Pyroconvection Detection Index

- **Domain:** Wildfire & Post-Fire (`wildfire`)
- **Capability role:** research-model in Smoke & Extreme Fire Behavior
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** GOES+TROPOMI
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
(BT_3.7µm − BT_11µm > 0) AND (AOD_TROPOMI > 1.0)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Pyrocumulus tops show reversed brightness temperature at 3.7µm + extreme AOD loading.

**Intended use and inference limit.** Real-time extreme fire behavior alert — pyroconvection creates erratic spotting kilometers ahead.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---


## Aquatic Blooms & Pigments

- **Family ID:** `aquatic-blooms`
- **Records:** 6 (1 primary; 1 variant; 1 component; 3 research-model)

<a id="peti"></a>
### PETI - Phytoplankton Bloom Context Proxy

- **Domain:** Water Quality & Freshwater (`waterquality`)
- **Capability role:** primary in Aquatic Blooms & Pigments
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Field-calibrated bloom model with temporal persistence and toxin assays
```

**Implemented or retained legacy formula**

```text
WaterGate × max[0, NDCI × RedEdgeContrast × 8]
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live formula combines red/red-edge contrasts over water. Sentinel-2 has no 620 nm phycocyanin band, and this output does not establish cyanobacterial toxicity.

**Intended use and inference limit.** Bloom-context screening for field sampling, not toxin or drinking-water safety determination.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [NOAA NCCOS Lake Erie HAB 2019 retrospective](https://coastalscience.noaa.gov/news/lake-erie-hab-2019-retrospective-bloom-severity-was-7-3-as-predicted-by-the-seasonal-forecast/)

---

<a id="csrc"></a>
### CSRC - Surface Scum Context Composite

- **Domain:** Water Quality & Freshwater (`waterquality`)
- **Capability role:** variant in Aquatic Blooms & Pigments
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Temporal surface-scum model with repeated clear observations and toxin assays
```

**Implemented or retained legacy formula**

```text
WaterGate × max(0, NDCI + NIRScumBoost) × (1 − TurbidityReject)
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live formula combines a red-edge bloom feature, elevated NIR, and a turbidity rejection term. It does not calculate persistence or cyanotoxin risk.

**Intended use and inference limit.** Locates surface-scum-like optical conditions for review and sampling.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [NASA Earthdata: Cleaner Water from Space (Lake Taihu HAB monitoring)](https://www.earthdata.nasa.gov/news/feature-articles/cleaner-water-from-space)

---

<a id="ctpsti"></a>
### CTPSTI - Phytoplankton Pigment Contrast Feature

- **Domain:** Water Quality & Freshwater (`waterquality`)
- **Capability role:** component in Aquatic Blooms & Pigments
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** PACE / DESIS
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
[ρ(560nm) − ρ(620nm)] / [ρ(560nm) + ρ(620nm)]
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The contrast may respond to pigment composition after aquatic atmospheric correction. It cannot determine species, toxin genes, or toxin concentration.

**Intended use and inference limit.** Candidate pigment-balance feature for studies with taxonomy and toxin assays.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="habsdi"></a>
### HABSDI - HAB Species-Level Discrimination Index

- **Domain:** Marine & Coastal (`marine`)
- **Capability role:** research-model in Aquatic Blooms & Pigments
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** PACE / DESIS
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
PC_index − FX_index (cyano) | FX_index − PC_index (diatom)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Cyanobacteria → phycocyanin (620 nm). Diatoms → fucoxanthin (510–540 nm). PACE OCI 5 nm bands resolve both pigment packages simultaneously.

**Intended use and inference limit.** Transforms HAB monitoring from presence/absence to toxin-risk species assessment.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="dpcci"></a>
### DPCCI - DESIS Phycocyanin Column Concentration Index

- **Domain:** Hyperspectral-Enabled (`hyperspectral`)
- **Capability role:** research-model in Aquatic Blooms & Pigments
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** DESIS + PACE
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
depth(621nm) / continuum from DESIS 2.55 nm resolution
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Phycocyanin has a sharp absorption at 621 nm. DESIS 2.55 nm resolution resolves this feature precisely — interpolated continuum removes background water-leaving radiance.

**Intended use and inference limit.** Accurate phycocyanin concentration mapping for drinking water reservoir management.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="pftib"></a>
### PFTIB - Phytoplankton Functional Type Index Battery

- **Domain:** Hyperspectral-Enabled (`hyperspectral`)
- **Capability role:** research-model in Aquatic Blooms & Pigments
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** PACE OCI
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
PFT_diatom=Abs(490)/Abs(440) | PFT_hapto=Abs(453)/Abs(490) | etc.
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** PACE OCI 5 nm bands resolve diatom (fucoxanthin 490–510 nm), haptophyte (19-hex-fucoxanthin 453 nm), and cyanobacteria (divinyl chlorophyll 440 nm shift) pigment packages simultaneously.

**Intended use and inference limit.** Global phytoplankton community composition — enables carbon export estimates and HAB species prediction.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---


## Water Condition & Plumes

- **Family ID:** `water-condition-plumes`
- **Records:** 10 (8 research-model; 1 primary; 1 variant)

<a id="swri"></a>
### SWRI - Sewage-Water Release Index

- **Domain:** Water Quality & Freshwater (`waterquality`)
- **Capability role:** research-model in Water Condition & Plumes
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-2 context; proof target pending
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
turbidity_shock × organic_bloom_proxy × persistence
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Sewage effluent combines turbidity spike (suspended solids), organic bloom signal (elevated NDCI), and distinctive green-to-blue ratio from nutrient loading.

**Intended use and inference limit.** Early warning for municipal wastewater failures — actionable within hours of Sentinel-2 overpass.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [NOAA Florida HAB Event Tracker (2018)](https://www.climate.gov/news-features/event-tracker/harmful-algal-blooms-linger-parts-southern-florida-july-and-august-2018)

---

<a id="dwci"></a>
### DWCI - Drinking Water Catchment Injury Index

- **Domain:** Water Quality & Freshwater (`waterquality`)
- **Capability role:** research-model in Water Condition & Plumes
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-2 context; proof target pending
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
turbidity_anomaly × upstream_flow_weight × persistence
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Turbidity in upstream catchment zones propagates to water treatment intake points; early detection at source reduces treatment cost and protects public supply.

**Intended use and inference limit.** Early warning for water treatment facilities — detects turbidity events before they reach intakes.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [California Water Boards Camp Fire Report (2018)](https://www.waterboards.ca.gov/drinking_water/certlic/drinkingwater/CampFire.html)

---

<a id="epdi"></a>
### EPDI - Bare-Surface and Water-Turbidity Context

- **Domain:** Water Quality & Freshwater (`waterquality`)
- **Capability role:** primary in Water Condition & Plumes
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
ΔBSI_upslope × TurbidityAnomaly_downstream × Persistence with flow-network linkage
```

**Implemented or retained legacy formula**

```text
0.5 × BareSurfaceHeuristic + 3 × TurbidityContrast × WaterGate
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live formula adds same-pixel bare-surface and water-turbidity features. It does not compute upslope/downstream linkage, change, or persistence.

**Intended use and inference limit.** Context layer for designing an erosion-delivery time-series study.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [California DWR Pajaro River levee break response (2023)](https://water.ca.gov/News/Blog/2023/Mar-23/DWR-Supports-Flood-Fight-Efforts-at-Pajaro-River-Levee-Break)

---

<a id="rdoci"></a>
### RDOCI - CDOM Spectral-Slope Research Specification

- **Domain:** Water Quality & Freshwater (`waterquality`)
- **Capability role:** research-model in Water Condition & Plumes
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Retrieval workflow required
- **Required inputs:** PACE OCI water-leaving reflectance | atmospheric correction | in-water absorption | field DOC/CDOM
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
DOC_estimate = f[aCDOM, spectral slope, optical water type] calibrated to field DOC
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Spectral slope: inverse wavelength; DOC units depend on calibration
- **Calibration:** Uncalibrated

**Physical rationale.** CDOM spectral slope is defined from absorption after atmospheric and aquatic retrieval, not directly from raw 320/412 nm reflectance. DOC inference requires field calibration and water-type controls.

**Intended use and inference limit.** Specifies the measurements needed to test a PACE-enabled DOC/CDOM relationship.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="dtpsi"></a>
### DTPSI - Dam Thermal Plume Stratification Index

- **Domain:** Water Quality & Freshwater (`waterquality`)
- **Capability role:** research-model in Water Condition & Plumes
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** Landsat TIRS
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
(LST_downstream_1km − LST_reservoir) / (LST_upstream − LST_reservoir)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** <0 = cold hypolimnetic release; >0 = warm surface release. Thermal stratification controls dissolved oxygen and fish habitat quality downstream.

**Intended use and inference limit.** Dam operations optimization for cold-water fisheries and downstream aquatic habitat.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="gmcpi"></a>
### GMCPI - Glacial Meltwater Chemistry Proxy Index

- **Domain:** Water Quality & Freshwater (`waterquality`)
- **Capability role:** research-model in Water Condition & Plumes
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-2 + PACE
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
CDOM ratio × turbidity proxy in glacier outflow plumes
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Meltwater carries distinct glacial flour turbidity (B04/B03 ratio) and low CDOM (high B03/B04 vs. downstream). Combines visible turbidity with spectral signature of rock flour.

**Intended use and inference limit.** Tracks glacial meltwater contribution to freshwater chemistry — crucial for downstream communities.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [USGS / NPS Glacier Monitoring Program](https://www.nps.gov/kefj/index.htm)

---

<a id="sgdci"></a>
### SGDCI - Submarine Groundwater Discharge Chemistry Index

- **Domain:** Marine & Coastal (`marine`)
- **Capability role:** research-model in Water Condition & Plumes
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** PACE + ECOSTRESS
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
(ρ_412 / ρ_550) − CDOM_regional_mean within thermal anomaly mask
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** SGD creates localized CDOM-depleted (low UV/blue absorption) zones combined with thermal anomalies at seafloor seep points. Requires PACE UV channels.

**Intended use and inference limit.** Maps submarine freshwater discharge — a cryptic but critical coastal nutrient source.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="cd-uai"></a>
### CD-UAI - Coastal Water Turbidity Context

- **Domain:** Marine & Coastal (`marine`)
- **Capability role:** variant in Water Condition & Plumes
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Turbidity anomaly with cloud mask, plume morphology, source context, and multi-date persistence
```

**Implemented or retained legacy formula**

```text
max(0, RedGreenContrast + 0.05) × WaterGate × 6
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live formula is a red/green water-contrast feature. It does not contain an explicit cloud mask or establish dredging as the cause.

**Intended use and inference limit.** Highlights turbid coastal-water context for source and time-series review.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [Scientific Reports study on anthropogenic change in Pearl River Estuary sediment dynamics](https://www.nature.com/articles/s41598-021-96183-0)

---

<a id="trsi"></a>
### TRSI - Tailings River Shock Index

- **Domain:** Mining & Industrial (`mining`)
- **Capability role:** research-model in Water Condition & Plumes
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-2 context; proof target pending
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
turbidity_jump × ferric_color_shift × mine_proximity × persistence
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Tailings releases create ferric iron turbidity plumes (red-orange discoloration in B04/B03 ratio) combined with extreme turbidity — a signature distinct from natural sediment loads.

**Intended use and inference limit.** Real-time tailings spill detection downstream of active mines — enables emergency response within days.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [UNEP Samarco disaster profile (2015)](https://www.unep.org/news-and-stories/story/brazil-mine-disaster)

---

<a id="ierpi"></a>
### IERPI - Industrial Effluent River Plume Index

- **Domain:** Mining & Industrial (`mining`)
- **Capability role:** research-model in Water Condition & Plumes
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Landsat-family/Sentinel-2 context
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
turbidity × iron_color_shift × channel_mask
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Industrial discharge creates turbidity and iron/chemical color shifts in river channels. Landsat captures with S2 spatial logic; S2 approximation works with same band equivalents.

**Intended use and inference limit.** Documents illegal industrial discharge events — enables enforcement action with satellite evidence.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [EPA Gold King Mine Response Action](https://www.epa.gov/goldkingmine)

---


## Riparian & Floodplain Condition

- **Family ID:** `riparian-flood`
- **Records:** 3 (2 variant; 1 primary)

<a id="rrfi"></a>
### RRFI - Riparian Dry-Bare Context Composite

- **Domain:** Water Quality & Freshwater (`waterquality`)
- **Capability role:** variant in Riparian & Floodplain Condition
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
ΔNDVI_riparian × ΔNDWI_channel × ΔBSI_bank with mapped riparian and channel zones
```

**Implemented or retained legacy formula**

```text
max(0, 0.3−NDVI) × max(0, −NDWI) × max(0, BSI) × 40
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live layer is a single-scene dry, sparsely vegetated, bare-surface feature. It does not measure riparian loss or channel decline without a baseline and spatial masks.

**Intended use and inference limit.** Surfaces candidate dry/bare riparian context for time-series analysis.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [USGS Upper Rio Grande streamflow and climate response study](https://pubs.usgs.gov/publication/sir20215138)

---

<a id="fcli"></a>
### FCLI - Floodplain SWIR-Vegetation Context

- **Domain:** Water Quality & Freshwater (`waterquality`)
- **Capability role:** primary in Riparian & Floodplain Condition
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
SWIR2 anomaly after inundation × next-season vegetation suppression
```

**Implemented or retained legacy formula**

```text
max(0, B12−0.18) × max(0, 0.4−NDVI) × 8
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live layer is a single-scene SWIR2 and low-vegetation feature. It does not compute an anomaly, flood history, contamination, or next-season response.

**Intended use and inference limit.** Identifies candidate floodplain surface context for a longitudinal contamination study.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [EPA Harvey Response / USGS Sediment Studies](https://www.epa.gov/archive/epa/newsreleases/status-water-systems-areas-affected-harvey.html)

---

<a id="wda-csi"></a>
### WDA-CSI - Wetland-Agriculture Edge Context

- **Domain:** Agriculture & Food (`agriculture`)
- **Capability role:** variant in Riparian & Floodplain Condition
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Multi-date crop-green anomaly × wetland drainage change × mapped peat disturbance
```

**Implemented or retained legacy formula**

```text
max(0, NDCI) × max(0, −NDWI) × OrganicSurfaceHeuristic × 10
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live formula is a single-scene optical conjunction. It does not measure drainage, NDWI loss, nitrogen addition, or agricultural intrusion.

**Intended use and inference limit.** Context for reviewing wetland edges before land-cover and hydrologic analysis.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [Everglades Foundation on Everglades Agricultural Area peat subsidence](https://www.evergladesfoundation.org/post/everglades-restoration-water-and-climate-change)

---


## Floating & Surface Material

- **Family ID:** `floating-material`
- **Records:** 4 (1 primary; 3 variant)

<a id="smpdi"></a>
### SMPDI - Floating-Material Spectral Contrast

- **Domain:** Marine & Coastal (`marine`)
- **Capability role:** primary in Floating & Surface Material
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 + EMIT
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
WaterGate × LandReject × [FAI − ((B8A−B11)/(B8A+B11))]
```

**Implemented or retained legacy formula**

```text
WaterGate × LandReject × [FAI − ((B8A−B11)/(B8A+B11))]
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live feature combines a floating-algae-style baseline residual with NIR/SWIR contrast and water/land gates. Sargassum-versus-plastic discrimination has not been independently evaluated.

**Intended use and inference limit.** Candidate feature for labeled floating-material classification against established FDI baselines.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [USF Sargassum Watch System Caribbean bulletins](https://optics.marine.usf.edu/projects/saws.html)

---

<a id="kcdsi"></a>
### KCDSI - Floating or Shallow-Water Vegetation Context

- **Domain:** Marine & Coastal (`marine`)
- **Capability role:** variant in Floating & Surface Material
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 + S3
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Depth-corrected multi-date kelp-canopy condition model
```

**Implemented or retained legacy formula**

```text
max(0, NDVI) × I[B11<0.04 and B03<0.16]
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live layer displays positive NDVI under a simple low-SWIR water-context gate. It does not correct bathymetry or measure kelp stress.

**Intended use and inference limit.** Candidate floating/shallow vegetation context for labeled kelp mapping.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [Monterey Bay National Marine Sanctuary Kelp Studies](https://montereybay.noaa.gov/)

---

<a id="owsi"></a>
### OWSI - Oil Spill Weathering Stage Index

- **Domain:** Marine & Coastal (`marine`)
- **Capability role:** variant in Floating & Surface Material
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** EMIT + Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
NDOI × (B11/B12) weathering ratio
```

**Implemented or retained legacy formula**

```text
NDOI × (B11/B12) weathering ratio
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Fresh crude: high SWIR absorption. Weathered oil: oxidized surface changes B11/B12 ratio. Combining NDOI with SWIR slope tracks oil age from fresh (days) to emulsified (weeks).

**Intended use and inference limit.** Real-time spill response prioritization — fresh vs. weathered oil requires different cleanup methods.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [NOAA Deepwater Horizon oil spill case study](https://response.restoration.noaa.gov/deepwater-horizon-oil-spill-case-study)

---

<a id="mp-pdi"></a>
### MP-PDI - Floating-Debris Candidate Feature

- **Domain:** Marine & Coastal (`marine`)
- **Capability role:** variant in Floating & Surface Material
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Labeled floating-material classifier with explicit natural-debris, foam, Sargassum, cloud, glint, and turbidity controls
```

**Implemented or retained legacy formula**

```text
max(0, FAI) × NonVegetationGate × LowTurbidityGate × 10
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live formula does not implement explicit foam or Sargassum terms and cannot identify polymer composition from Sentinel-2 alone.

**Intended use and inference limit.** Candidate floating-debris feature for comparison with FDI-based classification.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [UNEP X-Press Pearl maritime disaster report](https://www.unep.org/resources/report/x-press-pearl-maritime-disaster-sri-lanka-report-un-environmental-advisory-mission)

---


## Coastal Habitat Condition

- **Family ID:** `coastal-habitats`
- **Records:** 3 (1 primary; 2 research-model)

<a id="cbsdi"></a>
### CBSDI - Coral Brightness Context Proxy

- **Domain:** Marine & Coastal (`marine`)
- **Capability role:** primary in Coastal Habitat Condition
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 + PRISMA
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Multi-date, depth-corrected benthic change model with field coral-condition labels
```

**Implemented or retained legacy formula**

```text
I[(B03−B04)/(B03+B04) < 0.05 and B02 > 0.06] × (0.5 + 3B02)
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live code implements one brightness/green-red condition only. It does not implement the advertised three stages or determine bleaching, mortality, or algal colonization.

**Intended use and inference limit.** Single-scene shallow-water brightness context for selecting field-reviewed change targets.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [Mongabay report on the 2020 Great Barrier Reef bleaching event](https://news.mongabay.com/2020/04/great-barrier-reef-suffers-biggest-bleaching-event-yet/)

---

<a id="mdspi"></a>
### MDSPI - Mangrove Dieback Spatial Pattern Index

- **Domain:** Marine & Coastal (`marine`)
- **Capability role:** research-model in Coastal Habitat Condition
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-2 + S1; proof target pending
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
NDVI_loss in mangrove zone × BSI_increase
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Mangrove dieback creates characteristic spatial NDVI loss patterns (canopy collapse) combined with exposed substrate (elevated BSI) — distinguishing it from seasonal leaf drop.

**Intended use and inference limit.** Alerts coastal managers to accelerating mangrove dieback — protecting storm surge buffers.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [Sundarbans Forestry Department / UNESCO](https://whc.unesco.org/en/list/798/)

---

<a id="spei"></a>
### SPEI - Seagrass Photosynthetic Efficiency Index

- **Domain:** Marine & Coastal (`marine`)
- **Capability role:** research-model in Coastal Habitat Condition
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-2 + DESIS
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Water-depth corrected NDVI in shallow coastal bathymetry window
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Seagrass has distinct NIR-red reflectance ratio in clear shallow water. Depth correction using Lyzenga water column model reduces false positives from benthic sediment.

**Intended use and inference limit.** Monitors critical blue-carbon seagrass meadows — CO₂ sequestration baseline for coastal carbon accounting.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [Lyzenga (1978) / Adriatic Seagrass Monitoring](https://doi.org/10.1016/0034-4257(78)90029-7)

---


## Crop & Soil Stress

- **Family ID:** `crop-stress`
- **Records:** 4 (1 primary; 2 research-model; 1 variant)

<a id="npdefi"></a>
### NPDefI - Nitrogen vs. Phosphorus Deficiency Discrimination Index

- **Domain:** Agriculture & Food (`agriculture`)
- **Capability role:** primary in Crop & Soil Stress
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 + EnMAP
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
[(B04−B05)/(B04+B05)] − [(B12−B11)/(B12+B11)]
```

**Implemented or retained legacy formula**

```text
[(B04−B05)/(B04+B05)] − [(B12−B11)/(B12+B11)]
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** N deficiency → chlorophyll degradation → red-edge shift (B05/B04 signal). P deficiency → anthocyanin → SWIR2 (B12). Subtraction yields a signed nutrient discriminator.

**Intended use and inference limit.** Precision nutrient prescription from orbit — reduces fertilizer over-application and nutrient runoff.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [Iowa State nutrient deficiencies guide](https://www.agronext.iastate.edu/soilfertility/nutrientdeficiencies.html)

---

<a id="scspi"></a>
### SCSPI - Soil Compaction Spectral Proxy Index

- **Domain:** Agriculture & Food (`agriculture`)
- **Capability role:** research-model in Crop & Soil Stress
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-2 context; proof target pending
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
[1−(B11/B12)] × (B03/B02)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Compacted soils show distinctive SWIR ratio from reduced porosity and altered surface crust mineralogy. Applied during bare-field windows when vegetation is absent.

**Intended use and inference limit.** Identifies compaction zones in farm fields — guides subsoiling operations to restore yield.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [Kansas State Agricultural Extension Soil Studies](https://www.ksre.k-state.edu/)

---

<a id="apri"></a>
### APRI - Aflatoxin Pre-Harvest Risk Index

- **Domain:** Agriculture & Food (`agriculture`)
- **Capability role:** research-model in Crop & Soil Stress
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** ECOSTRESS + S2 + ERA5
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
(LST_anomaly/σ) × [1−NDWI] × heat_accumulation_days
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Aspergillus infection risk peaks when heat stress + moisture deficit + heat accumulation coincide during flowering-to-grain-fill. LST anomaly from ECOSTRESS required.

**Intended use and inference limit.** Pre-harvest aflatoxin risk maps at field scale — estimated 25% reduction could prevent millions of cancer cases globally.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="pdsdi"></a>
### PDSDI - Crop Red-Edge and Dryness Context

- **Domain:** Agriculture & Food (`agriculture`)
- **Capability role:** variant in Crop & Soil Stress
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Spatial NDVI texture normalized by crop, phenology, moisture, and management baselines
```

**Implemented or retained legacy formula**

```text
max(0, 0.6−NDRE) × max(0, B11/B08−0.5) × 4
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live layer contains no texture or spatial variance and cannot distinguish pesticide stress from drought, disease, nutrient limitation, or management.

**Intended use and inference limit.** Crop stress context for a labeled causal-discrimination study.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [University of Illinois Crop Sciences Research](https://cropsciences.illinois.edu/)

---


## Agricultural Management

- **Family ID:** `agri-management`
- **Records:** 2 (1 primary; 1 research-model)

<a id="cctti"></a>
### CCTTI - Cover Crop Termination Timing Index

- **Domain:** Agriculture & Food (`agriculture`)
- **Capability role:** primary in Agricultural Management
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 time series
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
NDVI_cover_green × (1−soil_tillage_signal)
```

**Implemented or retained legacy formula**

```text
NDVI_cover_green × (1−soil_tillage_signal)
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Cover crops maintain distinctive NDVI signature before termination; rapid NDVI drop + BSI increase marks termination event. Timing optimizes nitrogen fixation vs. cash crop planting window.

**Intended use and inference limit.** Precision timing recommendations for cover crop termination — maximizes nitrogen credit to cash crops.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [Illinois Department of Agriculture I-COVER program](https://agr.illinois.gov/resources/landwater/i-cover.html)

---

<a id="iwuei"></a>
### IWUEI - Irrigation Water Use Efficiency Index

- **Domain:** Agriculture & Food (`agriculture`)
- **Capability role:** research-model in Agricultural Management
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** ECOSTRESS + S1
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
ET_ecostress / (precipitation_ERA5 + irrigation_proxy_S1)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** High ET relative to precipitation confirms active irrigation; SAR soil moisture change detects recent wetting events. Ratio encodes how efficiently applied water converts to crop ET.

**Intended use and inference limit.** Identifies fields wasting irrigation water — direct targets for smart irrigation system installation.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---


## Mining Surfaces & Risk

- **Family ID:** `mining-risk`
- **Records:** 6 (1 primary; 1 retired; 4 research-model)

<a id="tdr-asi"></a>
### TDR-ASI - Mining Iron-SWIR Context Proxy

- **Domain:** Mining & Industrial (`mining`)
- **Capability role:** primary in Mining Surfaces & Risk
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Field-informed mineral/turbidity anomaly with mine, channel, and time-series context
```

**Implemented or retained legacy formula**

```text
max(0, RedBlueContrast−0.05) × max(0, B11/B12−1) × 3
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live formula contains no mine-proximity term and cannot uniquely identify jarosite, sulfate, or a tailings release from Sentinel-2 ratios.

**Intended use and inference limit.** Mining-area iron/SWIR context for field-informed mineral analysis.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [NASA Earth Observatory: Mining Peru's Cerro de Pasco](https://science.nasa.gov/earth/earth-observatory/mining-perus-cerro-de-pasco-144481/)

---

<a id="amdphi"></a>
### AMDPHI - AMD Iron-Mineral Calibration Specification

- **Domain:** Mining & Industrial (`mining`)
- **Capability role:** retired in Mining Surfaces & Risk
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Retired record; not live
- **Formula status:** Rebuild required
- **Required inputs:** surface reflectance | field pH | XRD/mineralogy | spectral library | held-out sites
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
pH_estimate = f(mineral features, field pH, water/soil context) with held-out sites
```

**Implemented or retained legacy formula**

```text
Legacy visible ratio-of-ratios retired from live display because its denominator is unstable near zero
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Iron-mineral assemblages can be associated with acidity, but the prior ratio was numerically unstable and not a direct pH measurement.

**Intended use and inference limit.** Defines a mineral and field-chemistry calibration study; no current pH retrieval is claimed.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [USGS Iron Mountain environmental effects profile](https://ca.water.usgs.gov/projects/iron_mountain/environment.html)

---

<a id="tdsii"></a>
### TDSII - Tailings Change-Risk Calibration Model

- **Domain:** Mining & Industrial (`mining`)
- **Capability role:** research-model in Mining Surfaces & Risk
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Calibrated model required
- **Required inputs:** S2 + S1 InSAR
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Coefficients fitted to documented incidents and stable control facilities
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Calibrated event probability or declared risk score
- **Calibration:** Uncalibrated

**Physical rationale.** Optical indices and deformation rates have different units and cannot be added with arbitrary weights. Predictors require normalization, temporal alignment, labels, and learned coefficients.

**Intended use and inference limit.** Specifies a prospective multi-sensor risk experiment, not a deployed failure-warning system.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="reesai"></a>
### REESAI - Rare Earth Element Surface Anomaly Index

- **Domain:** Mining & Industrial (`mining`)
- **Capability role:** research-model in Mining Surfaces & Risk
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** EnMAP + EMIT
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
1−ρ(803nm)/[ρ(780nm)+interpolated_continuum]
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Nd³⁺ f-f transition absorption at 803 nm in REE carbonate/phosphate minerals. Requires EnMAP 5–10 nm spectral resolution to resolve the 803 nm feature.

**Intended use and inference limit.** Transforms REE exploration from field-campaign to satellite-first screening.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="ccrbi"></a>
### CCRBI - Coal Combustion Residue Bioaccumulation Index

- **Domain:** Mining & Industrial (`mining`)
- **Capability role:** research-model in Mining Surfaces & Risk
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-2 context; proof target pending
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
[(B04−B08)/(B04+B08)] × [B03/(B11+0.01)]
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Grass over CCR impoundments accumulates As/Se causing anthocyanin stress response (elevated red). Harkness et al. 2025: "grass is a tattletale" — phytotoxic stress reveals buried coal ash.

**Intended use and inference limit.** Maps CCR impoundment footprints and leachate migration without drilling.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [TVA Kingston Fossil Plant Recovery / EPA Reports](https://www.epa.gov/tn/kingston-coal-ash-spill)

---

<a id="hlpii"></a>
### HLPII - Heap Leach Pad Integrity Index

- **Domain:** Mining & Industrial (`mining`)
- **Capability role:** research-model in Mining Surfaces & Risk
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** S2 + EMIT
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
SWIR2_anomaly in liner failure zone + EMIT mineral alteration downslope
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Liner failure causes SWIR2 elevation from leachate-altered soil mineralogy. EMIT resolves the specific alteration mineral suite. S2 alone lacks the spectral resolution.

**Intended use and inference limit.** Monitors cyanide/acid leachate containment integrity at 1,000+ active heap leach operations.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---


## Urban Surface Condition

- **Family ID:** `urban-surfaces`
- **Records:** 6 (1 primary; 2 component; 3 research-model)

<a id="ec-aci"></a>
### EC-ACI - Evapotranspirative Canopy & Asphalt Contrast Index

- **Domain:** Urban & Infrastructure (`urban`)
- **Capability role:** primary in Urban Surface Condition
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 + ECOSTRESS
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
(1−NDVI) × low_moisture_proxy
```

**Implemented or retained legacy formula**

```text
(1−NDVI) × low_moisture_proxy
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Urban heat islands form where high-albedo vegetation is replaced by low-albedo asphalt. S2 NDVI loss combined with MSI moisture stress proxies urban heat island formation without thermal data.

**Intended use and inference limit.** Maps urban heat island intensity at neighborhood scale — guides heat-resilience infrastructure investment.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [WMO July 2019 hottest-month analysis](https://wmo.int/media/july-matched-and-maybe-broke-record-hottest-month-analysis-began)

---

<a id="hsai"></a>
### HSAI - Low-Vegetation Bare-Surface Context

- **Domain:** Urban & Infrastructure (`urban`)
- **Capability role:** component in Urban Surface Condition
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Tree-canopy and shade-access model inside an explicit urban residential mask
```

**Implemented or retained legacy formula**

```text
max(0, 0.3−NDVI) × max(0, BSI+0.05) × 6
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live formula contains no urban, residential, tree-crown, or shade mask. It is a generic low-vegetation/bare-surface feature.

**Intended use and inference limit.** Input feature for an urban shade-access model with canopy and population data.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [NASA VEDA Urban Heating dashboard](https://www.earthdata.nasa.gov/dashboard/data-catalog/urban-heating)

---

<a id="spsri"></a>
### SPSRI - Solar Panel Soiling Remote Index

- **Domain:** Urban & Infrastructure (`urban`)
- **Capability role:** research-model in Urban Surface Condition
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-2 + Planet
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
(ρ_B02 − baseline_B02) / baseline_B02 × (B11/B12)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Clean PV panels have very low reflectance (~5%). Dust-coated panels show elevated reflectance. B11/B12 ratio encodes dust mineral type (silica vs. carbonate).

**Intended use and inference limit.** Optimizes cleaning crew deployment — global PV soiling loss exceeds $5B/year.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [NREL Solar Soiling Mitigation Studies](https://www.nrel.gov/pv/soiling.html)

---

<a id="uciei"></a>
### UCIEI - Urban Cool Infrastructure Effectiveness Index

- **Domain:** Urban & Infrastructure (`urban`)
- **Capability role:** research-model in Urban Surface Condition
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** S2 + ECOSTRESS
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
(1−albedo_satellite) × LST_anomaly
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** High UCIEI = hot dark surface (old asphalt). Low UCIEI = effective cool infrastructure. Green roofs have low UCIEI despite low albedo because they convert absorbed energy to ET.

**Intended use and inference limit.** Parcel-level scorecard for cool infrastructure programs — enables evidence-based urban policy.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="pcadi"></a>
### PCADI - Dark Paved-Surface Context

- **Domain:** Urban & Infrastructure (`urban`)
- **Capability role:** component in Urban Surface Condition
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
RoadMask × (B02_t−B02_baseline)/B02_baseline with material and maintenance controls
```

**Implemented or retained legacy formula**

```text
I[B02,B03,B04<0.15 and NDVI<0.05] × (1−8×mean(B02,B03,B04))
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live formula has neither a road mask nor a temporal baseline and therefore cannot retrieve pavement age or condition.

**Intended use and inference limit.** Dark, low-vegetation surface context for a road-condition change study.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [SEMCOG 2021 pavement condition dataset](https://hub.arcgis.com/maps/SEMCOG%3A%3Apavement-condition-2021)

---

<a id="csdei"></a>
### CSDEI - Construction Site Silica Dust Emission Index

- **Domain:** Urban & Infrastructure (`urban`)
- **Capability role:** research-model in Urban Surface Condition
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** TROPOMI + GIS
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
AOD_anomaly × construction_site_proximity × wind_vector
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Silica dust from active construction sites creates AOD anomalies traceable with wind-direction analysis. Requires TROPOMI aerosol optical depth, not available as S2 WMS.

**Intended use and inference limit.** Identifies silica exposure hot zones for occupational health enforcement near construction sites.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---


## Landfill Surface Context

- **Family ID:** `landfill-context`
- **Records:** 2 (2 component)

<a id="lfgvi"></a>
### LFGVI - Landfill Vegetation-Stress Context

- **Domain:** Urban & Infrastructure (`urban`)
- **Capability role:** component in Landfill Surface Context
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
LandfillMask × temporal vegetation anomaly × spatial-pattern features × field gas measurements
```

**Implemented or retained legacy formula**

```text
max(0,0.5−NDVI) × max(0,0.2−RedEdgeContrast) × max(0,0.3−NDMI) × 20
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live code contains no annular/ring-pattern operator and vegetation stress is not specific to landfill gas.

**Intended use and inference limit.** Vegetation-stress context for landfill inspection when combined with geology and field gas measurements.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [Freshkills Park landfill gas collection and processing](https://freshkillspark.org/landfill-engineering/collection-and-processing)

---

<a id="lrd-vsi"></a>
### LRD-VSI - Vegetation-Moisture Anomaly Context

- **Domain:** Urban & Infrastructure (`urban`)
- **Capability role:** component in Landfill Surface Context
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
LandfillMask × downslope flow path × temporal vegetation and water anomaly
```

**Implemented or retained legacy formula**

```text
max(0,0.4−NDVI) × max(0,NDWI+0.2) × 5
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live formula contains no landfill boundary, downslope channel, baseline, or source attribution.

**Intended use and inference limit.** Wet, low-vegetation context for designing a field-verified leachate study.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [NOAA Newtown Creek hazardous-waste profile](https://darrp.noaa.gov/hazardous-waste/newtown-creek)

---


## Permafrost & Peat Change

- **Family ID:** `permafrost-change`
- **Records:** 5 (2 component; 1 primary; 2 research-model)

<a id="tt-api"></a>
### TT-API - Wet Exposed-Peat Context

- **Domain:** Permafrost & Arctic (`permafrost`)
- **Capability role:** component in Permafrost & Peat Change
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Multi-date peat exposure × mapped slump-edge displacement × terrain context
```

**Implemented or retained legacy formula**

```text
PeatReflectanceHeuristic × max(0,0.3−NDVI) × max(0,NDWI+0.3) × 8
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live code contains no edge-collapse or change operator and cannot establish active thermokarst expansion.

**Intended use and inference limit.** Wet exposed-organic-surface context for time-series thermokarst mapping.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [High carbon emissions from thermokarst lakes of Western Siberia](https://www.nature.com/articles/s41467-019-09592-1)

---

<a id="tperi"></a>
### TPERI - Thermokarst Pond-Edge Context

- **Domain:** Permafrost & Arctic (`permafrost`)
- **Capability role:** component in Permafrost & Peat Change
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 bi-temporal
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Expansion rate = [Area(t2)−Area(t1)] / [t2−t1], with boundary-registration uncertainty
```

**Implemented or retained legacy formula**

```text
I[B12>0.08 and −0.2<NDWI<0.4] × max(0,NDWI+0.2) × 3
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Live: dimensionless context; proposed rate: area/time or distance/time
- **Calibration:** Uncalibrated

**Physical rationale.** The live layer is a single-scene wet peat-edge feature. Rate and expansion require registered dates and mapped boundaries.

**Intended use and inference limit.** Selects candidate pond margins for a reproducible change-rate workflow.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [Natural Resources Canada Mackenzie Valley permafrost monitoring publication](https://ostrnrcan-dostrncan.canada.ca/entities/publication/322833e9-a6fa-41bc-8b67-de66b1b39940)

---

<a id="pcei"></a>
### PCEI - Peat Carbon Exposure Index

- **Domain:** Permafrost & Arctic (`permafrost`)
- **Capability role:** primary in Permafrost & Peat Change
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
(1−NDVI) × high_SWIR2 × (1−NDWI)
```

**Implemented or retained legacy formula**

```text
(1−NDVI) × high_SWIR2 × (1−NDWI)
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Exposed dark peat (thawed, not waterlogged) has distinctive spectral signature: low NIR (low NDVI), elevated SWIR2 from organic matter, and low surface moisture (low NDWI).

**Intended use and inference limit.** Satellite proxy for peat carbon vulnerability — identifies zones at highest risk of rapid oxidation.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [WCS Canada Hudson Bay Lowland peatland synthesis](https://wcscanada.org/about/our-programs/forests-peatlands-and-climate-change/synthesis-of-peatland-knowledge-in-the-hudson-bay-lowland/)

---

<a id="fgdci"></a>
### FGDCI - Frozen Ground Dielectric Change Index

- **Domain:** Permafrost & Arctic (`permafrost`)
- **Capability role:** research-model in Permafrost & Peat Change
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-1 SAR proof target pending
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
(VV_dB − VH_dB) − seasonal_mean(VV_dB − VH_dB)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Frozen soil dielectric ~4; thawed ~20–30. 3–6 dB shifts in C-band VV. VV-VH difference normalizes vegetation; anomaly from seasonal mean isolates freeze/thaw transition.

**Intended use and inference limit.** Pan-Arctic freeze/thaw monitoring — tracks permafrost active layer dynamics from Sentinel-1 global coverage.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [C-band SAR freeze/thaw detection (Sentinel-1) — see ESA S1 user guide](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar)

---

<a id="alsi"></a>
### ALSI - Active Layer Depth Thermal-Spectral Composite

- **Domain:** Permafrost & Arctic (`permafrost`)
- **Capability role:** research-model in Permafrost & Peat Change
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** ECOSTRESS + Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
0.6×(LST_anomaly/σ) + 0.4×[(B12−B11)/(B12+B11)]
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Deeper active layers → warmer surface temperatures (ECOSTRESS LST) + greater clay mineral exposure from frost churning (SWIR B12/B11 ratio). Requires ECOSTRESS thermal.

**Intended use and inference limit.** Satellite proxy for active layer depth — orders of magnitude denser than field probe networks.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---


## Snow Pigment Context

- **Family ID:** `snow-algae`
- **Records:** 1 (1 primary)

<a id="sabsi"></a>
### SABSI - Bright-Snow Red-Green Context

- **Domain:** Permafrost & Arctic (`permafrost`)
- **Capability role:** primary in Snow Pigment Context
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 + Planet
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
SnowMask × pigment model calibrated to algae abundance and impurities
```

**Implemented or retained legacy formula**

```text
I[B02>0.4 and B03>0.4] × max[0, (B04−B03)/(B04+B03)+0.05] × 10
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live code uses visible-band brightness rather than NDSI and cannot uniquely attribute red snow to algae.

**Intended use and inference limit.** Red/green spectral context over bright snow for field-reviewed algae studies.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [Greenland Ice Sheet Algae Project / Nature](https://www.nature.com/articles/s41561-020-0582-5)

---


## Wetland Gas Surface Context

- **Family ID:** `wetland-gas`
- **Records:** 2 (2 component)

<a id="mepsi"></a>
### MEPSI - CH₄ Ebullition Pond Spectral Proxy

- **Domain:** Permafrost & Arctic (`permafrost`)
- **Capability role:** component in Wetland Gas Surface Context
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 + Planet
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
high_NDWI × low_NDVI × low_macrophyte_index
```

**Implemented or retained legacy formula**

```text
high_NDWI × low_NDVI × low_macrophyte_index
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Active ebullition ponds are open sediment-covered shallow water: high NDWI (water), low NDVI (no aquatic vegetation), and low chlorophyll index (bare water surface).

**Intended use and inference limit.** Maps active methane-ebullition ponds — the largest unmonitored non-CO₂ greenhouse gas source in Arctic.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [High carbon emissions from thermokarst lakes of Western Siberia](https://www.nature.com/articles/s41467-019-09592-1)

---

<a id="mhssp"></a>
### MHSSP - Open Anoxic-Surface Context Proxy

- **Domain:** Wetland & Peatland (`wetland`)
- **Capability role:** component in Wetland Gas Surface Context
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 + TROPOMI
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
NDWI × (1−NDVI) × (1−CI_rededge/local_max)
```

**Implemented or retained legacy formula**

```text
NDWI × (1−NDVI) × (1−CI_rededge/local_max)
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live formula identifies wet, low-vegetation, low-red-edge surfaces. It does not measure methane flux or identify emission hotspots.

**Intended use and inference limit.** Candidate surface-context feature for studies with chamber, tower, or atmospheric methane measurements.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [NASA DeltaX Project / USGS Wetlands Center](https://deltax.jpl.nasa.gov/)

---


## Forest Canopy Condition

- **Family ID:** `forest-canopy`
- **Records:** 3 (1 primary; 1 variant; 1 research-model)

<a id="pdcsi"></a>
### PDCSI - Pre-Deforestation Canopy Stress Index

- **Domain:** Tropical Forest (`tropicalforest`)
- **Capability role:** primary in Forest Canopy Condition
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
[(B06−B05)/(B06+B05)] − [(B8A−B08)/(B8A+B08)]
```

**Implemented or retained legacy formula**

```text
[(B06−B05)/(B06+B05)] − [(B8A−B08)/(B8A+B08)]
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Early-stage canopy thinning shifts the red-edge toward 705 nm (B05 dominance over B06) — detectable 6–18 months before clear-cutting by selective logging or burning.

**Intended use and inference limit.** Provides a 6–18 month warning before deforestation becomes visible — enables preventive enforcement.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [INPE TerraBrasilis PRODES and DETER data platform](https://terrabrasilis.dpi.inpe.br/en/home-page/)

---

<a id="lisi"></a>
### LISI - Liana Infestation Structural Index

- **Domain:** Tropical Forest (`tropicalforest`)
- **Capability role:** variant in Forest Canopy Condition
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
2.5×[(B08−B11)/(B08+6B04−7.5B02+1)] × (B08/B11)
```

**Implemented or retained legacy formula**

```text
2.5×[(B08−B11)/(B08+6B04−7.5B02+1)] × (B08/B11)
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Lianas have higher SWIR1 absorption than tree canopies due to different leaf water content and structure. EVI-like combination × SWIR ratio discriminates vine-dominated from tree canopy.

**Intended use and inference limit.** Maps liana infestation extent — lianas suppress forest carbon storage by 20–30%.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [PMC review on remote sensing for liana infestation detection](https://pmc.ncbi.nlm.nih.gov/articles/PMC12035525/)

---

<a id="etcsi"></a>
### ETCSI - Emergent Tree Crown Stress Index

- **Domain:** Tropical Forest (`tropicalforest`)
- **Capability role:** research-model in Forest Canopy Condition
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** Planet + Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Per-crown red-edge stress from Planet 3 m delineation + S2 spectral
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Individual emergent tree crown delineation requires Planet 3 m resolution; red-edge stress per delineated crown uses S2 spectral information. Requires Planet sensor, not available via SH WMS.

**Intended use and inference limit.** Monitors individual emergent tree health — sentinels for whole-forest stress propagation.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---


## Forest Disturbance & Carbon

- **Family ID:** `forest-disturbance`
- **Records:** 3 (3 research-model)

<a id="fedgi"></a>
### FEDGI - Forest Edge Degradation Gradient Index

- **Domain:** Tropical Forest (`tropicalforest`)
- **Capability role:** research-model in Forest Disturbance & Carbon
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-2 context; proof target pending
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
NDVI gradient magnitude from interior toward edge
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Edge-effect degradation creates a systematic NDVI gradient from forest interior toward the clearcut boundary — the gradient magnitude encodes how severe and how far edge effects penetrate.

**Intended use and inference limit.** Quantifies edge-effect fragmentation — estimates effective forest area accounting for border degradation.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [Hansen et al. Global Forest Change](https://glads.umd.edu/dataset/global-forest-change)

---

<a id="slsdi"></a>
### SLSDI - Selective Logging Scar Detection Index

- **Domain:** Tropical Forest (`tropicalforest`)
- **Capability role:** research-model in Forest Disturbance & Carbon
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-2 + Planet
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
BSI_gap × NDVI_gap × canopy_context
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Selective logging creates small-scale (<1 ha) gap openings within intact canopy — elevated BSI and reduced NDVI in a high-NDVI surrounding matrix signals logging scars.

**Intended use and inference limit.** Monitors illegal selective logging in concessions — actionable for forest governance enforcement.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [PNG Forest Authority Concession Audits](http://www.forestry.gov.pg/)

---

<a id="nfcai"></a>
### NFCAI - NISAR-Optical Biomass Calibration Model

- **Domain:** Cross-Sensor Fusion (`crosssensor`)
- **Capability role:** research-model in Forest Disturbance & Carbon
- **Contribution:** C3 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Field calibration required
- **Required inputs:** NISAR L-band products | Sentinel-2 canopy features | topography | biomass plots | allometry
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Carbon = AGB_estimate × carbon_fraction with plot, allometric, saturation, and model uncertainty
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Biomass or carbon per area after calibration
- **Calibration:** Uncalibrated

**Physical rationale.** Radar backscatter and NDVI trend cannot be combined as an uncalibrated carbon equation, and NDVI trend is not a stand-age measurement. NISAR launched in 2025.

**Intended use and inference limit.** Defines a plot-calibrated biomass and carbon experiment using NISAR science data.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---


## Dryland Surface Processes

- **Family ID:** `dryland-processes`
- **Records:** 6 (5 research-model; 1 component)

<a id="bscmci"></a>
### BSCMCI - Biological Soil Crust Multi-Condition Index

- **Domain:** Dryland & Arid (`dryland`)
- **Capability role:** research-model in Dryland Surface Processes
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** PRISMA / DESIS
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
[(ρ680−ρ720)/(ρ680+ρ720)] × [(ρ550/ρ670)−1]
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** BSC development stages have distinctive pigment signatures: cyanobacteria (680 nm), green algae (550 nm), lichen (usnic acid). Requires sub-10 nm spectral resolution from PRISMA or DESIS.

**Intended use and inference limit.** Maps biological soil crust condition — BSCs stabilize desert soils and prevent dust emission.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="sbci"></a>
### SBCI - Sabkha Brine Chemistry Index

- **Domain:** Dryland & Arid (`dryland`)
- **Capability role:** research-model in Dryland Surface Processes
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** EMIT
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
depth(2217nm) / depth(2175nm)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Gypsum at 2217 nm; anhydrite at 2175 nm. Anhydrite forms at higher brine concentration — ratio encodes brine concentration history. Requires EMIT 5 nm bands.

**Intended use and inference limit.** Maps sabkha brine chemistry — tracks paleo-hydrological conditions in hyperarid environments.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="cscai"></a>
### CSCAI - Caliche Surface Carbonate Accumulation Index

- **Domain:** Dryland & Arid (`dryland`)
- **Capability role:** research-model in Dryland Surface Processes
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** EnMAP
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
depth(2335nm) / depth(2160nm)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Calcite CO₃²⁻ absorption at 2335 nm vs. weaker feature at 2160 nm. Ratio encodes carbonate accumulation grade (Stage I–VI caliche). Requires EnMAP 10 nm resolution.

**Intended use and inference limit.** Maps caliche distribution — critical for water infiltration modeling in arid agriculture.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="defpi"></a>
### DEFPI - Dust Emission Flux Proxy Index

- **Domain:** Dryland & Arid (`dryland`)
- **Capability role:** research-model in Dryland Surface Processes
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** EMIT + S2 + SMAP
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
mineral_erodibility(EMIT) × BSI(S2) × (1−soil_moisture(SMAP))
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Three factors control dust emission: mineral erodibility (EMIT), bare soil fraction (BSI), and dry surface (SMAP inverted). Multi-sensor fusion required for accurate emission flux.

**Intended use and inference limit.** Improves global dust emission inventories — critical for aerosol climate modeling.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="dlpehi"></a>
### DLPEHI - Desert Locust Pre-Emergence Habitat Index

- **Domain:** Dryland & Arid (`dryland`)
- **Capability role:** component in Dryland Surface Processes
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 + GPM
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
NDWI × (0.1<NDVI<0.3) × (NDTI>−0.2) — without rainfall gate
```

**Implemented or retained legacy formula**

```text
NDWI × (0.1<NDVI<0.3) × (NDTI>−0.2) — without rainfall gate
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Oviposition habitat requires moist sandy soil + sparse vegetation + sandy loam texture. S2 approximation without rainfall gate; GPM data adds rainfall confirmation in operational use.

**Intended use and inference limit.** 2–4 week earlier warning of locust outbreak habitat — enables preventive treatment before swarm formation.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [FAO desert locust crisis response page](https://www.fao.org/emergencies/where-we-work/desert-locust-crisis/)

---

<a id="aibeai"></a>
### AIBEAI - Arroyo Incision and Bank Erosion Activity Index

- **Domain:** Dryland & Arid (`dryland`)
- **Capability role:** research-model in Dryland Surface Processes
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Executable but non-live
- **Required inputs:** Sentinel-2 + Planet
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
BSI_channel_bottom / NDVI_channel_margin
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Active incision exposes fresh bright mineral soils (high BSI). Stable channels have established bank vegetation (positive NDVI at margins). Ratio encodes incision vs. stability state.

**Intended use and inference limit.** Maps actively eroding arroyos — guides erosion control investment and predicts downstream sediment loads.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [USGS Arroyo Restoration / Bureau of Land Management](https://www.blm.gov/new-mexico)

---


## Wetland Hydrology

- **Family ID:** `wetland-hydrology`
- **Records:** 3 (1 research-model; 2 component)

<a id="pwtdi"></a>
### PWTDI - Peatland Water-Table Calibration Model

- **Domain:** Wetland & Peatland (`wetland`)
- **Capability role:** research-model in Wetland Hydrology
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M2 - Executable formula; not live
- **Formula status:** Field calibration required
- **Required inputs:** Sentinel-1 GRD | Sentinel-2 L2A | water-table loggers | vegetation and seasonal covariates
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Logger-calibrated regression with geographic and temporal holdouts
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Estimated depth after calibration
- **Calibration:** Uncalibrated

**Physical rationale.** Sentinel-2 B09 is a coarse atmospheric-water-vapor band, not a direct 970/1020 nm Sphagnum water-content channel. Water-table depth must be calibrated to in-situ loggers.

**Intended use and inference limit.** Defines a radar-optical water-table experiment rather than an operational WTD product.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** [Biebrza National Park Research / Copernicus EMS](https://www.biebrza.org.pl/)

---

<a id="tfidi"></a>
### TFIDI - Single-Date Tidal-Zone Wetness Context

- **Domain:** Wetland & Peatland (`wetland`)
- **Capability role:** component in Wetland Hydrology
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 monthly
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Clear-observation NDWI percentile spread across a tidal time series
```

**Implemented or retained legacy formula**

```text
I[−0.1<NDWI<0.4] × I[B11<0.1] × max(0,NDWI+0.15) × 2
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live layer contains no variability calculation. It displays a single-date intermediate wetness condition.

**Intended use and inference limit.** Selects likely tidal-transition surfaces for a hydroperiod time-series analysis.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [Frontiers study of Yellow River Delta tidal-flat dynamics](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2023.1259081/full)

---

<a id="wdptzi"></a>
### WDPTZI - Peat Moisture Transition Proxy

- **Domain:** Wetland & Peatland (`wetland`)
- **Capability role:** component in Wetland Hydrology
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Spatial gradient magnitude or edge detector applied to a co-registered peat-moisture surface
```

**Implemented or retained legacy formula**

```text
I[0.05<|(B11−B8A)/(B11+B8A)|<0.3] × |NDWI| × 3
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** The live evalscript is per-pixel and does not calculate a Sobel operator or neighborhood gradient.

**Intended use and inference limit.** Moisture-transition context for a later spatial edge-analysis workflow.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [The Cryosphere study of Western Siberian thermokarst lake waters](https://tc.copernicus.org/articles/8/1177/2014/tc-8-1177-2014.pdf)

---


## Wetland Vegetation Structure

- **Family ID:** `wetland-vegetation`
- **Records:** 2 (1 primary; 1 variant)

<a id="ipvsi"></a>
### IPVSI - Invasive Phragmites vs. Native Vegetation Discrimination

- **Domain:** Wetland & Peatland (`wetland`)
- **Capability role:** primary in Wetland Vegetation Structure
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 seasonal
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Red-edge structural proxy for dense monoculture vs. diverse native marsh
```

**Implemented or retained legacy formula**

```text
Red-edge structural proxy for dense monoculture vs. diverse native marsh
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Invasive Phragmites forms dense monocultures with distinctive high NIR and low red-edge separation. Native wetland diversity creates more spectrally heterogeneous signals.

**Intended use and inference limit.** Maps invasive Phragmites extent — guides targeted herbicide treatment to restore native wetlands.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [Great Lakes Phragmites Collaborative](https://www.greatlakesphragmites.net/)

---

<a id="wvtdi"></a>
### WVTDI - Wetland Vegetation Type Discrimination Index

- **Domain:** Wetland & Peatland (`wetland`)
- **Capability role:** variant in Wetland Vegetation Structure
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M3 - Live catalog visualization
- **Formula status:** Live screening proxy
- **Required inputs:** Sentinel-2 time series
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
NDWI + NDVI composite for vegetation-water ratio classification
```

**Implemented or retained legacy formula**

```text
NDWI + NDVI composite for vegetation-water ratio classification
```

- **Temporal operator:** Single-scene
- **Spatial operator:** Per-pixel
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Different wetland vegetation types (sedge, rush, forb, reed) have distinct NDWI/NDVI combinations reflecting moisture holding and canopy structure. Single-date approximation shows dominant type.

**Intended use and inference limit.** Baseline wetland vegetation mapping — essential for carbon stock estimation and restoration planning.

**Evidence and validation.** Reviewed event context; not performance evidence. Not independently evaluated (below V1).

**Context source.** [Tour du Valat Research Institute / Camargue](https://tourduvalat.org/en/)

---


## Hyperspectral Materials

- **Family ID:** `hyperspectral-materials`
- **Records:** 5 (5 research-model)

<a id="cmsti"></a>
### CMSTI - Clay-Mineral Absorption-Position Model

- **Domain:** Hyperspectral-Enabled (`hyperspectral`)
- **Capability role:** research-model in Hyperspectral Materials
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Spectral fitting required
- **Required inputs:** EMIT
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Mineral classification f(λ_min, feature shape, spectral library, mixture model, uncertainty)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Fitted wavelength and classification uncertainty
- **Calibration:** Uncalibrated

**Physical rationale.** An approximately 8 nm target shift is comparable to EMIT sampling and cannot be treated as a direct one-channel minimum. Spectral fitting, signal-to-noise, mixtures, and wavelength uncertainty are required.

**Intended use and inference limit.** Defines a falsifiable clay-mineral separability experiment.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="afcdi"></a>
### AFCDI - Asbestos Fiber Chrysotile Detection Index

- **Domain:** Hyperspectral-Enabled (`hyperspectral`)
- **Capability role:** research-model in Hyperspectral Materials
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** EMIT + PRISMA
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
depth(2317nm) / depth(2387nm)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Chrysotile Mg-OH doublet at 2317/2387 nm discriminated from antigorite (2320/2100 nm) and lizardite (2320/2390 nm). EMIT 5 nm sampling resolves the 70 nm separation.

**Intended use and inference limit.** Natural asbestos zone mapping near communities — eliminates the highest-uncertainty step in exposure assessment.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="scfgosi"></a>
### SCFGOSI - Soil Carbon Functional Group Oxidation State Index

- **Domain:** Hyperspectral-Enabled (`hyperspectral`)
- **Capability role:** research-model in Hyperspectral Materials
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** EMIT + EnMAP
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
depth(1730nm) / (1−mean_reflectance_400-2500nm)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Labile C (lipids, proteins) → C-H overtone at 1730 nm. Recalcitrant C (aromatic humus, char) → broad spectral darkness. Ratio encodes labile vs. recalcitrant proportion.

**Intended use and inference limit.** Distinguishes stable carbon from labile — critical for understanding which soils store carbon permanently.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="reenbi"></a>
### REENBI - REE Neodymium Band-Depth Feature

- **Domain:** Hyperspectral-Enabled (`hyperspectral`)
- **Capability role:** research-model in Hyperspectral Materials
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Continuum-removal specification
- **Required inputs:** EnMAP
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Rc803 = linearly interpolated continuum between validated shoulders; interpret through mixture and field tests
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Dimensionless continuum-removed band depth
- **Calibration:** Uncalibrated

**Physical rationale.** The prior denominator incorrectly added a shoulder reflectance to an interpolated continuum. Standard continuum removal uses the continuum value at the feature center.

**Intended use and inference limit.** Candidate neodymium absorption feature for spectral-library and field validation.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="epcase"></a>
### EPCASE - EnMAP Porphyry Cu Alteration Sequence Index

- **Domain:** Hyperspectral-Enabled (`hyperspectral`)
- **Capability role:** research-model in Hyperspectral Materials
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** EnMAP
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
SAM distance to porphyry alteration sequence endmember
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Porphyry Cu deposits have phyllic → potassic → propylitic alteration zones with diagnostic mineral assemblages in SWIR. EnMAP L2A provides the spectral resolution for alteration mapping.

**Intended use and inference limit.** Transforms Cu exploration — reduces discovery cost for critical battery mineral.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---


## Atmospheric Methane & Carbon

- **Family ID:** `atmospheric-carbon`
- **Records:** 2 (2 research-model)

<a id="mpssfi"></a>
### MPSSFI - Methane Matched-Filter Research Specification

- **Domain:** Hyperspectral-Enabled (`hyperspectral`)
- **Capability role:** research-model in Atmospheric Methane & Carbon
- **Contribution:** C2 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Atmospheric retrieval required
- **Required inputs:** EMIT
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Plume/background retrieval followed by wind-informed flux estimation and uncertainty
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Column enhancement; flux only after wind-informed inversion
- **Calibration:** Uncalibrated

**Physical rationale.** A three-band surface-reflectance depth at 1667 nm is not a robust atmospheric methane retrieval and does not isolate water vapor or carbon dioxide by itself.

**Intended use and inference limit.** Specifies an imaging-spectroscopy methane workflow consistent with plume retrieval practice.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="tseai"></a>
### TSEAI - Methane Inventory Residual Research Model

- **Domain:** Cross-Sensor Fusion (`crosssensor`)
- **Capability role:** research-model in Atmospheric Methane & Carbon
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Transport inversion required
- **Required inputs:** S5P TROPOMI + S2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
Source posterior p(source | residual, transport, inventory, land-cover prior, uncertainty)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Concentration residual; source flux only after inversion
- **Calibration:** Uncalibrated

**Physical rationale.** XCH4 concentration cannot be divided by land-cover fractions and emission factors with incompatible units. Land cover is a prior; attribution requires transport and uncertainty.

**Intended use and inference limit.** Defines the residual and evidence required for methane-source attribution.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---


## Cross-Sensor Decision Models

- **Family ID:** `cross-sensor-systems`
- **Records:** 5 (5 research-model)

<a id="issai"></a>
### ISSAI - ICESat-2 + Sentinel-1 Subsidence Attribution Index

- **Domain:** Cross-Sensor Fusion (`crosssensor`)
- **Capability role:** research-model in Cross-Sensor Decision Models
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** ICESat-2 + S1 + S2
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
(ICESat2_dZ/dt − InSAR_LOS_vertical) / ICESat2_dZ/dt
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** ICESat-2 measures absolute elevation change; InSAR measures relative deformation. Discrepancy identifies rapid incoherent subsidence or different temporal sampling.

**Intended use and inference limit.** Subsidence cause attribution for tens of millions in sinking coastal cities.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="geawsi"></a>
### GEAWSI - GRACE-FO + ECOSTRESS Agricultural Water Stress Index

- **Domain:** Cross-Sensor Fusion (`crosssensor`)
- **Capability role:** research-model in Cross-Sensor Decision Models
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** GRACE-FO + ECOSTRESS
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
(ET_ecostress / PET_estimate) × TWS_anomaly_sign
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** ET/PET < 1 = crop water stress. Negative TWS anomaly simultaneously = groundwater drawdown. Co-occurrence identifies the most urgent water security scenario.

**Intended use and inference limit.** Identifies irrigation systems where crop stress AND aquifer depletion co-occur.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="emsmmi"></a>
### EMSMMI - EMIT Mineral + Sentinel-1 Soil Moisture Index

- **Domain:** Cross-Sensor Fusion (`crosssensor`)
- **Capability role:** research-model in Cross-Sensor Decision Models
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** EMIT + S1
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
VWC_S1_raw / (1 + clay_fraction_EMIT × clay_dielectric_correction)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** Smectite clay inflates C-band backscatter-to-moisture retrieval. EMIT mineral fraction maps provide the clay correction enabling mineralogy-specific VWC retrieval.

**Intended use and inference limit.** Improved soil moisture accuracy at global scale — particularly in high-clay agricultural regions.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="snuvqi"></a>
### SNUVQI - NO₂ + Sentinel-2 Urban Vegetation Air Quality Index

- **Domain:** Cross-Sensor Fusion (`crosssensor`)
- **Capability role:** research-model in Cross-Sensor Decision Models
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Formula specified; not implemented in Atlas
- **Required inputs:** TROPOMI + S2 + ERA5
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
NO2_TROPOMI_downscaled − f(NDVI_S2, wind_ERA5)
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Uncalibrated dimensionless screening score
- **Calibration:** Uncalibrated

**Physical rationale.** S2 NDVI at 10 m constrains tree deposition capacity; ERA5 wind constrains dispersion. Residual NO₂ after tree-deposition model reveals neighborhoods with air quality benefit from urban forest.

**Intended use and inference limit.** Maps which neighborhoods receive NO₂ benefit from urban trees — environmental justice analysis.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

<a id="puenpi"></a>
### PUENPI - Coastal Wetland Carbon-Budget Research Model

- **Domain:** Cross-Sensor Fusion (`crosssensor`)
- **Capability role:** research-model in Cross-Sensor Decision Models
- **Contribution:** C1 - Provisional; entry-level prior-art review pending
- **Maturity:** M1 - Specified research concept; not live
- **Formula status:** Carbon-budget model required
- **Required inputs:** PACE OCI + ECOSTRESS
- **Formula version:** 2.0

**Proposed formula or workflow**

```text
All components harmonized to common carbon units, spatial support, interval, and system boundary
```

**Implemented or retained legacy formula**

```text
Not implemented in the current Atlas release.
```

- **Temporal operator:** Declared workflow; not implemented in Atlas
- **Spatial operator:** Declared workflow; not implemented in Atlas
- **Units:** Carbon per area per time after harmonization
- **Calibration:** Uncalibrated

**Physical rationale.** The prior expression subtracted aquatic primary production and mixed products with incompatible meanings and supports. A coastal carbon budget requires an explicit system boundary and sign convention.

**Intended use and inference limit.** Defines the accounting structure needed before combining PACE and thermal/ecosystem products.

**Evidence and validation.** Context location only. Not independently evaluated (below V1).

**Context source.** No context source recorded in the governed supplement.

---

## Reproducibility

Regenerate this document from the governed supplement:

```bash
python3 scripts/generate_gsia_v2_formula_catalog.py \
  preprint/gsia_preprint_v2_status_supplement_2026-07-21.csv \
  formulas/gsia-v2-formula-catalog.md
```

The generator fails if record counts, maturity counts, method-role counts, capability-family counts, unique identifiers, or the Atlas publication boundary do not match the governed release.
