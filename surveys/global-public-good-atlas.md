---
title: "The Global Public-Good Atlas of Satellite Band Combinations"
pillar: tool-critic
status: research-vault
origin_project: limn
tags: [remote-sensing, spectral-indices, satellite, public-good, environmental-monitoring, hyperspectral, sentinel-2, landsat, emit, pace]
date_researched: 2026-05-25
slug: global-public-good-band-combinations
---

# Research Vault: Global Public-Good Satellite Band Combinations

> **For article and prototype use.** This expands the Permian Basin sensor survey into a global research map: where public satellite bands can be recombined into helpful, testable signals for environmental health, climate accountability, food security, water quality, disaster response, and human welfare.
>
> **Scientific guardrail:** this document does not claim a new discovery as proven. It identifies claim-space: combinations that are established, adaptations of known literature into a new public-good workflow, or hypotheses that need field validation.

---

## The Core Claim

Most public satellite monitoring still lives inside a small handful of familiar indices: NDVI, NDWI, NBR, NDBI, NDSI. That is understandable. They are easy, stable, and portable.

But the public sensor stack is no longer just red, green, blue, and NIR.

Sentinel-2 adds three red-edge bands at 705, 740, and 783 nm. Landsat 8/9 adds stable SWIR and thermal continuity. Sentinel-3 OLCI and PACE OCI open ocean-color style reasoning to inland water and coastal health. EMIT, EnMAP, and PRISMA make imaging spectroscopy public enough to search for mineral, hydrocarbon, methane, and vegetation chemistry signals. Sentinel-1, NISAR, SMAP, and other microwave missions add structure, moisture, and deformation.

The opportunity is not "invent 100 more acronyms." The opportunity is to publish a useful public-good atlas of **what physical signal each band combination is trying to isolate**, where it is already supported by literature, and where the next honest experiment should happen.

---

## Claim Status Key

| Status | Meaning | Publication posture |
|---|---|---|
| **Established** | Similar band math or spectral method is already widely used in the literature. | Use as baseline or public explainer. |
| **Adaptation** | Known spectral physics, sensor capability, or index family applied to a new public-good monitoring workflow. | Claim "new application/workflow", not new physics. |
| **Hypothesis** | Plausible spectral rationale but needs validation against field data, lab spectra, or labeled events. | Claim as experiment only. |

---

## High-Confidence Public-Good Shortlist

These are the best candidates to prototype first because the physics is strong, the data is public, and the social value is clear.

| Priority | Candidate | Target signal | Why it matters |
|---|---|---|---|
| 1 | **CyanoRE-705** | Cyanobacteria and harmful algal blooms in small lakes | Public health warnings where field sampling is sparse. |
| 2 | **Plastic-FDI+SWIR** | Floating plastic/debris patches | Coastal cleanup, disaster debris, river outflow monitoring. |
| 3 | **MineDrain-Jarosite** | Acid mine drainage and exposed tailings | Downstream water risk and abandoned mine accountability. |
| 4 | **Heat-Vulnerability Albedo/TIR** | Urban surfaces that amplify heat exposure | Neighborhood-scale heat mitigation and cool-roof targeting. |
| 5 | **Drought Early-Warning RE/SWIR** | Chlorophyll decline before visible crop failure | Food security and farmer advisory systems. |
| 6 | **Snow-Darkening VIS/NIR** | Soot, dust, or algae lowering snow albedo | Water supply timing and glacier melt acceleration. |
| 7 | **Methane Plume SWIR** | Point-source methane plumes | Public greenhouse-gas accountability. |
| 8 | **Flood SAR-Optical Concordance** | Flooding under clouds or vegetation | Disaster response where optical water maps fail. |
| 9 | **Landfill Leachate Stress** | Vegetation and wetness anomalies around dumps | Environmental justice screening. |
| 10 | **Peat Drydown Fire-Risk** | Peatland drying before fire or carbon loss | Carbon protection and haze prevention. |

---

## Scholarly Synthesis: What the Literature Actually Supports

### 1. Water-quality indices are powerful but local.

The water-quality literature supports red/red-edge/NIR band ratios for chlorophyll-a, cyanobacteria, turbidity, total suspended solids, and floating algae. The catch is that optically complex inland and coastal waters do not behave like open ocean. Suspended sediment, CDOM, bottom reflectance, shallow water, sunglint, adjacency effects, and atmospheric correction can dominate the signal. That is why this vault treats water-quality combinations as **screening and prioritization tools** unless field samples or published local algorithms are available.

Practical implication: publish water candidates with calibration warnings, not universal thresholds.

### 2. Sentinel-2 red-edge is the current public workhorse for vegetation stress.

Sentinel-2's 705, 740, and 783 nm red-edge bands make it unusually useful for chlorophyll, crop stress, phenology, post-fire recovery, invasive species, and early drought work. The recurring finding across vegetation reviews is that NDVI is robust but saturates in dense vegetation, while red-edge and SWIR combinations can expose stress and water-content changes earlier or with finer discrimination.

Practical implication: the most defensible "new" vegetation claims are not brand-new physiology claims; they are workflow claims that combine red-edge, SWIR, thermal, and time-series context for decisions people already need to make.

### 3. Soil salinity is real but easy to overclaim.

Salt-affected soils can be bright in visible and SWIR wavelengths, and many salinity indices exist. But brightness is confounded by soil texture, moisture, crusting, residue, carbonate, gypsum, and vegetation cover. The salinity literature repeatedly points toward combining spectral indices with terrain, moisture, land use, and field measurements.

Practical implication: salinity candidates should be published as regional models or alert layers, not global salt maps.

### 4. Fire mapping has strong baselines.

NBR, dNBR, RdNBR, fuel moisture indices, VIIRS active fire products, and GOES ABI fire-temperature logic are well established. A new public-good contribution should beat or complement these baselines. Sentinel-2 red-edge recovery and GOES high-cadence event context are promising additions, but they should not pretend the burn-severity problem starts from zero.

Practical implication: any fire candidate must compare against NBR/dNBR and VIIRS/GOES active fire products.

### 5. Marine plastic detection is promising but not operationally simple.

The floating debris literature supports FDI-like approaches and benchmark datasets, but it also emphasizes limits: mixed debris, partial pixels, sea state, clouds, sunglint, algae, foam, wood, and sparse aggregation. Detecting "a debris-like floating target" is more defensible than detecting "plastic" without follow-up.

Practical implication: label outputs as suspected floating debris unless material class is validated.

### 6. Mining and acid drainage benefit from hyperspectral physics.

Mine drainage and tailings work is where hyperspectral public data can be genuinely different. Iron oxides, clays, sulfates, hydroxyl-bearing minerals, and evaporites have diagnostic spectral features. Sentinel-2 and Landsat can screen broad alteration and turbidity patterns, but EMIT/EnMAP/PRISMA make mineral-specific claims more plausible.

Practical implication: use multispectral screening for where to look; use hyperspectral evidence for what material may be present.

### 7. Urban heat is scientifically mature but politically useful.

Remote sensing of surface urban heat islands is a mature field. The public-good opportunity is not discovering that impervious, dark, unvegetated surfaces are hot. It is translating thermal, albedo, vegetation, roof, and equity layers into open, auditable intervention lists.

Practical implication: the claim is civic prioritization, not new heat physics.

### 8. Methane has strong spectroscopy but uneven public coverage.

Methane retrieval from TROPOMI and plume mapping from imaging spectrometers are established. The hard part is temporal intermittency, detection limits, wind, surface albedo, clouds, pixel size, and whether the relevant plume product is public and repeated enough for accountability.

Practical implication: claim "public plume/accountability workflow" only where instrument coverage and detection limits support it.

### 9. Humanitarian and environmental-justice uses require extra humility.

Indices aimed at informal settlements, sewage, landfills, vector habitat, asbestos-bearing geology, or industrial dust can stigmatize communities or imply wrongdoing. For those, the product must be framed as screening for support, field sampling, or environmental justice investigation, not enforcement or accusation.

Practical implication: sensitive maps need uncertainty, opt-out/community review where possible, and "no enforcement use alone" language.

---

## Candidate Discovery Inventory

Formula notation: `R_x` means reflectance near wavelength `x` nm. Sentinel-2 band names use `S2_B5`, Landsat uses `L8_B6`, etc. Several entries are intentionally "index concepts" rather than final equations because final coefficients should be calibrated per biome, sensor, and atmospheric correction pipeline.

### Water, Coast, and Public Health

| ID | Candidate | Target signal | Sensor family | Formula concept | Status | Spectral rationale |
|---|---|---|---|---|---|---|
| W01 | CyanoRE-705 | Cyanobacteria bloom risk | Sentinel-2 MSI, Sentinel-3 OLCI, PACE OCI | `(R_705 - R_665) / (R_705 + R_665)` | Adaptation | Red-edge bloom/chlorophyll detection is established, but cyanobacteria-specific interpretation remains conditional unless paired with phycocyanin bands, species data, or local validation. |
| W02 | Phyco620-665 | Phycocyanin-rich bloom cue | Sentinel-3 OLCI, PACE OCI | `(R_620 - R_665) / (R_620 + R_665)` | Adaptation | Phycocyanin has absorption near 620 nm; PACE/OLCI can test the feature better than S2, which lacks a clean 620 nm band. |
| W03 | HAB-PeakHeight | Floating or dense algae peak | Sentinel-3 OLCI, PACE OCI | `R_709 - baseline(R_665,R_754)` | Established | Maximum chlorophyll index / peak-height logic isolates the red-edge bump above a local spectral baseline. |
| W04 | TurbidRedNIR | Suspended sediment and turbidity | Sentinel-2 MSI, Landsat OLI | `R_red / R_green` or `R_NIR / R_red` | Established | Turbid water increases red and sometimes NIR reflectance while clear water absorbs strongly outside blue-green wavelengths. |
| W05 | Sewage-CDOM-Slope | Colored dissolved organic matter / sewage plume screen | PACE OCI, Sentinel-3 OLCI | `(R_412 - R_443) / (R_490 + eps)` plus turbidity mask | Adaptation | CDOM depresses blue/UV reflectance; pairing blue slope with red/NIR turbidity helps separate organic plumes from sediment-only plumes. |
| W06 | AcidMine-WaterIron | Acid mine drainage in streams | Sentinel-2 MSI, Landsat OLI, hyperspectral | `(R_red + R_rededge) / (R_blue + R_green)` | Adaptation | Ferric iron precipitates and acidic mine drainage often redden/orange water and banks; hyperspectral data can separate iron minerals more cleanly. |
| W07 | Plastic-FDI+SWIR | Floating macroplastic and mixed debris | Sentinel-2 MSI | `FDI = R_NIR - baseline(R_red,R_SWIR1)` plus `R_SWIR1/R_NIR` | Adaptation | Floating debris is brighter than water in NIR, but plastic-specific use is constrained by aggregation size, mixed debris, foam, algae, sunglint, cloud, and 10 m pixel mixing. |
| W08 | Storm-Debris-Mix | Post-hurricane river/coastal debris | Sentinel-2 MSI, Landsat OLI, Planet if available | `FDI + NDVI + NDWI disagreement` | Hypothesis | Mixed debris fields contain plastic, wood, vegetation, and sediment; disagreement among debris, vegetation, and water indices may flag cleanup targets. |
| W09 | OilThin-OpticalThermal | Thin oil slick screening | Landsat TIRS/OLI, ECOSTRESS, Sentinel-2, SAR | `SAR dark spot + TIR contrast + VIS/NIR contrast` | Adaptation | SAR detects damping of surface roughness; TIR can help distinguish oil from look-alikes; optical/hyperspectral supports type/thickness experiments. |
| W10 | CoralBleach-BlueGreen | Coral bleaching / reef stress | Sentinel-2 MSI, PACE OCI | `(R_blue/R_green)` anomaly after depth correction | Adaptation | Bleaching changes benthic brightness and color in shallow clear water; blue-green ratios must be corrected for depth and water column effects. |
| W11 | Aquaculture-EutroRisk | Fish-farm eutrophication risk | Sentinel-2 MSI, Sentinel-3 OLCI, PACE OCI | `chlorophyll index + turbidity + thermal anomaly` | Adaptation | Nutrient enrichment increases chlorophyll/turbidity; warm low-flush conditions raise fish-kill and bloom risk. |
| W12 | River-Industrial-Plume | Industrial discharge plume screen | Sentinel-2 MSI, Landsat OLI/TIRS, PACE OCI | `thermal anomaly + CDOM/turbidity color shift` | Hypothesis | Discharge often differs in temperature, turbidity, or dissolved color; false positives require facility maps and upstream/downstream controls. |

### Food, Agriculture, Ecosystems, and Drought

| ID | Candidate | Target signal | Sensor family | Formula concept | Status | Spectral rationale |
|---|---|---|---|---|---|---|
| A01 | Drought-RE-SWIR | Early crop/forest water stress | Sentinel-2 MSI, Landsat OLI | `NDRE - NDMI` anomaly | Adaptation | Red-edge responds to chlorophyll/canopy stress; SWIR responds to vegetation water content. Divergence can appear before visible browning. |
| A02 | CropHeat-WUE | Crop water-use stress | Landsat TIRS/OLI, ECOSTRESS, Sentinel-2 | `LST / NDMI` or `LST residual after NDVI` | Established | Water-stressed vegetation is hotter and has lower SWIR moisture; thermal plus optical is a standard crop stress pathway. |
| A03 | Irrigation-Leak-Salt | Irrigation-induced salinity | Sentinel-2 MSI, Landsat OLI | `salinity index + NDVI suppression + wetness persistence` | Adaptation | Salts brighten soil in visible/SWIR and suppress vegetation; persistent wetness helps separate irrigation leakage from bare bright soil. |
| A04 | Nitrogen-RE-Green | Crop nitrogen/chlorophyll deficiency | Sentinel-2 MSI, hyperspectral | `(R_740 - R_705)/(R_740 + R_705)` with green correction | Adaptation | Nitrogen deficiency alters chlorophyll and red-edge position; narrow red-edge bands are more informative than broad NDVI in dense canopies. |
| A05 | Pest-Previsible-RE | Pest/disease stress before browning | Sentinel-2 MSI, hyperspectral | `red-edge slope drop + SWIR moisture residual` | Hypothesis | Many pests reduce chlorophyll or canopy water before visible defoliation; needs labeled outbreak time series. |
| A06 | FloodedCrop-SAR-RE | Crop flood damage under clouds | Sentinel-1 SAR + Sentinel-2 MSI | `SAR water detection + post-event red-edge decline` | Adaptation | SAR sees inundation through clouds; red-edge recovery or decline separates short flood exposure from crop damage. |
| A07 | Rangeland-Degradation | Overgrazing / bare soil exposure | Sentinel-2 MSI, Landsat OLI | `BSI + red-edge productivity trend` | Adaptation | Bare soil indices show exposure; red-edge time series helps distinguish seasonal dormancy from chronic loss of vegetation vigor. |
| A08 | Invasive-Phenology | Invasive plant expansion | Sentinel-2 MSI, Landsat OLI | `seasonal NDRE phase shift vs native baseline` | Adaptation | Many invasives green up earlier, senesce later, or differ in red-edge/SWIR behavior from native vegetation. |
| A09 | Mangrove-SaltStress | Saltwater intrusion and mangrove decline | Sentinel-2 MSI, Landsat OLI | `NDMI decline + red-edge decline + water-edge migration` | Adaptation | Mangrove stress reduces canopy water and chlorophyll; shoreline/wetness context helps separate cutting, drought, and salinity. |
| A10 | Peat-Drydown-FireRisk | Peatland drying and fire vulnerability | Sentinel-1 SAR, Sentinel-2 MSI, SMAP, Landsat TIR | `SAR moisture drop + NDMI drop + LST rise` | Adaptation | Peat drydown changes dielectric moisture, vegetation water, and surface temperature before fire. |
| A11 | Locust-Greenup-Moisture | Desert locust habitat emergence | Sentinel-2 MSI, SMAP, rainfall | `NDVI/NDRE green-up + soil moisture anomaly` | Hypothesis | Locust breeding risk follows ephemeral vegetation and soil moisture pulses in arid zones; spectral signal is indirect but actionable. |
| A12 | TreeHeat-Equity | Urban tree water stress | Sentinel-2 MSI, Landsat/ECOSTRESS TIR | `LST residual high + NDMI low + NDRE low` | Adaptation | Heat-vulnerable neighborhoods need tree health monitoring, not just canopy coverage. |

### Soil, Minerals, Pollution, and Extractive Industry

| ID | Candidate | Target signal | Sensor family | Formula concept | Status | Spectral rationale |
|---|---|---|---|---|---|---|
| S01 | Salinity-VisibleSWIR | Exposed soil salinity | Sentinel-2 MSI, Landsat OLI | `sqrt(R_green * R_red) + SWIR brightness` | Established | Salt crusts raise visible/SWIR brightness; vegetation masks and soil moisture must be controlled. |
| S02 | BrineScar-Sulfate | Persistent sulfate/evaporite contamination | EMIT, EnMAP, PRISMA, ASTER | absorption depth near `2160/2210 nm` | Adaptation | Gypsum and related sulfates have diagnostic SWIR features; hyperspectral sensors can detect mineral scars after water evaporates. |
| S03 | Jarosite-Tailings | Acid mine drainage tailings | EMIT, EnMAP, PRISMA, Sentinel-2 | `R_900 iron + Al/OH/SO4 SWIR absorption` | Adaptation | Jarosite/goethite/hematite and clay alteration are classic acid mine drainage indicators; S2 can screen, hyperspectral can identify. |
| S04 | MineDrain-Downstream | Tailings leakage into riparian corridors | Sentinel-2 MSI, Landsat OLI, hyperspectral | `water iron index + riparian NDRE stress` | Hypothesis | Combining water color and vegetation stress may reveal chronic leakage where direct water chemistry data is absent. |
| S05 | DustToxicity-Proxy | Harmful dust source mineralogy | EMIT, EnMAP, PRISMA | spectral mixture of iron oxides, clays, carbonates, evaporites | Adaptation | EMIT was built to map dust-source mineralogy; public-health use can prioritize dust types and source regions, not just dust quantity. |
| S06 | Asbestos-Serpentine-Screen | Naturally occurring asbestos proxy zones | EnMAP, PRISMA, EMIT | Mg-OH/carbonate absorption near `2310-2350 nm` plus geology mask | Hypothesis | Imaging spectroscopy can map serpentine/talc-carbonate assemblages, but asbestos itself requires careful ground validation. |
| S07 | Landfill-Leachate-Stress | Leachate and dump-edge vegetation stress | Sentinel-2 MSI, Landsat TIR, TROPOMI/EMIT CH4 | `NDMI/NDRE anomaly + wetness + heat/CH4 context` | Hypothesis | Leachate can create wet, nutrient-rich, saline, or toxic stress zones; methane/thermal context improves prioritization. |
| S08 | CoalWaste-Combustion | Burning coal waste piles | Landsat TIR, ECOSTRESS, Sentinel-2 MSI | `persistent LST hotspot + iron/ash spectral contrast` | Adaptation | Coal-waste fires produce thermal anomalies and altered mineral/ash surfaces; useful for safety and air-quality response. |
| S09 | CementKiln-Dust | Alkaline industrial dust deposition | Sentinel-2 MSI, Landsat OLI, hyperspectral | `bright carbonate-like dust + vegetation stress gradient` | Hypothesis | Carbonate/alkaline dust changes soil brightness and can stress vegetation downwind; requires wind and facility controls. |
| S10 | Urban-Industrial-Dust | Metal-bearing urban dust proxy | EnMAP/EMIT + Sentinel-2 | `iron oxide/clay/carbonate mix + impervious edge context` | Hypothesis | Satellites cannot directly see lead or many metals at policy-grade accuracy, but mineral dust proxies can prioritize field sampling. |
| S11 | IllegalMining-BareWater | Artisanal mining expansion | Sentinel-2 MSI, Landsat OLI, Sentinel-1 SAR | `bare soil growth + turbidity plume + forest loss` | Adaptation | Mining often creates bright bare soil, turbid ponds/rivers, and deforestation; the novelty is the fused public-risk score. |
| S12 | Oilfield-Hydrocarbon-Soil | Hydrocarbon-stained soil | EMIT, EnMAP, PRISMA | C-H absorption near `1700-1730` and `2300-2350 nm` | Adaptation | Hydrocarbons have SWIR absorption features; public satellite imaging spectroscopy can screen for persistent staining where coverage exists. |

### Fire, Disasters, and Humanitarian Response

| ID | Candidate | Target signal | Sensor family | Formula concept | Status | Spectral rationale |
|---|---|---|---|---|---|---|
| D01 | BurnNBR-Standard | Burn severity | Landsat OLI, Sentinel-2 MSI, MODIS | `(NIR - SWIR2) / (NIR + SWIR2)` and differenced NBR | Established | Fire lowers NIR vegetation reflectance and raises SWIR charcoal/soil response; dNBR is the dominant baseline. |
| D02 | Burn-RedEdge-Recovery | Post-fire vegetation recovery | Sentinel-2 MSI | `post-fire NDRE trajectory vs dNBR` | Adaptation | Red-edge bands can detect chlorophyll recovery and stress in regenerating vegetation where NDVI saturates. |
| D03 | FuelMoisture-SWIR | Pre-fire fuel moisture | Sentinel-2 MSI, Landsat OLI | `(NIR - SWIR1)/(NIR + SWIR1)` plus SWIR2 | Established | SWIR is sensitive to leaf and canopy water; low moisture plus high biomass is a fire-risk ingredient. |
| D04 | ActiveFire-GEO | Rapid active fire / flare screening | GOES ABI, VIIRS | `3.9 um brightness temperature anomaly` plus 11 um background | Established | Midwave infrared channels respond strongly to high-temperature subpixel fires; GOES adds 5-minute cadence. |
| D05 | AshHealth-Deposition | Ash/dust deposition after fires or volcanoes | Sentinel-2 MSI, Landsat OLI, hyperspectral | `blue/red darkening + SWIR mineral/char signal` | Hypothesis | Ash alters albedo and mineral/char spectral response; public-health use needs wind, PM, and ground confirmation. |
| D06 | Flood-SAR-Optical | Flood extent through clouds | Sentinel-1 SAR + Sentinel-2/Landsat | `SAR backscatter drop + optical NDWI/MNDWI agreement` | Established | Smooth open water is dark in SAR and bright in optical water indices; fusion reduces cloud and urban false positives. |
| D07 | Flood-Urban-Hidden | Urban flood on impervious surfaces | Sentinel-1 SAR, Landsat/S2, DEM | `SAR anomaly + low-slope drainage + impervious mask` | Adaptation | Optical water indices struggle in cities; SAR plus terrain and built-up masks can flag likely flooded streets/blocks. |
| D08 | ConflictBurn-Damage | Burned structures and scorched fields | Sentinel-2 MSI, Landsat OLI, VIIRS | `NBR drop + NDBI/BSI shift + nighttime fire context` | Adaptation | Structure burns, field burning, and artillery fires change SWIR/NIR and sometimes nighttime thermal signatures. |
| D09 | Camp-Heat-WaterRisk | Refugee/IDP camp heat and water stress | Landsat/ECOSTRESS TIR, Sentinel-2 MSI | `LST high + low vegetation + water-distance/wetness screen` | Hypothesis | Camps can face extreme heat and limited cooling vegetation; satellite indices can prioritize field support, not replace surveys. |
| D10 | Landslide-FreshScar | Fresh landslide scar mapping | Sentinel-2 MSI, Landsat OLI, Sentinel-1 SAR | `NBR/NDVI drop + BSI rise + SAR coherence loss` | Established | Landslides remove vegetation, expose soil/rock, and disturb radar coherence. |

### Cryosphere, Mountains, and Water Supply

| ID | Candidate | Target signal | Sensor family | Formula concept | Status | Spectral rationale |
|---|---|---|---|---|---|---|
| C01 | SnowNDSI-Standard | Snow cover | Landsat OLI, Sentinel-2 MSI, MODIS | `(green - SWIR1)/(green + SWIR1)` | Established | Snow is bright in visible green and dark in SWIR; clouds and shadows need masking. |
| C02 | Snow-Darkening-VISNIR | Dust, soot, or biological darkening on snow | Sentinel-2 MSI, Landsat OLI, PACE OCI | `visible albedo drop + NDSI-still-snow mask` | Adaptation | Impurities reduce snow albedo while the pixel may still classify as snow; blue/green/red slopes can indicate darkening. |
| C03 | SnowAlgae-RedEdge | Snow algae / biological bloom | Sentinel-2 MSI, hyperspectral | `red/green anomaly + red-edge cue inside snow mask` | Hypothesis | Red/pink snow algae alter visible reflectance; hyperspectral/PACE-style bands can improve separation from dust. |
| C04 | GlacierDebris-Ice | Debris-covered glacier ice | Sentinel-2 MSI, Landsat TIR | `cool thermal residual + rock-like optical spectrum` | Adaptation | Debris-covered ice can look like rock optically but remain cooler or show different moisture/thermal behavior. |
| C05 | MeltPond-Depth | Supraglacial or sea-ice melt pond depth | Sentinel-2 MSI, Landsat OLI, PACE OCI | `blue/green ratio within ice mask` | Adaptation | Water absorbs red/NIR strongly; blue-green ratios can estimate shallow water optical depth after calibration. |
| C06 | Permafrost-Thermokarst | New thaw ponds / thermokarst expansion | Sentinel-1 SAR, Sentinel-2 MSI, Landsat | `new water + vegetation wetness + SAR coherence change` | Adaptation | Thaw creates ponds, wetland expansion, slumps, and vegetation change; multi-sensor time series is stronger than one index. |

### Urban, Infrastructure, and Environmental Justice

| ID | Candidate | Target signal | Sensor family | Formula concept | Status | Spectral rationale |
|---|---|---|---|---|---|---|
| U01 | Heat-Albedo-TIR | Surfaces amplifying heat exposure | Landsat OLI/TIRS, ECOSTRESS, Sentinel-2 | `high LST + low albedo + low NDVI` | Established | Urban heat is driven by surface temperature, imperviousness, albedo, and vegetation cover. |
| U02 | CoolRoof-Candidate | High-value cool-roof targets | Sentinel-2 MSI, Landsat TIR | `dark roof albedo + high daytime LST + large roof footprint` | Adaptation | Dark roofs store heat; public data can rank interventions where parcel data is open. |
| U03 | InformalSettlement-Heat | Informal settlement heat vulnerability | Landsat/ECOSTRESS TIR, Sentinel-2, VIIRS DNB | `high LST + low vegetation + dense built texture + night lights` | Hypothesis | Heat risk is not just temperature; combining thermal, vegetation, density, and services proxies can prioritize response. |
| U04 | StandingWater-Vector | Mosquito/vector habitat screen | Sentinel-2 MSI, Sentinel-1 SAR, Landsat TIR | `persistent shallow water + warm LST + low flow context` | Hypothesis | Stagnant warm water supports vector risk; satellites can screen habitats but disease risk needs health data. |
| U05 | Construction-Dust | Dust from construction / bare lots | Sentinel-2 MSI, Landsat OLI | `BSI high + vegetation loss + downwind brightness gradient` | Hypothesis | Exposed dry soil and dust deposition alter visible/SWIR brightness; wind and land-use context are essential. |
| U06 | RoadFlood-Access | Road access loss after floods | Sentinel-1 SAR + Sentinel-2 + road vectors | `road-water intersection + SAR flood confidence` | Adaptation | Public disaster value comes from intersecting flood detections with roads, bridges, clinics, and schools. |
| U07 | NightHeat-Outage | Power outage plus heat emergency risk | VIIRS DNB, Landsat/ECOSTRESS TIR | `night-light drop + high LST/air-temperature proxy` | Adaptation | Nighttime lights can flag outages; combining with heat identifies urgent welfare checks. |
| U08 | UrbanStream-Sewage | Informal sewage / failing drainage screen | Sentinel-2 MSI, Landsat TIR | `warm/turbid water + persistent channel anomaly` | Hypothesis | Sewage often changes water color, turbidity, temperature, and vegetation near channels; requires local sampling. |

### Atmospheric Accountability and Climate

| ID | Candidate | Target signal | Sensor family | Formula concept | Status | Spectral rationale |
|---|---|---|---|---|---|---|
| G01 | Methane-Plume-SWIR | Point-source methane plume | EMIT, AVIRIS-NG, Carbon Mapper/Tanager where public, Sentinel-5P for coarse screen | matched filter near methane SWIR absorption | Established | Methane has diagnostic SWIR absorption; imaging spectrometers can map plumes, but global repeatability depends on coverage, overpass timing, surface brightness, wind, clouds, and data access. |
| G02 | Landfill-CH4-Heat | Landfill methane and active waste zones | TROPOMI, EMIT, Landsat/ECOSTRESS TIR | `CH4 enhancement + thermal anomaly + landfill mask` | Adaptation | Waste methane is spatially clustered; thermal and land-use context can prioritize plume searches and field inspection. |
| G03 | Flare-Efficiency-Proxy | Inefficient combustion / flaring accountability | VIIRS/GOES + TROPOMI | `CH4 or CO anomaly / fire radiative power` | Hypothesis | A hot flare with low methane suggests combustion; methane/CO near fire detections may flag malfunction or unlit vents. |
| G04 | NO2-Equity-Gradient | Neighborhood combustion exposure | TROPOMI NO2 + urban land cover | `NO2 column anomaly + road/industrial context` | Established | TROPOMI monitors NO2 globally; local exposure interpretation needs downscaling and ground sensors. |
| G05 | SO2-MineSmelter | Smelter/refinery/volcanic SO2 screen | TROPOMI, OMI legacy | `SO2 column anomaly + wind/facility mask` | Established | SO2 has strong UV retrieval pathways; useful for industrial and volcanic public alerts. |
| G06 | Formaldehyde-FireSmoke | Fire smoke and VOC oxidation proxy | TROPOMI HCHO, GOES/VIIRS fire | `HCHO anomaly downwind of active fire` | Adaptation | HCHO tracks VOC oxidation and fire/biogenic chemistry; pairing with fire detections helps separate sources. |

---

## What We Can Honestly Claim

### Claim 1: A public-good taxonomy is missing.

The literature is rich but fragmented by domain: water quality, soil salinity, wildfire, urban heat, methane, mining, plastic debris, crop stress. A useful contribution is a practitioner-facing taxonomy that puts the physical target, sensor bands, claim status, and validation burden in one place.

### Claim 2: The biggest near-term novelty is cross-sensor accountability.

Many indices already exist. The underbuilt part is public workflow design:

- water color plus land-use context for sewage and industrial discharge screening
- red-edge stress plus thermal heat for urban tree failure
- methane columns plus thermal/fire detections for landfill and flare triage
- SAR flood extent plus roads/clinics/schools for disaster access
- hyperspectral mineral maps plus water/vegetation stress for mine drainage

The "discovery" is often not a single ratio. It is a public, reproducible fusion that answers a civic question.

### Claim 3: Hyperspectral public data changes the question.

With EMIT, EnMAP, PRISMA, PACE, and future Surface Biology and Geology style missions, we can stop pretending every environmental signal has to fit through NDVI-shaped keyholes. Mineral absorption, algal pigments, hydrocarbon features, snow impurities, and vegetation chemistry all become public-good candidates.

### Claim 4: The right language is "candidate signal" until validated.

A band combination becomes a public discovery only after:

1. It is tested against labeled events, field samples, or lab spectra.
2. It beats strong baselines such as NDVI, NDWI, NBR, NDBI, and standard water-quality algorithms.
3. It survives across at least two geographies or explicitly declares its biome/region limits.
4. It publishes failure modes, not just success screenshots.
5. It provides reproducible code and open data references.

### Claim 5: The claimable discoveries are workflow discoveries.

Right now, the strongest claimable discoveries are not "we discovered cyanobacteria from space" or "we discovered methane spectroscopy." Those would be false. The responsible claims are:

| Claimable contribution | Why it is defensible |
|---|---|
| A 66-candidate global public-good signal atlas | The candidates are organized by target, sensor, formula concept, status, and rationale. |
| A claim-status discipline for remote-sensing novelty | It separates established practice, adapted workflow, and hypothesis before public claims are made. |
| A public-good shortlist for first prototypes | It prioritizes social value and validation feasibility instead of novelty theater. |
| A cross-sensor accountability framework | It identifies where the civic value comes from fusing optical, thermal, SAR, hyperspectral, and atmospheric data. |
| A validation roadmap for turning candidates into real discoveries | It defines what must happen before any candidate can be promoted from signal to discovery. |

The bolder scientific discoveries come later, after validation. That is not a weakness. That is the route to publishing something people can trust.

---

## Proposed Validation Roadmap

### Phase 1: Literature-to-index registry

Create a machine-readable registry with fields:

- `id`
- `target_signal`
- `sensor`
- `bands`
- `formula`
- `claim_status`
- `source_family`
- `known_false_positives`
- `validation_dataset`
- `public_good_use_case`

### Phase 2: Baseline notebooks

Build one notebook each for:

- Sentinel-2 water quality and plastic debris
- Sentinel-2/Landsat drought and heat
- Sentinel-2/Landsat/Sentinel-1 flood and disaster access
- EMIT/EnMAP mineral and contamination screening
- TROPOMI/EMIT methane accountability

### Phase 3: Public event library

Assemble 100 labeled public events:

- harmful algal blooms
- large floods
- major wildfires
- mine tailings failures or known acid mine drainage sites
- large landfills
- urban heat islands
- marine debris aggregations
- oil spills
- salinity-affected irrigation districts
- glacier/snow impurity case studies

### Phase 4: Claim discipline

Publish each candidate as one of:

- **Baseline:** known index made easier to use.
- **Workflow contribution:** known physics recombined for a public-good decision.
- **Validated new signal:** candidate beats baselines across tests.
- **Failed gracefully:** plausible idea that did not survive validation.

The failed ideas may be as useful as the successful ones because they prevent civic users from overtrusting pretty maps.

---

## Ethical and Practical Safeguards

These candidates are designed for public good, but several can harm people if treated as proof.

### Screening-only domains

The following should always be labeled **screening only**:

- `S06 Asbestos-Serpentine-Screen`
- `S07 Landfill-Leachate-Stress`
- `S10 Urban-Industrial-Dust`
- `S11 IllegalMining-BareWater`
- `D08 ConflictBurn-Damage`
- `D09 Camp-Heat-WaterRisk`
- `U03 InformalSettlement-Heat`
- `U04 StandingWater-Vector`
- `U08 UrbanStream-Sewage`

Required caveat:

> This map is a remote-sensing screen. It is not proof of contamination, disease risk, illegal activity, or unsafe living conditions. It should be used to prioritize field validation, community support, sampling, or further investigation. It should not be used alone for enforcement, displacement, denial of service, insurance decisions, or public accusation.

### False-positive discipline

Every candidate needs a false-positive section before publication. Examples:

- bloom indices: sediment, submerged vegetation, bottom reflectance, sunglint
- plastic/debris indices: foam, algae, wood, cloud edge, wave state
- salinity indices: dry bright soil, carbonate, gypsum, tillage, residue
- landfill/leachate stress: irrigation, mowing, seasonal vegetation, stormwater
- methane plumes: wind errors, surface albedo, clouds, intermittent sources
- urban heat: weather timing, roof material, shade, sensor overpass time

### Community framing

For humanitarian and environmental-justice use, the product should answer:

- Who benefits if this signal is right?
- Who is harmed if this signal is wrong?
- What field check, local partner, or public agency can validate it?
- What language prevents stigma while still making risk visible?

---

## Evidence Pointers by Candidate

This table ties every candidate ID to the source families that support it. It is still a research-vault layer, not a full annotated bibliography; the next step is to promote high-priority candidates into standalone notes with paper-by-paper annotations.

| ID | Evidence pointer | Audit note |
|---|---|---|
| W01 | HAB optical review; cyanobacteria scoping review; S2/OLCI/PACE sensor references | Red-edge bloom detection is supported; cyanobacteria specificity requires validation. |
| W02 | HAB optical review; cyanobacteria scoping review; PACE/OLCI band references | Phycocyanin logic is supported, but S2 is not ideal because it lacks a clean 620 nm band. |
| W03 | HAB review; water-quality review; OLCI/PACE references | Peak-height and maximum chlorophyll logic are established water-color practices. |
| W04 | Water-quality reviews; NASA ARSET inland water quality | Red/NIR turbidity and suspended-sediment ratios are common, but local calibration matters. |
| W05 | Water-quality reviews; PACE OCI references | CDOM/blue-slope reasoning is established; sewage attribution is an adaptation. |
| W06 | Acid mine drainage literature; water-quality reviews; mineral references | Iron-rich water and banks can be screened optically; chemistry needs validation. |
| W07 | MARIDA benchmark; marine plastic reviews; Sentinel-2 references | FDI/debris detection is supported; plastic-specific claims are constrained. |
| W08 | MARIDA benchmark; marine debris reviews; disaster debris practice | Mixed debris screening is plausible but material classification is not proven. |
| W09 | Oil spill reviews; optical oil spill synthesis; SAR/TIR practice | Multi-sensor oil screening is supported; thin oil/type estimates need event calibration. |
| W10 | Water-quality and coastal remote-sensing practice; S2/PACE references | Bleaching indices are possible only with water-column and depth correction. |
| W11 | Water-quality reviews; HAB reviews; PACE/S2/OLCI references | Eutrophication screening is supported; fish-kill risk requires ecological context. |
| W12 | Water-quality reviews; Landsat thermal and PACE references | Discharge plumes can differ in temperature/color; source attribution is speculative. |
| A01 | Sentinel-2 drought review; crop water stress review; S2 red-edge references | Red-edge plus SWIR stress logic is supported as an adapted workflow. |
| A02 | Crop water stress reviews; Landsat/ECOSTRESS thermal references | Thermal plus optical crop stress is established. |
| A03 | Soil salinity reviews; S2/Landsat references | Salinity detection is supported but confounded by soil/vegetation/moisture. |
| A04 | Sentinel-2 drought and phenology reviews; red-edge literature | Red-edge chlorophyll/nitrogen logic is supported; agronomic calibration needed. |
| A05 | Crop stress reviews; hyperspectral vegetation practice | Pest stress is plausible through chlorophyll/moisture change but needs outbreak labels. |
| A06 | Flood mapping practice; S1/S2 references; vegetation stress literature | SAR flood plus red-edge damage monitoring is a defensible adaptation. |
| A07 | Soil spectral-index review; rangeland/vegetation index practice | Bare soil plus productivity trend is supported but grazing attribution needs context. |
| A08 | Invasive plants review; Sentinel-2 phenology review | Phenology and red-edge/SWIR seasonality are supported for invasive mapping. |
| A09 | Vegetation water stress reviews; coastal/mangrove monitoring practice | Mangrove stress signals are plausible; salinity attribution needs local controls. |
| A10 | Crop/vegetation water stress reviews; SAR soil-moisture practice | Multi-sensor peat drydown is a supported adaptation, not a single optical index. |
| A11 | Drought/soil-moisture/green-up practice; SMAP/S2 references | Locust habitat is indirect; useful as risk screening only. |
| A12 | Urban heat review; crop/tree water stress literature; Landsat/ECOSTRESS references | Tree heat and water stress fusion is a strong urban adaptation. |
| S01 | Soil salinity reviews; soil spectral-index overview | Visible/SWIR salt brightness is supported; universal thresholds are not. |
| S02 | USGS Spectral Library; EMIT/EnMAP/PRISMA references; mineral literature | Sulfate/evaporite absorption logic is strong where hyperspectral coverage exists. |
| S03 | Acid mine drainage and secondary iron mineral literature; hyperspectral references | Jarosite/iron/clay alteration mapping is strongly supported. |
| S04 | Acid mine drainage literature; riparian stress practice | Fused leakage screening is plausible but not proof of contaminant transport. |
| S05 | EMIT mission references; USGS Spectral Library | Dust mineralogy is central to EMIT; toxicity interpretation requires health/geochemistry data. |
| S06 | Hyperspectral mineral practice; USGS Spectral Library | Serpentine/talc-carbonate mapping is plausible; asbestos claims require ground truth. |
| S07 | Landfill methane literature; water/vegetation stress practice | Leachate screening is plausible but sensitive and must be field-validated. |
| S08 | Landsat/ECOSTRESS thermal references; fire/industrial heat practice | Persistent thermal anomalies for burning waste are supported. |
| S09 | Mineral/dust spectral references; vegetation stress practice | Cement dust deposition is plausible but needs wind, field, and facility validation. |
| S10 | EMIT/EnMAP references; urban dust public-health rationale | Metal-bearing dust cannot be directly claimed; mineral proxy sampling priority only. |
| S11 | Artisanal mining review; S2/Landsat/S1 land disturbance practice | Bare soil, water turbidity, and deforestation fusion is supported. |
| S12 | Oil spill/hyperspectral reviews; EMIT/EnMAP/PRISMA references | Hydrocarbon SWIR features are supported; satellite screening depends on concentration and substrate. |
| D01 | Fire ecology review; burn severity review; Landsat/S2 references | NBR/dNBR is a strong established baseline. |
| D02 | Fire ecology review; Sentinel-2 red-edge literature | Red-edge recovery is an adaptation around established fire baselines. |
| D03 | Fire ecology review; crop/vegetation water stress reviews | SWIR fuel moisture indices are established. |
| D04 | GOES ABI references; VIIRS band/fire practice | Midwave IR fire detection is established. |
| D05 | Fire/volcano ash spectral practice; hyperspectral/mineral references | Ash deposition screening is plausible but public-health inference requires PM/field data. |
| D06 | Flood mapping literature; Sentinel-1/Sentinel-2 references | SAR-optical flood fusion is established. |
| D07 | Flood mapping literature; SAR urban flood practice | Urban flood adaptation is defensible but needs terrain/infrastructure context. |
| D08 | Fire/burn severity literature; VIIRS/GOES references | Conflict damage mapping is a workflow adaptation with attribution caveats. |
| D09 | Urban heat review; humanitarian mapping practice | Camp heat/water risk is screening only and ethically sensitive. |
| D10 | Landslide spectral/coherence practice; S1/S2 references | Vegetation loss, bare scar, and coherence loss are established landslide cues. |
| C01 | NDSI practice; Landsat/S2/MODIS references | Snow visible/SWIR contrast is established. |
| C02 | Snow/ice spectral practice; PACE/S2/Landsat references | Snow darkening from impurities is supported but source attribution needs validation. |
| C03 | Snow algae spectral literature/practice; hyperspectral/PACE logic | Biological snow bloom screening is plausible; dust/algae separation is hard. |
| C04 | Thermal/optical glacier mapping practice; Landsat/S2 references | Debris-covered ice detection is an adaptation using thermal residuals. |
| C05 | Water optical-depth practice; S2/PACE references | Melt-pond depth via blue/green ratios is plausible after calibration. |
| C06 | Permafrost/thermokarst mapping practice; S1/S2/Landsat references | New water plus wetness/coherence change is a supported adaptation. |
| U01 | Urban heat island review; Landsat/ECOSTRESS references | Surface heat, albedo, vegetation, and imperviousness are established. |
| U02 | Urban heat review; albedo/cool-roof remote-sensing practice | Cool-roof prioritization is a civic workflow adaptation. |
| U03 | Urban heat review; VIIRS DNB references; humanitarian caveats | Informal-settlement heat mapping is screening only. |
| U04 | Water/wetness mapping practice; public-health caveats | Vector habitat screening is indirect and must not imply disease presence. |
| U05 | Soil/bare-ground spectral practice; urban dust caveats | Construction dust is plausible but attribution needs wind and land-use data. |
| U06 | Flood mapping practice; road network overlay workflows | Road-access loss is an applied disaster workflow, not a spectral discovery. |
| U07 | VIIRS DNB references; urban heat references | Night-light outage plus heat risk is a defensible welfare-screening workflow. |
| U08 | Water-quality reviews; thermal/wetness references; ethical caveats | Sewage/drainage screening is sensitive and requires sampling. |
| G01 | EMIT methane references; JPL methane plume work; TROPOMI methane literature | Methane SWIR spectroscopy is established; coverage and detection limits govern claims. |
| G02 | TROPOMI landfill methane papers; EMIT methane product references | Landfill methane monitoring is supported; thermal context is prioritization. |
| G03 | VIIRS/GOES fire references; methane/CO retrieval practice | Flare efficiency proxy is plausible but requires facility-level validation. |
| G04 | TROPOMI air-quality literature; Sentinel-5P references | NO2 column monitoring is established; exposure downscaling is not automatic. |
| G05 | TROPOMI/Sentinel-5P air-quality references | SO2 anomaly monitoring is established. |
| G06 | TROPOMI HCHO references; GOES/VIIRS fire references | HCHO-fire pairing is a source-separation adaptation. |

---

## Source Map

### Sensor capability references

- USGS Sentinel-2 archive and MSI band overview: https://www.usgs.gov/centers/eros/science/usgs-eros-archive-sentinel-2
- ESA Sentinel-2 product specification: https://sentinels.copernicus.eu/documents/d/sentinel/sentinel-2-products-specification-document-15_1
- NASA Landsat spectral bands and applications: https://science.nasa.gov/mission/landsat/spectral-bands-and-applications
- USGS Landsat 8 mission page: https://www.usgs.gov/landsat-missions/landsat-8
- NASA/JPL EMIT instrument specifications: https://earth.jpl.nasa.gov/emit/instrument/specifications/
- EnMAP mission specifications: https://www.enmap.org/mission/
- USGS EnMAP mission overview: https://www.usgs.gov/publications/enmap-imaging-spectroscopy-mission-towards-operations
- NASA PACE OCI overview: https://pace.oceansciences.org/oci.cgi
- NOAA GOES-R ABI overview: https://www.goes-r.gov/spacesegment/abi.html
- NOAA GOES ABI band guides: https://goes-r.noaa.gov/mission/ABI-bands-quick-info.html
- NOAA VIIRS band reference: https://www.ospo.noaa.gov/Products/Suites/files/VIIRS_bands_and_bandwidths.pdf
- USGS Spectral Library: https://www.usgs.gov/centers/gggsc/science/usgs-high-resolution-spectral-library

### Domain literature and practice references

- Spectral indices in remote sensing of soil, critical overview: https://www.sciencedirect.com/science/article/pii/S0034425725003220
- Water quality remote sensing overview: https://www.mdpi.com/2231916
- Comprehensive water quality parameter review: https://pmc.ncbi.nlm.nih.gov/articles/PMC5017463/
- NASA ARSET inland water quality training: https://appliedsciences.nasa.gov/sites/default/files/2023-07/WaterQuality_Part3_Final_1.pdf
- Harmful algal bloom optical remote sensing review: https://www.mdpi.com/2072-4292/17/8/1381
- Freshwater cyanobacterial bloom scoping review: https://www.mdpi.com/2072-4292/17/5/918
- Marine debris benchmark and floating debris indices: https://pmc.ncbi.nlm.nih.gov/articles/PMC8740969/
- Marine plastic remote sensing meta-analysis: https://www.sciencedirect.com/science/article/pii/S0025326X23011815
- Coastal and marine plastic litter monitoring review: https://www.sciencedirect.com/science/article/pii/S0272771422004188
- Oil spill remote sensing review: https://www.mdpi.com/1424-8220/18/1/91
- Optical remote sensing of oil spills: https://spj.science.org/doi/10.34133/2021/9141902
- Soil salinity remote sensing review: https://www.mdpi.com/2072-4292/15/10/2540
- Longitudinal soil salinity mapping with remote sensing: https://www.nature.com/articles/s41598-024-60033-6
- Sentinel-2 drought assessment review: https://www.mdpi.com/2072-4292/13/17/3355
- Crop water stress remote sensing review: https://www.mdpi.com/2072-4292/13/20/4155
- Invasive plants remote sensing review: https://www.mdpi.com/2072-4292/16/20/3781
- Sentinel-2 phenology review: https://www.mdpi.com/2072-4292/12/17/2760/html
- Fire ecology remote sensing review: https://www.mdpi.com/2072-4292/11/22/2638
- Burned area / burn severity review: https://www.mdpi.com/2072-4292/14/19/4714
- Urban heat island remote sensing review: https://www.mdpi.com/2072-4292/11/1/48
- Public-domain Landsat/Sentinel mineral exploration review: https://www.sciencedirect.com/science/article/pii/S0169136819305517
- Secondary iron mineral detection and acid mine drainage context: https://www.sciencedirect.com/science/article/pii/S0303243421000507
- Artisanal and small-scale mining remote sensing review: https://www.sciencedirect.com/science/article/pii/S0048969724059175
- NASA EMIT greenhouse gas plume report: https://www.nasa.gov/centers-and-facilities/jpl/nasa-mission-excels-at-spotting-greenhouse-gas-emission-sources/
- NASA EMIT methane data workshop: https://nasa-openscapes.github.io/news/2024-03-14-emit-methane/
- JPL methane plume detection with imaging spectroscopy: https://ml.jpl.nasa.gov/sciences/methane-plume.html
- Landfill methane with TROPOMI: https://pmc.ncbi.nlm.nih.gov/articles/PMC9365275/
- Global oil and gas methane coverage with TROPOMI: https://pubmed.ncbi.nlm.nih.gov/37798261/
- TROPOMI 2019-2024 methane attribution: https://pmc.ncbi.nlm.nih.gov/articles/PMC13068062/

---

## Article Angles

- "NDVI Was the Hello World. The Public Satellite Stack Has Grown Up."
- "The Global Public-Good Atlas of Satellite Band Combinations"
- "Stop Inventing Indices. Start Publishing What They Actually See."
- "66 Satellite Signals Worth Testing for the Public Good"
- "The Next Environmental Watchdog Is a Band Ratio With Receipts"
