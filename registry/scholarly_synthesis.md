# Remote Sensing Science & Policy Guide

This guide establishes the scholarly synthesis, prior art analysis, ethical safeguards, and validation roadmaps for the Global Spectral Index Atlas. It serves as the primary scientific guardrail, outlining what can be responsibly claimed and how to transition candidate signals into trusted discoveries.

---

## 1. Scholarly Synthesis by Domain

Public satellite monitoring has historically been dominated by a few simple, robust indices (NDVI, NDWI, NBR, NDSI). However, modern multi-spectral and hyperspectral sensors provide a much richer array of environmental signals. The remote sensing literature supports the following domain-specific guidelines and constraints:

### Inland Water Quality & Coastal Health
*   **The Science**: Ratios of red, red-edge, and NIR bands are highly sensitive to chlorophyll-a, cyanobacteria biomass, and suspended sediments.
*   **The Constraint**: Optically complex inland and coastal waters (Case 2 waters) are highly localized. Suspended soils, colored dissolved organic matter (CDOM), bottom reflectance, and atmospheric correction anomalies can dominate the signal.
*   **Policy Posture**: Treat water-quality index outputs as **prioritization and screening alerts** rather than universal concentrations, unless validated by site-specific ground-truth or local algorithm calibrations.

### Vegetation Stress & Early Drought Detection
*   **The Science**: Sentinel-2's narrow red-edge bands (705 nm, 740 nm, 783 nm) and SWIR bands (1610 nm, 2190 nm) probe chlorophyll absorption and leaf equivalent water thickness (EWT). They detect physiological stress weeks before biomass decline is visible to NDVI.
*   **The Constraint**: Stomatal closure and moisture loss signals can be caused by multiple co-occurring stressors (salinity, pesticide toxicity, drought, disease).
*   **Policy Posture**: Position vegetation stress contributions as **applied decision-ready workflows** that combine spectral stress indicators with temporal and spatial context, rather than absolute physiological diagnoses.

### Soil Salinity & Surface Evaporites
*   **The Science**: Evaporated salt crusts exhibit highly elevated visible and SWIR reflectance. Hyperspectral SWIR bands (EMIT, EnMAP) can resolve mineral-specific absorptions for gypsum and sulfates.
*   **The Constraint**: Soil brightness is heavily confounded by soil texture, background tillage, organic matter, surface moisture, and vegetation cover.
*   **Policy Posture**: Salinity indices must be framed as regional risk models or alert layers, never as universal salt maps.

### Wildfire & Burn Severity
*   **The Science**: Fire drastically lowers NIR canopy scattering and elevates SWIR charcoal/soil reflectance, making the Normalized Burn Ratio (NBR) and its temporal difference (dNBR) highly reliable.
*   **The Constraint**: Charred biomass acts as a near-total absorber, suppressing both numerator and denominator in standard water/vegetation ratios and causing them to collapse on heavily burned pixels.
*   **Policy Posture**: Any new fire or post-fire hazard index must be explicitly benchmarked against established baselines (NBR, dNBR, RdNBR) and active fire thermal detections (VIIRS, GOES).

### Floating Marine Debris
*   **The Science**: Floating macro-debris accumulations increase NIR reflectance above the water background, enabling Floating Debris Index (FDI) styles of detection.
*   **The Constraint**: Standard debris indices are heavily confounded by sea foam, sunglint, cloud edges, and organic macroalgae (Sargassum).
*   **Policy Posture**: Label outputs as **suspected floating debris** rather than "plastic," using active vegetation rejection (NDVI) and SWIR polymer slopes to isolate synthetic materials.

---

## 2. Ethical Safeguards & Screening-Only Designations

Several high-utility public-good indices target sensitive domains such as informal settlement heat, landfill leakage, illegal mining, or industrial dust deposition. Because satellite screening can stigmatize communities or imply wrongdoing without ground-truth, the following indices are strictly designated as **Screening-Only**:

*   **S07 Landfill-Leachate-Stress** (Landfill leachate seeps)
*   **S10 Urban-Industrial-Dust** (Metal-bearing urban dust)
*   **S11 IllegalMining-BareWater** (Artisanal mining expansion)
*   **D08 ConflictBurn-Damage** (Structure and agricultural burns in conflict zones)
*   **D09 Camp-Heat-WaterRisk** (Refugee/IDP camp heat vulnerability)
*   **U03 InformalSettlement-Heat** (Informal settlement thermal stress)
*   **U04 StandingWater-Vector** (Mosquito/vector breeding habitat)
*   **U08 UrbanStream-Sewage** (Informal sewage / failing urban drainage)

### Required Caveat for Sensitive Maps
> **CRITICAL DISCLAIMER**: This layer is a remote-sensing screening tool. It is not legal proof of environmental contamination, disease presence, illegal activity, or unsafe living conditions. It is designed to prioritize field validation, community support, environmental justice sampling, or further public investigation. It must not be used alone for regulatory enforcement, community displacement, denial of public services, insurance underwriting, or public accusation.

---

## 3. Claim & Authorship Posture

To preserve scientific integrity and prevent overclaiming, all Remote Sensing Research contributions must adhere to a strict claim-status discipline:

### The Defensive Claim Rule
**NEVER make "first-in-history" or "invented" claims for basic physics or established spectral bands.**
The defensible claim for any novel index is:
> *A named, transparent, decision-ready composite built from established spectral mechanisms, domain gates, and confounder rejection — applied to a specific public-good screening workflow.*

### The Authorship Boundary
*   **What you DO claim**: The unique formulation (recipes), the multi-gate composite logic, the public-good decision framing, target benchmark curation, and active web-app implementation.
*   **What you DO NOT claim**: Invention of the underlying band physics, the individual spectral ratios (NDVI, NDWI) used as inputs, or the existence of the environmental hazard itself.

### Claim Classification System
Before public release, every index must be classified into its proper scientific tier:

| Status | Meaning | Publication Posture |
|---|---|---|
| **Established** | Band math or spectral ratio is already widely documented in literature. | Explainer/baseline; no novelty claim. |
| **Adaptation** | Known spectral physics or index family applied to a new public-good workflow. | Claim "new application/workflow", not new physics. |
| **Hypothesis** | Plausible spectral rationale but awaiting validation against field datasets. | Publish as experimental only; declare uncertainty. |

---

## 4. Proposed Validation Roadmap

To transition a candidate signal from a "hypothesis" into a validated "discovery," the following four-phase roadmap is established:

```
[Phase 1: Literature-to-Index Registry]
                │
                ▼
[Phase 2: Open-Source Baseline Notebooks]
                │
                ▼
[Phase 3: Multi-Geography Event Library]
                │
                ▼
[Phase 4: Peer-Review & Workflow Promotion]
```

### Phase 1: Machine-Readable Registry
Each index must be cataloged in a standardized schema detailing:
*   `id`, `target_signal`, and `sensor_compatibility`
*   `formula` (clean mathematical expressions)
*   `claim_status` (Established, Adaptation, Hypothesis)
*   `known_false_positives` (confounder lists)
*   `public_good_use_case`

### Phase 2: Open-Source Notebooks
Develop reproducible, open-access Jupyter Notebooks demonstrating index computation, cloud masking, and baseline comparisons (e.g., comparing VSI against standard NDVI, or PETI against NDCI).

### Phase 3: Labeled Event Library
Compile a diverse database of at least 100 geographically distinct, labeled events for empirical testing:
*   Harmful algal blooms with concurrent water-sampling records.
*   Documented mine tailings failures (e.g., Jagersfontein, Brumadinho).
*   State-reported brine spill locations (e.g., Texas Railroad Commission 27-site dataset).
*   EPA-reported landfill boundaries and flight-verified methane plumes.

### Phase 4: Peer Review & Fail-Safe Reporting
Publish the index performance results transparently. **Documenting failures is as critical as documenting successes** — reporting where an index false-fires prevents public-good users from overtrusting satellite maps and making erroneous policy decisions.
