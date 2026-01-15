\
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "vulnlab.db")

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

schema_users = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL,
  email TEXT NOT NULL,
  role TEXT NOT NULL
);
"""

schema_comments = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  comment TEXT NOT NULL,
  created_at TEXT NOT NULL
);
"""

seed_users = [
    ("admin", "admin123", "admin@vulnlab.local", "admin"),
    ("user1", "pass123", "user1@vulnlab.local", "user"),
    ("user2", "pass123", "user2@vulnlab.local", "user"),
]

def main():
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(schema_users)
        conn.execute(schema_comments)
        conn.commit()

        # insert seeds if not exists
        for u, p, e, r in seed_users:
            conn.execute(
                "INSERT OR IGNORE INTO users(username, password, email, role) VALUES (?, ?, ?, ?)",
                (u, p, e, r),
            )
        conn.commit()
        print("✅ Database initialized:", DB_PATH)
        print("✅ Seed users inserted (admin/user1/user2).")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
