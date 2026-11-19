---
name: brand-name-availability
description: Run an early, evidence-based viability screen for candidate brand names across domains, company registers, trademarks and digital presence before investing in concept development.
---

# Brand Name Availability

## Purpose

Filter naming candidates early so creative and strategic effort is spent only on names with a plausible path to use. This is a preliminary commercial and legal-risk screen, not legal clearance.

## When to use

Run immediately after a raw naming batch is generated and before writing detailed concepts, stories, taglines, identity territories or presentation decks. Also rerun when spelling, target markets, goods/services or launch plans materially change.

## Required inputs

- Candidate names with exact spelling and any intended pronunciation.
- Required domain extensions. Default to checking both `.pt` and `.com` when Portugal and international use are in scope.
- Countries of operation and intended company-registration jurisdiction(s).
- Product/service description and likely trademark goods/services classes.
- Languages and priority markets.
- Hard constraints: domains that must be available, acceptable spelling variants, budget or launch timing.
- Access to authoritative or reputable live lookup sources. If unavailable, state that the screen cannot be completed; do not infer availability from search-engine results.

Ask only for missing inputs that change the screen. If the brief already makes Portugal and .pt/.com mandatory, do not ask again.

## Fast-gate workflow

### 1. Batch intake

- Screen the complete raw batch together (normally 10–30 candidates).
- Normalize case, punctuation, spacing and obvious spelling variants, but preserve the exact proposed brand form.
- Do not spend time writing long rationales for every candidate. A one-line meaning/territory note is enough at this stage.

### 2. Domain gate — mandatory

For every candidate, check each required extension separately.

- Use DNS.PT WHOIS for .pt and Verisign RDAP for .com as the direct registry lookups.
- Record exact domain, result, source, timestamp, evidence and confidence.
- Distinguish `available`, `registered`, `reserved/restricted` and `unknown`.
- A missing website, failed DNS resolution or no search-engine result does **not** prove availability.
- Ambiguous responses remain unknown.
- Do not suggest spelling workarounds unless each exact variant is separately screened and accepted by the owner.

**Hard-stop rule:** if any required exact domain is registered, reserved, restricted or unknown, do not advance the candidate without explicit owner approval.

### Executable direct check

From the repository root:

```bash
python -m scripts.brand_availability.check_domains candidates.txt --json domain-report.json
```

This checks DNS.PT WHOIS over TCP/43 and Verisign RDAP over HTTPS. It only reports `DOMAIN_GATE_PASS` when both direct lookups explicitly confirm availability. Network errors, ambiguous responses, malformed payloads and timeouts remain unknown.

### Optional third-party cross-check: Dotsweep

Dotsweep documents a public JSON API without an API key: `GET /check/{domain}` and `POST /check` for up to 10 domains. The bundled `scripts/brand_availability/dotsweep.py` client is optional and separate from the direct checker.

- Only accept `confidence=certain` with `status=available` as an availability signal.
- Only accept `confidence=certain` with `status=taken` as a registered signal.
- `estimated`, malformed, mismatched or failed responses remain unknown.
- Dotsweep is a third-party aggregator, not the registry. It must not override a conflicting direct registry result.
- Do not send confidential or unreleased candidate lists to third parties without the owner's authorisation.
- Review current API documentation, terms and rate limits before production use.

A cross-check does not turn a domain-gate result into legal clearance.

### 3. Company-name gate

For the relevant jurisdiction, search the official company-name register and any official name-approval/reservation service available (for Portugal, RNPC / Justiça services).

- Check exact matches and close phonetic, visual and semantic variants.
- Record whether the result is an exact match, similar entity, approved name, reserved name or inconclusive.
- A search result is not a formal name-approval decision.
- Flag close matches for human/legal review.

### 4. Trademark and market-conflict gate

Search official registers relevant to target markets, prioritising INPI Portugal, EUIPO and WIPO where applicable.

- Search exact wording, spelling variants, phonetic equivalents and highly similar marks.
- Identify likely Nice classes from actual goods/services; do not guess a definitive class where scope is unclear.
- Check status, owner, territory and goods/services descriptions.
- Flag identical or confusingly similar marks in relevant classes/markets as high risk.
- A quick register search is only a screening signal. Recommend trademark counsel before adoption or filing.

### 5. Digital footprint and collision scan

- Search exact phrase and variants across general web results and priority social platforms.
- Identify active businesses, products, apps, domains, media properties and strong existing associations.
- Record handles only when directly checked on the platform or a reliable source.
- Separate unrelated uses from plausible commercial confusion.

### 6. Decide the gate

- `PASS — preliminary screen`: every mandatory domain has a positive direct-registry availability result and no material company/trademark collision was found in checked sources.
- `BLOCKED — hard constraint`: a mandatory domain is registered/reserved/restricted, or a material conflict makes the candidate unsuitable.
- `REVIEW — potential conflict`: a close company name, trademark, market or linguistic collision needs human/legal review.
- `UNKNOWN — evidence insufficient`: one or more required checks could not be completed or a source was ambiguous.

Only PASS candidates move to detailed concept development. REVIEW requires explicit owner decision. BLOCKED candidates leave the shortlist unless a constraint changes. UNKNOWN is never treated as available.

## Output

Provide a compact matrix first:

| Candidate | .pt | .com | Company register | Trademark | Market collision | Gate |
|---|---|---|---|---|---|---|

For material results include exact query, source URL, access timestamp/timezone, evidence, confidence, limitations and next action.

Then provide:
1. Candidates that passed.
2. Blocked candidates and hard-stop reasons.
3. Review/unknown candidates and minimum verification needed.
4. Assumptions or owner decisions required.

## Efficiency rules

- Screen batches, not one name at a time.
- Apply mandatory domain constraints first.
- Do not write full rationales, taglines or identity territories for candidates that fail a hard gate.
- Stop researching blocked candidates once reliable blocking evidence exists.
- Recheck finalists immediately before commitment.

## Quality, legal and safety rules

- Prefer official registries and primary sources; record access dates and direct URLs.
- Never fabricate a lookup, result, source, timestamp, company record or trademark status.
- Never claim a name is legally safe, trademark-clear, exclusive or guaranteed registrable.
- Domain availability can change; recommend immediate registration only after owner approval.
- Do not register, purchase, reserve, file, contact third parties or spend money.
- Protect confidential naming briefs; do not submit unpublished candidates to third-party services without authorisation.
- Use `brand-naming-validation` for linguistic, cultural and confusion-risk analysis after the early viability gate, and obtain qualified legal advice before final adoption.
