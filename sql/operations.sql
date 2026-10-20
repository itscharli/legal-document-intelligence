-- Counts describe only this five-template sample, not litigation workload.
SELECT form_number, title, family, subtype
FROM documents
ORDER BY form_number;

-- Discovery templates.
SELECT form_number, title, source_url FROM documents
WHERE family = 'DSC' ORDER BY form_number;

-- Source references still requiring current statutory verification.
SELECT d.form_number, a.citation, a.verification_status
FROM authority_references a JOIN documents d USING(document_id)
WHERE a.verification_status <> 'current_rule_text_reviewed'
ORDER BY d.form_number, a.reference_number;

-- Label acceptance is separate from model-use and redistribution review.
SELECT form_number, label_review_status, redistribution_review, model_use_review
FROM documents ORDER BY form_number;

