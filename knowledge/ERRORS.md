# Errors

Record deterministic errors, root causes, and fixes here.

## 2026-05-26 - Operator Spacing Split in Exponents
- **Error**: Spacing normalization regex split `**3` exponent into `*  * 3` in `PWCI` code block.
- **Cause**: The split-by-backtick parsed code blocks inside triple-backticks as inline tick segments, and standard asterisk matching `\s*\*\s*` ran on individual characters of the `**` operator.
- **Fix**: Corrected formula on line 177 in `ATLAS.private.md` to `NDSI**3`. Standardized single-asterisk lookbehind/lookahead `(?<!\*)\*(?!\*)` to avoid exponent disruption in future parsing pipelines.
