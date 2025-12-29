import sqlite3
from pathlib import Path


def test_pets_database_has_expected_tables():
    repo_root = Path(__file__).resolve().parents[1]
    db_path = repo_root / "pets_database.db"
    assert db_path.exists(), f"Database file not found at {db_path}"

    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = {row[0].lower() for row in cur.fetchall()}
    conn.close()

    assert "cats" in tables, "Expected table 'cats' not found in database"
    assert "owners" in tables, "Expected table 'owners' not found in database"
