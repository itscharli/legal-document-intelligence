# Public-source annotation guidelines — draft v0.1

Status: proposed workflow; no documents have been collected or annotated under this draft.

## Unit of annotation

A source file is a container. A document component is the classification unit. Retain an internal file identifier and page range for each component. Use the labels in [the taxonomy](taxonomy.md). For non-paginated material, record the available segment locator and flag the record for review.

## Source screening

1. Prefer official court or agency forms, instructions, and deliberately published examples for the initial pilot.
2. Record the source page URL, direct document URL, publisher, retrieval date, and reuse basis before downloading.
3. Public accessibility alone does not establish permission to redistribute, train on, or publish personal information. Record access, redistribution, and model-use review separately.
4. Exclude sealed, restricted, leaked, privileged, or confidential client material. Do not bypass login, paywalls, access restrictions, or redactions.
5. Do not commit raw case documents or sensitive extracts by default. For the first pilot, publish source links and non-sensitive metadata only after review. Use blank official forms to test the workflow without presenting them as real case examples.
6. Quarantine a source with personal identifiers, medical details, allegations, or uncertain reuse terms pending review. Do not copy those details into public annotation notes.

## Minimum annotation record

| Field | Meaning |
| --- | --- |
| document_id | Stable project identifier, not a person's name |
| source_file_id | Links components from the same source container |
| source_page_url | Page describing or hosting the source |
| source_document_url | Direct source link, when available |
| publisher | Source organization |
| retrieved_at | ISO date of access |
| reuse_basis | Evidence or link supporting intended use; unknown if unresolved |
| redistribution_review | pending, approved, rejected |
| model_use_review | pending, approved, rejected |
| privacy_review | pending, approved, rejected |
| original_title | Visible title; omit or redact sensitive content |
| form_number | Official form identifier when visible; otherwise null |
| component_start_page / component_end_page | Inclusive, one-based PDF pages; null if unavailable |
| family / subtype | Primary taxonomy label |
| stage / forum / document_status | Separate contextual labels |
| subject_tags / motion_topic | Optional tags supported by visible content |
| container_role | Relationship to the source container |
| taxonomy_version | Vocabulary version used |
| annotator_id / annotated_at | Non-sensitive annotator ID and ISO date |
| confidence | high, medium, low |
| review_status | pending, accepted, needs_revision, excluded |
| evidence_note | Brief non-sensitive reason for the label |
| ambiguity_note | Competing labels or missing evidence; no private excerpts |

Later implementation should normalize multiple tags and review events into separate tables. Missing information remains null or unknown; never fabricate metadata.

## Labeling procedure

1. Screen the source and record its provenance and review states.
2. Inspect title, issuer, purpose, and component boundaries. A filename alone is insufficient.
3. Assign family and subtype first, then contextual attributes.
4. Write a short evidence note, such as “Official blank employment interrogatories form; form number visible.”
5. Use high confidence for clear function and boundaries; medium for incomplete context; low for competing labels or unreadable material.
6. Flag low-confidence, mixed, or novel types for review. Preserve the original annotation when recording a correction.
7. Require a second review before including an item in a future evaluation set. Review approval of the label does not replace privacy or reuse approval.

## Pilot and quality checks

Proposed pilot: 20–30 screened public templates or examples, with source type recorded. Template results must be reported separately from case-document results.

Before publishing a pilot: check unique IDs, valid vocabulary values, required provenance, valid page ranges, consistent form numbers, duplicate sources, and unresolved review states. Have a second reviewer independently label a subset and record disagreements before adjudication. If only one annotator is available, report that limitation instead of claiming inter-annotator agreement.

Future model evaluation should group related case documents and duplicates together when splitting data to reduce leakage. No accuracy, coverage, or operational-efficiency claims should be made before measured evaluation.

## Next deliverable

A reviewed source register and a small metadata-only pilot. No dataset or classifier is delivered by these guidelines.
