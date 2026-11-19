# Brand domain availability checker

This is an early domain-only gate for naming batches. The direct checker queries DNS.PT WHOIS for .pt and Verisign RDAP for .com. A separate Dotsweep client is available as an optional third-party cross-check.

## Run the direct registry checker

Create a UTF-8 text file with one candidate per line, then run:

    python -m scripts.brand_availability.check_domains candidates.txt --json domain-report.json

The script requires only the Python standard library. It needs outbound TCP port 43 for DNS.PT WHOIS and HTTPS access to Verisign RDAP.

## Optional Dotsweep cross-check

Dotsweep offers a public, read-only JSON API with no API key. Its documented endpoints are:

- Single domain: `GET https://dotsweep.com/check/example.com`
- Batch (up to 10 domains): `POST https://dotsweep.com/check` with `{"domains":["one.pt","two.com"]}`

Use the bundled client:

    python -c "from scripts.brand_availability.dotsweep import check_domains; print(check_domains(['example.pt','example.com']))"

The client maps only `confidence=certain` plus `status=available` to available, and only `confidence=certain` plus `status=taken` to registered. `estimated`, mismatched, malformed and failed responses remain unknown. Dotsweep is an independent third-party service, not the registry; never let its result silently override a conflicting official lookup. Review its current documentation and terms before production use.

## Status interpretation

- available: explicit registry-level not-found response.
- registered: registry record exists.
- reserved: DNS.PT explicitly reports a reserved domain.
- unknown: timeout, network error, rate limit, malformed response or ambiguous text.
- DOMAIN_GATE_PASS: both required direct registry lookups returned explicit availability.
- BLOCKED: at least one required domain is registered or reserved.
- UNKNOWN: evidence is insufficient.

The optional Dotsweep client is a cross-check only; it does not change the direct checker's gate. This tooling does not check company names, trademarks, social handles or legal availability. It does not register or reserve domains. Recheck finalists immediately before purchase.

## Sources

- DNS.PT WHOIS: https://www.pt.pt/pt/ferramentas/whois/
- Verisign RDAP: https://rdap.verisign.com/com/v1/domain/
- IANA RDAP bootstrap: https://data.iana.org/rdap/dns.json
- Dotsweep API documentation: https://www.dotsweep.com/docs
- Dotsweep single-domain endpoint documentation: https://www.dotsweep.com/docs/check

The .pt response parser is deliberately conservative. If DNS.PT changes its wording, add a captured, non-personal test fixture before extending the parser. Do not turn ambiguous responses into available.
