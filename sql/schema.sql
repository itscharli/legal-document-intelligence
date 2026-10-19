PRAGMA foreign_keys = ON;
CREATE TABLE documents (
 document_id TEXT PRIMARY KEY,
 form_number TEXT NOT NULL UNIQUE,
 title TEXT NOT NULL,
 family TEXT NOT NULL,
 subtype TEXT NOT NULL,
 stage TEXT NOT NULL,
 document_status TEXT NOT NULL CHECK(document_status = 'blank_template'),
 form_effective_date TEXT NOT NULL,
 source_url TEXT NOT NULL,
 source_checked_at TEXT NOT NULL,
 label_review_status TEXT NOT NULL,
 redistribution_review TEXT NOT NULL,
 model_use_review TEXT NOT NULL,
 taxonomy_version TEXT NOT NULL
);
CREATE TABLE authority_references (
 document_id TEXT NOT NULL REFERENCES documents(document_id),
 reference_number INTEGER NOT NULL,
 citation TEXT NOT NULL,
 source_url TEXT NOT NULL,
 verification_status TEXT NOT NULL,
 PRIMARY KEY(document_id, reference_number)
);
