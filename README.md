# Remote Sensing Research

Unified repository for spectral index discovery, band combination research, and novel index development across all projects. Aggregates work from **limn**, **civic-sentinel**, and **globe-and-atlas** into one organized reference.

**Total indices cataloged: ~164** across three projects and 12 environmental domains.

---

## What's Here

```
remote-sensing-research/
├── surveys/                    ← Deep research documents (the "why")
│   ├── permian-basin-platform-survey.md    31-platform free satellite survey
│   ├── global-novel-index-survey.md        74 novel unclaimed global indices
│   └── global-public-good-atlas.md         Band combination public-good atlas
│
├── catalogs/                   ← Index lists (the "what")
│   ├── limn-index-catalog.md               53-index limn catalog with validation rates
│   ├── civic-sentinel-composite-slate.md   24-composite civic sentinel slate
│   └── civic-sentinel-composite-atlas.md   18 ranked composites with full formulas
│
├── formulas/                   ← Quick reference
│   └── formula-quick-reference.md          Every formula, all projects, one file
│
└── authorship/                 ← Claim language
    └── (see civic-sentinel-composite-slate.md for claim rules)
```

---

## Navigation by Question

**"What can I actually claim as novel?"**
→ [`surveys/global-novel-index-survey.md`](surveys/global-novel-index-survey.md) — 74 indices, ~42 Tier 1 (Genuinely Unclaimed)
→ [`catalogs/civic-sentinel-composite-slate.md`](catalogs/civic-sentinel-composite-slate.md) — Claim language per composite

**"What does limn currently implement?"**
→ [`catalogs/limn-index-catalog.md`](catalogs/limn-index-catalog.md) — all 53 indices with TRRC validation rates

**"What formula does index X use?"**
→ [`formulas/formula-quick-reference.md`](formulas/formula-quick-reference.md) — ~164 formulas, grouped by domain

**"Which civic-sentinel composites are highest priority?"**
→ [`catalogs/civic-sentinel-composite-atlas.md`](catalogs/civic-sentinel-composite-atlas.md) — ranked 1–18 with full formula detail

**"What sensors beyond Sentinel-2 should I add?"**
→ [`surveys/permian-basin-platform-survey.md`](surveys/permian-basin-platform-survey.md) — 31-platform ranked survey with integration roadmap

**"What's the scientific basis for public-good band combinations?"**
→ [`surveys/global-public-good-atlas.md`](surveys/global-public-good-atlas.md) — scholarly synthesis + claim status key

---

## Index Count by Project

| Project | Index Count | Source |
|---------|-------------|--------|
| **limn** (Permian Basin) | 53 operational | CDSE WMS, S2 + S1 |
| **civic-sentinel** | 24 composites (18 ranked with full formulas) | Sentinel-2 |
| **global novel survey** | 74 proposed (42 Tier 1 unclaimed) | Multi-sensor |
| **platform extensions** | ~20 additional | EMIT, TROPOMI, Landsat, S3, NISAR |

---

## Index Count by Domain

| Domain | Indices | Key Tools |
|--------|---------|-----------|
| Produced water / Permian Basin | 35+ | S2, S1, EMIT, TROPOMI |
| Permafrost & Arctic | 6 | S2 bi-temporal, S1 SAR, ECOSTRESS |
| Tropical Forest | 5 | S2 red-edge, Planet |
| Marine & Coastal | 11 | S2, PACE OCI, EMIT |
| Agriculture | 6 | S2, EnMAP, ECOSTRESS + ERA5 |
| Mining & Industrial | 6+ | S2, EMIT, S1 InSAR |
| Wildfire | 5 | S2, EMIT, TROPOMI, GOES |
| Urban & Infrastructure | 4 | S2, ECOSTRESS, TROPOMI |
| Water Quality & Freshwater | 4+ | PACE OCI, Landsat TIRS, S2 |
| Dryland & Arid | 6 | EMIT, EnMAP, S2, SMAP |
| Wetland & Peatland | 5 | S2 + S1 fusion |
| Hyperspectral-only | 11 | EMIT, EnMAP, PRISMA, DESIS, PACE |
| Cross-sensor fusion | 8 | TROPOMI+S2, GRACE+ECOSTRESS, NISAR+S2 |

---

## The Top 10 Priority Novel Indices

From [`surveys/global-novel-index-survey.md`](surveys/global-novel-index-survey.md):

| Rank | Acronym | Name | Why |
|------|---------|------|-----|
| 1 | TSEAI | TROPOMI–Sentinel-2 Emission Attribution | CH4 source attribution at field scale — climate monitoring's most urgent gap |
| 2 | HABSDI | HAB Species-Level Discrimination | Toxic vs. non-toxic cyanobacteria — PACE (2024) makes it possible globally |
| 3 | NPDDI | N vs. P Deficiency Discrimination | Precision fertilizer prescription from orbit |
| 4 | SMADI | Sargassum vs. Microplastic Discrimination | Both global crises, current indices conflate them |
| 5 | FGDCI | Frozen Ground Dielectric Change | Pan-Arctic freeze/thaw from Sentinel-1 |
| 6 | CBSDI | Coral Bleaching Stage Discrimination | Stages bleaching vs. binary detection |
| 7 | REESAI | Rare Earth Element Surface Anomaly | EnMAP Nd detection — clean energy supply chain |
| 8 | BSMTI | Burn Severity Mineralogy Transition | Post-fire debris flow risk via EMIT soil mineralogy |
| 9 | PWTDI | Peatland Water Table Depth | Most important unmeasured variable in wetland carbon accounting |
| 10 | RDOCI | River Dissolved Organic Carbon | PACE OCI UV channels (2024) make this orbital for the first time |

---

## Claim Philosophy

From [`catalogs/civic-sentinel-composite-slate.md`](catalogs/civic-sentinel-composite-slate.md):

> The defensible claim for each index is: *a named, transparent, decision-ready composite built from established spectral mechanisms, domain gates, and confounder rejection — applied to a specific public-good screening workflow.*

**Claim:** the named workflow, the gate logic, the confounder rejection, the civic framing.
**Don't claim:** invention of the underlying band physics, the individual ratios, or the environmental problem itself.

---

## Source Projects

| Project | Path | Role |
|---------|------|------|
| limn | `/Users/danielbally/Git/limn` | Permian Basin environmental monitoring tool |
| civic-sentinel | `/Users/danielbally/Git/civic-sentinel` | Public-good composite index web app |
| globe-and-atlas | `/Users/danielbally/Git/globe-and-atlas` | Research vault and content strategy |

---

*Last updated: 2026-05-25. Research spans sensors operational through Q1 2026.*
