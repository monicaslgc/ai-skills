# E-commerce Operations references

Use approved catalogue, order-event and source-system exports. Treat SKU as an identifier, not fuzzy text. Check uniqueness, variant parent/child consistency, required attributes, valid state transitions and source-to-destination field mappings. Do not infer product claims or silently merge records. Compare before/after snapshots, quarantine ambiguous records, require approval for deletes or high-volume changes, and preserve rollback/audit evidence.
