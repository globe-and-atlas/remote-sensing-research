# The Global Spectral Index Atlas: A Systematic Framework of Novel Spectral Indices for Environmental Monitoring Across Thirteen Domains

**Daniel Bally**  
Globe & Atlas, Spring, Texas, USA  
Correspondence: dbally@gmail.com

*Preprint submitted to ESSOAr and arXiv — May 2026*

---

## Abstract

The proliferation of free, high-resolution satellite data — led by the Sentinel constellation, EMIT, PACE OCI, and a wave of 2019–2024 sensor launches — has created an untapped detection opportunity: the spectral physics to identify environmental hazards from orbit is documented in the literature, but no organized, named index registry exists beyond vegetation and general water-body estimation. We introduce the Global Spectral Index Atlas (GSIA), a systematic compilation of 91 novel spectral indices spanning 12 environmental domains: wildfire, freshwater quality, marine and coastal systems, agriculture, mining, urban infrastructure, permafrost, tropical forest, dryland, wetland, hyperspectral-enabled detection, and cross-sensor fusion. Indices are classified under a three-tier novelty taxonomy distinguishing (T1) first-formula proposals — detection problems with no equivalent standardized formula in the published literature — from (T2) first standardized formulations of qualitatively described concepts, and (T3) newly computable indices enabled by sensors operational since 2019. The atlas is publicly available at https://github.com/globe-and-atlas/remote-sensing-research under an open license and is intended as a community resource for triage-level environmental screening, not as a substitute for field measurement or regulatory certification.


---

## 1. Introduction

Free satellite data now covers the planet at 10-meter spatial resolution and five-day temporal repeat. The spectral physics to read environmental signals from this data — surface salinity, hydrocarbon exposure, vegetation osmotic stress, mineral composition, methane emission attribution — is documented in peer-reviewed literature. What has been missing is one organized place that names the formulas, defines the band inputs, explains the spectral mechanism, and states explicitly what each index can and cannot detect.

The existing spectral index literature is vast but fragmented. Normalized difference indices dominate the vegetation literature since Tucker (1979), and the Awesome Spectral Indices repository (Montero et al., 2023) provides a structured registry of published vegetation, water, soil, and burn indices. However, a large class of detection problems — urgent, technically feasible, and empirically grounded in physical spectroscopy — remains unaddressed by any named, standardized formula.

A parallel challenge involves sensor latency. EMIT (2022), PACE OCI (2024), EnMAP (2022), and NISAR (2024) have launched with spectral and spatial capabilities that make previously impossible detections practical. Hyperspectral mineral fingerprinting of altered soils, phycocyanin species discrimination for harmful algal bloom toxicity, and Sphagnum leaf water-content monitoring for peatland carbon accounting are now computable from open data — but no formula registry has emerged to make these capabilities accessible to the broader environmental monitoring community.

The Global Spectral Index Atlas (GSIA) addresses both gaps. It is a systematic compilation and naming of spectral indices, organized by domain, platform, and novelty tier, designed to function as a public-good reference that researchers, regulators, and environmental practitioners can use, extend, and validate. This paper introduces the atlas structure and novelty taxonomy, and surveys the twelve domains.


---

## 2. The Global Spectral Index Atlas: Structure and Taxonomy

### 2.1 Scope

The GSIA v1.0 (May 2026) contains 91 named indices across 12 environmental domains (Table 1). Each entry specifies: a short acronym, a full name, the spectral formula using standardized Sentinel-2 band notation (B01–B12, B8A) or equivalent sensor-specific notation, the physical mechanism targeted, the satellite platform(s) required, and a limit clause stating what the index does not detect. To avoid redundancy and maintain a sharp focus on under-addressed environmental hazards, the GSIA explicitly excludes long-established, standard index families (such as NDVI, NDWI, NBR, and NDSI) that are already comprehensively documented and cataloged in community libraries (e.g., Montero et al., 2023).


Index coverage spans three classes of sensor: (1) multispectral indices computable from Sentinel-2, Sentinel-1, Landsat-9, GOES ABI, ECOSTRESS, or TROPOMI; (2) hyperspectral indices requiring EMIT, PACE OCI, EnMAP, DESIS, or PRISMA; and (3) cross-sensor fusion indices that combine signals from multiple platforms in a single expression.

**Table 1. Domain coverage in the Global Spectral Index Atlas v1.0.**

| Domain | Count | Tier Mix | Primary Platform(s) |
|--------|-------|----------|---------------------|
| Wildfire | 7 | T1/T2 | S2, TROPOMI, EMIT, GOES |
| Freshwater Quality | 11 | T1/T2 | S2, PACE OCI, Landsat-9 |
| Marine & Coastal | 12 | T1/T2 | S2, PACE, EMIT, PRISMA |
| Agriculture & Food Security | 7 | T1/T2 | S2, EnMAP, ECOSTRESS, ERA5 |
| Mining & Industrial | 8 | T1/T2 | S2, EMIT, EnMAP, Landsat |
| Urban & Infrastructure | 8 | T1/T2 | S2, ECOSTRESS, TROPOMI |
| Permafrost & Arctic | 7 | T1/T2 | S2, S1, ECOSTRESS |
| Tropical Forest | 6 | T1/T2 | S2, Planet |
| Dryland & Arid | 6 | T1 | S2, EMIT, EnMAP, SMAP |
| Wetland & Peatland | 6 | T1/T2 | S2, S1 |
| Hyperspectral-Enabled | 8 | T1/T2 | EMIT, EnMAP, DESIS, PACE |
| Cross-Sensor Fusion | 7 | T1/T3 | Multiple |

### 2.2 Novelty Tier Taxonomy

Spectral indices differ in the type and degree of novelty they represent. The GSIA introduces a three-tier taxonomy to make this distinction explicit and to calibrate appropriate validation expectations for users.

**T1 — First formula.** The detection problem is recognized, the physical spectral mechanism has been described in the literature, but no named, standardized formula with defined band inputs has been published as of May 2026. T1 entries propose the first formula. They are testable scientific hypotheses, not validated products, unless empirical evidence is explicitly noted. The majority of GSIA indices are T1.

**T2 — First standardized formula.** The detection concept appears in peer-reviewed literature, sometimes with quantitative spectral rationale, but only as a qualitative description without a named acronym or defined band inputs. T2 entries write that formula explicitly, enabling reproducibility and direct computation from satellite archives. The underlying spectral physics is inherited from cited prior work; the contribution is formalization.

**T3 — Newly computable.** The spectral physics and formula structure have been published, but the sensor required to compute the formula only became operationally available between 2019 and 2024. These indices are not novel in concept; they are novel in that they can now be computed from open satellite data for the first time.

T1 entries carry the highest novelty claim and the highest validation burden. T2 entries inherit spectral physics credibility from prior work. T3 entries can leverage existing validation literature for their underlying physics.

### 2.3 Limit Clauses

Every index in the atlas carries an explicit limit clause — a statement of what the index cannot confirm. This is not ancillary; it is the scientific boundary condition separating a defensible screening tool from an overclaim. Users of GSIA indices should cite the relevant limit clause alongside any reported detections. As a representative example, the VSI limit clause reads: *"VSI cannot confirm the exact physiological cause of vegetation stress (e.g. distinguishing brine osmotic stress from extreme drought, soil compaction, or pesticide exposure) or subsurface migration pathways. It is a sub-lethal screening indicator, not a substitute for field inspection, crop health assessments, or regulatory testing."*

---

## 3. Domain Survey

Space permits only brief characterization of the remaining twelve domains. Full formulas, physical mechanisms, and limit clauses for all 91 indices are available in the public repository.


**Wildfire.** BH-DFSI (Burnt Hillside Debris-Flow Susceptibility Index) targets pre-event evacuation triage for communities below burned watersheds by requiring simultaneous expression of severe char severity, complete canopy loss, soil moisture loading, and a terrain-proxy chromatic signal — all four must exceed threshold to fire (T1). SF-EII (Wildfire Fuel Hazard & Canopy Dehydration Index) combines SWIR1 canopy water content with a cell-wall structural integrity ratio for pre-fire ignition risk mapping (T1). SACI (Smoke Aerosol Composition Index) uses TROPOMI UV/visible AOD ratio to discriminate smoldering from flaming combustion for real-time public health advisory support (T1).

**Freshwater Quality.** RDOCI (River Dissolved Organic Carbon Index) approximates the CDOM spectral slope coefficient S₂₇₅₋₂₉₅ from PACE OCI UV channels — enabled by the 320 nm channel unavailable on prior ocean color sensors (T1). CTPSTI uses PACE OCI's 560/620 nm ratio to discriminate microcystin-producing *Microcystis* (phycocyanin-dominant) from non-toxic *Aphanizomenon* (phycoerythrin-shifted spectrum), transforming HAB detection from biomass to toxin-risk species classification (T1).

**Mining.** AMDPHI (Acid Mine Drainage pH Proxy Index) encodes the pH-diagnostic iron mineral precipitate assemblage — jarosite (pH 2–3.5), schwertmannite (pH 3–4.5), goethite (pH 4.5–6) — in a Sentinel-2 red/green to blue/green ratio. TDSII (Tailings Dam Structural Integrity Index) fuses downstream NDWI anomaly, InSAR LOS subsidence rate, and NDVI decline rate into a three-precursor early warning formulation applicable to the 14,000+ operational tailings dams globally (T1).

**Permafrost and Wetlands.** PWTDI (Peatland Water Table Depth Index) fuses Sentinel-2 Sphagnum leaf tissue moisture (970 nm absorption) with Sentinel-1 C-band cross-polarization backscatter (VV - VH), providing a cloud-resilient orbital proxy for sub-surface water table depth (T2). FGDCI (Frozen Ground Dielectric Change Index) leverages Sentinel-1 C-band backscatter dielectric sensitivity (phase transition from ice dielectric ~4 to thawed water dielectric ~20–30) to map Arctic freeze-thaw soil states cloud-independently (T1). TPERI (Thermokarst Pond Expansion Rate Index) tracks bi-temporal green/SWIR ratios to map sub-pixel peat erosion expansion velocity (T1).

**Hyperspectral-Enabled.** CMSTI (Clay Mineral Stress Transition Index) targets the 8 nm Al-OH absorption wavelength shift between smectite (2200 nm) and illite (2208 nm) — invisible to Sentinel-2's 20 nm SWIR bands, resolved by EMIT's 5 nm sampling. This shift marks irreversible soil degradation taking centuries to reverse (T1). AFCDI (Asbestos Fiber Chrysotile Detection Index) discriminates chrysotile from antigorite and lizardite using the Mg-OH doublet separation at 2317/2387 nm — a 70 nm difference resolved by EMIT's spectral sampling (T1). REENBI (REE Neodymium Band Depth Index) encodes the Nd³⁺ f-f electronic transition absorption at 803 nm for satellite-first rare earth element deposit screening from EnMAP (T1).

**Cross-Sensor Fusion.** TSEAI (TROPOMI–Sentinel-2 Emission Attribution Index) addresses the methane source attribution problem: by computing emission source-type fractions within each 5.5 × 7 km TROPOMI pixel from Sentinel-2 land cover classification, the index identifies the fraction of observed XCH₄ enhancement not explained by known source types, flagging unaccounted emitters (T1). NFCAI (NISAR+Sentinel-2 Forest Carbon Accumulation Index) uses NISAR L-band HV backscatter for woody volume estimation fused with NDVI time-series stand age proxy — classified T3 because NISAR's 24 cm L-band wavelength makes this the first global 10 m forest carbon monitoring capability (T3).

---

## 4. Discussion

### 5.1 What the Atlas Is Not

The GSIA is a registry of named, physically grounded spectral formulas. The majority of indices are proposed formulas based on published spectral physics; independent field validation has not been completed for most of them. T1 and T2 indices should be treated as testable hypotheses, not calibrated detection products, until validation is documented.

Cross-sensor fusion indices present additional operational complexity: temporal co-registration of sensors with different orbital repeat cycles, spatial resolutions, and atmospheric correction pipelines introduces artifacts not captured by the formula alone. Platform-specific preprocessing steps (atmospheric correction quality, geometric co-registration) substantially affect index performance and are not addressed by index formulas.

The atlas does not address scene-specific thresholding, atmospheric correction methodology, shadow detection, or spatial masking. Users working in regions with heavy dust loading (relevant to dryland and agricultural optical indices), persistent cloud cover (tropical forest indices), or specularly reflective water surfaces (coastal indices) should apply caution and validate locally.

### 5.2 The Novelty Tier as a Scientific Contribution

The T1/T2/T3 taxonomy proposed here is, to our knowledge, the first formal attempt to classify spectral index novelty systematically across environmental domains. The existing literature distinguishes empirically derived indices from physically based indices (Delegido et al., 2011; Verrelst et al., 2019), but not by type of formalization novelty. The taxonomy is designed to let users calibrate citation and validation expectations: a T1 index carries a "first formula" claim requiring independent validation; a T2 index inherits spectral physics credibility from cited prior work but still requires formula-level testing; a T3 index can leverage existing physics validation literature but requires commissioning-era data.

For the priority claim implicit in T1 designation: T1 status is asserted as of the date of this preprint (May 2026). Priority can be contested by any publication predating this work that contains an equivalent named formula and band inputs for the same detection purpose. We explicitly invite such corrections. To prevent naming collisions in community registries (such as the Awesome Spectral Indices catalogue), all acronyms in this atlas underwent a systematic validation audit against global remote sensing databases. This audit resulted in key renamings to resolve overlaps—specifically renaming the marine Sargassum/microplastic index from SMADI to SMPDI to prevent conflict with the Soil Moisture Agricultural Drought Index, and renaming the agricultural nutrient index from NPDDI to NPDefI to avoid conflict with the atmospheric cloud-masking Normalized Polarization Degree Difference Index.

### 5.3 Open Research Questions

Key validation questions arising from this atlas:

1. What scene-specific detection thresholds — optimized by vegetation type, soil background, and image acquisition geometry — maximize precision-recall for the agricultural and dryland indices?
2. How do EMIT-based hyperspectral indices (CMSTI, AFCDI, REENBI) generalize from EMIT's 60 m spatial footprint to finer-scale field observations?
3. Can the Peatland Water Table Depth Index (PWTDI) provide skill scores comparable to field WTD logger networks for carbon accounting applications?
4. Do T2 water quality indices (CSRC, SWRI) generalize across bloom types, turbidity regimes, and geographic regions, or do they require region-specific calibration?

---

## 5. Conclusion

The Global Spectral Index Atlas v1.0 introduces 91 novel spectral indices across 12 environmental domains, organized under a three-tier novelty taxonomy that distinguishes first-formula proposals from first standardized formulations and newly computable sensor-enabled indices.

The atlas is a starting point, not a finished product. The primary contribution is the naming and formulating of detection problems for which the spectral physics exists but a standardized formula did not. Independent validation, threshold calibration, and cross-regional testing are needed before operational deployment of any index in a regulatory context.

The atlas is publicly available at https://github.com/globe-and-atlas/remote-sensing-research under an open license. Contributions, validations, corrections, and additions are welcomed. For indices that have passed independent validation, submission to the Awesome Spectral Indices registry (Montero et al., 2023) is encouraged to accelerate community adoption.

---

## Data Availability

All index formulas, physical descriptions, and limit clauses are available in the project repository at https://github.com/globe-and-atlas/remote-sensing-research, archived under DOI: [10.5281/zenodo.20400744](https://doi.org/10.5281/zenodo.20400744). Sentinel-2 data was accessed through the Copernicus Open Access Hub (https://scihub.copernicus.eu). EMIT data can be accessed through the NASA DAAC at https://lpdaac.usgs.gov.


---

## Author Contributions

D.B. conceived the novelty tier taxonomy, authored all index formulas, and wrote the manuscript.

---

## Competing Interests

The author declares no competing interests.

---

## References

Delegido, J., Verrelst, J., Alonso, L., & Moreno, J. (2011). Evaluation of Sentinel-2 red-edge bands for empirical estimation of green LAI and chlorophyll content. *Sensors*, 11(7), 7063–7081.

Drusch, M., Del Bello, U., Carlier, S., Colin, O., Fernandez, V., Gascon, F., ... & Bargellini, P. (2012). Sentinel-2: ESA's optical high-resolution mission for GMES operational services. *Remote Sensing of Environment*, 120, 25–36.

Gao, B. C. (1996). NDWI — A normalized difference water index for remote sensing of vegetation liquid water from space. *Remote Sensing of Environment*, 58(3), 257–266.

Green, R. O., Mahowald, N. M., Ung, C., Thompson, D. R., Bator, L., Bennie, R. L., ... & Yokota, T. (2023). The Earth Surface Mineral Dust Source Investigation: An Earth Science Imaging Spectroscopy Mission. *Bulletin of the American Meteorological Society*, in press.

Kondash, A. J., Lauer, N. E., & Vengosh, A. (2018). The intensification of the water footprint of hydraulic fracturing. *Science Advances*, 4(8), eaar5982.

Montero, D., Aybar, C., Mahecha, M. D., Martinuzzi, F., Söchting, M., & Wieneke, S. (2023). A standardized catalogue of spectral indices to advance the use of remote sensing in Earth system research. *Scientific Data*, 10, 197.

Torres, R., Snoeij, P., Geudtner, D., Bibby, D., Davidson, M., Attema, E., ... & Rostan, F. (2012). GMES Sentinel-1 mission. *Remote Sensing of Environment*, 120, 9–24.

Tucker, C. J. (1979). Red and photographic infrared linear combinations for monitoring vegetation. *Remote Sensing of Environment*, 8(2), 127–150.

Verrelst, J., Malenovský, Z., Van der Tol, C., Camps-Valls, G., Gastellu-Etchegorry, J. P., Lewis, P., ... & Moreno, J. (2019). Quantifying vegetation biophysical variables from imaging spectroscopy data: A review on retrieval methods. *Surveys in Geophysics*, 40(3), 589–629.

Zhang, Y., Gautam, R., Pandey, S., Omara, M., Maasakkers, J. D., Sadavarte, P., ... & Zavala-Araiza, D. (2020). Quantifying methane emissions from the largest oil-producing basin in the United States from space. *Science Advances*, 6(17), eaaz5120.

---

*Preprint version 1.0 — May 2026. Not yet peer reviewed.*  
*© 2026 Daniel Bally / Globe & Atlas — Licensed under CC BY 4.0*