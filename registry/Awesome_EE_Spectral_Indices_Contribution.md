# Awesome Spectral Indices Submission Directory
### Complete Registry of Novel Formulations Ready for Contribution

Updated: 2026-05-27 | Format: SpectralIndex() Python constructor (current ASI template)

Paste each block below directly into a **"Submit a Spectral Index"** issue at
[github.com/awesome-spectral-indices/awesome-spectral-indices](https://github.com/awesome-spectral-indices/awesome-spectral-indices)

Allowed `application_domain` values: `vegetation` · `burn` · `water` · `snow` · `kernel`

---

## SUBMIT-READY — 23 indices

These have clean, single-image formulas and a valid application_domain mapping.

---

### BH_DFSI

**Issue title:** `NEW INDEX: BH_DFSI (Burnt Hillside Debris-Flow Susceptibility Index)`

```python
BH_DFSI=SpectralIndex(
    short_name='BH_DFSI',
    long_name='Burnt Hillside Debris-Flow Susceptibility Index',
    formula='clamp((0.15 - ((N - S2) / (N + S2))) / 0.30, 0.0, 1.0) * clamp(((((S1 + R) - (N + B)) / ((S1 + R) + (N + B))) - 0.10) / 0.20, 0.0, 1.0) * clamp((((G - S1) / (G + S1)) + 0.35) / 0.50, 0.0, 1.0) * clamp(((R - B) / (R + B)) * 2.0, 0.0, 1.0)',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='burn',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

> ⚠️ Note: uses `clamp()` — confirm this function is supported in the ASI evaluator before submitting.

---

### SF_EII

**Issue title:** `NEW INDEX: SF_EII (Wildfire Fuel Hazard and Canopy Dehydration Index)`

```python
SF_EII=SpectralIndex(
    short_name='SF_EII',
    long_name='Wildfire Fuel Hazard and Canopy Dehydration Index',
    formula='((RE4 - S1) / (RE4 + S1)) * (1.0 - (N / S2))',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='vegetation',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### LFMPI

**Issue title:** `NEW INDEX: LFMPI (Live Fuel Moisture Pre-Ignition Index)`

```python
LFMPI=SpectralIndex(
    short_name='LFMPI',
    long_name='Live Fuel Moisture Pre-Ignition Index',
    formula='2.5 * ((RE4 - S1) / (RE4 + S1 + 6.0 * R - 7.5 * B + 1.0)) - (S2 / S1)',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='vegetation',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### PETI

**Issue title:** `NEW INDEX: PETI (Phycocyanin Eutrophication Toxicity Index)`

```python
PETI=SpectralIndex(
    short_name='PETI',
    long_name='Phycocyanin Eutrophication Toxicity Index',
    formula='(R - RE1) / (R + RE1)',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='water',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### CSRC

**Issue title:** `NEW INDEX: CSRC (Cyanotoxin Scum Risk Composite)`

```python
CSRC=SpectralIndex(
    short_name='CSRC',
    long_name='Cyanotoxin Scum Risk Composite',
    formula='((RE1 - R) / (RE1 + R)) * N',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='water',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### HABSDI_cyano

**Issue title:** `NEW INDEX: HABSDI_cyano (HAB Species-Level Discrimination Index (Cyanobacteria))`

```python
HABSDI_cyano=SpectralIndex(
    short_name='HABSDI_cyano',
    long_name='HAB Species-Level Discrimination Index (Cyanobacteria)',
    formula='(G - RE1) - (B - G)',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='water',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### SMPDI

**Issue title:** `NEW INDEX: SMPDI (Sargassum vs. Microplastic Discrimination Index)`

```python
SMPDI=SpectralIndex(
    short_name='SMPDI',
    long_name='Sargassum vs. Microplastic Discrimination Index',
    formula='(N - S1) - ((RE4 - S1) / (RE4 + S1))',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='water',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### KCDSI

**Issue title:** `NEW INDEX: KCDSI (Kelp Canopy Density and Stress Index)`

```python
KCDSI=SpectralIndex(
    short_name='KCDSI',
    long_name='Kelp Canopy Density and Stress Index',
    formula='(N / S1) * ((RE1 - R) / (RE1 + R))',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='vegetation',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### OWSI

**Issue title:** `NEW INDEX: OWSI (Oil Spill Weathering Stage Index)`

```python
OWSI=SpectralIndex(
    short_name='OWSI',
    long_name='Oil Spill Weathering Stage Index',
    formula='((S2 - S1) / (S2 + S1)) / ((B + G) / (N + S1) + 0.01)',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='water',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### CD_UAI

**Issue title:** `NEW INDEX: CD_UAI (Coastal Dredging and Marine Siltation Plume Index)`

```python
CD_UAI=SpectralIndex(
    short_name='CD_UAI',
    long_name='Coastal Dredging and Marine Siltation Plume Index',
    formula='((G - B) / (G + B)) * ((G - R) / (G + R))',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='water',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### MP_PDI

**Issue title:** `NEW INDEX: MP_PDI (Marine Plastisphere and Polymer Differentiation Index)`

```python
MP_PDI=SpectralIndex(
    short_name='MP_PDI',
    long_name='Marine Plastisphere and Polymer Differentiation Index',
    formula='(N - S1) / (G + S1)',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='water',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### CTPSTI

**Issue title:** `NEW INDEX: CTPSTI (Cyanobacterial Toxin Proxy Spectral Index)`

```python
CTPSTI=SpectralIndex(
    short_name='CTPSTI',
    long_name='Cyanobacterial Toxin Proxy Spectral Index',
    formula='(G - RE1) / (G + RE1)',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='water',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### NPDefI

**Issue title:** `NEW INDEX: NPDefI (Nitrogen vs. Phosphorus Deficiency Discrimination Index)`

```python
NPDefI=SpectralIndex(
    short_name='NPDefI',
    long_name='Nitrogen vs. Phosphorus Deficiency Discrimination Index',
    formula='((R - RE1) / (R + RE1)) - ((S2 - S1) / (S2 + S1))',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='vegetation',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### SCSPI

**Issue title:** `NEW INDEX: SCSPI (Soil Compaction Spectral Proxy Index)`

```python
SCSPI=SpectralIndex(
    short_name='SCSPI',
    long_name='Soil Compaction Spectral Proxy Index',
    formula='(1.0 - (S1 / S2)) * (G / B)',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='vegetation',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### AMDPHI

**Issue title:** `NEW INDEX: AMDPHI (Acid Mine Drainage pH Proxy Index)`

```python
AMDPHI=SpectralIndex(
    short_name='AMDPHI',
    long_name='Acid Mine Drainage pH Proxy Index',
    formula='((R - G) / (R + G)) / ((B - G) / (B + G + 0.001))',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='water',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### CCRBI

**Issue title:** `NEW INDEX: CCRBI (Coal Combustion Residue Bioaccumulation Index)`

```python
CCRBI=SpectralIndex(
    short_name='CCRBI',
    long_name='Coal Combustion Residue Bioaccumulation Index',
    formula='((R - N) / (R + N)) * (G / (S1 + 0.01))',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='vegetation',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### PCEI

**Issue title:** `NEW INDEX: PCEI (Peat Carbon Exposure Index)`

```python
PCEI=SpectralIndex(
    short_name='PCEI',
    long_name='Peat Carbon Exposure Index',
    formula='(1.0 - (N - R) / (N + R)) * S2 * (1.0 - ((G - N) / (G + N)))',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='vegetation',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### SABSI

**Issue title:** `NEW INDEX: SABSI (Snow and Ice Algae Bloom Severity Index)`

```python
SABSI=SpectralIndex(
    short_name='SABSI',
    long_name='Snow and Ice Algae Bloom Severity Index',
    formula='((R - N) / (R + N)) + 0.5 * ((B - G) / (B + G))',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='snow',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### MEPSI

**Issue title:** `NEW INDEX: MEPSI (CH4 Ebullition Pond Spectral Proxy Index)`

```python
MEPSI=SpectralIndex(
    short_name='MEPSI',
    long_name='CH4 Ebullition Pond Spectral Proxy Index',
    formula='(N / B) - ((G - N) / (G + N))',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='water',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### PDCSI

**Issue title:** `NEW INDEX: PDCSI (Pre-Deforestation Canopy Stress Index)`

```python
PDCSI=SpectralIndex(
    short_name='PDCSI',
    long_name='Pre-Deforestation Canopy Stress Index',
    formula='((RE2 - RE1) / (RE2 + RE1)) - ((RE4 - N) / (RE4 + N))',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='vegetation',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### LISI

**Issue title:** `NEW INDEX: LISI (Liana Infestation Structural Index)`

```python
LISI=SpectralIndex(
    short_name='LISI',
    long_name='Liana Infestation Structural Index',
    formula='2.5 * ((N - S1) / (N + 6.0 * R - 7.5 * B + 1.0)) * (N / S1)',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='vegetation',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### SLSDI

**Issue title:** `NEW INDEX: SLSDI (Selective Logging Scar Detection Index)`

```python
SLSDI=SpectralIndex(
    short_name='SLSDI',
    long_name='Selective Logging Scar Detection Index',
    formula='((B + G) / (N + 0.01)) * (S2 / (S2 + RE4))',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='vegetation',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

---

### RDOCI

**Issue title:** `NEW INDEX: RDOCI (River Dissolved Organic Carbon Index)`

```python
RDOCI=SpectralIndex(
    short_name='RDOCI',
    long_name='River Dissolved Organic Carbon Index',
    formula='log(A / B) / 92 * (-1.0)',
    reference='https://doi.org/10.5281/zenodo.20400743',
    application_domain='water',
    date_of_addition='2026-05-27',
    contributor="https://github.com/globe-and-atlas"
)
```

> ⚠️ Note: changed `ln()` → `log()` to match numpy convention. Verify with ASI maintainers that `log()` is supported in their formula evaluator.

---

## NEEDS FORMULA REVISION — 11 indices

These are excluded from submission until their formula or domain issue is resolved.

| Index | Problem | Fix needed |
| ----- | ------- | ---------- |
| PSHRI | Bi-temporal formula (`_post`, `_pre` suffixes) | ASI has no multi-image support — reframe as single-date or drop |
| TPERI | Bi-temporal formula (`S1_t1`, `S1_t2`, `G_t1`, `G_t2`) | Same — no multi-temporal support in ASI |
| UBCDI | Bi-temporal formula (`N_post`, `N_pre`, `R_post`, `R_pre`) | Same |
| PDSDI | Uses `CV_NDVI` (coefficient of variation — not a band) | Replace with a single-image spatial texture proxy or drop |
| IPVSI | Uses `texture` (undefined parameter) | Define texture as a specific band ratio or drop |
| TFIDI | Uses `NDWI_p90`, `NDWI_p10`, `NDWI_mean` (percentile composites) | Percentile aggregation not supported in ASI formula syntax |
| WDPTZI | Uses `spatial_gradient()` (kernel operation) | Gradient operations not supported in ASI formula syntax |
| ALSI | Uses `T1_anomaly` (ECOSTRESS thermal parameter, not a spectral band) | Cross-sensor thermal inputs not in ASI band vocabulary |
| SPSRI | Uses `B_clean` (site-specific baseline, not a standard band) | Baseline subtraction not expressible in ASI formula syntax |
| PCADI | `urban` domain — no mapping to the 5 allowed values | No suitable domain; not a good ASI fit |
| PWTDI | Fuses `B9` (S2) + `VV`/`VH` (S1 SAR) — cross-sensor | Verify ASI supports SAR bands; `B9` notation may also need checking |
