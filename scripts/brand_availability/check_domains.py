#!/usr/bin/env python3
"""Conservative .pt WHOIS and .com RDAP checks. Unknown is never treated as available."""
from __future__ import annotations
import argparse, json, socket, sys, urllib.error, urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote

DNS_PT_WHOIS = "whois.dns.pt"
DNS_PT_SOURCE = "https://www.pt.pt/pt/ferramentas/whois/"
VERISIGN_RDAP = "https://rdap.verisign.com/com/v1/domain/"
VERISIGN_SOURCE = "https://www.verisign.com/news-insights/registration-data-access-protocol/help/"

def normalize_label(value: str) -> str:
    raw = value.strip().rstrip(".")
    if not raw or "." in raw or any(ch.isspace() for ch in raw) or "/" in raw or "://" in raw:
        raise ValueError(f"Invalid domain candidate: {value!r}")
    label = raw.split(".")[0].strip().lower()
    ascii_label = label.encode("idna").decode("ascii")
    if not ascii_label or len(ascii_label) > 63 or ascii_label[0] == "-" or ascii_label[-1] == "-" or not all(c.isalnum() or c == "-" for c in ascii_label):
        raise ValueError(f"Invalid domain label: {value!r}")
    return ascii_label

def _result(domain: str, extension: str, status: str, source: str, evidence: str, confidence: str = "high") -> dict[str, Any]:
    return {"domain": domain, "extension": extension, "status": status, "source": source,
            "checked_at": datetime.now(timezone.utc).isoformat(), "confidence": confidence,
            "evidence": evidence[:500]}

def classify_pt_response(response: str, domain: str) -> tuple[str, str]:
    text = " ".join(response.lower().split())
    if not text:
        return "unknown", "Empty WHOIS response"
    markers = ("no match for", "no entries found", "no object found", "domain not found",
               "não foi encontrado", "nao foi encontrado", "não existem resultados", "nao existem resultados")
    if any(marker in text for marker in markers):
        return "available", response
    if "status" in text and ("reserved" in text or "reservado" in text):
        return "reserved", response
    if "status" in text and ("registered" in text or "registado" in text or "registrado" in text):
        return "registered", response
    if domain.lower() in text and any(k in text for k in ("domain:", "domínio", "dominio")):
        return "registered", response
    return "unknown", response

def check_pt(label: str, timeout: float = 8.0) -> dict[str, Any]:
    domain = f"{label}.pt"
    try:
        with socket.create_connection((DNS_PT_WHOIS, 43), timeout=timeout) as sock:
            sock.settimeout(timeout)
            sock.sendall((domain + "\r\n").encode("ascii"))
            chunks = []
            total = 0
            while True:
                try:
                    chunk = sock.recv(4096)
                except socket.timeout:
                    return _result(domain, ".pt", "unknown", DNS_PT_SOURCE, "WHOIS response timed out while reading", "low")
                if not chunk:
                    break
                chunks.append(chunk); total += len(chunk)
                if total > 65536:
                    return _result(domain, ".pt", "unknown", DNS_PT_SOURCE, "WHOIS response exceeded 64 KiB", "low")
        response = b"".join(chunks).decode("utf-8", errors="replace")
        status, evidence = classify_pt_response(response, domain)
        confidence = "medium" if status == "registered" and "domain:" in evidence.lower() else "high"
        return _result(domain, ".pt", status, DNS_PT_SOURCE, evidence, confidence)
    except (OSError, UnicodeError, ValueError) as exc:
        return _result(domain, ".pt", "unknown", DNS_PT_SOURCE, f"WHOIS lookup failed: {type(exc).__name__}: {exc}", "low")

def check_com(label: str, timeout: float = 8.0) -> dict[str, Any]:
    domain = f"{label}.com"
    request = urllib.request.Request(VERISIGN_RDAP + quote(domain, safe="."),
        headers={"Accept": "application/rdap+json, application/json", "User-Agent": "brand-name-availability/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read(65536).decode("utf-8"))
            if response.status == 200 and isinstance(payload, dict) and payload.get("ldhName"):
                return _result(domain, ".com", "registered", VERISIGN_SOURCE, f"RDAP record returned for {payload.get('ldhName')}")
            return _result(domain, ".com", "unknown", VERISIGN_SOURCE, "RDAP returned an unexpected success payload", "low")
    except urllib.error.HTTPError as exc:
        try:
            payload = json.loads(exc.read(16384).decode("utf-8"))
        except (ValueError, UnicodeError):
            payload = {}
        if exc.code == 404 and isinstance(payload, dict) and payload.get("errorCode") == 404:
            return _result(domain, ".com", "available", VERISIGN_SOURCE, "Verisign RDAP returned a structured 404 object-not-found response")
        return _result(domain, ".com", "unknown", VERISIGN_SOURCE, f"RDAP HTTP {exc.code}; not a confirmed not-found result", "low")
    except (OSError, TimeoutError, ValueError, UnicodeError) as exc:
        return _result(domain, ".com", "unknown", VERISIGN_SOURCE, f"RDAP lookup failed: {type(exc).__name__}: {exc}", "low")

def load_candidates(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")]

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 text file: one candidate name per line")
    parser.add_argument("--timeout", type=float, default=8.0)
    parser.add_argument("--json", dest="output", type=Path, help="Write JSON report to this path")
    args = parser.parse_args(argv)
    report = []
    for candidate in load_candidates(args.input):
        try:
            label = normalize_label(candidate)
        except ValueError as exc:
            report.append({"candidate": candidate, "gate": "UNKNOWN", "error": str(exc), "domains": []})
            continue
        domains = [check_pt(label, args.timeout), check_com(label, args.timeout)]
        statuses = {item["status"] for item in domains}
        gate = "BLOCKED" if statuses.intersection({"registered", "reserved"}) else (
            "DOMAIN_GATE_PASS" if statuses == {"available"} else "UNKNOWN")
        report.append({"candidate": candidate, "normalized": label, "gate": gate, "domains": domains})
    rendered = json.dumps({"generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": "domain checks only; not company/trademark clearance", "results": report},
        ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
