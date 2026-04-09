from __future__ import annotations

import sqlite3
from typing import Any

import pandas as pd


def build_demo(
    db_path: str = ":memory:",
) -> tuple[sqlite3.Connection, sqlite3.Cursor, pd.DataFrame, pd.DataFrame]:
    """Build a tiny SQLite database and matching pandas DataFrames.

    This helper keeps the SQL setup boilerplate out of the teaching narrative.
    It returns:

    - `conn`: an open SQLite connection
    - `cur`: a cursor for executing queries
    - `orders`: a DataFrame with the same `orders` rows
    - `customers`: a DataFrame with the same `customers` rows
    """

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    order_rows: list[tuple[Any, ...]] = [
        (1, 101, 120.5, "2024-01-02"),
        (2, 102, 75.0, "2024-01-03"),
        (3, 103, 210.0, "2024-01-04"),
        (4, 101, 55.0, "2024-01-05"),
        (5, 104, 320.0, "2024-01-06"),
    ]

    customer_rows: list[tuple[Any, ...]] = [
        (101, "US"),
        (102, "UK"),
        (103, "DE"),
        (104, "US"),
    ]

    schema_sql = """
    CREATE TABLE orders (
        order_id INTEGER,
        customer_id INTEGER,
        amount REAL,
        order_date TEXT
    );
    CREATE TABLE customers (
        customer_id INTEGER,
        country TEXT
    );
    """

    cur.executescript(schema_sql)
    cur.executemany(
        "INSERT INTO orders VALUES (?, ?, ?, ?);",
        order_rows,
    )
    cur.executemany(
        "INSERT INTO customers VALUES (?, ?);",
        customer_rows,
    )

    orders = pd.DataFrame(
        order_rows,
        columns=["order_id", "customer_id", "amount", "order_date"],
    )
    customers = pd.DataFrame(
        customer_rows,
        columns=["customer_id", "country"],
    )

    return conn, cur, orders, customers


if __name__ == "__main__":
    conn, cur, orders, customers = build_demo()
    print(orders)
    conn.close()
