"""Small helper for connecting to SQLite.

The main reason this exists is so every route uses the same connection settings
(like sqlite3.Row so we can access columns by name).
"""

import sqlite3

def get_db_connection():
    conn = sqlite3.connect('quiz.db')
    conn.row_factory = sqlite3.Row
    return conn
