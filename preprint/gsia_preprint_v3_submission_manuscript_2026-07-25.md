# The Global Spectral Index Atlas: An Open Catalog of Proposed Environmental Remote-Sensing Index Specifications Across Twelve Domains

**Daniel Bally**  
Globe & Atlas, Spring, Texas, USA  
Correspondence: dbally@gmail.com

**ESS Open Archive preprint, version 3 - July 2026**  
**Not peer reviewed**

*Version 3 supersedes version 2 (posted 21 July 2026). It corrects errors found in a 2026-07-25 review of the implementation and its Sentinel processing chain. No reported count, class, or audit outcome from version 2 changed; the corrections affect per-record descriptions and one rendering path. See Section 4.6 and the accompanying erratum.*

**ESS Open Archive record:** [https://essopenarchive.org/doc/007f7377-d063-474f-9ba0-d776c927729e](https://essopenarchive.org/doc/007f7377-d063-474f-9ba0-d776c927729e)

**Scope boundary:** This manuscript and its supplement report only the GSIA registry, its implementation state, and its Atlas-specific evidence and audit results. Methods, evidence, results, and case studies from other applications are outside scope.

## Abstract

Open Earth-observation missions have expanded the spectral, spatial, and temporal information available for environmental screening, but candidate remote-sensing methods remain dispersed across application domains and vary widely in implementation and validation maturity. We present the Global Spectral Index Atlas (GSIA), an open catalog of 91 proposed environmental remote-sensing index specifications spanning twelve domains and organized into 24 capability families. Each record documents an intended observable, proposed and implemented formulas where applicable, required sensors and operators, physical rationale, anticipated confounders, contribution class, method role, maturity, and an explicit inference limit. The version 2 registry contains 37 live M3 screening proxies, 16 M2 executable but non-live formulas, and 38 M1 specified concepts or retired formulas. Method roles identify 15 primary representatives, 10 variants, 12 components, one reference product, 51 research models, and two retired records; these roles organize the catalog and do not establish novelty or performance. All 37 renderable evalscripts passed static band and output checks. A public-service display audit returned nonblank overlays for all 37; the one record whose script was subsequently corrected was re-audited and retained its verdict. All 42 evidence packs associated with the 37 live records and five separate Sentinel-1 or Sentinel-5P demonstrations met the registry's source-coverage rule. These are software, display, and provenance results, not measurements of environmental detection performance. No catalog entry has completed the independent, held-out accuracy assessment defined in this paper. Targeted prior-art review identified related methods in several showcased domains, so catalog-wide priority and "first formula" claims are not made. GSIA is therefore presented as a transparent hypothesis and specification registry rather than a collection of validated detectors. Version 3 additionally reports a structured review that found seven records overstating their required sensors, four whose implemented formula did not match their executing code, one incorrect physical rationale, and a scene-dependent radiometric offset defect in one rendering path; all are corrected and documented here as a demonstration of the registry's intended correction pathway. We define a validation protocol using explicit labels, hard negative controls, locked formulas, geographic and temporal holdouts, established baselines, uncertainty estimates, and external replication. The catalog is intended to make environmental remote-sensing hypotheses inspectable, testable, and correctable, not to replace field measurement or regulatory assessment.

**Keywords:** spectral index; Earth observation; environmental monitoring; Sentinel; imaging spectroscopy; hypothesis registry; validation; open science

## 1. Introduction

Open Earth-observation missions now provide complementary optical, radar, thermal, atmospheric, and imaging-spectroscopy observations. Their spatial resolution, revisit interval, coverage, processing level, and uncertainty vary substantially by sensor, latitude, acquisition plan, cloud conditions, and product. These observations create opportunities for environmental screening, but the existence of a potentially informative band or physical relationship does not by itself establish a target-specific detector.

Spectral-index research is extensive. Normalized band combinations have been used for vegetation monitoring since at least Tucker (1979), and community resources such as the Awesome Spectral Indices catalog provide a structured vocabulary and machine-readable registry for established indices (Montero et al., 2023). Domain literatures also contain retrieval algorithms, threshold rules, classifiers, time-series methods, and data-fusion workflows for water quality, fire, minerals, methane, wetlands, marine debris, and other applications. However, candidate methods are not always documented in a common form that distinguishes their intended observable, formula, prerequisites, implementation state, confounders, and validation evidence.

The Global Spectral Index Atlas (GSIA) was created to address that documentation problem. It assembles 91 proposed environmental remote-sensing index specifications across twelve domains in a single open registry. The Atlas is deliberately broader than a catalog of established normalized differences. Entries may be simple ratios, gated rules, temporal-change measures, multi-sensor combinations, or research specifications for newer imaging-spectroscopy missions. The common unit is therefore an **index specification**: a documented and testable mapping from declared observations and preprocessing to an output intended for a stated screening purpose.

Version 1 of this preprint described all 91 entries as novel spectral indices and organized them with a T1/T2/T3 priority taxonomy. Subsequent implementation, evidence, formula, and prior-art audits showed that this framing combined four questions that must remain separate:

1. Is the record useful and clearly specified?
2. Is the advertised calculation implemented and executable?
3. Is the formulation scientifically distinct from earlier methods?
4. Does it perform accurately and transfer across places and times?

Version 2 corrected that category error. It reported the Atlas as a catalog and hypothesis-registry contribution, not as evidence that 91 target-specific detectors have been discovered or validated. It also treated the current interactive deployment as an auditable research interface rather than an accuracy study.

Version 3 retains that framing unchanged and adds a second class of correction. The version 2 audit verified that each record was internally complete and that each live script declared the bands it referenced. It did not verify that a record's stated sensor requirements matched the sensors its code actually samples, that its implemented formula matched the expression the code evaluates, or that the reflectance conversion feeding those expressions was radiometrically correct. A review on 25 July 2026 tested all three and found failures in each. Section 4.6 reports them in full.

This paper has four objectives. First, it defines the scope and record structure of GSIA. Second, it reports a reproducible July 2026 inventory and software/provenance audit. Third, it replaces priority tiers with independent contribution and maturity dimensions. Fourth, it defines the evidence required to promote a proposal from an executable visualization to an independently evaluated method.

## 2. Atlas design and scope

### 2.1 Registry contents

GSIA contains 91 records grouped into twelve environmental domains (Table 1). Long-established general-purpose indices such as NDVI, NDWI, NBR, and NDSI are excluded as standalone entries, although proposed records may use them as components. The five established Sentinel-1 and Sentinel-5P demonstrations in the Limn interface are also excluded from the count of 91 because their purpose is to demonstrate sensor access and rendering, not to claim new formulations.

**Table 1. Domain coverage in GSIA version 2. Counts sum to 91.**

| Domain | Count | Typical observation families |
|---|---:|---|
| Wildfire | 7 | Multispectral reflectance, canopy moisture context, aerosol products |
| Freshwater quality | 11 | Water color, turbidity context, surface temperature, optical change |
| Marine and coastal | 10 | Floating material, oil and sediment context, coastal water color |
| Agriculture and food security | 7 | Vegetation condition, red-edge response, water and heat stress |
| Mining and industrial | 8 | Iron minerals, surface disturbance, thermal and deformation context |
| Urban and infrastructure | 8 | Heat, impervious surface, vegetation stress, industrial context |
| Permafrost and Arctic | 7 | Freeze-thaw, surface water, thermokarst, snow and vegetation context |
| Tropical forest | 6 | Disturbance, liana context, canopy condition, edge and loss patterns |
| Dryland and arid systems | 6 | Bare soil, crust, erosion, salinity, dust-source context |
| Wetland and peatland | 6 | Inundation, hydroperiod, vegetation moisture, water-table hypotheses |
| Hyperspectral applications | 8 | Mineral and material absorption features, pigment hypotheses |
| Cross-sensor fusion | 7 | Radar-optical, atmospheric-surface, thermal-optical combinations |
| **Total** | **91** | |

Each version 2 registry record contains or explicitly statuses the following fields:

- identifier and full name;
- environmental domain and intended screening use;
- direct observable, meaning the quantity calculated from the declared data;
- proposed formula or processing specification and, where present, the implemented formula;
- sensor, product, band, unit, and preprocessing requirements;
- spatial, temporal, meteorological, or ancillary inputs;
- physical rationale and closest known methods;
- capability family, method role, provisional contribution class, implementation maturity, and evidence status;
- anticipated confounders;
- an inference limit stating what the output cannot establish;
- formula version, authorship, and change history.

This structure is the Atlas's primary design contribution. It makes incomplete records visible. A scientifically interesting concept may be retained at an early maturity state, but it is not presented as a deployed or validated result.

### 2.2 What an Atlas output means

An Atlas output is a screening variable or visualization unless an entry-specific study establishes a stronger interpretation. Three levels of statement must be distinguished:

1. **Direct observation:** what the input product and formula calculate, such as a reflectance ratio, single-band aerosol-index value, backscatter difference, or temporal change.
2. **Proxy interpretation:** the physical or empirical condition hypothesized to influence that calculation, such as canopy dryness, suspended material, mineral assemblage, or surface change.
3. **Environmental inference:** the target condition a user may wish to infer, such as hazardous debris-flow susceptibility, toxin production, pollutant attribution, structural failure, pH, or carbon stock.

Most current GSIA entries connect levels 1 and 2 through physical reasoning. The connection from level 2 to level 3 generally remains to be calibrated and tested. The formula is therefore not equivalent to the environmental conclusion.

### 2.3 Observable and inference-limit clauses

Every entry should publish two paired clauses:

- **Observable clause:** a plain-language statement of what the sensor and method directly compute.
- **Inference limit:** the conditions, causes, concentrations, risks, future outcomes, or regulatory conclusions that cannot be established from that observable alone.

For example, a vegetation-stress output may identify an unusual spectral response, but it cannot by itself distinguish drought, disease, root-zone gas exposure, soil compaction, salinity, chemical exposure, or management history. Remote sensing of landfill-gas-related vegetation stress predates GSIA and was explicitly recommended as a complement to field measurements and site information, not a stand-alone gas measurement (Jones and Elgy, 1994). The paired-clause design preserves this distinction in every record.

### 2.4 Contribution types

Version 2 replaces the earlier T1/T2/T3 priority taxonomy with three neutral contribution types. These describe what GSIA contributes without asserting absence of earlier work.

| Code | Contribution type | Meaning |
|---|---|---|
| C1 | Proposed formulation | GSIA documents a named formula or workflow; scientific priority is not asserted |
| C2 | Adapted formalization | GSIA converts prior qualitative, fragmented, or differently scoped methods into an explicit specification and documents the adaptation |
| C3 | Sensor-enabled implementation concept | GSIA specifies how newer open observations could operationalize prior physics or methods |

Contribution type is independent of scientific performance. A C2 adaptation can eventually outperform a C1 proposal, and a C1 proposal can fail empirical testing.

### 2.5 Maturity states

GSIA also adopts a staged maturity scale (Table 2). The scale separates documentation, execution, demonstration, evaluation, and replication.

**Table 2. GSIA maturity scale.**

| Code | State | Minimum evidence |
|---|---|---|
| M0 | Concept | Intended observable and rationale documented |
| M1 | Formula specified | Inputs, preprocessing, and equation or workflow documented |
| M2 | Executable | Code parses and runs on its declared data |
| M3 | Demonstrated | Reviewed example rendering with date, location, data provenance, and event context |
| V1 | Independently evaluated | Locked method tested against labeled positives, hard negatives, and held-out geography or time, with uncertainty and metrics |
| V2 | Externally replicated | Independent data or team reproduces useful performance |

Maturity codes do not imply novelty. M3 does not imply accuracy. A record can regress in maturity if a previously executable dependency or data service becomes unavailable, and validation can be superseded if later evaluation identifies failure modes.

### 2.6 Capability families and method roles

The 91 records are organized into 24 capability families defined by a shared physical question or decision context. Families are the primary navigation structure; the twelve domains remain a complementary application view. This prevents small algebraic variants, supporting components, and future workflows from being presented as 91 independent inventions.

Every record also carries one method role. A **primary** record is the clearest current representative of a capability family, not a validated winner. A **variant** is an alternate formulation or target interpretation. A **component** is useful context or an input that is weaker as a standalone decision product. A **reference** is an established sensor product retained for interpretation. A **research model** requires retrieval, calibration, temporal, spatial, or cross-sensor operations not implemented as a current Atlas result. A **retired** record is preserved for traceability but removed from live scientific use.

Formula schema version 2.0 further separates the proposed formula from the implemented formula. This distinction is essential for specifications that name terrain, rainfall, time change, spatial aggregation, inversion, or field calibration that a current single-scene per-pixel script does not compute.

## 3. July 2026 audit methods

### 3.1 Audit scope and snapshot

The release audit used the Atlas registry, Limn Atlas deployment, renderable evalscripts, automated test suite, event-source links, reviewed bookmarks, and associated public research documentation as reconciled on 21 July 2026. The version 2 audit ran against source snapshot `e50c2eda5cf405c7693e5210e04894c691e5f2eb`. The version 3 corrections in Section 4.6 were applied and re-verified against snapshot `fd00b890c16105d2e011f85d9e182ec5b709ab57`, tagged `gsia-v3-audit`, which is the snapshot this version describes. That implementation repository has since been made private; an independently verifiable copy of every Atlas-relevant file at that exact snapshot is public at the `gsia-v3-audit` tag in [globe-and-atlas/limn-atlas](https://github.com/globe-and-atlas/limn-atlas/tree/gsia-v3-audit), confirmed file-for-file identical before that tag was created (see the availability list). Counts are properties of those versioned snapshots, not permanent properties of the project. The complete entry-level inventory is supplied with this preprint.

The audit addressed five questions:

1. How many records are live M3 visualizations, M2 executable formulas, or M1 specified concepts and retirements?
2. Do live scripts declare the bands they use and return the expected output structure?
3. Does every record have a capability family, method role, contribution class, maturity state, and formula version?
4. What do the evidence links and bookmarked examples actually establish?
5. Do representative priority claims survive targeted search for closely related methods?

### 3.2 Deployment classification

Records were classified by the reconciled registry and the calculation presented in the interactive deployment:

- **Live catalog visualization:** the application requests and renders the entry's declared calculation from a public satellite service.
- **Non-live executable formula:** entry-specific executable code exists, but the catalog does not currently expose it as a live layer.
- **Specified concept or retired formula:** the entry remains a documented M1 research object but is not presented as a current live calculation. This class includes explicitly retired legacy formulas.

The M1 class is not a judgment that the scientific question is meaningless. It indicates that the declared workflow is not a current executable Atlas result, or that a prior implementation was retired because its formula could not support its advertised interpretation.

### 3.3 Software checks

Static checks compared bands referenced in each of the 37 renderable evalscripts with its declared inputs and checked the returned output structure. Formula-schema tests checked the version 2 metadata, live-formula reconciliation, retirement rules, and declared implementation states. Capability-family tests required complete family membership, stable method-role counts, no orphaned families, non-live status for research and retired records, and the presence of family, domain, and research navigation. A focused LFMPI test examined water rejection and the live-vegetation gate.

Version 3 adds three checks that the version 2 audit did not perform, each of which compares a *declared* property against the *executing* code rather than against the schema:

1. **Declared inputs against sampled inputs.** Every sensor named in a record's required inputs must be sampled by its evalscript. A record may not advertise an instrument it does not read.
2. **Implemented formula against executing expression.** The implemented-formula field must reproduce the arithmetic the code evaluates, including gates, coefficients, and thresholds. A prose description does not satisfy this check.
3. **Radiometric conversion.** Each rendering path must convert digital numbers to surface reflectance using the offset appropriate to the scene's processing baseline.

These checks answer whether software is internally runnable and whether its documentation describes it accurately under the tested conditions. They do not answer whether a formula retrieves the intended physical variable, separates a target from confounders, or transfers to new scenes.

### 3.4 Evidence and bookmark review

The interactive system associates live layers and demonstrations with incident or domain sources, a reviewed location and search-window end date, and a saved view. Link availability was checked for 42 evidence packs: 37 live catalog visualizations and five separate established-sensor demonstrations. A Gold-ready evidence pack requires at least three reachable incident or domain sources; method references and technical sensor or WMS links are recorded separately.

The public WMS display audit requested a 512 by 512 pixel tile for each of the 37 live records using a 15-day search window ending on the stored bookmark date and a maximum cloud-cover setting of 30%. Automated visibility, high-signal coverage, and luminance criteria categorized the returned overlay. The stored bookmark date is therefore a search-window endpoint, not necessarily an image acquisition date. Actual acquisition timestamps must be reported from catalog metadata, such as Copernicus Data Space Ecosystem STAC records, when an article or case study discusses a specific scene.

The evidence model was interpreted conservatively. A news report, agency page, or event database can establish that an event occurred in a general place and period. It cannot establish pixel-level labels, causal correspondence, absence of confounders, or detector accuracy. Likewise, the bookmark quality-control approach measures rendering properties such as visibility, brightness, chroma, and coverage. Those are display-quality variables, not true-positive, false-positive, or calibration statistics.

### 3.5 Targeted prior-art review

The review searched representative high-claim examples by environmental target, physical mechanism, sensor family, formula structure, and retrieval task rather than by proposed acronym alone. This was a targeted falsification exercise, not a systematic review of all 91 records.

The review found close or relevant earlier work for live fuel moisture estimation (Yebra et al., 2018), floating plastic and natural-debris discrimination (Biermann et al., 2020), landfill-gas-related vegetation stress (Jones and Elgy, 1994), coral mapping and bleaching limits with Sentinel-2-class observations (Hedley et al., 2012), acid-mine-drainage mineral and pH mapping using field-informed spectroscopy (Zabcic et al., 2014; Soydan et al., 2021), liana infestation mapping (Waite et al., 2019; Chandler et al., 2021), and Sentinel-2 methane plume retrieval (Varon et al., 2021). These findings are sufficient to reject catalog-wide claims of established priority. They are not sufficient to determine the exact contribution type of every entry.

### 3.6 Definition of scientific validation

For this paper, a method reaches V1 only when an entry-specific evaluation includes:

- a locked formula, preprocessing chain, threshold policy, and version;
- independent target labels with spatial and temporal alignment rules;
- representative positives and hard negatives;
- separation of development, threshold-tuning, and held-out test data;
- geographic or temporal holdout, preferably both;
- comparison with established baselines and simpler ablations;
- uncertainty and sensitivity analysis;
- task-appropriate metrics, including error rates rather than selected examples only;
- explicit failure cases and a documented domain of applicability.

For continuous variables, validation should report calibration and residual statistics such as bias, MAE or RMSE, uncertainty intervals, and stratified performance. For detection or classification, it should report a confusion matrix, precision, recall, specificity, and precision-recall behavior at declared operating points. Area estimates should use probability-based sampling and good-practice accuracy-adjustment methods where relevant (Olofsson et al., 2014). Spatially clustered observations require blocked or environmental cross-validation rather than random pixel splits (Roberts et al., 2017).

## 4. Audit results

### 4.1 Deployment inventory

The 91 proposed records divide into three implementation classes (Table 3).

**Table 3. Reconciled registry and implementation state on 21 July 2026.**

| State | Count | Maturity interpretation |
|---|---:|---|
| Live catalog visualizations | 37 | M3; demonstration is not validation |
| Non-live executable formulas | 16 | M2 |
| Specified concepts or retired formulas | 38 | M1 |
| **Total catalog entries** | **91** | |
| Separate established-sensor demonstrations | 5 | Excluded from the 91 and from contribution claims |

The five separate demonstrations are three Sentinel-1 examples and two Sentinel-5P examples. Keeping them outside the 91 is scientifically useful because it distinguishes demonstration of a known sensor product from a proposed Atlas formulation.

The 91 records are distributed across 24 capability families. Method roles comprise 15 primary records, 10 variants, 12 components, one reference, 51 research models, and two retired records. Provisional contribution classes comprise 68 C1, 22 C2, and one C3 record. Contribution classification remains subject to entry-level prior-art review and does not assert scientific priority.

### 4.2 Software results

All 37 renderable catalog evalscripts passed the static band-declaration and output-shape audit with zero flags, both at the version 2 snapshot and after the version 3 corrections. Formula-schema, retirement, live-formula reconciliation, capability-family, and focused LFMPI tests also passed. The public WMS audit returned a nonblank overlay for all 37 live records at the version 2 snapshot, and each met the script's automated "strong" display threshold in that run.

One record, DLPEHI, had its evalscript corrected after that audit (Section 4.6). Because a display verdict must describe the script that produced it, its carried-forward result was discarded and the record re-audited on 25 July 2026 under identical settings: the same public endpoint and layer, a 512 by 512 pixel tile, a 15-day window ending on the stored bookmark date, and a 30% maximum cloud-cover setting. The re-audit returned visible coverage of 57.392% and high-signal coverage of 55.602%, against 58.800% and 57.658% before the correction, with an identical 99th-percentile luminance of 0.666. The verdict remains "strong". Substituting the blue band for the green band in that record's bare-soil term therefore changed its rendered output only marginally. The remaining 36 verdicts are unchanged and still describe their current scripts, so the supplement reports a display verdict for all 37 live records.

The renderable audit certifies the 37 live evalscripts. It does not certify every proposed external workflow among the 54 non-live records, and this paper therefore makes no 91-of-91 execution claim. WMS rendering is also service-, date-, cloud-, and configuration-dependent. These results support current code consistency and display availability under the declared audit settings; they do not support accuracy, specificity, transferability, causal attribution, or operational-reliability claims.

### 4.3 Evidence and provenance results

At audit time, all 42 live or demonstration evidence packs met the three-reachable-source rule. The 42 comprise 37 live Atlas records and five separate established-sensor demonstrations. Link reachability changes over time and should be maintained through archived copies or persistent identifiers where licensing permits.

The event-source packs are valuable provenance. They help reviewers inspect whether a date and location are plausibly connected to the intended use case. They do not provide pixel labels or matched controls. The terms **event documentation** and **reviewed display example** are therefore used in place of **validation evidence** and **validated peak-signal bookmark**.

### 4.4 Formula-claim concordance

The audit found several places where an entry's live calculation, name, or public description implied more than the current implementation could establish. Table 4 gives representative corrections. These corrections are not removals; they define the experiments needed to make each proposal useful.

**Table 4. Representative specification and claim corrections.** Rows above the divider were identified in the version 2 audit; rows below it in the version 3 review of declared-versus-executing properties (Section 4.6).

| Entry | Current observable or state | Defensible interpretation | Evidence needed for stronger claim |
|---|---|---|---|
| BH-DFSI | Live post-event multispectral context; current script lacks the advertised terrain, rainfall, and moisture gates | Burn-scar and surface-context visualization, not debris-flow susceptibility or evacuation guidance | DEM and rainfall integration; inventories of debris flows and stable burned slopes; held-out watershed evaluation |
| SF-EII | Retired M1 legacy expression; its `1 - B08/B12` factor has an unstable physical direction over vegetation | Traceable canopy-moisture calibration specification; removed from live scientific use | Rebuild from a seasonal moisture deficit and field live-fuel-moisture measurements across species and biomes |
| LFMPI | Live M3 `FuelGate × WaterReject × (1 - NDMI) / 2` | Normalized NDMI-deficit screening proxy over live vegetation; not percent LFMC, ignition probability, or fire danger | Field LFMC, species and season strata, geographic holdouts, and comparison with Yebra et al. (2018) and simpler indices |
| SACI | Live display of a single TROPOMI ultraviolet aerosol-index product | Absorbing-aerosol context layer | Implement the proposed multi-variable method; collocated aerosol and combustion labels; uncertainty and plume-transport controls |
| RDOCI | PACE research specification without implemented field-calibrated retrieval | Candidate DOC/CDOM-related ocean-color hypothesis | Atmospheric correction, in-water radiometry, field DOC and CDOM, regional and seasonal holdouts |
| CTPSTI | Pigment/composition concept | Candidate phytoplankton pigment or composition hypothesis; not a toxin or species determination | Taxonomic and toxin assays, mixed-community experiments, optical water-type controls |
| AMDPHI | Retired M1 visible ratio-of-ratios; denominator instability and missing field calibration prevent defensible pH interpretation | Traceable AMD mineral and field-chemistry calibration specification; no current pH retrieval | Field pH, mineralogy, spectral libraries, atmospheric correction, a stable feature design, and comparison with field-informed methods |
| TDSII | Cross-sensor specification | Tailings change-monitoring hypothesis, not a deployed failure-warning system | Co-registered InSAR and optical time series, documented incidents and stable sites, prospective evaluation |
| PWTDI | Formula-specified and non-live | Peatland water-table hypothesis | Logger calibration, seasonal and vegetation controls, site holdouts |
| FGDCI | Executable but non-live | Freeze-thaw research specification | Comparison with established SAR freeze-thaw methods and in situ soil-state observations |
| TPERI | Live single-scene layer | Surface-water or pond-context visualization; not a rate or velocity measurement | Locked two-date or time-series workflow, registration and uncertainty analysis, mapped erosion boundaries |
| CMSTI, AFCDI, REENBI | Imaging-spectroscopy concepts | Mineral/material screening specifications | Sensor-bandpass simulation, atmospheric correction, spectral libraries, mixed-pixel tests, field samples |
| TSEAI | Land-cover fractions combined with atmospheric context | Source-context hypothesis; land-cover fractions do not attribute methane emissions | Methane retrieval, winds, plume transport, background model, source inventory, uncertainty, independent sites |
| NFCAI | NISAR-optical fusion concept | Forest-biomass or carbon-estimation hypothesis | Biomass plots, sensor calibration, saturation analysis, allometric uncertainty, geographic holdouts |
| *— version 3 review —* | | | |
| DLPEHI | Live layer gates sparse-vegetation NDVI and intermediate NDWI, then scales a bare-soil index; the advertised NDTI term was never implemented and no rainfall input exists | Dryland surface-context screening, not locust-habitat or outbreak warning | Rainfall history, soil texture, ground locust survey records, held-out regions and seasons |
| LISI | Live NIR/SWIR contrast scaled by an EVI-style denominator that includes an undocumented B11 term and a NIR:SWIR1 ratio | Canopy structural contrast, not liana infestation mapping | Crown-level infestation labels, geographically blocked evaluation, comparison with Waite et al. (2019) and Chandler et al. (2021) |
| NPDefI | Live red/red-edge contrast differenced against a SWIR2/SWIR1 contrast over vegetation; the prior rationale attributed the SWIR term to anthocyanins, which have no SWIR2 feature | Crop-stress contrast proxy, not nitrogen-versus-phosphorus discrimination | Measured tissue nutrient concentrations, crop and cultivar strata, phenology, soil-background controls |
| SMPDI | Live floating-material contrast whose baseline is interpolated B04 to B12, not the B04 to B11 pairing used in common Sentinel-2 FAI implementations | An FAI variant for floating-material context, not Sargassum-versus-plastic discrimination | Labeled floating-material references and comparison against FDI-based classification (Biermann et al., 2020) |
| IPVSI, WVTDI | Live single-date layers that published prose descriptions in place of an implemented formula | Dense-canopy and vegetation-water context proxies with stated equations | Multi-date series, surveyed stands of the target communities, seasonal controls |
| OWSI, SABSI, MEPSI, MHSSP | Live Sentinel-2 layers that named EMIT, Planet, or TROPOMI among their required inputs while sampling no such data | Sentinel-2 context proxies; the additional instruments describe the proposed experiment, not the current layer | The named instrument, plus the calibration and labels specific to each target |

NISAR launched on 30 July 2025, not in 2024 (NASA/JPL, 2025). NFCAI is therefore described as a post-launch research concept; neither sensor availability nor spatial sampling establishes global 10 m forest-carbon accuracy.

### 4.5 Novelty and priority result

The earlier Atlas acronym audit successfully found naming collisions and improved identifiers. It was a naming-collision audit, not a prior-art review. Exact-name absence cannot establish scientific priority because equivalent methods may use different names, bands, algebra, thresholds, or problem language.

The targeted review found sufficient related work to invalidate the catalog-wide statements "91 novel spectral indices," "first formula," and "first standardized formula." No claim is made here that every record lacks originality. Instead, priority is recorded as **not established** until an entry-level dossier:

1. identifies the closest pre-existing methods;
2. compares intended observables, inputs, preprocessing, algebra, and validation target;
3. states the substantive difference;
4. distinguishes scientific contribution from naming, packaging, or software formalization; and
5. is reviewed by a domain specialist.

The remaining original contribution is substantial but different: GSIA is a cross-domain, open, inspectable architecture for turning environmental remote-sensing ideas into versioned specifications with visible limits and maturity. The 24-family structure and explicit method roles make redundancy inspectable by separating a family's primary representative from variants, components, references, research models, and retired records.

### 4.6 Corrections since version 2

Section 7.4 requires each release to publish a change log. This section is that
log for version 2 to version 3. Every correction below moves a claim toward what
the code does; none arises from new data or a changed scientific position.

**No reported quantity changed.** The registry still contains 91 records in 24
capability families across twelve domains, with 37 M3, 16 M2, and 38 M1 entries;
15 primary, 10 variant, 12 component, one reference, 51 research-model, and two
retired roles; and 68 C1, 22 C2, and one C3 provisional contribution class. All
37 renderable evalscripts still pass the static band and output audit with zero
flags. No record changed maturity, method role, contribution class, capability
family, or render state.

**Seven records overstated their required sensors.** SMPDI, OWSI, NPDefI, SABSI,
MEPSI, DLPEHI, and MHSSP named EMIT, EnMAP, Planet, GPM, or TROPOMI among their
inputs while their evalscripts sampled Sentinel-2 alone. Because the required-inputs
field defaulted to the platform string, the version 2 supplement reproduced the
overstatement. Each record now declares Sentinel-2 L2A as its required input, and
the additional instrument is stated in the proposed formula, where it describes the
experiment needed to promote the record. SACI is unaffected: it renders a genuine
TROPOMI product.

**Four implemented formulas did not describe the executing code.** LISI published a
denominator omitting a `B11` term the code evaluates, so the expression is not the
EVI denominator its shape suggests. DLPEHI advertised an `NDTI > -0.2` term that was
never implemented, because NDTI requires a band the script does not load; a bare-soil
index stood in for it, and the published NDVI window differed from the coded one.
IPVSI and WVTDI published prose in the implemented-formula field, which is not
reproducible. All four now state the expression the code evaluates, with the target
interpretation moved to the proposed formula.

**One physical rationale was incorrect.** NPDefI attributed its SWIR2 term to
anthocyanin accumulation under phosphorus limitation. Anthocyanins absorb near 500
to 550 nm and have no SWIR2 absorption feature; the SWIR2 to SWIR1 contrast responds
to canopy water and dry-matter absorption. The nitrogen-versus-phosphorus separation
is therefore hypothesized rather than mechanistically supported, and the record is
renamed accordingly.

**One rendering path was radiometrically incorrect, intermittently.** The
Cloud-Optimized GeoTIFF provider converted digital numbers to reflectance by
dividing by the quantification value alone. Since ESA processing baseline 04.00,
operational 25 January 2022, Sentinel-2 L2A carries an additive offset of -1000.

The archive serving those assets applies that offset to most, but not all, of its
baseline 04.00 and later items, and publishes a per-item flag recording which. A
survey of the project's test area on 25 July 2026 found 38 of 589 items, or 6.5%,
carrying the offset unapplied, concentrated in 2022 and 2025 with none in 2023 or
2024. Reflectance for those scenes was 0.1 too high while neighbouring scenes were
correct, and because an additive offset does not cancel in a normalized difference
the error propagated to ratios as well as absolute thresholds.

The scene-dependent character is more consequential than the magnitude. A uniform
bias is at least internally consistent; an intermittent one makes two observations
of the same location differ by 0.1 reflectance with nothing in the output to
indicate which convention applied, which silently invalidates multi-date
comparison. No acquisition-date rule can resolve it. The offset is now read per
item from the archive flag, falling back to the processing baseline and then to
acquisition date, and is covered by a regression test.

This is a general hazard rather than a project-specific slip. Any catalog that
renders Sentinel-2 from a public cloud-optimized archive inherits the same
ambiguity, and a per-item check is the only reliable resolution.

The audit reported in Sections 4.2 and 4.3 used the public Web Map Service path,
which applies this harmonization by default, so **no result reported in version 2
depended on the affected path**. Threshold work carried out elsewhere in the project
draws its band statistics from a harmonized statistics service and was confirmed
unaffected by inspection, and a re-run of the affected renderer over the project's
own reviewed locations resolved an offset of zero for every tile, reproducing the
prior qualitative result.

The defect therefore did not reach a reported result. It is documented because it
would have corrupted any future multi-date product rendered through that path, and
because a latent defect found and closed before it propagates is the outcome the
correction pathway in Section 7.4 is intended to produce. The correction matters
prospectively: any entry-level validation study that renders from a cloud-optimized
archive must resolve the offset per item, and any absolute threshold fitted on that
path beforehand should be refitted.

**Internal consistency.** The bare-soil index had three incompatible definitions
across evalscripts; one record substituted a green band for the blue band used
elsewhere. That deviation is corrected. Because it altered the record's rendered
output, its display QC was re-run rather than carried forward; the verdict was
unaffected (Section 4.2). Two further variable
names that collided with standard index names were renamed without altering any
arithmetic.

**Provenance data.** The source-reviewed event reference file contained 21 rows whose
event dates precede the Sentinel-2 mission, the earliest by seventeen years. No
Sentinel-2 observation of those events exists at any processing level. Event dates
are now recorded separately from the Sentinel search-window date, which is null where
the event is unobservable, and nine further rows falling inside the mission but before
the dense L2A archive are flagged. This file was not read by application code at the
time of the version 2 audit, so no reported result and no user-facing view depended on
it.

**Interface.** The paired clauses required by Sections 2.3 and 7.1 are now labelled
"Observable" and "Intended use and inference limit" in the deployment. An authorship
and priority block was added: records with an explicit claim display it with their
contribution class and status, and the remainder display the registry-wide statement
that priority is not established. The author's own confidence annotations are
deliberately not displayed, because a strength badge would contradict Section 4.5.

**Interpretation.** These corrections are reported in full rather than silently
applied because they are the intended behaviour of the architecture described in
Section 7.1, not exceptions to it. A registry whose records name their inputs,
formulas, and limits explicitly is one where a mismatch between claim and code is a
findable defect. Seven overstated sensor lists and four inaccurate formulas survived
an audit that checked schema completeness; they did not survive an audit that
compared declarations against executing code. The lesson for other catalogs is that
completeness checks and correspondence checks are different instruments, and only the
second constrains what a record may claim.


## 5. Domain survey and research priorities

This section summarizes the purpose and major validation burden of each domain. The complete entry list and deployment status appear in the accompanying supplement.

### 5.1 Wildfire

The seven wildfire records address burned-slope context, fuel or canopy moisture, smoke and aerosol context, and post-fire impacts. The live deployment provides useful examples for exploring candidate signals, but the highest-consequence applications require separate evidence chains. Burn severity, rainfall forcing, slope, soil, and watershed geometry must all be represented before a burned-slope formula can be evaluated for debris-flow susceptibility. Fuel-moisture proposals must be calibrated against field measurements and compared with existing radiative-transfer and statistical approaches. Yebra et al. (2018), for example, used 360 observations from 32 sites to evaluate live fuel moisture content. A reflectance formula that behaves sensibly on synthetic samples remains several steps below that standard.

### 5.2 Freshwater quality

The eleven freshwater records include surface-temperature, reflectance, turbidity, color, and emerging PACE-related hypotheses. These records are useful as research specifications because they identify the required spectral regions and expected confounders. Their most important boundary is that water-leaving reflectance is affected by atmospheric correction, bottom effects, sun glint, adjacency, suspended sediment, colored dissolved organic matter, particle type, and concentration. Pigment relationships do not establish toxin production. DOC, nutrient, cyanobacteria, and contaminant claims require in-water sampling with acquisition-time matching and optical-water-type stratification.

### 5.3 Marine and coastal systems

The ten marine and coastal records examine floating material, coastal sediment, water color, oil-related context, and marine debris. This is a strong area for a family-level validation study because established baselines exist. Biermann et al. (2020) combined the Floating Debris Index with NDVI and reported discrimination among floating plastics and natural materials. GSIA's SMPDI and MP-PDI should therefore be evaluated as adaptations or alternatives against FDI-based classification, not presented as the first attempt to distinguish floating material. Coral-related specifications should also reflect the limits shown by Hedley et al. (2012): Sentinel-2-class measurements can improve benthic discrimination, but coral mortality and algal-cover mapping are not reliably established from a single multispectral observation.

### 5.4 Agriculture and food security

The seven agriculture records combine red-edge, vegetation, water, and heat-stress signals. Their central scientific risk is non-specificity. Nutrient limitation, water stress, heat, disease, soil background, cultivar, planting date, canopy structure, and management can produce overlapping responses. Validation should use measured nutrient, water, and yield variables; include phenology; and hold out farms, years, and crop types. Existing simple indices and operational agronomic models are necessary baselines.

### 5.5 Mining and industrial systems

The eight mining and industrial records include mineral, acidity, disturbance, and infrastructure-change hypotheses. Published AMD work demonstrates both the promise and burden of these applications. Zabcic et al. (2014) characterized surface pH and mineralogy using airborne hyperspectral data and field information; Soydan et al. (2021) used field X-ray diffraction, chemistry, and spectra to guide Sentinel-2 mineral analysis. AMDPHI is retired from live display and retained as a traceable M1 calibration specification because the prior ratio was numerically unstable and was not a direct pH measurement. A rebuilt study could still test lower-cost mineral features, but it requires field chemistry, mineralogy, stable feature design, and held-out sites. Tailings monitoring similarly requires time-aligned deformation, hydrology, optical change, engineering context, and prospective testing. High-consequence warnings require explicit false-alarm and missed-event analysis.

### 5.6 Urban and infrastructure systems

The eight urban records cover heat, imperviousness, vegetation stress, landfill context, industrial activity, and infrastructure-related screening. Urban mixtures and causal ambiguity dominate this domain. Roof materials, shadows, irrigation, traffic, seasonal vegetation, land management, and neighborhood morphology can mimic or mask target signals. The existence of airborne remote sensing for landfill-gas-related vegetation stress since at least Jones and Elgy (1994) also illustrates why priority must be determined by mechanism and task rather than acronym. Field gas measurements and site geology remain necessary for landfill-gas inference.

### 5.7 Permafrost and Arctic systems

The seven permafrost and Arctic records consider freeze-thaw state, thermokarst, pond dynamics, snow, surface moisture, and vegetation context. Radar is valuable in cloud-prone high latitudes, but backscatter is influenced by roughness, geometry, vegetation, snow, and moisture as well as phase state. Optical pond change requires co-registration, consistent seasonal windows, and uncertainty in shoreline delineation. Rate terminology should be reserved for a multi-date estimator with declared time interval and propagated positional error.

### 5.8 Tropical forest

The six tropical-forest records examine disturbance, canopy condition, liana context, and related patterns. Persistent cloud, shadow, phenology, mixed crowns, forest type, degradation history, and spatial autocorrelation complicate evaluation. Liana mapping is an active prior field, including UAV and airborne studies (Waite et al., 2019; Chandler et al., 2021). Any Sentinel-2 liana index should therefore be positioned as a testable low-cost adaptation and evaluated against crown-level labels with geographically blocked tests.

### 5.9 Dryland and arid systems

The six dryland records address soil, crust, erosion, dust, and salinity context. Bright substrates and mineral mixtures make physically plausible ratios particularly vulnerable to non-specific response. Surface moisture, roughness, gypsum, carbonate, iron oxides, vegetation cover, atmospheric dust, and view geometry should be treated as explicit strata or controls. Imaging spectroscopy may improve mineral discrimination, but spectral libraries, atmospheric correction, and mixed-pixel analysis remain essential.

### 5.10 Wetland and peatland systems

The six wetland and peatland records cover inundation, vegetation moisture, hydroperiod, and water-table hypotheses. Single-date greenness is rarely sufficient because wetland plant communities and hydrology are seasonal. Time-series phenology and radar-optical fusion are promising, but water-table-depth claims require co-located loggers and controls for vegetation structure, rainfall history, and peat properties. PWTDI is currently an M2 formula, not an operational water-table product.

### 5.11 Hyperspectral applications

The eight hyperspectral records use narrow absorption features or dense spectral shape. EMIT has provided calibrated orbital imaging spectroscopy since 2022, with on-orbit performance documented by Thompson et al. (2024). Sensor availability makes these proposals testable, but it does not establish material separability at scene scale. Validation must convolve laboratory spectra to the instrument response, model atmosphere and noise, quantify sub-pixel abundance and background sensitivity, and compare against field or laboratory reference measurements. CMSTI, AFCDI, and REENBI remain specifications rather than Atlas results.

### 5.12 Cross-sensor fusion

The seven fusion records combine atmospheric, radar, optical, thermal, land-cover, or time-series inputs. Their potential value is also their main risk: a compact expression can hide spatial support, time mismatch, product uncertainty, and causal assumptions. Methane illustrates this clearly. Sentinel-2 can support plume retrieval for sufficiently large point sources when the method accounts for background and plume physics (Varon et al., 2021). Land-cover fractions inside a coarse atmospheric pixel cannot independently attribute an enhancement. Forest biomass and carbon fusion likewise requires plots, allometry, calibration, saturation assessment, and uncertainty propagation.

## 6. Validation and promotion protocol

### 6.1 Select coherent families

Validation should proceed by small, coherent method families rather than by attempting shallow confirmation of all 91 records. A family should share a target variable, label type, sensor path, and baseline literature. Strong candidates include:

- floating-material discrimination, because field and airborne reference datasets and established FDI baselines exist;
- live-fuel-moisture estimation, because protocols and public field observations exist;
- peatland water-table estimation, because continuous logger measurements provide a direct target;
- AMD mineral/acidity screening, because field chemistry and mineralogy can separate proxy from target;
- wetland hydroperiod mapping, because multi-date water labels can be defined;
- permafrost pond-change measurement, because boundaries and rates can be evaluated explicitly.

### 6.2 Preregister the specification

Before viewing held-out test outcomes, the study should freeze:

- target variable and unit;
- formula and preprocessing;
- masks and quality flags;
- spatial support and temporal matching window;
- threshold-selection rule;
- positive and negative inclusion criteria;
- confounder strata;
- primary and secondary metrics;
- exclusion and missing-data rules.

Versioned code and a machine-readable manifest should identify the exact method evaluated.

### 6.3 Use hard negatives

Random background is not enough. Each study should include plausible confounders that share relevant spectral properties. Examples include natural woody debris for marine plastics, drought and disease for pollution-related vegetation stress, bright carbonate or gypsum for mine and dryland mineral indices, non-toxic blooms for toxin-risk hypotheses, stable burned slopes for debris-flow methods, and seasonal shoreline change for thermokarst expansion.

### 6.4 Separate development and test geography

Pixels from the same event, site, or image are not independent replicates. Development and test sets should be separated by site, event, watershed, farm, wetland, mine, or other process-relevant unit. Temporal holdout should test a later season or event. Environmental blocking should test extrapolation across climate, substrate, vegetation, or water type. Results should state whether the intended use is interpolation within a calibrated region or transfer to new regions.

### 6.5 Compare baselines and ablations

Every proposed index should be compared with:

- the strongest established method that uses comparable data;
- a simple single-band, ratio, or standard-index baseline;
- the complete proposed formula;
- ablations that remove each gate or component;
- where appropriate, a statistical or machine-learning model using the same inputs.

This design reveals whether added complexity produces real out-of-sample information rather than more visually compelling maps.

### 6.6 Report uncertainty and failure

Validation reports should include calibration plots, confusion matrices or residual distributions, threshold sensitivity, geographic and environmental stratification, missing-data behavior, and representative false positives and false negatives. A result is more useful when it defines where the method fails. Entries that do not outperform a baseline should remain in the registry with a negative or superseded status rather than disappear.

### 6.7 External replication

Promotion to V2 should require reproduction by an independent analyst, dataset, or team. The replication package should include raw-data identifiers, preprocessing configuration, labels or label-generation code, environment information, and a versioned result manifest. External replication is especially important for high-consequence applications and for indices developed from a small number of visually selected events.

## 7. Discussion

### 7.1 What remains novel, unique, and useful

The revised claim is narrower than version 1 and more defensible. GSIA's principal contribution is not the assertion that every formula has scientific priority. It is the integration of six practices that are rarely combined across many environmental domains:

1. a single open registry for 91 environmental screening hypotheses;
2. a 24-family organization with explicit primary, variant, component, reference, research-model, and retired roles;
3. separate proposed and implemented formulas tied to declared sensor products and formula versions;
4. observable and inference-limit clauses that constrain interpretation;
5. public implementation and event-context surfaces that can be inspected; and
6. independent contribution and maturity states that allow proposals, executable code, demonstrations, evaluations, negative results, retirements, and replications to coexist without being confused.

That architecture is useful even when individual proposals are later modified or rejected. It converts informal ideas into falsifiable objects, makes hidden dependencies visible, and gives domain experts a concrete target for correction. Cross-domain breadth also exposes recurring methodological problems - background confusion, temporal mismatch, causal attribution, scale mismatch, and the difference between rendering and retrieval - that can be obscured within domain-specific silos.

The Atlas additionally lowers the cost of pilot research. A candidate method can begin with an explicit record, executable prototype, known confounders, closest baselines, and a planned promotion path. This does not replace peer review or fieldwork. It makes them easier to direct.

### 7.2 What the Atlas is not

GSIA is not a catalog of 91 validated environmental detectors. It is not evidence that 91 formulas are scientifically unprecedented. A live colored layer is not a concentration map, causal diagnosis, risk forecast, or regulatory finding unless an entry-specific study supports that interpretation. The Atlas does not remove the need for atmospheric correction, geometric alignment, quality masks, field calibration, uncertainty propagation, or domain expertise.

The catalog is also not a substitute for established retrieval algorithms. Some environmental variables are inverse problems requiring radiative transfer, plume transport, allometry, or site-specific calibration. A compact index may be useful as a feature, screen, or hypothesis even when it cannot carry the final inference.

### 7.3 Limitations of this study

This version reports an internal audit performed by the Atlas author with tool-assisted review. It is not an independent peer review. The prior-art assessment was targeted toward representative high-claim entries, not a systematic search for all 91 records. Entry-level contribution classes in the supplement are therefore provisional and do not establish priority.

The evalscript audit covered the 37 renderable records. It did not execute every external retrieval, calibration, temporal, spatial, inversion, or cross-sensor workflow represented by the 54 M1 or M2 records. The WMS display audit reproduced overlays, but automated visibility and luminance thresholds cannot reproduce target labels, atmospheric artifacts, sensor noise, spatial mixtures, missing data, or environmental confounders. A strong overlay is a legible visualization, not a correct environmental inference.

The interactive deployment will change. Link availability, public data services, code, and catalog state should be versioned and re-audited for each archival release. Counts and test results in this paper apply to the 21 July 2026 release audit of the cited source snapshot, as corrected on 25 July 2026 (Section 4.6).

The corrections in Section 4.6 also bound what the version 2 audit established. Schema completeness was verified; correspondence between declaration and executing code was not, and when it was tested ten of the 91 records required correction. Readers should assume that any registry field not covered by an explicit check in Section 3.3 remains unverified, and that further correspondence checks may find further defects.

### 7.4 Research governance

Each future release should publish a change log for formulas, labels, limits, and maturity. Evidence terminology should be mechanically constrained: event sources cannot populate validation fields, display-QC cannot generate accuracy labels, and M3 cannot be promoted to V1 without a result package containing labels, controls, metrics, and a held-out design.

Entries should be correctable without implying failure of the project. A healthy registry records correction, negative evidence, and retirement. Proposed priority should remain "not established" until reviewed. High-consequence claims should receive domain-specialist review before prominent public display.

## 8. Conclusion

The Global Spectral Index Atlas version 2 catalogs 91 proposed environmental remote-sensing index specifications across twelve domains. Its contribution is an open structure for documenting intended observables, formulas, sensor requirements, implementation maturity, event context, confounders, and validation status.

A July 2026 release audit, with corrections applied on 25 July 2026, found 37 live M3 screening proxies, 16 executable but non-live M2 formulas, and 38 M1 specified concepts or retired formulas, plus five established sensor demonstrations maintained outside the 91. The 91 records are organized into 24 capability families and explicit method roles so variants, components, future workflows, and retirements are not mistaken for independent validated inventions. Software-level checks support the internal consistency of the 37 renderable scripts and current display path, while the absence of labeled controls and held-out evaluation prevents catalog-wide accuracy, specificity, transferability, or causal claims. Targeted prior-art findings also prevent a defensible catalog-wide claim of 91 scientifically novel formulas.

GSIA should therefore be used as a hypothesis and specification registry from which smaller, coherent index families can be selected for preregistered validation. Its public-good value lies in making environmental remote-sensing hypotheses inspectable, falsifiable, comparable, and correctable. Field measurement, domain expertise, uncertainty analysis, and independent replication remain the route from a promising Atlas entry to a trusted environmental method.

## Data and code availability

The versioned resources for this manuscript are:

- ESS Open Archive record: [https://essopenarchive.org/doc/007f7377-d063-474f-9ba0-d776c927729e](https://essopenarchive.org/doc/007f7377-d063-474f-9ba0-d776c927729e);
- archival Atlas concept record: [https://doi.org/10.5281/zenodo.20400743](https://doi.org/10.5281/zenodo.20400743);
- version 1 Zenodo record: [https://doi.org/10.5281/zenodo.20400744](https://doi.org/10.5281/zenodo.20400744);
- registry source: [https://github.com/globe-and-atlas/remote-sensing-research](https://github.com/globe-and-atlas/remote-sensing-research);
- human-readable catalog of all 91 formulas: [GSIA v2 Formula Catalog](https://github.com/globe-and-atlas/remote-sensing-research/blob/gsia-v3-preprint/formulas/gsia-v2-formula-catalog.md);
- machine-readable 91-record supplement (version 3): [GSIA v3 status supplement](https://github.com/globe-and-atlas/remote-sensing-research/blob/gsia-v3-preprint/preprint/gsia_preprint_v3_status_supplement_2026-07-25.csv);
- superseded version 2 supplement, retained for comparison: [GSIA v2 status supplement](https://github.com/globe-and-atlas/remote-sensing-research/blob/gsia-v3-preprint/preprint/gsia_preprint_v2_status_supplement_2026-07-21.csv);
- version 2 to version 3 erratum: [GSIA v2 erratum](https://github.com/globe-and-atlas/remote-sensing-research/blob/gsia-v3-preprint/preprint/gsia_preprint_v2_erratum_2026-07-25.md);
- version 2 audited commit: `e50c2eda5cf405c7693e5210e04894c691e5f2eb`, in the original Limn implementation repository, since made private;
- version 3 audited commit, tagged `gsia-v3-audit`: `fd00b890c16105d2e011f85d9e182ec5b709ab57`, in the same now-private repository; and
- public, independently verifiable copy of that snapshot: [globe-and-atlas/limn-atlas, tag `gsia-v3-audit`](https://github.com/globe-and-atlas/limn-atlas/tree/gsia-v3-audit) (commit `dd12f3c8e2e987480e2811599da0a11e6a23ec24`). Every file this paper's audit covers — the 91-record registry, evalscripts, authorship claims, event references, and the audit scripts in Section 3.3 — was confirmed identical between the two repositories before the tag was cut. The public repository is the citation target for independent verification; the private repository remains the source of truth for produced-water development, which is out of scope for this paper (Scope boundary, page 1).

Repository links above are pinned to the immutable tag `gsia-v3-preprint` rather than to a branch, so they resolve to the exact files described here even after later development. The human-readable catalog presents the proposed and implemented formula fields for every record, organized by capability family. The accompanying CSV contains the same governed records together with formula version, method role, contribution class, maturity, implementation state, calibration and validation status, bookmark-date semantics, display-QC metadata, and source snapshot.

Sentinel data are available through the [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/). PACE and other NASA mission data are available through [NASA Earthdata](https://www.earthdata.nasa.gov/). EMIT products are distributed through the NASA Land Processes Distributed Active Archive Center.

Repository code and third-party data products retain their respective licenses. The manuscript and Atlas documentation are released under CC BY 4.0 unless otherwise noted.

## Author contributions

D.B. conceived the Atlas and registry structure, authored the proposed specifications, implemented or assembled the public catalog, conducted the July 2026 audit, and wrote and revised the manuscript.

## Competing interests

The author declares no competing interests.

## AI-assistance disclosure

Generative AI tools were used during revision to assist with language editing, reference discovery, software-audit synthesis, and consistency checking. The author reviewed the source materials, verified the reported claims and citations, made the scientific judgments, and accepts responsibility for the manuscript.

## Acknowledgments

The author acknowledges the scientists, mission teams, open-data providers, and open-source contributors whose work makes transparent Earth-observation research possible. Corrections, validation studies, negative results, and entry-level prior-art comparisons are welcomed through the public repositories.

## References

Biermann, L., Clewley, D., Martinez-Vicente, V., and Topouzelis, K. (2020). Finding plastic patches in coastal waters using optical satellite data. *Scientific Reports*, 10, 5364. [https://doi.org/10.1038/s41598-020-62298-z](https://doi.org/10.1038/s41598-020-62298-z)

Chandler, C. J., et al. (2021). Remote sensing liana infestation in an aseasonal tropical forest: addressing mismatch in spatial units of analyses. *Remote Sensing in Ecology and Conservation*, 7. [https://doi.org/10.1002/rse2.197](https://doi.org/10.1002/rse2.197)

Drusch, M., et al. (2012). Sentinel-2: ESA's optical high-resolution mission for GMES operational services. *Remote Sensing of Environment*, 120, 25-36. [https://doi.org/10.1016/j.rse.2011.11.026](https://doi.org/10.1016/j.rse.2011.11.026)

Hedley, J., Roelfsema, C., Koetz, B., and Phinn, S. (2012). Capability of the Sentinel 2 mission for tropical coral reef mapping and coral bleaching detection. *Remote Sensing of Environment*, 120, 145-155. [https://doi.org/10.1016/j.rse.2011.06.028](https://doi.org/10.1016/j.rse.2011.06.028)

Jones, H. K., and Elgy, J. (1994). Remote sensing to assess landfill gas migration. *Waste Management & Research*, 12, 327-337. [https://doi.org/10.1177/0734242X9401200405](https://doi.org/10.1177/0734242X9401200405)

Montero, D., Aybar, C., Mahecha, M. D., Martinuzzi, F., Sochting, M., and Wieneke, S. (2023). A standardized catalogue of spectral indices to advance the use of remote sensing in Earth system research. *Scientific Data*, 10, 197. [https://doi.org/10.1038/s41597-023-02096-0](https://doi.org/10.1038/s41597-023-02096-0)

NASA Jet Propulsion Laboratory (NASA/JPL). (2025). NASA-ISRO satellite launches to track changes of Earth's surface. 30 July 2025. [https://www.jpl.nasa.gov/news/nasa-isro-satellite-launches-to-track-changes-of-earths-surface/](https://www.jpl.nasa.gov/news/nasa-isro-satellite-launches-to-track-changes-of-earths-surface/)

Olofsson, P., Foody, G. M., Herold, M., Stehman, S. V., Woodcock, C. E., and Wulder, M. A. (2014). Good practices for estimating area and assessing accuracy of land change. *Remote Sensing of Environment*, 148, 42-57. [https://doi.org/10.1016/j.rse.2014.02.015](https://doi.org/10.1016/j.rse.2014.02.015)

Roberts, D. R., et al. (2017). Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure. *Ecography*, 40, 913-929. [https://doi.org/10.1111/ecog.02881](https://doi.org/10.1111/ecog.02881)

Soydan, H., Koz, A., and Duzgun, H. S. (2021). Secondary iron mineral detection via hyperspectral unmixing analysis with Sentinel-2 imagery. *International Journal of Applied Earth Observation and Geoinformation*, 101, 102343. [https://doi.org/10.1016/j.jag.2021.102343](https://doi.org/10.1016/j.jag.2021.102343)

Thompson, D. R., et al. (2024). On-orbit calibration and performance of the EMIT imaging spectrometer. *Remote Sensing of Environment*, 303, 113986. [https://doi.org/10.1016/j.rse.2023.113986](https://doi.org/10.1016/j.rse.2023.113986)

Torres, R., et al. (2012). GMES Sentinel-1 mission. *Remote Sensing of Environment*, 120, 9-24. [https://doi.org/10.1016/j.rse.2011.05.028](https://doi.org/10.1016/j.rse.2011.05.028)

Tucker, C. J. (1979). Red and photographic infrared linear combinations for monitoring vegetation. *Remote Sensing of Environment*, 8, 127-150. [https://doi.org/10.1016/0034-4257(79)90013-0](https://doi.org/10.1016/0034-4257%2879%2990013-0)

Varon, D. J., Jervis, D., McKeever, J., Spence, I., Gains, D., and Jacob, D. J. (2021). Monitoring large methane point sources with Sentinel-2 satellite observations. *Atmospheric Measurement Techniques*, 14, 2771-2785. [https://doi.org/10.5194/amt-14-2771-2021](https://doi.org/10.5194/amt-14-2771-2021)

Waite, C. E., et al. (2019). A view from above: Unmanned aerial vehicles provide a new tool for assessing liana infestation in tropical forest canopies. *Journal of Applied Ecology*, 56. [https://doi.org/10.1111/1365-2664.13318](https://doi.org/10.1111/1365-2664.13318)

Werdell, P. J., et al. (2019). The Plankton, Aerosol, Cloud, ocean Ecosystem mission: Status, science, advances. *Frontiers in Earth Science*, 7, 283. [https://doi.org/10.3389/feart.2019.00283](https://doi.org/10.3389/feart.2019.00283)

Yebra, M., et al. (2018). A fuel moisture content and flammability monitoring methodology for continental Australia based on optical remote sensing. *Remote Sensing of Environment*, 212, 260-272. [https://doi.org/10.1016/j.rse.2018.04.053](https://doi.org/10.1016/j.rse.2018.04.053)

Zabcic, N., Rivard, B., Ong, C., and Muller, A. (2014). Using airborne hyperspectral data to characterize the surface pH and mineralogy of pyrite mine tailings. *International Journal of Applied Earth Observation and Geoinformation*, 32, 152-162. [https://doi.org/10.1016/j.jag.2014.04.008](https://doi.org/10.1016/j.jag.2014.04.008)

---

**Version note.** This version supersedes the scientific framing of version 1. It corrects the marine-domain count from 12 to 10, replaces the T1/T2/T3 priority taxonomy, corrects the NISAR launch year, distinguishes deployment from validation, organizes the 91 records into 24 capability families and method roles, retires SF-EII and AMDPHI from live scientific use, replaces the prior LFMPI interpretation with a normalized NDMI-deficit proxy, reports the 21 July 2026 release audit, and narrows representative environmental claims to their current observables and evidence.

**Suggested citation:** Bally, D. (2026). The Global Spectral Index Atlas: An Open Catalog of Proposed Environmental Remote-Sensing Index Specifications Across Twelve Domains. ESS Open Archive preprint, version 2.
