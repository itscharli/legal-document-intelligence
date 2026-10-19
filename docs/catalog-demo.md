# Searchable catalog and SQL prototype

Status: working command-line prototype for five blank-template metadata records. No AI classification, web interface, deadline calculation, or legal-compliance validation is implemented.

## Try it

Download or clone this repository and open a terminal in its root. Requires Python 3; no third-party packages.

```sh
python3 scripts/catalog.py
python3 scripts/catalog.py --search employment
python3 scripts/catalog.py --search POS-010
```

The first command runs the four queries in [operations.sql](../sql/operations.sql). Search matches literal form numbers, titles, or subtype text, without case sensitivity for ASCII text. Empty search lists all records. No match returns an empty list.

The catalog is rebuilt in memory from [pilot metadata](../data/pilot/templates.json) on each run. It writes no database file and does not download source documents. Metadata JSON is the source of truth.

## Structure

- [schema.sql](../sql/schema.sql): documents and related authority references, with primary keys and foreign keys.
- [catalog.py](../scripts/catalog.py): imports the pilot metadata and runs parameterized searches.
- [operations.sql](../sql/operations.sql): counts by family, finds discovery forms, lists references needing statutory verification, and shows separate review states.

This is a deliberately small operational subset of the annotation design. Additional tags and review history remain in the source metadata; they are not yet normalized into SQL tables.

## Observed results — October 19, 2026

| Query | Result |
| --- | --- |
| Counts by family | ADM 2; SVC 2; DSC 1 |
| Discovery forms | DISC-002 |
| References without current statutory-text verification | DISC-002, POS-010, SUM-100: 3 reference records |
| Label review | 5 accepted by project owner |
| Redistribution/model-use review | Pending for all 5 |
| Search employment | DISC-002 |
| Search containing an SQL-like quote/expression | No matches; treated as literal search text |

Verification: the full report and employment search ran successfully using Python's standard-library SQLite. A quoted SQL-like search was also run to check literal handling. These results describe five curated templates, not litigation volumes or classifier accuracy. Current statutory and full-PDF checks remain outstanding; see [pilot review](pilot-review.md).
