import importlib.util
import math
from pathlib import Path
import sys
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "audit_band_algebra.py"
SPEC = importlib.util.spec_from_file_location("audit_band_algebra", SCRIPT)
audit = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class BandAlgebraAuditTests(unittest.TestCase):
    def test_full_instrument_band_set_count_is_1079(self):
        count = sum(math.comb(len(audit.MSI_BANDS), arity) for arity in (2, 3, 4))
        self.assertEqual(count, 1079)

    def test_surface_core_band_set_count_is_375(self):
        count = sum(
            math.comb(len(audit.SURFACE_CORE_BANDS), arity)
            for arity in (2, 3, 4)
        )
        self.assertEqual(count, 375)

    def test_full_candidate_count_is_15054(self):
        candidates = list(audit.enumerate_candidates(audit.MSI_BANDS, "full-13"))
        self.assertEqual(len(candidates), 15054)
        self.assertEqual(
            len({candidate.direction_neutral_key for candidate in candidates}),
            7527,
        )
        self.assertEqual(
            len({candidate.information_key for candidate in candidates}),
            7449,
        )

    def test_surface_candidate_count_is_4770(self):
        candidates = list(
            audit.enumerate_candidates(
                audit.SURFACE_CORE_BANDS,
                "surface-core-10",
            )
        )
        self.assertEqual(len(candidates), 4770)
        self.assertEqual(
            len({candidate.direction_neutral_key for candidate in candidates}),
            2385,
        )
        self.assertEqual(
            len({candidate.information_key for candidate in candidates}),
            2340,
        )

    def test_double_contrast_generation_has_no_exact_duplicates(self):
        candidates = [
            candidate
            for candidate in audit.enumerate_candidates(
                ("B02", "B03", "B04", "B08"),
                "test",
            )
            if candidate.family == "difference-of-contrasts"
        ]
        self.assertEqual(len(candidates), 12)
        self.assertEqual(len({candidate.signed_key for candidate in candidates}), 12)

    def test_gsia_formula_normalization_handles_unicode_operators(self):
        samples = audit.deterministic_reflectance_samples()
        values = audit.safe_msi_formula_values(
            "[(B06−B05)/(B06+B05)] − [(B8A−B08)/(B8A+B08)]",
            samples,
        )
        self.assertIsNotNone(values)
        self.assertEqual(values.shape, (64,))

    def test_gsia_formula_normalization_handles_implicit_coefficients(self):
        samples = audit.deterministic_reflectance_samples()
        values = audit.safe_msi_formula_values(
            "2.5 × [(B08−B11)/(B08+B11+6B04−7.5B02+1)] × (B08/B11)",
            samples,
        )
        self.assertIsNotNone(values)
        self.assertEqual(values.shape, (64,))


if __name__ == "__main__":
    unittest.main()
