from __future__ import annotations

import sqlite3


def read_metadata(conn: sqlite3.Connection, key: str) -> str | None:
    row = conn.execute("SELECT value FROM metadata WHERE key = ?", (key,)).fetchone()
    if row is None:
        return None
    return str(row[0])


def write_metadata(conn: sqlite3.Connection, key: str, value: str) -> None:
    conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", (key, value))


def write_metadata_map(conn: sqlite3.Connection, values: dict[str, str]) -> None:
    conn.executemany(
        "INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)",
        list(values.items()),
    )
