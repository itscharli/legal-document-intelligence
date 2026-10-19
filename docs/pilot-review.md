# Five-form classification pilot — draft

Reviewed October 19, 2026. This is a metadata-only, assistant-labeled pilot of five official blank California Judicial Council forms. It is not a case-document dataset, independent expert review, compliance audit, or classifier evaluation. No PDFs or completed case records are included.

| ID | Form | Primary label | Intended-use stage | Form effective date |
| --- | --- | --- | --- | --- |
| TPL-001 | [CM-010 — Civil Case Cover Sheet](https://selfhelp.courts.ca.gov/jcc-form/CM-010) | ADM.civil_case_cover_sheet | pleadings | 2026-07-01 |
| TPL-002 | [SUM-100 — Summons](https://selfhelp.courts.ca.gov/jcc-form/SUM-100) | SVC.summons | pleadings | 2009-07-01 |
| TPL-003 | [POS-010 — Proof of Service of Summons](https://selfhelp.courts.ca.gov/jcc-form/POS-010) | SVC.proof_of_service | pleadings | 2007-01-01 |
| TPL-004 | [CM-110 — Case Management Statement](https://selfhelp.courts.ca.gov/jcc-form/CM-110) | ADM.case_management_statement | pretrial | 2024-01-01 |
| TPL-005 | [DISC-002 — Form Interrogatories—Employment Law](https://selfhelp.courts.ca.gov/jcc-form/DISC-002) | DSC.form_interrogatories | discovery | 2009-01-01 |

See [machine-readable metadata](../data/pilot/templates.json). All classifications remain pending human review. Stage describes intended use, not an event in a real case. No subject-matter claim is inferred from the employment form.

## Procedural references and verification

- CM-010: [CRC 3.220](https://courts.ca.gov/cms/rules/index/three/rule3_220) supports the cover-sheet relationship, with stated exceptions. The official form page lists July 1, 2026; older indexed PDFs must not silently replace that edition.
- SUM-100: the official form cites CCP sections 412.20 and 465. This confirms the citation appears on the form, not that the live statutory text has been audited.
- POS-010: [CRC 2.150](https://courts.ca.gov/cms/rules/index/two/rule2_150) addresses computer-generated/typewritten proof-of-service alternatives. An official court copy cites CCP 417.10; current statutory verification remains outstanding.
- CM-110: [CRC 3.725](https://courts.ca.gov/cms/rules/index/three/rule3_725) identifies the form and filing/service requirement. The pilot does not calculate deadlines.
- DISC-002: official form instructions refer to CCP 2030.010–2030.410. It is a discovery request template, not a response. Current statutory text remains unverified.

Official form listings and indexed official form text were used. Several direct form-page requests returned access errors; full PDF page-by-page review, component page ranges, and content hashes remain outstanding. Effective dates reflect the official listings or form text, not website crawl/publication dates. No access restrictions were bypassed.

The [official forms directory](https://selfhelp.courts.ca.gov/find-forms/all-by-category) and [July 2026 forms appendix](https://courts.ca.gov/system/files?file=rules-court%2Fappendix_0.pdf) supplement individual listings. Recheck the current official listing before use; a proposal for a future form revision is not an in-effect form.

## What this tests

- Distinguishes administrative forms from pleadings.
- Distinguishes a summons from evidence of its service.
- Distinguishes discovery questions from responses.
- Records form version, provenance, and authority-verification status separately.
- Tests only 3 of 14 taxonomy families. No coverage or accuracy percentage is warranted.

## Human review task

For each row, confirm the family/subtype, intended-use stage, and short evidence note. Record reviewer identity/date and disagreements before changing review_status to accepted. In particular, decide whether pretrial is useful for CM-110 or whether a dedicated case_management stage is needed.

## Next work

Verify remaining statutory text and current PDFs, resolve page ranges and reuse review, then expand to a more varied pilot. Redistribution and model-use reviews stay pending; these links do not authorize training or republication.
