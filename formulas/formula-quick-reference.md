---
title: "Formula Quick Reference — All Spectral Indices"
last_updated: 2026-05-25
total: 150+
sources: [limn, civic-sentinel, permian-basin-survey, global-novel-survey]
---

# Formula Quick Reference

Every formula across all projects in one place. Grouped by domain. Formulas use Sentinel-2 band notation unless noted.

**Band key (Sentinel-2):** B01=443 nm, B02=490 nm, B03=560 nm, B04=665 nm, B05=705 nm, B06=740 nm, B07=783 nm, B08=842 nm, B8A=865 nm, B09=945 nm, B11=1610 nm, B12=2190 nm

---

## 1. Standard Baselines (Tier 0 — No Claim)

| Acronym | Formula | Purpose |
|---------|---------|---------|
| NDVI | `(B08 - B04) / (B08 + B04)` | Vegetation density |
| NDWI | `(B03 - B08) / (B03 + B08)` | Surface water |
| NDMI | `(B08 - B11) / (B08 + B11)` | Soil/canopy moisture |
| SAVI | `1.5 * (B08 - B04) / (B08 + B04 + 0.5)` | Vegetation, soil-corrected |
| MSI | `B11 / B08` | Moisture stress |
| BSI | `((B11 + B04) - (B08 + B02)) / ((B11 + B04) + (B08 + B02))` | Bare soil |
| NDSI | `(B08 - B11) / (B08 + B11)` | Salt surface |
| SI | `sqrt(B02 * B04)` | General salinity |
| HCAI | `(B11 - B12) / (B11 + B12)` | Hydrocarbon SWIR shoulder |
| HMRI | `(B03 - B02) / (B03 + B02)` | Heavy metal reflectance shift |
| NDOI | `(B03 - B11) / (B03 + B11)` | Oil slick |
| AOI | `(B04 - B02) / (B04 + B02)` | Fe³⁺ / anoxic iron oxidation |
| CRSI | `(B08 - B04) / (B08 + B04)` | Chloride root stress (NDVI-derived) |
| NBR | `(B08 - B12) / (B08 + B12)` | Normalized Burn Ratio |
| dNBR | `NBR_pre - NBR_post` | Burn severity change |

---

## 2. Limn — Produced Water / Permian Basin

### Active Brine & Chemistry

| Acronym | Formula Concept | Bands | Detection |
|---------|----------------|-------|-----------|
| **PWCI** | `NDSI^3 * HCAI * HMRI` (cubic three-gate AND) | B02–B12 | 81.5% |
| **ASAI** | `max(NDSI_dry, NDWI_specular) * (1 - NDVI)` | B03, B11, B12 | 77.8% |
| **LBI** | `NDSI * adj_NDWI * (1 - NDVI) * BSI` | B03, B08, B11, B12 | 63.0% |
| **OBEC** | `optical_smoothness * NDOI * NDSI` | B02–B12 | 66.7% |
| **FBC** | `AOI * NDSI * HMRI` (iron oxidation gate) | B02–B12 | 66.7% |

### Vegetation Stress

| Acronym | Formula Concept | Bands | Detection |
|---------|----------------|-------|-----------|
| **VSI** | `(B8A - B07) / (B8A + B07) - (B07 - B05) / (B07 + B05)` | B05, B07, B8A, B11 | 74.1% |
| **VCBI** | `NDSI * (1 - NDVI_normalized)` | B04, B08, B11, B12 | — |
| **REAI** | `(B06 - B05) / (B06 + B05)` | B05, B06 | — |

### Forensic / Residue

| Acronym | Formula Concept | Bands | Notes |
|---------|----------------|-------|-------|
| **TRI** | `NDSI * HMRI * AOI` (post-evaporation mineral scar) | B02–B12 | High specificity |
| **CMA** | `(B12 - B11) / (B12 + B11) * NDSI` | B02, B04, B11, B12 | Survives months post-evaporation |
| **HMI** | `HMRI * (B12 - B11) / (B12 + B11)` | B02, B03, B11, B12 | Ba/Sr precipitation |
| **EHC** | False-color: NDOI→R, BSI→G, NDSI→B | B04, B11, B12 | Evaporite halo morphology |

### Pad-Level Signals

| Acronym | Formula Concept | Bands |
|---------|----------------|-------|
| **BPI** | `BSI * HCAI * NDSI` | B04, B08, B11, B12 |
| **PHI** | `HCAI * NDSI * (1 - NDWI)` | B11, B12 |
| **SCRI** | `(VV - VH) / (VV + VH)` smooth salt surface | S1 VV, VH |

### Novel Sensor Extensions (Permian)

| Acronym | Formula | Platform |
|---------|---------|----------|
| PBMEI | `(XCH4_obs − XCH4_bg) / (FRP_VIIRS + 1)` | TROPOMI + VIIRS |
| PBSI | `(SWIR2−SWIR1)/(SWIR2+SWIR1) − NDVI` | Landsat OLI |
| PW-ATI | `(1−Albedo)/(T_day−T_night)` | Landsat TIRS |
| EMIT-BMIN | SAM distance to brine mineral endmember | EMIT |
| EMIT-HC | `(R_1730−R_1750)/(R_1730+R_1750)` | EMIT |
| PW-ETA | `ET_observed / ET_expected` | ECOSTRESS |
| FARI | `FRP_VIIRS / Well_area` | VIIRS + registry |
| EnMAP-EVI | `B_2163 / B_2211` absorption depth ratio | EnMAP |
| ASTER-GSI | `(B11−B12)/(B11+B12)` TIR ratio | ASTER TIR |
| PB-CDI | Coherence deviation from multi-year baseline | Sentinel-1 |
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

---

## 3. Civic Sentinel — Environmental / Civic Atlas

Full formulas in [`civic-sentinel-composite-atlas.md`](../catalogs/civic-sentinel-composite-atlas.md). Quick reference:

| Acronym | Key Components | Ranked Score |
|---------|---------------|-------------|
| **BH-DFSI** | `BurnGate × SoilGate × MoistureSignal × ChromaticSlopeProxy` | 10/10 |
| **PETI** | Virtual phycocyanin: `(B04 - B05) / (B04 + B05)` × turbidity gate × persistence | 9/10 |
| **MP-PDI** | `FDI_like * (1 - SargassumRejection) * (1 - VegetationRejection) * (1 - FoamRejection)` | 9/10 |
| **TT-API** | `PeatExposure * WetAnoxic * EdgeCollapse` | 9/10 |
| **CD-UAI** | `TurbidityPlume * SiltGreen * (1 - CloudMask)` | 8/10 |
| **EC-ACI** | `(1 - canopy_ET_proxy) * impervious_brightness` | 8/10 |
| **LRD-VSI** | `red_edge_stress * moisture_loss * proximity_to_landfill` | 8/10 |
| **TDR-ASI** | `jarosite_signal * sulfate_absorption * mine_proximity` | 7/10 |
| **SF-EII** | `canopy_moisture_deficit * cell_wall_collapse_proxy` | 7/10 |
| **WDA-CSI** | `nitrogen_spike * peat_drainage_signal * NDWI_loss` | 7/10 |
| **TRSI** | `turbidity_jump + ferric_shift + persistence` | 6/10 |
| **CSRC** | `NDCI * NIR_boost * (1 - turbidity) * (1 - floating_veg)` | 6/10 |
| **SWRI** | `turbidity_shock * organic_bloom * context` | 5/10 |
| **DWCI** | `upstream_contamination * watershed_flow_path` | 5/10 |
| **LFGVI** | `red_edge_stress * moisture_loss * radial_ring_pattern` | 5/10 |
| **RRFI** | `NDVI_corridor_loss * moisture_deficit` | 4/10 |
| **EPDI** | `turbidity_surge * sediment_source_proximity` | 4/10 |
| **HSAI** | `(1 - canopy_albedo) * impervious_fraction` | 3/10 |

---

## 4. Global Novel Indices — Permafrost & Arctic

| Acronym | Formula | Platform |
|---------|---------|----------|
| **TPERI** | `Δ(B11_t1 - B11_t2) / Δ(B3_t1 - B3_t2)` | S2 bi-temporal |
| **PCEI** | `(B12 - B8A) / (B12 + B8A + B5)` | S2 |
| **SABSI** | `(B4 - B8) / (B4 + B8) + 0.5 * (B2 - B3) / (B2 + B3)` | S2 |
| **FGDCI** | `(VV_dB - VH_dB) - seasonal_mean(VV_dB - VH_dB)` | S1 SAR |
| **MEPSI** | `(B8 / B2) - NDWI_local_mean` | S2 |
| **ALSI** | `0.6 * (LST_anomaly / σ_LST) + 0.4 * [(B12 - B11) / (B12 + B11)]` | ECOSTRESS + S2 |

---

## 5. Global Novel Indices — Tropical Forest

| Acronym | Formula | Platform |
|---------|---------|----------|
| **PDCSI** | `[(B6 - B5) / (B6 + B5)] - [(B8A - B8) / (B8A + B8)]` | S2 red-edge |
| **LISI** | `2.5 * [(B8 - B11) / (B8 + 6*B4 - 7.5*B2 + 1)] * (B8 / B11)` | S2 |
| **UBCDI** | `(ΔB8 / B8_pre) / (ΔB4 / B4_pre)` | S2 bi-temporal |
| **SLSDI** | `[(B2 + B3) / (B8 + 0.01)] * [B12 / (B12 + B8A)]` | S2 |
| **FEDGI** | `distance_from_edge * [-(B11 - B8) / (B11 + B8)]` | S2 + spatial |

---

## 6. Global Novel Indices — Marine & Coastal

| Acronym | Formula | Platform |
|---------|---------|----------|
| **CBSDI_pale** | `(B3 - B4) / (B3 + B4)` | S2 |
| **CBSDI_full** | `B2 / (B3 + B4 + B1)` | S2 |
| **CBSDI_dead** | `(B3 / B4) - (B2 / B4)` | S2 |
| **HABSDI_cyano** | `[(B3 - B5) / (B3 + B5)] - [(B2 - B3) / (B2 + B3)]` | PACE OCI |
| **HABSDI_diatom** | `[(B2 - B3) / (B2 + B3)] - [(B3 - B5) / (B3 + B5)]` | PACE OCI |
| **SMADI** | `FAI - [(B8A - B11) / (B8A + B11)]` | S2, EMIT |
| **KCDSI** | `(B8 / B11) * [(B5 - B4) / (B5 + B4)]` | S2 + S3 |
| **OWSI** | `[(B12 - B11) / (B12 + B11)] / [(B2 + B3) / (B8 + B11) + 0.01]` | EMIT, S2 |
| **MDSPI** | `texture(NDVI, 5×5) / mean(NDVI, 5×5)` | S2 |
| **SGDCI** | `(ρ_412 / ρ_550) - CDOM_regional_mean` | PACE + ECOSTRESS |
| **CTPSTI** | `[ρ(560nm) - ρ(620nm)] / [ρ(560nm) + ρ(620nm)]` | PACE OCI |

---

## 7. Global Novel Indices — Agriculture

| Acronym | Formula | Platform |
|---------|---------|----------|
| **NPDDI** | `[(B4 - B5) / (B4 + B5)] - [(B12 - B11) / (B12 + B11)]` | S2, EnMAP |
| **SCSPI** | `[1 - (B11 / B12)] * (B3 / B2)` | S2 bare soil |
| **APRI** | `(LST_anomaly / σ) * [1 - NDWI] * heat_accumulation_days` | ECOSTRESS + S2 + ERA5 |
| **PDSDI** | `texture_cv(NDVI, 3×3) / [(B5 - B4) / (B5 + B4)]` | S2 |
| **CCTTI** | `dNDVI/dt + (B11 / B8)` | S2 time series |
| **IWUEI** | `ET_ecostress / (VWC_sentinel1 + 0.01)` | ECOSTRESS + S1 |

---

## 8. Global Novel Indices — Mining & Industrial

| Acronym | Formula | Platform |
|---------|---------|----------|
| **AMDPHI** | `[(B4 - B3) / (B4 + B3)] / [(B2 - B3) / (B2 + B3 + 0.001)]` | S2, EMIT |
| **TDSII** | `w1 * NDWI_anomaly + w2 * (-InSAR_rate) + w3 * NDVI_decline` | S2 + S1 InSAR |
| **REESAI** | `1 - ρ(803nm) / [ρ(780nm) + (803-780)/(830-780) * (ρ(830nm) - ρ(780nm))]` | EnMAP |
| **CCRBI** | `[(B4 - B8) / (B4 + B8)] * [B3 / (B11 + 0.01)]` | S2 |
| **HLPII** | `SWIR_mineralogy_gradient / distance_from_pad_edge` | S2, EMIT |
| **IERPI** | `(B4 / B3) * (LST_pixel - LST_upstream_mean) / σ_LST` | Landsat |

---

## 9. Global Novel Indices — Wildfire

| Acronym | Formula | Platform |
|---------|---------|----------|
| **LFMPI** | `2.5 * [(B8A - B11) / (B8A + B11 + 6*B4 - 7.5*B2 + 1)] - (B12 / B11)` | S2 |
| **PSHRI** | `NDWI_post-rain - NDWI_pre-rain` (applied over confirmed rain window) | S2 + ERA5 |
| **BSMTI** | `depth(535nm) / depth(486nm)` [EMIT L2A] | EMIT |
| **SACI** | `AOD_UV340 / AOD_550` | TROPOMI |
| **PCSII** | `BT_3.7µm - BT_11µm > 0 AND AOD_TROPOMI > 1.0` | GOES + TROPOMI |

---

## 10. Global Novel Indices — Urban & Infrastructure

| Acronym | Formula | Platform |
|---------|---------|----------|
| **SPSRI** | `(ρ_B2 - ρ_clean_B2) / ρ_clean_B2 * (B11 / B12)` | S2, Planet |
| **UCIEI** | `(1 - albedo_sat) * LST_anomaly` | S2 + ECOSTRESS |
| **PCADI** | `(B3 / B2) - 1 + NDVI * 5` [within road mask] | S2, WorldView |
| **CSDEI** | `AOD_550 * (1 / α_TROPOMI) * site_mask` | TROPOMI + GIS |

---

## 11. Global Novel Indices — Water Quality & Freshwater

| Acronym | Formula | Platform |
|---------|---------|----------|
| **RDOCI** | `ln(ρ_320nm / ρ_412nm) / (412 - 320) * (-1)` | PACE OCI |
| **DTPSI** | `(LST_downstream_1km - LST_reservoir) / (LST_upstream_1km - LST_reservoir)` | Landsat TIRS |
| **GMCPI** | `(B1 - B3) / (B1 + B3) - CDOM_background` | S2, PACE |
| **FCLI** | `(B12_post-flood - B12_pre-flood) * (1 - NDVI_next-season)` | S2 bi-temporal |

---

## 12. Global Novel Indices — Dryland & Arid

| Acronym | Formula | Platform |
|---------|---------|----------|
| **BSCMCI** | `[(ρ680 - ρ720) / (ρ680 + ρ720)] * [(ρ550 / ρ670) - 1]` | PRISMA, DESIS |
| **SBCI** | `depth(2217nm) / depth(2175nm)` | EMIT |
| **CSCAI** | `depth(2335nm) / depth(2160nm)` | EnMAP |
| **DEFPI** | `(1 - NDVI) * clay_fraction_EMIT * (1 - SMC_SMAP)` | EMIT + S2 + SMAP |
| **DLPEHI** | `NDWI * (0.1 < NDVI < 0.3) * (NDTI > -0.2) * rainfall_binary` | S2 + GPM |
| **AIBEAI** | `BSI_channel_bottom / NDVI_channel_margin` | S2, Planet |

---

## 13. Global Novel Indices — Wetland & Peatland

| Acronym | Formula | Platform |
|---------|---------|----------|
| **PWTDI** | `0.65 * (B8A - B9) / (B8A + B9) + 0.35 * (VV_dB - VH_dB)` | S2 + S1 |
| **MHSSP** | `NDWI * (1 - NDVI) * (1 - CI_rededge / max_CI_rededge)` | S2 + TROPOMI |
| **TFIDI** | `(NDWI_p90 - NDWI_p10) / NDWI_mean` [monthly composite] | S2 |
| **WDPTZI** | `spatial_gradient_magnitude[(B11 - B8A) / (B11 + B8A)]` | S2 |
| **IPVSI** | `(B11_late - B8_late) / (B11_late + B8_late) * texture_homogeneity` | S2 seasonal |

---

## 14. Hyperspectral-Only Indices (EMIT, EnMAP, PRISMA, PACE)

| Acronym | Formula | Platform |
|---------|---------|----------|
| **CMSTI** | `position_minimum(2190-2220nm) - 2200` | EMIT only |
| **MPSSFI** | `1 - ρ(1667nm) / [0.5 * (ρ(1640nm) + ρ(1700nm))]` | EMIT |
| **AFCDI** | `depth(2317nm) / depth(2387nm)` | EMIT, PRISMA |
| **SCFGOSI** | `depth(1730nm) / (1 - mean_reflectance_400_2500nm)` | EMIT, EnMAP |
| **REENBI** | `1 - ρ(803nm) / linear_continuum(780nm, 830nm)` | EnMAP |
| **EPCASE** | `position_minimum(2190-2220nm) + depth(2325nm) / depth(2200nm)` | EnMAP |
| **DPCCI** | `(ρ550 + ρ650) / ρ620 - 2` | DESIS, PACE |
| **PFTIB_diatom** | `absorption(490nm) / absorption(440nm)` | PACE OCI |
| **PFTIB_hapto** | `absorption(453nm) / absorption(490nm)` | PACE OCI |
| **PFTIB_prokary** | `ρ(490nm) / ρ(440nm)` | PACE OCI |
| **PFTIB_crypto** | `absorption(565nm) / absorption(490nm)` | PACE OCI |

---

## 15. Cross-Sensor Fusion Indices

| Acronym | Formula | Platforms |
|---------|---------|-----------|
| **TSEAI** | `XCH4_anomaly / Σ(source_fraction_i * emission_factor_i)` | TROPOMI + S2 |
| **ISSAI** | `(ICESat2_dZ/dt - InSAR_LOS_vertical) / ICESat2_dZ/dt` | ICESat-2 + S1 + S2 |
| **GEAWSI** | `(ET_ecostress / PET_estimate) * TWS_anomaly_sign` | ECOSTRESS + GRACE-FO + ERA5 |
| **EMSMMI** | `VWC_S1_raw / (1 + clay_fraction_EMIT * clay_dielectric_correction)` | EMIT + S1 |
| **NFCAI** | `L-band_HV * (1 - canopy_cover_S2) + HH * age_proxy_NDVI_trend` | NISAR + S2 |
| **SNUVQI** | `NO2_TROPOMI_downscaled - f(NDVI_S2, wind_ERA5)` | TROPOMI + S2 + ERA5 |
| **PUENPI** | `GPP_ECOSTRESS - NPP_PACE_aquatic - R_temperature_model` | PACE + ECOSTRESS + ERA5 |
| **LBSMI** | `(L_VV − S_VV) / (L_VV + S_VV)` | NISAR (L + S band) |

---

## Count Summary

| Section | Index Count |
|---------|-------------|
| Standard baselines (Tier 0) | 15 |
| Limn Permian Basin composites (optical) | 15 |
| Limn Permian Basin novel sensor extensions | 20 |
| Limn Environmental / Civic Atlas (Tier 2) | 19 |
| Civic Sentinel ranked composites | 18 |
| Global novel — Permafrost | 6 |
| Global novel — Tropical Forest | 5 |
| Global novel — Marine & Coastal | 11 |
| Global novel — Agriculture | 6 |
| Global novel — Mining & Industrial | 6 |
| Global novel — Wildfire | 5 |
| Global novel — Urban | 4 |
| Global novel — Water Quality | 4 |
| Global novel — Dryland | 6 |
| Global novel — Wetland & Peatland | 5 |
| Hyperspectral-only | 11 |
| Cross-sensor fusion | 8 |
| **TOTAL** | **~164** |

---

*Quick reference only — full spectral physics, citations, and claim language in the survey documents under `../surveys/` and `../catalogs/`.*
