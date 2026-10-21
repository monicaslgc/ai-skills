# Fictional example: catalogue import review

A fictional shop receives a CSV containing new products, updates, duplicate SKUs, blank required attributes and several deletion rows. Expected result: additions/updates/deletions separated; duplicate IDs quarantined; missing fields reported by row/SKU; product copy grounded only in supplied facts; sample checks and rollback plan included. No live publication or automatic merge.
