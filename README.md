# Legal Document Intelligence

**Status: In development — initial documentation drafts.** A draft taxonomy and annotation guidelines are available for review. They have not been validated against a document corpus. A five-form metadata pilot is available with labels accepted by the project owner; source checks remain pending. A working SQLite catalog and command-line search cover the five template records. No case-document dataset or AI classifier is available yet.

## Working prototype

[Catalog demo and run instructions](docs/catalog-demo.md): search five official-form metadata records and run SQL queries for counts, discovery forms, and outstanding source checks.

## Current drafts

- [Document taxonomy v0.2](docs/taxonomy.md): candidate families, subtypes, contextual attributes, boundary rules, and dated references to current civil rules and the U.S. Courts glossary.
- [Annotation guidelines v0.1](docs/annotation-guidelines.md): source screening, metadata fields, labeling procedure, and proposed pilot checks.

- [Five-form pilot review](docs/pilot-review.md) and [metadata](data/pilot/templates.json): official blank forms with owner-accepted classifications and explicit authority-verification states.

Next milestone: completion of outstanding statutory and PDF checks.

A portfolio project exploring how documents in California employment litigation can be organized, annotated, and analyzed to support legal operations.

## Planned scope

- **Document taxonomy:** Define document families and subtypes across the litigation lifecycle, including pre-litigation and administrative records, pleadings, service and case-management documents, discovery requests and responses, productions, motions and supporting papers, orders, settlement materials, trial documents, and post-judgment or appellate records.
- **Public-source annotation:** Develop annotation guidelines and label a curated set of publicly available documents, recording source URLs, provenance, document type, litigation stage, and ambiguous cases. Review reuse permissions and privacy before including any source material; exclude confidential client files.
- **SQL operations analysis:** Design a relational schema and queries to examine document volumes, type and stage distributions, metadata completeness, and annotation quality.
- **Eventual AI-assisted classification:** Explore document-type classification after the taxonomy and labeled examples are established, with a baseline, held-out evaluation, error analysis, and human review.

## Planned sequence

1. Draft the taxonomy and annotation guidelines.
2. Curate public sources and annotate an initial sample.
3. Build the SQL schema and operations analysis.
4. Evaluate an AI-assisted classification prototype.

This is an educational portfolio project, not legal advice or a production legal system.
