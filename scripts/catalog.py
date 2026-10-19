"""Build and search a metadata-only SQLite catalog. Python standard library only."""
import argparse
import json
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[1]

def build():
    data = json.loads((ROOT / "data/pilot/templates.json").read_text())
    db = sqlite3.connect(":memory:")
    db.row_factory = sqlite3.Row
    db.executescript((ROOT / "sql/schema.sql").read_text())
    for r in data["records"]:
        db.execute("INSERT INTO documents VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
            r["document_id"], r["form_number"], r["original_title"],
            r["family"], r["subtype"], r["stage"], r["document_status"],
            r["form_effective_date"], r["source_page_url"], r["retrieved_at"],
            r["review_status"], r["redistribution_review"], r["model_use_review"],
            r["taxonomy_version"]))
        for n, ref in enumerate(r["authority_references"], 1):
            db.execute("INSERT INTO authority_references VALUES (?,?,?,?,?)",
                       (r["document_id"], n, ref["citation"], ref["url"], ref["status"]))
    db.commit()
    return db

def search(db, text):
    # Bind parameters; escape LIKE wildcards so search text stays literal.
    term = "%" + text.replace("!", "!!").replace("%", "!%").replace("_", "!_") + "%"
    return db.execute(
        """SELECT form_number, title, family, subtype, source_url
        FROM documents
        WHERE form_number LIKE ? ESCAPE '!' OR title LIKE ? ESCAPE '!'
           OR subtype LIKE ? ESCAPE '!'
        ORDER BY form_number""", (term, term, term)).fetchall()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--search", help="Find a form by number, title, or subtype")
    args = parser.parse_args()
    db = build()
    print("Five-form blank-template prototype. Labels accepted by owner; source checks remain pending.")
    if args.search is not None:
        rows = search(db, args.search)
        print(json.dumps([dict(r) for r in rows], indent=2, ensure_ascii=False))
    else:
        sql = (ROOT / "sql/operations.sql").read_text()
        for query in sql.split(";"):
            if query.strip():
                rows = db.execute(query).fetchall()
                print(json.dumps([dict(r) for r in rows], indent=2, ensure_ascii=False))
    db.close()

if __name__ == "__main__":
    main()
