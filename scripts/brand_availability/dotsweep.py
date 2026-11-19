"""Read-only Dotsweep domain availability API client.

Dotsweep is a third-party cross-check, not a legal or registry authority.
Only registry-confirmed (confidence=certain) results are mapped to available/taken.
Estimated, malformed, mismatched and failed responses remain unknown.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any
from urllib.parse import quote

BASE_URL = "https://dotsweep.com"


def _normalise_result(item: Any, requested_domain: str) -> dict[str, Any]:
    if not isinstance(item, dict):
        return {"domain": requested_domain, "status": "unknown", "confidence": "low",
                "source": "dotsweep", "evidence": "Malformed response item"}
    returned_domain = str(item.get("domain", "")).lower().rstrip(".")
    if returned_domain != requested_domain.lower():
        return {"domain": requested_domain, "status": "unknown", "confidence": "low",
                "source": "dotsweep", "evidence": f"Domain mismatch: {returned_domain or 'missing'}"}
    status = item.get("status")
    confidence = item.get("confidence")
    if confidence == "certain" and status == "available":
        mapped = "available"
    elif confidence == "certain" and status == "taken":
        mapped = "registered"
    else:
        mapped = "unknown"
    return {
        "domain": requested_domain,
        "status": mapped,
        "confidence": "high" if mapped != "unknown" else "low",
        "provider_confidence": confidence,
        "source": f"dotsweep:{item.get('source', 'unspecified')}",
        "evidence": f"provider_status={status}; confidence={confidence}",
    }


def check_domain(domain: str, timeout: float = 10.0) -> dict[str, Any]:
    url = f"{BASE_URL}/check/{quote(domain.lower(), safe='.-')}"
    request = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "User-Agent": "brand-name-availability/1.0",
    })
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read(65536).decode("utf-8"))
        return _normalise_result(payload, domain)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, UnicodeError) as exc:
        return {"domain": domain, "status": "unknown", "confidence": "low",
                "source": "dotsweep", "evidence": f"Lookup failed: {type(exc).__name__}: {exc}"}


def check_domains(domains: list[str], timeout: float = 10.0) -> list[dict[str, Any]]:
    if not domains:
        return []
    if len(domains) > 10:
        raise ValueError("Dotsweep batch endpoint accepts at most 10 domains")
    body = json.dumps({"domains": [d.lower() for d in domains]}).encode("utf-8")
    request = urllib.request.Request(f"{BASE_URL}/check", data=body, method="POST",
        headers={"Accept": "application/json", "Content-Type": "application/json",
                 "User-Agent": "brand-name-availability/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read(131072).decode("utf-8"))
        results = payload.get("results") if isinstance(payload, dict) else None
        if not isinstance(results, list):
            raise ValueError("Missing results array")
        indexed = {str(x.get("domain", "")).lower(): x for x in results if isinstance(x, dict)}
        return [_normalise_result(indexed.get(d.lower()), d) for d in domains]
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, UnicodeError) as exc:
        return [{"domain": d, "status": "unknown", "confidence": "low",
                 "source": "dotsweep", "evidence": f"Batch lookup failed: {type(exc).__name__}: {exc}"}
                for d in domains]
