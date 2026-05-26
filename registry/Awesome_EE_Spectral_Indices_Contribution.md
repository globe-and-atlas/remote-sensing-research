# Awesome Spectral Indices Submission Directory
### Complete Registry of Novel Formulations Ready for Contribution

*Generated: 2026-05-26 | Total: 46 proprietary indices citable under Daniel Bally / Globe & Atlas*

This document maps every single multi-spectral, multi-temporal, and radar index originated or formalized in this repository to the standard GEE band notations required by the [Awesome Spectral Indices](https://github.com/awesome-spectral-indices/awesome-spectral-indices) guidelines.

You can copy and paste any index block directly into a new **'Submit a Spectral Index'** issue on their repository.

---

## Standard Band & Parameter Key (Guidelines)
*   `A`: Aerosols (Sentinel-2 B1)
*   `B`: Blue (Sentinel-2 B2)
*   `G`: Green (Sentinel-2 B3)
*   `R`: Red (Sentinel-2 B4)
*   `RE1`: Red Edge 1 (Sentinel-2 B5 - 705 nm)
*   `RE2`: Red Edge 2 (Sentinel-2 B6 - 740 nm)
*   `RE3`: Red Edge 3 (Sentinel-2 B7 - 783 nm)
*   `RE4`: Red Edge 4 (Sentinel-2 B8A - 865 nm)
*   `N`: NIR (Sentinel-2 B8 - 842 nm)
*   `S1`: SWIR 1 (Sentinel-2 B11 - 1610 nm)
*   `S2`: SWIR 2 (Sentinel-2 B12 - 2190 nm)
*   `VV`: Sentinel-1 Vertical-Vertical polarization backscatter
*   `VH`: Sentinel-1 Vertical-Horizontal polarization backscatter

---

## Index 1: PWCI (Produced Water Chemical Index)

> **Description**: Detects produced water chemical mixture containing salts, hydrocarbons, and dissolved heavy metals.

```yaml
short_name: PWCI
long_name: Produced Water Chemical Index
formula: "(((N - S1) / (N + S1))**3) * ((S1 - S2) / (S1 + S2)) * ((G - B) / (G + B))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 2: ASAI (Arid Salinity Anomaly Index)

> **Description**: Continuous detection of dynamic salinity lifecycle (from liquid brine pool green specular reflectance to evaporated SWIR salt crust).

```yaml
short_name: ASAI
long_name: Arid Salinity Anomaly Index
formula: "max((S1 - S2) / (S1 + S2), G) * (1.0 - (N - R) / (N + R))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 3: VSI (Vegetation Stress Index)

> **Description**: Measures the narrow red-edge blue-shift to identify sub-lethal vegetation stress from osmotic brine shock before biomass decline occurs.

```yaml
short_name: VSI
long_name: Vegetation Stress Index
formula: "((RE4 - RE3) / (RE4 + RE3)) - ((RE3 - RE1) / (RE3 + RE1))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: vegetation
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 4: OBEC (Oil-Brine Emulsion Composite)

> **Description**: Isolates mixed oil-brine emulsion signatures by combining surface oil slick (NDOI) and brine salinity ratios.

```yaml
short_name: OBEC
long_name: Oil-Brine Emulsion Composite
formula: "((G - S1) / (G + S1)) * ((N - S1) / (N + S1))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: water
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 5: FBC (Ferrugination-Brine Composite)

> **Description**: Detects anoxic iron oxidation staining resulting from surfacing deep reservoir produced water carrying dissolved Fe.

```yaml
short_name: FBC
long_name: Ferrugination-Brine Composite
formula: "((R - B) / (R + B)) * ((N - S1) / (N + S1)) * ((G - B) / (G + B))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 6: LBI (Liquid Brine Index)

> **Description**: Four-factor proxy specifically isolating active, standing saline water pools from clean runoff in bare soil context.

```yaml
short_name: LBI
long_name: Liquid Brine Index
formula: "((N - S1) / (N + S1)) * ((G - S1) / (G + S1)) * (1.0 - (N - R) / (N + R)) * (((S1 + R) - (N + B)) / ((S1 + R) + (N + B)))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 7: TRI (Toxic Residue Index)

> **Description**: Forensic mineral scar detection targeting evaporated brine salt co-deposits, heavy metal hydroxides, and iron staining.

```yaml
short_name: TRI
long_name: Toxic Residue Index
formula: "((N - S1) / (N + S1)) * ((G - B) / (G + B)) * ((R - B) / (R + B))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 8: BPI (Brine-Pavement Index)

> **Description**: Identifies produced water and hydrocarbon leakage on highly compacted bare surfaces (such as well pads and roads).

```yaml
short_name: BPI
long_name: Brine-Pavement Index
formula: "(((S1 + R) - (N + B)) / ((S1 + R) + (N + B))) * ((S1 - S2) / (S1 + S2)) * ((N - S1) / (N + S1))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: urban
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 9: REAI (Red Edge Alteration Index)

> **Description**: Measures red-edge slope alterations triggered by leaf deposition of heavy metal iron oxides from produced water aerosols.

```yaml
short_name: REAI
long_name: Red Edge Alteration Index
formula: "(RE2 - RE1) / (RE2 + RE1)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: vegetation
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 10: VCBI (Vegetation-Confirmed Brine Index)

> **Description**: Identifies active spill migration boundaries by coupling high surface salinity (NDSI) with active vegetation kill patterns.

```yaml
short_name: VCBI
long_name: Vegetation-Confirmed Brine Index
formula: "((N - S1) / (N + S1)) * (1.0 - (N - R) / (N + R))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: vegetation
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 11: PHI (Petro-Hydrocarbon Index)

> **Description**: Isolates oily produced water hydrocarbons from clean water runoff using coupled SWIR2 hydrocarbon and SWIR1 salt gates.

```yaml
short_name: PHI
long_name: Petro-Hydrocarbon Index
formula: "((S1 - S2) / (S1 + S2)) * ((N - S1) / (N + S1)) * (1.0 - ((G - N) / (G + N)))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 12: HMI (Heavy Metal Interaction)

> **Description**: Flags soil chemical alterations resulting from barium and strontium chloride precipitation in evaporated brine zones.

```yaml
short_name: HMI
long_name: Heavy Metal Interaction
formula: "((G - B) / (G + B)) * ((N - S1) / (N + S1))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 13: BH_DFSI (Burnt Hillside Debris-Flow Susceptibility Index)

> **Description**: Pre-event mudslide and debris flow susceptibility hazard mapping by coupling severe burn severity, soil exposure, moisture, and terrain slopes.

```yaml
short_name: BH_DFSI
long_name: Burnt Hillside Debris-Flow Susceptibility Index
formula: "clamp((0.15 - ((N - S2) / (N + S2))) / 0.30, 0.0, 1.0) * clamp(((((S1 + R) - (N + B)) / ((S1 + R) + (N + B))) - 0.10) / 0.20, 0.0, 1.0) * clamp((((G - S1) / (G + S1)) + 0.35) / 0.50, 0.0, 1.0) * clamp(((R - B) / (R + B)) * 2.0, 0.0, 1.0)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 14: SF_EII (Wildfire Fuel Hazard & Canopy Dehydration Index)

> **Description**: Pre-fire fuel stress assessment mapping bulk canopy water deficit and cell wall collapse from drought dehydration.

```yaml
short_name: SF_EII
long_name: Wildfire Fuel Hazard & Canopy Dehydration Index
formula: "((RE4 - S1) / (RE4 + S1)) * (1.0 - (N / S2))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: vegetation
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 15: LFMPI (Live Fuel Moisture Pre-Ignition Index)

> **Description**: Standardized live fuel moisture proxy tracking canopy water content and structural cell wall collapse prior to ignition.

```yaml
short_name: LFMPI
long_name: Live Fuel Moisture Pre-Ignition Index
formula: "2.5 * ((RE4 - S1) / (RE4 + S1 + 6.0 * R - 7.5 * B + 1.0)) - (S2 / S1)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: vegetation
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 16: PSHRI (Post-Fire Soil Hydrophobicity Risk Index)

> **Description**: Measures soil physical water-repulsion response immediately post-precipitation using pre/post rain bi-temporal differentials.

```yaml
short_name: PSHRI
long_name: Post-Fire Soil Hydrophobicity Risk Index
formula: "((G - N)/(G + N))_post - ((G - N)/(G + N))_pre"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 17: PETI (Phycocyanin Eutrophication Toxicity Index)

> **Description**: Flags virtual phycocyanin pigment absorption at 620 nm (between red and red-edge) for cyanobacterial bloom screening.

```yaml
short_name: PETI
long_name: Phycocyanin Eutrophication Toxicity Index
formula: "(R - RE1) / (R + RE1)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: water
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 18: CSRC (Cyanotoxin Scum Risk Composite)

> **Description**: Identifies dense floating cyanobacterial scum accumulations by coupling red-edge chlorophyll-a absorption with NIR cell scattering.

```yaml
short_name: CSRC
long_name: Cyanotoxin Scum Risk Composite
formula: "((RE1 - R) / (RE1 + R)) * N"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: water
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 19: HABSDI_cyano (HAB Species-Level Discrimination Index (Cyanobacteria))

> **Description**: Differentiates phycocyanin-dominant toxic cyanobacteria from fucoxanthin-dominant benign diatoms using hyperspectral slopes.

```yaml
short_name: HABSDI_cyano
long_name: HAB Species-Level Discrimination Index (Cyanobacteria)
formula: "(G - RE1) - (B - G)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: water
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 20: SMPDI (Sargassum vs. Microplastic Discrimination Index)

> **Description**: Separates synthetic marine microplastic polymer rafts from living photosynthesizing Sargassum seaweed.

```yaml
short_name: SMPDI
long_name: Sargassum vs. Microplastic Discrimination Index
formula: "(N - S1) - ((RE4 - S1) / (RE4 + S1))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: water
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 21: KCDSI (Kelp Canopy Density and Stress Index)

> **Description**: Fuses kelp canopy leaf density and chlorophyll absorption using narrow red-edge and SWIR band fusions.

```yaml
short_name: KCDSI
long_name: Kelp Canopy Density and Stress Index
formula: "(N / S1) * ((RE1 - R) / (RE1 + R))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: vegetation
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 22: OWSI (Oil Spill Weathering Stage Index)

> **Description**: Classifies marine crude oil spill weathering stages based on polymer volatility index division.

```yaml
short_name: OWSI
long_name: Oil Spill Weathering Stage Index
formula: "((S2 - S1) / (S2 + S1)) / ((B + G) / (N + S1) + 0.01)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: water
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 23: CD_UAI (Coastal Dredging & Marine Siltation Plume Index)

> **Description**: Isolates dredge plumes and marine siltation from standard turbidity by mapping sediment green reflectance.

```yaml
short_name: CD_UAI
long_name: Coastal Dredging & Marine Siltation Plume Index
formula: "((G - B) / (G + B)) * ((G - R) / (G + R))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: water
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 24: MP_PDI (Marine Plastisphere & Polymer Differentiation Index)

> **Description**: Fuses Floating Debris Index NIR enhancements with active chlorophyll-a and sea foam rejection gates.

```yaml
short_name: MP_PDI
long_name: Marine Plastisphere & Polymer Differentiation Index
formula: "(N - S1) / (G + S1)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: water
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 25: RDOCI (River Dissolved Organic Carbon Index)

> **Description**: Measures the steep exponential UV absorption slope of dissolved organic carbon using OCI deep UV bands.

```yaml
short_name: RDOCI
long_name: River Dissolved Organic Carbon Index
formula: "ln(A / B) / 92 * (-1.0)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: water
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 26: CTPSTI (Cyanobacterial Toxin Proxy Spectral Index)

> **Description**: Hyperspectral proxy mapping cyanobacteria phycocyanin pigment absorption at 620 nm.

```yaml
short_name: CTPSTI
long_name: Cyanobacterial Toxin Proxy Spectral Index
formula: "(G - RE1) / (G + RE1)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: water
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 27: NPDefI (Nitrogen vs. Phosphorus Deficiency Discrimination Index)

> **Description**: Signed macro-nutrient deficiency discriminator: positive maps Nitrogen deficiency, negative maps Phosphorus deficiency.

```yaml
short_name: NPDefI
long_name: Nitrogen vs. Phosphorus Deficiency Discrimination Index
formula: "((R - RE1) / (R + RE1)) - ((S2 - S1) / (S2 + S1))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: vegetation
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 28: SCSPI (Soil Compaction Spectral Proxy Index)

> **Description**: Flags structural compaction in bare agricultural soils based on SWIR mineral line deviations.

```yaml
short_name: SCSPI
long_name: Soil Compaction Spectral Proxy Index
formula: "(1.0 - (S1 / S2)) * (G / B)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 29: PDSDI (Pesticide vs. Drought Stress Discrimination Index)

> **Description**: Discriminates localized pesticide necrosis (high spatial variance) from uniform regional drought stress.

```yaml
short_name: PDSDI
long_name: Pesticide vs. Drought Stress Discrimination Index
formula: "CV_NDVI / ((RE1 - R) / (RE1 + R))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: vegetation
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 30: AMDPHI (Acid Mine Drainage pH Proxy Index)

> **Description**: Translates pH-dependent iron mineral precipitate assemblages (jarosite vs. goethite) to a pH acidity range.

```yaml
short_name: AMDPHI
long_name: Acid Mine Drainage pH Proxy Index
formula: "((R - G) / (R + G)) / ((B - G) / (B + G + 0.001))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: water
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 31: CCRBI (Coal Combustion Residue Bioaccumulation Index)

> **Description**: Detects heavy metal bioaccumulation (As/Se) stress in crop canopies over coal ash landfills.

```yaml
short_name: CCRBI
long_name: Coal Combustion Residue Bioaccumulation Index
formula: "((R - N) / (R + N)) * (G / (S1 + 0.01))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: vegetation
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 32: SPSRI (Solar Panel Soiling Remote Index)

> **Description**: Utility-scale photovoltaic soiling assessment mapping dust deposition albedo decay.

```yaml
short_name: SPSRI
long_name: Solar Panel Soiling Remote Index
formula: "((B - B_clean) / B_clean) * (S1 / S2)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: urban
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 33: PCADI (Pavement Condition and Albedo Decay Index)

> **Description**: Maps urban asphalt albedo degradation and structural aging within road masks.

```yaml
short_name: PCADI
long_name: Pavement Condition and Albedo Decay Index
formula: "(G / B) - 1.0 + ((N - R) / (N + R)) * 5.0"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: urban
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 34: TPERI (Thermokarst Pond Expansion Rate Index)

> **Description**: Tracks the bi-temporal saturation and slumping transition slope of expanding thermokarst ponds.

```yaml
short_name: TPERI
long_name: Thermokarst Pond Expansion Rate Index
formula: "(S1_t1 - S1_t2) / (G_t1 - G_t2)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 35: PCEI (Peat Carbon Exposure Index)

> **Description**: Isolates exposed dark peat soils lacking vegetation or water to feed carbon oxidation models.

```yaml
short_name: PCEI
long_name: Peat Carbon Exposure Index
formula: "(1.0 - (N - R) / (N + R)) * S2 * (1.0 - ((G - N) / (G + N)))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 36: SABSI (Snow/Ice Algae Bloom Severity Index)

> **Description**: Maps severity and distribution of cryospheric algae blooms on glaciers and snowpacks.

```yaml
short_name: SABSI
long_name: Snow/Ice Algae Bloom Severity Index
formula: "((R - N) / (R + N)) + 0.5 * ((B - G) / (B + G))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: snow
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 37: MEPSI (CH4 Ebullition Pond Spectral Proxy Index)

> **Description**: Identifies shallow, sediment-rich water columns prone to active benthic methane ebullition.

```yaml
short_name: MEPSI
long_name: CH4 Ebullition Pond Spectral Proxy Index
formula: "(N / B) - ((G - N) / (G + N))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: water
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 38: ALSI (Active Layer Depth Thermal-Spectral Index)

> **Description**: Scalable satellite ALT proxy coupling summer thermal anomalies with SWIR frost-churning clay exposure.

```yaml
short_name: ALSI
long_name: Active Layer Depth Thermal-Spectral Index
formula: "0.6 * T1_anomaly + 0.4 * ((S2 - S1) / (S2 + S1))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 39: PDCSI (Pre-Deforestation Canopy Stress Index)

> **Description**: Detects early-stage tropical canopy thinning and stress months before clear-cutting occurs.

```yaml
short_name: PDCSI
long_name: Pre-Deforestation Canopy Stress Index
formula: "((RE2 - RE1) / (RE2 + RE1)) - ((RE4 - N) / (RE4 + N))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: vegetation
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 40: LISI (Liana Infestation Structural Index)

> **Description**: Maps liana canopy infestation density using coupled structural and moisture indexes.

```yaml
short_name: LISI
long_name: Liana Infestation Structural Index
formula: "2.5 * ((N - S1) / (N + 6.0 * R - 7.5 * B + 1.0)) * (N / S1)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: vegetation
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 41: UBCDI (Understory vs. Canopy Burn Discrimination Index)

> **Description**: Isolates tropical understory surface fires beneath intact green forest canopies.

```yaml
short_name: UBCDI
long_name: Understory vs. Canopy Burn Discrimination Index
formula: "((N_post - N_pre) / N_pre) / ((R_post - R_pre) / R_pre)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: burn
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 42: SLSDI (Selective Logging Scar Detection Index)

> **Description**: Maps small structural canopy gaps and bare soil exposure driven by selective logging.

```yaml
short_name: SLSDI
long_name: Selective Logging Scar Detection Index
formula: "((B + G) / (N + 0.01)) * (S2 / (S2 + RE4))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: vegetation
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 43: PWTDI (Peatland Water Table Depth Index)

> **Description**: Fuses Sphagnum leaf tissue moisture (970 nm) with Sentinel-1 cross-polarization backscatter for sub-surface water table monitoring.

```yaml
short_name: PWTDI
long_name: Peatland Water Table Depth Index
formula: "0.65 * ((RE4 - B9) / (RE4 + B9)) + 0.35 * (VV - VH)"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: radar
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 44: TFIDI (Tidal Flat Inundation Dynamics Index)

> **Description**: Maps coastal tidal flat inundation ranges using temporal water index percentiles.

```yaml
short_name: TFIDI
long_name: Tidal Flat Inundation Dynamics Index
formula: "(NDWI_p90 - NDWI_p10) / NDWI_mean"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: water
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 45: WDPTZI (Wet-Dry Peatland Transition Zone Index)

> **Description**: Isolates the boundaries of peatland transition zones using SWIR/NIR spatial gradients.

```yaml
short_name: WDPTZI
long_name: Wet-Dry Peatland Transition Zone Index
formula: "spatial_gradient((S1 - RE4) / (S1 + RE4))"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: soil
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---

## Index 46: IPVSI (Invasive Phragmites vs. Native Vegetation)

> **Description**: Discriminates dense, structural invasive Phragmites monocultures from native marsh vegetation.

```yaml
short_name: IPVSI
long_name: Invasive Phragmites vs. Native Vegetation
formula: "((S1 - N) / (S1 + N)) * texture"
reference: "https://github.com/globe-and-atlas/remote-sensing-research"
type: vegetation
date_of_addition: "2026-05-26"
contributor: "https://github.com/danielbally"
```

---