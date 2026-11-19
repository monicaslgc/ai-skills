import unittest
from unittest.mock import patch
from scripts.brand_availability.check_domains import check_com, classify_pt_response, normalize_label

class DomainAvailabilityTests(unittest.TestCase):
    def test_normalizes_case(self):
        self.assertEqual(normalize_label("  HUMN  "), "humn")
    def test_rejects_url_input(self):
        with self.assertRaises(ValueError):
            normalize_label("https://example.com")
    def test_rejects_dotted_candidate_to_avoid_truncation(self):
        with self.assertRaises(ValueError):
            normalize_label("brand.pt")
    def test_pt_explicit_not_found_is_available(self):
        self.assertEqual(classify_pt_response("No match for humn.pt", "humn.pt")[0], "available")
    def test_pt_registered_status(self):
        self.assertEqual(classify_pt_response("Domain: humn.pt Status: Registered", "humn.pt")[0], "registered")
    def test_pt_reserved_status(self):
        self.assertEqual(classify_pt_response("Domain: humn.pt Status: Reserved", "humn.pt")[0], "reserved")
    def test_pt_ambiguous_response_is_unknown(self):
        self.assertEqual(classify_pt_response("Query processed successfully", "humn.pt")[0], "unknown")
    @patch("scripts.brand_availability.check_domains.urllib.request.urlopen")
    def test_com_registered_record(self, mocked):
        class Response:
            status = 200
            def __enter__(self): return self
            def __exit__(self, *args): return False
            def read(self, limit): return b'{"ldhName":"example.com"}'
        mocked.return_value = Response()
        self.assertEqual(check_com("example")["status"], "registered")
    @patch("scripts.brand_availability.check_domains.urllib.request.urlopen")
    def test_com_network_failure_is_unknown(self, mocked):
        mocked.side_effect = OSError("offline")
        self.assertEqual(check_com("example")["status"], "unknown")

if __name__ == "__main__":
    unittest.main()
