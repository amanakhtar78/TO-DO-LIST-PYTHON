import sqlite3
import os
from flask import current_app, g

def get_db():
    """Establish a connection to the SQLite database."""
    if 'db' not in g:
        db_path = os.path.join(current_app.instance_path, 'task_manager.db')
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row  # This allows accessing columns by name (e.g., row['column_name'])
    return g.db

def init_db():
    """Initialize the database with schema."""
    db = get_db()
    with current_app.open_resource('schema.sql', mode='r') as f:
        db.executescript(f.read())
    db.commit()

def close_db(e=None):
    """Close the database connection."""
    db = g.pop('db', None)
    if db is not None:
        db.close()
