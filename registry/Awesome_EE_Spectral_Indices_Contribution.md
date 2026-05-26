# Awesome Spectral Indices Submission Draft
### Ready-to-Copy Issue Template for Registry Contribution

This document maps the primary validated and priority novel indices from the Globe & Atlas registry to the standard band notations and schemas required for contribution to the [Awesome Spectral Indices (for Google Earth Engine)](https://github.com/awesome-spectral-indices/awesome-spectral-indices) repository.

You can copy and paste the sections below directly into a new issue on their repository under the **"Submit a Spectral Index"** template.

---

## Standard Band & Parameter Key (Awesome Spectral Indices Guidelines)
*   `A`: Aerosols (B1)
*   `B`: Blue (B2)
*   `G`: Green (B3)
*   `R`: Red (B4)
*   `RE1`: Red Edge 1 (B5 - 705 nm)
*   `RE2`: Red Edge 2 (B6 - 740 nm)
*   `RE3`: Red Edge 3 (B7 - 783 nm)
*   `RE4`: Red Edge 4 (B8A - 865 nm)
*   `N`: NIR (B8 - 842 nm)
*   `S1`: SWIR 1 (B11 - 1610 nm)
*   `S2`: SWIR 2 (B12 - 2190 nm)

---

## Index 1: PWCI (Produced Water Chemical Index)

*   **short_name**: `PWCI`
*   **long_name**: `Produced Water Chemical Index`
*   **formula**: `(((N - S1) / (N + S1))**3) * ((S1 - S2) / (S1 + S2)) * ((G - B) / (G + B))`
*   **reference**: `https://github.com/globe-and-atlas/remote-sensing-research`
*   **type**: `soil`
*   **date_of_addition**: `2026-05-26`
*   **contributor**: `https://github.com/danielbally`

---

## Index 2: ASAI (Arid Salinity Anomaly Index)

*   **short_name**: `ASAI`
*   **long_name**: `Arid Salinity Anomaly Index`
*   **formula**: `max((S1 - S2) / (S1 + S2), G) * (1.0 - (N - R) / (N + R))`
*   **reference**: `https://github.com/globe-and-atlas/remote-sensing-research`
*   **type**: `soil`
*   **date_of_addition**: `2026-05-26`
*   **contributor**: `https://github.com/danielbally`

---

## Index 3: VSI (Vegetation Stress Index)

*   **short_name**: `VSI`
*   **long_name**: `Vegetation Stress Index`
*   **formula**: `((RE4 - RE3) / (RE4 + RE3)) - ((RE3 - RE1) / (RE3 + RE1))`
*   **reference**: `https://github.com/globe-and-atlas/remote-sensing-research`
*   **type**: `vegetation`
*   **date_of_addition**: `2026-05-26`
*   **contributor**: `https://github.com/danielbally`

---

## Index 4: NPDDI (Nitrogen vs. Phosphorus Deficiency Discrimination Index)

*   **short_name**: `NPDDI`
*   **long_name**: `Nitrogen vs. Phosphorus Deficiency Discrimination Index`
*   **formula**: `((R - RE1) / (R + RE1)) - ((S2 - S1) / (S2 + S1))`
*   **reference**: `https://github.com/globe-and-atlas/remote-sensing-research`
*   **type**: `vegetation`
*   **date_of_addition**: `2026-05-26`
*   **contributor**: `https://github.com/danielbally`

---

## Index 5: AMDPHI (Acid Mine Drainage pH Proxy Index)

*   **short_name**: `AMDPHI`
*   **long_name**: `Acid Mine Drainage pH Proxy Index`
*   **formula**: `((R - G) / (R + G)) / ((B - G) / (B + G + 0.001))`
*   **reference**: `https://github.com/globe-and-atlas/remote-sensing-research`
*   **type**: `water`
*   **date_of_addition**: `2026-05-26`
*   **contributor**: `https://github.com/danielbally`

---

## Index 6: SMADI (Sargassum vs. Microplastic Discrimination Index)

*   **short_name**: `SMADI`
*   **long_name**: `Sargassum vs. Microplastic Discrimination Index`
*   **formula**: `(N - S1) - ((RE4 - S1) / (RE4 + S1))`
*   **reference**: `https://github.com/globe-and-atlas/remote-sensing-research`
*   **type**: `water`
*   **date_of_addition**: `2026-05-26`
*   **contributor**: `https://github.com/danielbally`

---

## Index 7: CBSDI (Coral Bleaching Stage Discrimination Index)

*   **short_name**: `CBSDI_pale`
*   **long_name**: `Coral Bleaching Stage Discrimination Index (Paleing)`
*   **formula**: `(G - R) / (G + R)`
*   **reference**: `https://github.com/globe-and-atlas/remote-sensing-research`
*   **type**: `water`
*   **date_of_addition**: `2026-05-26`
*   **contributor**: `https://github.com/danielbally`

---

## Index 8: CCRBI (Coal Combustion Residue Bioaccumulation Index)

*   **short_name**: `CCRBI`
*   **long_name**: `Coal Combustion Residue Bioaccumulation Index`
*   **formula**: `((R - N) / (R + N)) * (G / (S1 + 0.01))`
*   **reference**: `https://github.com/globe-and-atlas/remote-sensing-research`
*   **type**: `vegetation`
*   **date_of_addition**: `2026-05-26`
*   **contributor**: `https://github.com/danielbally`
