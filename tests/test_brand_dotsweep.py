import json
import unittest
from unittest.mock import patch
from scripts.brand_availability.dotsweep import _normalise_result, check_domain, check_domains


class DotsweepClientTests(unittest.TestCase):
    def test_registry_confirmed_available(self):
        result = _normalise_result({"domain": "sample.pt", "status": "available",
            "confidence": "certain", "source": "rdap"}, "sample.pt")
        self.assertEqual(result["status"], "available")

    def test_estimated_available_remains_unknown(self):
        result = _normalise_result({"domain": "sample.pt", "status": "available",
            "confidence": "estimated", "source": "dns"}, "sample.pt")
        self.assertEqual(result["status"], "unknown")

    def test_confirmed_taken_maps_to_registered(self):
        result = _normalise_result({"domain": "sample.com", "status": "taken",
            "confidence": "certain", "source": "rdap"}, "sample.com")
        self.assertEqual(result["status"], "registered")

    def test_domain_mismatch_is_unknown(self):
        result = _normalise_result({"domain": "other.com", "status": "available",
            "confidence": "certain"}, "sample.com")
        self.assertEqual(result["status"], "unknown")

    def test_malformed_result_is_unknown(self):
        self.assertEqual(_normalise_result(None, "sample.com")["status"], "unknown")

    @patch("scripts.brand_availability.dotsweep.urllib.request.urlopen")
    def test_batch_parses_live_api_response_shape(self, mocked):
        # Captured from a real Dotsweep POST /check response (prices omitted).
        payload = {
            "results": [
                {"domain": "example.pt", "tld": "pt", "status": "taken",
                 "confidence": "certain", "source": "dns"},
                {"domain": "example.com", "tld": "com", "status": "taken",
                 "confidence": "certain", "source": "dns"},
                {"domain": "vyora.pt", "tld": "pt", "status": "available",
                 "confidence": "estimated", "source": "dns"},
                {"domain": "vyora.com", "tld": "com", "status": "taken",
                 "confidence": "certain", "source": "dns"},
            ]
        }
        mocked.return_value.__enter__.return_value.read.return_value = json.dumps(payload).encode("utf-8")

        results = check_domains(["example.pt", "example.com", "vyora.pt", "vyora.com"])

        self.assertEqual([item["status"] for item in results],
                         ["registered", "registered", "unknown", "registered"])
        self.assertEqual(results[2]["provider_confidence"], "estimated")
        self.assertEqual(results[2]["source"], "dotsweep:dns")

    @patch("scripts.brand_availability.dotsweep.urllib.request.urlopen")
    def test_network_failure_is_unknown(self, mocked):
        mocked.side_effect = OSError("offline")
        self.assertEqual(check_domain("sample.com")["status"], "unknown")

    def test_batch_limit(self):
        with self.assertRaises(ValueError):
            check_domains([f"name{i}.com" for i in range(11)])


if __name__ == "__main__":
    unittest.main()
