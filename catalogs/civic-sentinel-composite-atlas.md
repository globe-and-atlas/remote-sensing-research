# Ranked Scientific & Public Good Atlas — All 18 Sentinel-2 Composites

*Corrected edition — 2026-05-23. Supersedes the draft circulated for critique.*

---

## Ranking Methodology

Indices are scored on two independent axes (1–5 each). The composite score (max 10) determines rank. Ties are broken first by deployment breadth (global-capable > regional-specific), then by harm reversibility (irreversible harms ranked higher).

| Axis | Definition | Score 5 | Score 1 |
|---|---|---|---|
| **Spectral Novelty (S)** | Uniqueness of formulation: novel confounder rejection gates, band combinations absent from established published indices, or hardware-limitation bypasses | Solves a documented hardware or false-positive limitation with an original multi-gate formulation | Applies a single established ratio with a threshold adjustment |
| **Public Good (G)** | Direct impact potential at deployment scale | Acute life-saving potential, global deployment | Incremental monitoring improvement, site-specific |

**Tiebreaker order:** (1) global deployment breadth > regional-only; (2) irreversible harm detected > reversible harm.

| Rank | Index | S | G | Score | Tiebreaker applied |
|:---:|---|:---:|:---:|:---:|---|
| 1 | BH-DFSI | 5 | 5 | 10 | — |
| 2 | PETI | 5 | 4 | 9 | global freshwater > Arctic-specific |
| 3 | MP-PDI | 4 | 5 | 9 | irreversible ocean harm |
| 4 | TT-API | 5 | 4 | 9 | Arctic-specific, climate feedback |
| 5 | CD-UAI | 3 | 5 | 8 | irreversible coral harm > chronic urban |
| 6 | EC-ACI | 4 | 4 | 8 | global urban deployment |
| 7 | LRD-VSI | 4 | 4 | 8 | site-specific, reversible |
| 8 | TDR-ASI | 4 | 3 | 7 | acute industrial disaster |
| 9 | SF-EII | 3 | 4 | 7 | global forest deployment |
| 10 | WDA-CSI | 3 | 4 | 7 | site-specific ecosystem |
| 11 | TRSI | 2 | 4 | 6 | acute, global mining |
| 12 | CSRC | 2 | 4 | 6 | small-water, less novel |
| 13 | SWRI | 2 | 3 | 5 | broader context needed |
| 14 | DWCI | 2 | 3 | 5 | watershed-scale only |
| 15 | LFGVI | 2 | 3 | 5 | spatial context required |
| 16 | RRFI | 2 | 2 | 4 | ecological, no acute harm |
| 17 | EPDI | 2 | 2 | 4 | storm-event specific |
| 18 | HSAI | 1 | 2 | 3 | well-covered domain |

---

## Claim Language Policy

Avoid first-in-history assertions. The defensible claim for each index is: *a named, transparent, decision-ready composite built from established Sentinel-2 spectral mechanisms, domain gates, and confounder rejection — applied to a specific public-good screening workflow.*

---

## Part 1: Primary High-Impact Slate (Ranks 1–10)

---

### Rank 1 — BH-DFSI: Burnt Hillside Debris-Flow Susceptibility Index

**Domain:** Post-wildfire hydrological hazard | **Bands:** B02, B03, B04, B08, B11, B12

**Public good:** Predicts catastrophic mudslides and debris flows in burned mountainous terrain to support pre-event evacuations.

#### Formula

$$\text{BH-DFSI} = \text{BurnGate} \times \text{SoilGate} \times \text{MoistureSignal} \times \text{ChromaticSlopeProxy}$$

| Component | Expression | Purpose |
|---|---|---|
| NBR | $(B08 - B12) / (B08 + B12)$ | Normalized Burn Ratio |
| BSI | $((B11 + B04) - (B08 + B02)) / ((B11 + B04) + (B08 + B02))$ | Bare Soil Index |
| NDWI_Gao | $(B03 - B11) / (B03 + B11)$ | Canopy/soil moisture (Gao 1996) |
| BurnGate | $\text{clamp}((0.15 - \text{NBR}) / 0.30,\ 0,\ 1)$ | Fires on severely charred surfaces (NBR < 0.15) |
| SoilGate | $\text{clamp}((\text{BSI} - 0.10) / 0.20,\ 0,\ 1)$ | Confirms canopy collapse and bare soil exposure |
| MoistureSignal | $\text{clamp}((\text{NDWI\_Gao} + 0.35) / 0.50,\ 0,\ 1)$ | Captures pre-flow moisture accumulation on burnt slopes |
| ChromaticSlopeProxy | $\text{clamp}((B04 - B02) / (B04 + B02) \times 2.0,\ 0,\ 1)$ | Red-to-blue contrast gradient as micro-relief proxy (see note) |

> **ChromaticSlopeProxy note:** B04/B02 is the normalized red-to-blue ratio. On sun-exposed steep terrain, differential Rayleigh scattering and surface geometry enhance red wavelengths relative to blue; shadowed faces attenuate both proportionally. This captures slope-orientation chromatic gradients as a micro-relief proxy without a DEM. It is **not** a topographic shadow detector — shadows suppress all VNIR bands nearly equally and would not produce a reliable red/blue contrast change. The mechanism is slope illumination geometry, not shadow detection.

> **Charred surface note:** Charred biomass is a near-total absorber across the VNIR-SWIR range (absorptivity > 0.95), not a perfect blackbody in the thermodynamic sense. The practical effect is that both the numerator (B03, green) and denominator (B11, SWIR) of standard NDWI are simultaneously depressed to near-zero, making the ratio unreliable on burned pixels. BH-DFSI bypasses this by using offset-shifted NDWI thresholds calibrated for the compressed post-fire reflectance range.

#### Prior art & distinguishing claim

Standard approaches combine: NBR (Key & Benson 2006) for fire severity; BSI (Rikimaru 1996–2002) for bare soil; static DEM-based slope models for terrain hazard. NDWI (Gao 1996) collapses on charred pixels. BH-DFSI distinguishes by multiplicatively gating all three signals simultaneously with offset thresholds calibrated for post-fire reflectance, plus a visible-band slope proxy that eliminates the DEM dependency for screening-level use.

#### Known limitations

- Requires clear-sky imagery. Dense post-fire smoke severely degrades B02–B04 bands; apply only after smoke clearance.
- Does not replace DEM-based slope analysis for final evacuation routing — it screens candidate slopes, not absolute risk.
- Effective primarily during the critical window between fire containment and first significant rainfall.

---

### Rank 2 — PETI: Phycocyanin Eutrophication Toxicity Index

**Domain:** Freshwater public health | **Bands:** B03, B04, B05, B11

**Public good:** Screens drinking water reservoirs for toxic cyanobacteria (blue-green algae) dominance, identifying microcystin and neurotoxin risk.

#### Formula

$$\text{PETI} = \text{WaterGate} \times \text{clamp}\!\left(\frac{\text{PC}_{\text{virtual}} - 0.05}{0.25},\ 0,\ 1\right)$$

| Component | Expression | Purpose |
|---|---|---|
| MNDWI | $(B03 - B11) / (B03 + B11)$ | Water mask (McFeeters) |
| WaterGate | $\text{clamp}((\text{MNDWI} - 0.15) / 0.30,\ 0,\ 1)$ | Restricts index to open water; suppresses land vegetation |
| PC_virtual | $\frac{B05 - B04}{B05 + B04} - \frac{B04 - B03}{B04 + B03}$ | Double-slope differential as 620 nm proxy (see note) |

> **PC_virtual note:** Phycocyanin absorbs at ~620 nm and fluoresces at ~650 nm. Sentinel-2 has no band at 620 nm. PC_virtual uses the curvature of the reflectance spectrum between the green (B03, 560 nm), red (B04, 665 nm), and red-edge (B05, 705 nm) bands to approximate the dip that phycocyanin creates in this region. This is a **spectral interpolation proxy**, not a direct retrieval — it captures the differential slope signature that cyanobacterial pigments create, amplified relative to green algae. The approach is more phycocyanin-selective than a single NDCI ratio but cannot replace a dedicated 620 nm band.

#### Prior art & distinguishing claim

NDCI (Mishra & Mishra 2012, *Remote Sensing of Environment*): $(B05 - B04) / (B05 + B04)$ — maps general cyanobacteria biomass. 2BDA and 3BDA (Simis et al. 2005, 2007) use hyperspectral 620 nm bands not available on S2. PETI distinguishes from NDCI by computing the **curvature** of the red-to-red-edge slope (two adjacent band-pair ratios subtracted) rather than a single ratio — capturing phycocyanin's differential effect on reflectance slope shape, which NDCI cannot separate from high-chlorophyll green algae.

#### Known limitations

- Cannot distinguish phycocyanin from other red-edge absorbers without ground truth.
- Wind speeds > 2 m/s disrupt floating bloom structure, degrading the spectral signature.
- Shallow water (< 2 m) bottom reflection can trigger false positives.
- Effective for screening and triage; quantitative PC concentration requires site-specific calibration.

---

### Rank 3 — MP-PDI: Marine Plastisphere & Polymer Differentiation Index

**Domain:** Marine pollution | **Bands:** B03, B04, B06, B08, B11, B12

**Public good:** Maps floating synthetic polymer accumulations in ocean gyres and river plumes to guide cleanup fleets and monitor illegal dumping.

#### Formula

$$\text{MP-PDI} = \text{MarineGate} \times \text{VegReject} \times \text{PolymerSignal} \times \text{SWIRShoulder}$$

| Component | Expression | Purpose |
|---|---|---|
| NDWI | $(B03 - B08) / (B03 + B08)$ | Water body gate |
| NDVI | $(B08 - B04) / (B08 + B04)$ | Vegetation index for Sargassum rejection |
| MarineGate | $\text{clamp}((\text{NDWI} - 0.20) / 0.40,\ 0,\ 1)$ | Restricts to open water pixels |
| VegReject | $\text{clamp}((0.15 - \text{NDVI}) / 0.25,\ 0,\ 1)$ | Suppresses organic floating vegetation (Sargassum, macroalgae) |
| PolymerSignal | $(B06 - B04) / (B06 + B04)$ | Red-edge anomaly from floating synthetic materials |
| SWIRShoulder | $B11 / (B12 + 0.001)$ | SWIR reflection slope distinguishing polymers from sediment and foam |

> **SWIRShoulder note:** Common synthetic polymers (PET, PP, HDPE) exhibit reflectance in the 1.4–1.7 µm range (B11 at 1610 nm), while B12 (2190 nm) falls in an atmospheric water absorption band that suppresses polymer reflectance. The B11/B12 ratio exploits this shoulder. It is a broad spectral slope indicator, not a narrow-band polymer spectral library match. Cannot reliably distinguish PET from PE or PP.

#### Prior art & distinguishing claim

FAI (Floating Algae Index, Hu 2009) maps floating organic matter but has no polymer specificity. FDI (Floating Debris Index, Biermann et al. 2020, *Scientific Reports*) uses a red-edge peak above the SWIR baseline to detect floating debris — but includes no SWIR polymer shoulder gate, making it susceptible to mineral sediment and sea foam false positives. MP-PDI distinguishes from FDI by adding VegReject (active Sargassum suppression via NDVI threshold) and SWIRShoulder (B11/B12 slope gate) as a second spectral discriminant.

#### Known limitations

- Minimum detectable patch size at S2 10 m resolution is approximately 100 m² aggregate — effective for macro-debris accumulations, not dispersed litter.
- Submerged and microplastic debris is not detectable.
- Glint-contaminated pixels (sun angle effects) can produce false positives. Apply glint correction before use.
- Effective primarily in calm or moderate sea states (Beaufort 0–3).

---

### Rank 4 — TT-API: Thermokarst Thaw & Anoxic Peat Index

**Domain:** Arctic climate / cryosphere | **Bands:** B02, B04, B05, B06, B8A, B11

**Public good:** Tracks active permafrost thaw fronts and methane outgassing hotspots for climate feedback modeling and early warning.

#### Formula

$$\text{TT-API} = \text{WetnessGate} \times \text{IronGate} \times \text{CanopyStress}$$

| Component | Expression | Purpose |
|---|---|---|
| NDMI | $(B8A - B11) / (B8A + B11)$ | Canopy/soil moisture index |
| REAI | $(B06 - B05) / (B06 + B05)$ | Red-Edge Area Index — moss/tundra health |
| WetnessGate | $\text{clamp}((\text{NDMI} - 0.15) / 0.35,\ 0,\ 1)$ | Isolates saturated organic soils |
| IronGate | $\text{clamp}((B02 / (B04 + 0.001)) \times 1.5,\ 0,\ 1)$ | Blue-to-red ratio proxy for Fe²⁺ speciation (see note) |
| CanopyStress | $\text{clamp}((0.15 - \text{REAI}) / 0.30,\ 0,\ 1)$ | Fires on dead/dying tundra vegetation at slump headwalls |

> **IronGate note:** Ferric iron (Fe³⁺, oxidized) — common in well-drained soils as goethite and hematite — strongly absorbs blue wavelengths and reflects red, yielding B04 > B02 (low B02/B04 ratio). Ferrous iron (Fe²⁺, reduced) — characteristic of waterlogged, chemically reducing peat slurries exposed at active thermokarst thaw headwalls — shows relatively higher blue reflectance, raising B02/B04 above 1.0. This is a **directional spectral indicator of soil reduction chemistry**, not a quantitative Fe²⁺ measurement. The label "anoxic" is a geochemical inference from the reducing conditions implied by Fe²⁺ dominance; it is not directly measurable from spectral reflectance.

#### Prior art & distinguishing claim

Permafrost thaw has been mapped with Landsat LST (surface temperature change), InSAR (land subsidence over years), and NDWI/NDMI for wetland expansion (multiple authors). TT-API distinguishes by integrating three simultaneous pixel-level signals — organic peat wetness, iron redox state, and canopy stress — gated multiplicatively to isolate active thaw slumping fronts from background stable wet tundra (which passes WetnessGate alone but fails IronGate and CanopyStress).

#### Known limitations

- Effective only during the Arctic ice-free window (approximately June–September).
- Cloud cover over Arctic regions is persistent; multi-date cloud-free compositing strongly recommended.
- High background soil moisture in non-thaw tundra can elevate WetnessGate; the multiplicative gate design reduces but does not eliminate this.
- Requires field verification to distinguish active thermokarst from drained lake basins.

---

### Rank 5 — CD-UAI: Coastal Dredging & Marine Siltation Plume Index

**Domain:** Marine biology / coral reef protection | **Bands:** B02, B03, B04, B11

**Public good:** Maps underwater siltation plumes from sand dredging, port construction, and coastal reclamation to identify coral reef smothering events.

#### Formula

$$\text{CD-UAI} = \text{Siltation} \times \text{CloudReject}$$

| Component | Expression | Purpose |
|---|---|---|
| MNDWI | $(B03 - B11) / (B03 + B11)$ | Water mask |
| Siltation | $\text{clamp}((B04 - B02) / (B04 + B02) + 0.10,\ 0,\ 1) \times \text{clamp}(B03 / (B02 + 0.001) \times 1.2,\ 0,\ 1)$ | Green-red suspended sediment chromatic signature (underwater) |
| CloudReject | $\text{clamp}((0.05 - B11) / 0.05,\ 0,\ 1) \times \text{clamp}((\text{MNDWI} - 0.20) / 0.40,\ 0,\ 1)$ | Dual gate: SWIR ensures water-only; rejects clouds, land, vessels |

> **SWIR water gate note:** Water absorbs SWIR radiation almost completely (B11 reflectance < 0.02 for clear or turbid water). Clouds, boat decks, and land all have B11 reflectance well above 0.05. This makes the SWIR gate a robust and well-established discriminant for open-water pixels — not a novel claim, but an essential foundation for the siltation signal.

#### Prior art & distinguishing claim

Suspended sediment mapping via turbidity indices is established (Nechad et al. 2010; NDTI, Lacaux et al. 2007). CD-UAI distinguishes by combining the underwater green-red chromatic siltation signal with a **dual** SWIR + MNDWI rejection gate that simultaneously eliminates clouds, vessels, and land — sources of false positives that standard single-gate NDTI-based approaches cannot fully reject.

#### Known limitations

- Does not penetrate to seabed in water depths > 2 m.
- Cannot distinguish biogenic turbidity (algal blooms, phytoplankton) from mineral siltation without additional temporal or spectral context.
- Effective for near-surface plumes; deeply submerged sediment resuspension is not detectable.

---

### Rank 6 — EC-ACI: Evapotranspirative Canopy & Asphalt Contrast Index

**Domain:** Urban heat / environmental justice | **Bands:** B02, B03, B04, B05, B07, B08, B11, B12

**Public good:** Exposes block-level urban heat-shelter inequality at 10 m resolution to guide municipal tree-planting and green infrastructure investment.

#### Formula

$$\text{EC-ACI} = \text{HeatTrap} \times (1.0 - \text{CanopyCooling}) \times 100$$

| Component | Expression | Purpose |
|---|---|---|
| Albedo | $(B02 + B03 + B04 + B08 + B11 + B12) / 6.0$ | Simple broadband albedo proxy |
| NDBI | $(B11 - B08) / (B11 + B08)$ | Normalized Difference Built-up Index |
| TreeCanopy | $(B07 - B05) / (B07 + B05)$ | Red-Edge 3 / Red-Edge 1 ratio: mature woody canopy proxy |
| NDWI_Gao | $(B03 - B11) / (B03 + B11)$ | Canopy water content proxy |
| HeatTrap | $\text{clamp}((0.20 - \text{Albedo}) / 0.15,\ 0,\ 1) \times \text{clamp}((\text{NDBI} - 0.05) / 0.25,\ 0,\ 1)$ | Low-albedo built-up surfaces |
| CanopyCooling | $\text{clamp}((\text{TreeCanopy} - 0.25) / 0.35,\ 0,\ 1) \times \text{clamp}((\text{NDWI\_Gao} + 0.30) / 0.50,\ 0,\ 1)$ | Mature, moisture-rich evapotranspirative tree canopies |

> **Sensor limitation correction:** Landsat 8/9 TIRS Band 10 has a **100 m native ground sampling distance (GSD)**, resampled to 30 m in Collection 2 products. A typical urban city block spans 80–120 m, meaning the 30 m resampled product blurs across block boundaries and cannot resolve which specific street, parcel, or parking lot is the thermal hotspot. Sentinel-2's 10 m optical bands provide 3–10× finer resolution for a heat-shelter proxy. However, EC-ACI is **not a surface temperature retrieval** — it is an optical proxy for heat-shelter availability (shade + canopy moisture). Ground-truth calibration against Landsat LST or ECOSTRESS is required before using EC-ACI outputs in policy or equity applications.

> **CanopyCooling note:** The B07/B05 ratio (Red-Edge 3 / Red-Edge 1) responds preferentially to mature, thick woody canopies (oaks, elms, mature maples) over dry lawns and sparse grass — a distinction that NDVI alone cannot make in summer when all green surfaces have similar NDVI. The NDWI_Gao gate further filters out lawns under irrigation stress.

#### Prior art & distinguishing claim

UHI analysis using Landsat LST (Peng et al. 2012) and NDBI-based impervious surface mapping (Zha et al. 2003) are established. EC-ACI distinguishes by using S2's Red-Edge 3 (B07) as a mature woody canopy selector — isolating evapotranspirative trees from dry turf — combined with the Gao NDWI moisture gate, an approach not implemented in existing published UHI optical composites.

#### Known limitations

- Not a temperature measurement. Requires LST or ECOSTRESS validation before quantitative policy use.
- NDBI false-fires on dry bare soil in semi-arid or newly developed areas without vegetation.
- Seasonal dependency: effective in growing season when canopy is leafed out; winter bare-deciduous canopy suppresses CanopyCooling.

---

### Rank 7 — LRD-VSI: Landfill Leachate & Runoff Degradation Vegetation Index

**Domain:** Waste containment / aquifer protection | **Bands:** B02, B03, B04, B08, B11

**Public good:** Detects boundary-zone vegetation damage from landfill leachate migration to protect municipal aquifers and drinking water wells.

#### Formula

$$\text{LRD-VSI} = \text{Chlorosis} \times \text{Desiccation} \times \text{Runoff}$$

| Component | Expression | Purpose |
|---|---|---|
| Chlorosis | $\text{clamp}((B03 - B04) / (B03 + B04) + 0.15,\ 0,\ 1)$ | Elevated green/red ratio from chlorophyll degradation (yellowing) |
| Desiccation | $\text{clamp}((B11 - B08) / (B11 + B08) + 0.10,\ 0,\ 1)$ | Elevated SWIR/NIR from canopy water loss |
| Runoff | $\text{clamp}(B04 / (B02 + 0.001) \times 0.8,\ 0,\ 1)$ | Elevated red/blue contrast from metal-rich soil seeps |

#### Prior art & distinguishing claim

Red-edge chlorosis mapping (Ustin et al.) and NDWI-based canopy moisture loss are established. LRD-VSI distinguishes by requiring the **co-presence** of three simultaneous stress signals — chlorosis + desiccation + ferric soil runout — in a multiplicative gate. Single-factor stress indices (NDVI, NDWI) respond to drought, disease, and herbicide identically; the triple-gate significantly reduces attribution ambiguity.

#### Known limitations

- Leachate-caused chlorosis is spectrally indistinguishable from drought or disease on a per-pixel basis. The triple gate reduces but does not eliminate ambiguity.
- Seasonal soil moisture variation affects the Runoff gate. Interpret in context of recent precipitation.
- Field verification at candidate pixels is essential before regulatory use.

---

### Rank 8 — TDR-ASI: Tailings Dam Runout & Acid Silt Index

**Domain:** Mine disasters / industrial safety | **Bands:** B02, B04, B08, B11, B12

**Public good:** Maps toxic tailings spill corridors and acid mine drainage (AMD) downstream of active or failed mine tailings impoundments.

#### Formula

$$\text{TDR-ASI} = \text{IronStain} \times \text{SulfateGate} \times \text{BareSoil}$$

| Component | Expression | Purpose |
|---|---|---|
| NDVI | $(B08 - B04) / (B08 + B04)$ | Vegetation index |
| IronStain | $\text{clamp}((B04 - B02) / (B04 + B02) - 0.20,\ 0,\ 1)$ | Intense orange-red ferric iron (goethite/hematite) staining |
| SulfateGate | $\text{clamp}((B11 - B12) / (B11 + B12) - 0.05,\ 0,\ 1)$ | SWIR slope toward sulfate mineral absorption (see note) |
| BareSoil | $\text{clamp}((0.15 - \text{NDVI}) / 0.25,\ 0,\ 1)$ | Rejects healthy vegetation canopy |

> **SulfateGate note:** Jarosite (KFe₃(SO₄)₂(OH)₆) has absorption features near 2.27 µm and alunite near 2.17 µm. Gypsum absorbs near 1.74 µm. Sentinel-2 B11 is at 1610 nm and B12 at 2190 nm — positioned near but not precisely at these absorption maxima. The B11 > B12 slope (positive SulfateGate) is a broad directional indicator of sulfate-bearing mineral assemblages, not a narrow-band mineral spectral library match. Kaolinite and some clay minerals also produce elevated B11/B12. Confirmation requires airborne hyperspectral (AVIRIS, PRISMA) or field spectrometry.

#### Prior art & distinguishing claim

AMD mapping with Landsat/HyMap (Kemper & Sommer 2002; Swayze et al. 1996) uses hyperspectral data. TDR-ASI distinguishes by deploying S2's SWIR bands (globally available, free, 20 m resolution) to produce a broad screening composite coupling ferric iron staining with a SWIR sulfate slope — accessible to agencies without airborne hyperspectral budgets.

#### Known limitations

- SWIR bands at S2 resolution cannot replace hyperspectral for definitive mineral ID.
- False positives possible in arid regions with natural ferricrete or evaporite deposits.
- Works on surface-exposed tailings mud; does not detect subsurface seepage without surface expression.

---

### Rank 9 — SF-EII: Wildfire Fuel Hazard & Canopy Dehydration Index

**Domain:** Forestry / fire prevention | **Bands:** B04, B08, B8A, B11, B12

**Public good:** Identifies forest tinderbox conditions — dense woody canopies with severe moisture deficit — to guide pre-fire fuel management.

#### Formula

$$\text{SF-EII} = \text{Dehydration} \times \text{CanopyDeficit} \times \text{ForestGate}$$

| Component | Expression | Purpose |
|---|---|---|
| NDVI | $(B08 - B04) / (B08 + B04)$ | Vegetation density gate |
| Dehydration | $\text{clamp}((B11 - B8A) / (B11 + B8A) + 0.15,\ 0,\ 1)$ | SWIR1/narrow-NIR moisture depletion (EWT proxy) |
| CanopyDeficit | $\text{clamp}(B12 / (B8A + 0.001) - 0.80,\ 0,\ 1)$ | SWIR2/narrow-NIR live fuel moisture content (LFMC) deficit proxy |
| ForestGate | $\text{clamp}((\text{NDVI} - 0.35) / 0.35,\ 0,\ 1)$ | Restricts to dense woody forest; filters out agricultural grass |

> **CanopyDeficit note:** B12 (2190 nm) and B8A (865 nm) straddle the primary liquid-water absorption features in leaf mesophyll. Elevated B12/B8A indicates severe equivalent water thickness (EWT) depletion and live fuel moisture content (LFMC) deficit — the measurable spectral consequence of prolonged drought stress in needle-bearing and woody canopies. "Cellular wall collapse" is a downstream biological consequence of this moisture deficit and is not directly measurable from satellite reflectance at 20 m resolution.

#### Prior art & distinguishing claim

LFMC estimation from S2 (Yebra et al., Camps-Valls group); FMC from NDWI (Chuvieco et al. 2002). SF-EII distinguishes by combining SWIR-based EWT depletion with a ForestGate threshold that filters agricultural grasses — which also show low LFMC but are not the high-fuel-load fire hazard target. The combined gate prevents misidentification of crop senescence as forest fire hazard.

#### Known limitations

- EWT/LFMC alone does not predict ignition — wind speed, relative humidity, and aspect are critical non-spectral factors. SF-EII is a necessary screening condition, not a sufficient fire-risk determination.
- Effective on conifers and chaparral; deciduous hardwood stress signatures differ and may require threshold recalibration.
- Smoke from adjacent fires can contaminate SWIR bands; apply atmospheric correction before use.

---

### Rank 10 — WDA-CSI: Wetland Encroachment & Agricultural Intrusion Index

**Domain:** Ecosystem protection / biodiversity | **Bands:** B02, B03, B04, B05, B06, B08, B11

**Public good:** Maps the agricultural boundary edge-effect on protected wetlands — detecting illegal farming intrusion and nitrogen-driven ecological damage.

#### Formula

$$\text{WDA-CSI} = \text{EutrophicPeak} \times \text{DredgingGate}$$

| Component | Expression | Purpose |
|---|---|---|
| BSI | $((B11 + B04) - (B08 + B02)) / ((B11 + B04) + (B08 + B02))$ | Bare Soil Index |
| NDWI_Gao | $(B03 - B11) / (B03 + B11)$ | Wetland moisture gate |
| EutrophicPeak | $\text{clamp}((B06 - B04) / (B06 + B04) - 0.35,\ 0,\ 1) \times \text{clamp}((B08 - B05) / (B08 + B05) - 0.10,\ 0,\ 1)$ | Nitrogen-forced red-edge chlorophyll spike in field crops |
| DredgingGate | $\text{clamp}((\text{BSI} - 0.05) / 0.25,\ 0,\ 1) \times \text{clamp}((0.10 - \text{NDWI\_Gao}) / 0.30,\ 0,\ 1)$ | Exposed wet peat / disturbed peat dredging signal |

#### Prior art & distinguishing claim

Red-edge chlorophyll analysis for agricultural monitoring (Delegido et al.); wetland mapping via BSI/NDWI (multiple authors). WDA-CSI distinguishes by requiring the **spatial co-occurrence** of high-nitrogen crop canopy peaks (EutrophicPeak) with active peat soil disturbance (DredgingGate) at the same edge — a signature neither agricultural nor wetland indices flag in isolation, and one that identifies active encroachment rather than pre-existing agriculture.

#### Known limitations

- High red-edge values occur in mature native wetland vegetation at peak growing season; temporal change detection is needed to distinguish intrusion from stable boundaries.
- Effective during active growing season only.
- The EutrophicPeak gate may not fire in early-season crops before canopy closure.

---

## Part 2: Calibrated & Operational Baseline Slate (Ranks 11–18)

These indices adapt established spectral mechanisms to specific public-good screening workflows. Novelty is lower (S score 1–2), but operational value is high for agencies without specialist remote-sensing capacity. All formulas below are single-date screening composites; temporal change detection (delta mode) increases specificity where noted.

---

### Rank 11 — TRSI: Tailings River Shock Index

**Domain:** Mining contamination | **Bands:** B02, B03, B04, B11

**Public good:** Real-time emergency screening for mine tailings shock in downstream rivers.

#### Formula

$$\text{TRSI} = \text{RiverGate} \times \text{FerricTurbidity}$$

| Component | Expression |
|---|---|
| MNDWI | $(B03 - B11) / (B03 + B11)$ |
| NDTI | $(B04 - B03) / (B04 + B03)$ |
| RiverGate | $\text{clamp}((0.05 - B11) / 0.05,\ 0,\ 1) \times \text{clamp}((\text{MNDWI} - 0.15) / 0.30,\ 0,\ 1)$ |
| FerricTurbidity | $\text{clamp}((\text{NDTI} - 0.02) / 0.18,\ 0,\ 1) \times \text{clamp}(B04 / (B02 + 0.001) - 1.20,\ 0,\ 1) / 0.40$ |

**Prior art:** NDTI (Lacaux et al. 2007); ferric iron B04/B02 ratios (established). TRSI claim: a decision-ready river-shock screening composite combining both in a dual gate for mine-context use.

**Limitation:** Cannot distinguish tailings turbidity from natural flood-pulse sediment without a pre-event temporal baseline. Whitecaps and foam can pass the RiverGate in coastal reaches.

---

### Rank 12 — CSRC: Cyanotoxin Scum Risk Composite

**Domain:** Small-water public health | **Bands:** B03, B04, B05, B08, B11

**Public good:** Surface scum triage for small lakes, farm dams, and recreational reservoirs with limited monitoring budgets.

#### Formula

$$\text{CSRC} = \text{WaterGate} \times \text{NDCIsignal} \times \text{ScumBrightness}$$

| Component | Expression |
|---|---|
| MNDWI | $(B03 - B11) / (B03 + B11)$ |
| NDCI | $(B05 - B04) / (B05 + B04)$ |
| WaterGate | $\text{clamp}((\text{MNDWI} - 0.10) / 0.30,\ 0,\ 1)$ |
| NDCIsignal | $\text{clamp}((\text{NDCI} - 0.02) / 0.18,\ 0,\ 1)$ |
| ScumBrightness | $\text{clamp}((B08 - 0.08) / 0.12,\ 0,\ 1)$ |

**Prior art:** NDCI (Mishra & Mishra 2012). CSRC claim: a public-health triage workflow, not the invention of chlorophyll detection.

**Limitation:** NDCI responds to all chlorophyll, not phycocyanin specifically. Dense green algae blooms will trigger the index. ScumBrightness threshold is size-dependent; sparse scum below the NIR detection threshold will be missed.

---

### Rank 13 — SWRI: Sewage-Water Release Index

**Domain:** Civic sanitation | **Bands:** B03, B04, B05, B11

**Public good:** Screening for raw sewage or blackwater discharge events in urban rivers and drainage canals.

#### Formula

$$\text{SWRI} = \text{WaterGate} \times \text{TurbidityPulse} \times \text{OrganicProxy}$$

| Component | Expression |
|---|---|
| MNDWI | $(B03 - B11) / (B03 + B11)$ |
| NDTI | $(B04 - B03) / (B04 + B03)$ |
| NDCI | $(B05 - B04) / (B05 + B04)$ |
| WaterGate | $\text{clamp}((\text{MNDWI} - 0.15) / 0.30,\ 0,\ 1)$ |
| TurbidityPulse | $\text{clamp}((\text{NDTI} + 0.05) / 0.20,\ 0,\ 1)$ |
| OrganicProxy | $\text{clamp}((\text{NDCI} + 0.05) / 0.20,\ 0,\ 1)$ |

**Prior art:** Water quality turbidity retrievals (established); NDCI for organic bloom initiation. SWRI claim: a civic sanitation screening composite that separates high-turbidity, high-organic-load discharge from ordinary muddy water.

**Limitation:** Agricultural runoff (soil + fertilizer) produces a nearly identical spectral signature to sewage. Urban spatial context (proximity to settlement, drainage channels, treatment bypass points) is the primary discriminant and cannot be encoded spectrally. Field sampling is required to confirm sewage.

---

### Rank 14 — DWCI: Drinking Water Catchment Injury Index

**Domain:** Source water protection | **Bands:** B02, B03, B04, B08, B11

**Public good:** Identifies upstream erosion sources threatening reservoir turbidity and treatment plant capacity for small utilities.

#### Formula

$$\text{DWCI} = \text{ErosionGate} \times \text{FerricSoilSignal} \times \text{VegetationAbsence}$$

| Component | Expression |
|---|---|
| BSI | $((B11 + B04) - (B08 + B02)) / ((B11 + B04) + (B08 + B02))$ |
| NDVI | $(B08 - B04) / (B08 + B04)$ |
| ErosionGate | $\text{clamp}((\text{BSI} - 0.08) / 0.22,\ 0,\ 1)$ |
| FerricSoilSignal | $\text{clamp}(B04 / (B02 + 0.001) - 1.15,\ 0,\ 1) / 0.35$ |
| VegetationAbsence | $\text{clamp}((0.20 - \text{NDVI}) / 0.25,\ 0,\ 1)$ |

**Prior art:** BSI for bare-soil erosion mapping; NDTI for reservoir turbidity. DWCI claim: the watershed-to-reservoir injury link as a single decision composite.

**Limitation:** Captures erosion sources spectrally; the hydrological connection to a specific downstream reservoir requires DEM-based flow-routing analysis not encodable in a spectral index. Interpret as a screening layer, not a causal proof.

---

### Rank 15 — LFGVI: Landfill Gas Vegetation Intrusion Index

**Domain:** Waste boundary health | **Bands:** B03, B04, B05, B8A, B11

**Public good:** Detects methane migration from landfills by mapping radial vegetation stress rings around known waste sites.

#### Formula

$$\text{LFGVI} = \text{VegetationGate} \times \text{RedEdgeStress} \times \text{CanopyDesiccation}$$

| Component | Expression |
|---|---|
| NDVI_A | $(B8A - B04) / (B8A + B04)$ |
| NDCI | $(B05 - B04) / (B05 + B04)$ |
| VegetationGate | $\text{clamp}((\text{NDVI\_A} - 0.25) / 0.30,\ 0,\ 1)$ |
| RedEdgeStress | $\text{clamp}((0.10 - \text{NDCI}) / 0.15,\ 0,\ 1)$ |
| CanopyDesiccation | $\text{clamp}(B11 / (B8A + 0.001) - 0.30,\ 0,\ 1) / 0.30$ |

> NDCI is inverted here: a low NDCI in a vegetated pixel (VegetationGate > 0) indicates reduced red-edge chlorophyll uptake — the signature of chlorotic/stressed vegetation.

**Prior art:** Vegetation stress mapping around landfill gas (established remote-sensing precedent). LFGVI claim: the radial red-edge boundary-ring composite for landfill gas screening using S2's Red-Edge 1 (B05) and narrow NIR (B8A).

**Limitation:** The spectral stress signal (chlorosis + desiccation) is non-specific — drought, disease, and herbicide exposure produce the same pixel-level signature. The **radial spatial pattern** around a known landfill point source is the diagnostic discriminant. This index requires spatial context (GIS proximity to known waste site boundaries) to reduce false positives.

---

### Rank 16 — RRFI: Riparian Refuge Failure Index

**Domain:** Drought ecology | **Bands:** B03, B05, B8A, B11, B12

**Public good:** Monitors collapse of riverbank vegetation refuges during drought and low-flow periods to guide ecological intervention.

#### Formula

$$\text{RRFI} = \text{VegetationGate} \times \text{MoistureDeficit} \times \text{DryStress}$$

| Component | Expression |
|---|---|
| NDMI | $(B8A - B11) / (B8A + B11)$ |
| VegetationGate | $\text{clamp}(B8A / (B03 + 0.001) - 1.5,\ 0,\ 1) / 1.0$ |
| MoistureDeficit | $\text{clamp}((0.10 - \text{NDMI}) / 0.40,\ 0,\ 1)$ |
| DryStress | $\text{clamp}(B12 / (B8A + 0.001) - 0.40,\ 0,\ 1) / 0.30$ |

> B04 is not in this band set, so standard NDVI cannot be computed. VegetationGate uses the NIR/Green ratio (B8A/B03) as a vegetation proxy.

**Prior art:** Riparian vegetation monitoring with NDMI and red-edge stress (multiple authors). RRFI claim: a refuge-failure composite scoring the **loss** of riverbank habitat, not general vegetation health — framing the output as an ecological sanctuary alarm rather than a standard health index.

**Limitation:** Cannot distinguish drought-induced stress from direct canopy removal (logging, grazing). Temporal change detection (NDMI delta from a reference period) is strongly recommended to increase specificity.

---

### Rank 17 — EPDI: Erosion Pulse Delivery Index

**Domain:** Storm sediment delivery | **Bands:** B02, B03, B04, B08, B11

**Public good:** Maps the coupled source-to-delivery sediment pathway after extreme rainfall events to identify estuary siltation risk.

#### Formula

EPDI operates as a **spatially selective composite** — applying different sub-indices to land and water pixels within the same image, enabling watershed-scale interpretation:

$$\text{EPDI} = \text{LandMask} \times \text{ErosionSignal} + \text{WaterMask} \times \text{SedimentSignal}$$

| Component | Expression |
|---|---|
| BSI | $((B11 + B04) - (B08 + B02)) / ((B11 + B04) + (B08 + B02))$ |
| NDTI | $(B04 - B03) / (B04 + B03)$ |
| LandMask | $\text{clamp}((B11 - 0.10) / 0.10,\ 0,\ 1)$ |
| WaterMask | $\text{clamp}((0.05 - B11) / 0.05,\ 0,\ 1)$ |
| ErosionSignal | $\text{clamp}((\text{BSI} - 0.08) / 0.22,\ 0,\ 1)$ |
| SedimentSignal | $\text{clamp}((\text{NDTI} + 0.02) / 0.18,\ 0,\ 1)$ |

**Prior art:** BSI for bare soil; NDTI for river turbidity. EPDI claim: the source-to-delivery linkage composite — a named decision workflow that combines both signals in a spatially selective formulation, interpretable as a watershed sediment pulse map.

**Limitation:** The additive land/water formulation means EPDI is interpretable only as a **watershed-scale mosaic**, not as a per-pixel absolute index. The analyst must know which pixels are erosion sources and which are delivery channels. DEM-based flow routing is required to trace the implied hydrological connection.

---

### Rank 18 — HSAI: Heat-Shelter Absence Index

**Domain:** Urban heat vulnerability | **Bands:** B04, B08, B8A, B11

**Public good:** Broad screening of urban areas lacking shade and surface moisture as a heat vulnerability proxy for planning campaigns.

#### Formula

$$\text{HSAI} = \text{ImpervGate} \times \text{VegetationAbsence} \times \text{MoistureAbsence}$$

| Component | Expression |
|---|---|
| NDBI | $(B11 - B08) / (B11 + B08)$ |
| NDVI | $(B08 - B04) / (B08 + B04)$ |
| ImpervGate | $\text{clamp}((\text{NDBI} - 0.05) / 0.25,\ 0,\ 1)$ |
| VegetationAbsence | $\text{clamp}((0.20 - \text{NDVI}) / 0.25,\ 0,\ 1)$ |
| MoistureAbsence | $\text{clamp}(B11 / (B8A + 0.001) - 0.50,\ 0,\ 1) / 0.30$ |

**Prior art:** NDBI impervious surface mapping (Zha et al. 2003); urban heat index literature (crowded). HSAI claim: an honest optical shelter-absence score that avoids claiming temperature retrieval — positioned as a planning screening tool, not a thermal measurement.

**Limitation:** NDBI false-fires on dry bare soil in semi-arid and arid regions. Apply an MNDWI > 0 exclusion gate in arid climates to suppress non-urban false positives. Ranked 18 because the domain is well-covered by Landsat LST and other established products; HSAI's primary value is credential-free, open-access screening at 10 m.

---

## Summary of Corrections Applied

| Issue | Resolution |
|---|---|
| Missing formulas for all 18 indices | Added complete mathematical expressions for Ranks 11–18; confirmed/cited existing formulas for Ranks 1–10 |
| "Blackbody" for charcoal | Corrected to "near-total absorber (absorptivity > 0.95 across VNIR-SWIR)" |
| "Ray-scattering Topographic Shadow Proxy" for B04/B02 | Renamed ChromaticSlopeProxy; mechanism corrected to slope-orientation chromatic gradient, not shadow detection |
| "Anoxic reduced-iron soil chemistry" for B02/B04 | Corrected to "Fe²⁺ speciation proxy consistent with reducing/waterlogged conditions" with explicit geochemical logic |
| "Cellular wall collapse" for SWIR ratios | Corrected to EWT depletion / LFMC deficit with explanation of what S2 SWIR bands actually measure |
| "Landsat thermal is too coarse (100m)" | Corrected: 100 m native GSD, resampled to 30 m in Collection 2; limitation is block-level resolution, not 100m raw; EC-ACI is an optical proxy, not LST |
| No ranking rubric | Added explicit two-axis scoring table with tiebreaker rules |
| No prior art citations | Added prior art and distinguishing claim for every index |
| No known limitations | Added limitations section for every index |
| Part 2 described in bullets without formulas | All 8 Part 2 indices now have full formula tables |
