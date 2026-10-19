# Legal Document Intelligence

**Status: In development — planning stage.** This repository currently documents the project scope. The taxonomy, annotated dataset, SQL analysis, and AI classifier are planned; none is complete.

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
