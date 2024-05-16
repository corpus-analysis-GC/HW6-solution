#!/usr/bin/env python
"""Runs queries for HW6."""

import sqlite3


DB_PATH = "hw6.db"


def main() -> None:
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        hundred_pmw = cursor.execute(
            """
            SELECT SUM(frequency) / 10000 FROM frequencies
            """
        ).fetchone()[0]
        for row in cursor.execute(
            f"""
            SELECT DISTINCT frequencies.word
            FROM frequencies
            JOIN morphology
            ON frequencies.word = morphology.word
            WHERE morphology.features LIKE 'N;%'
            AND frequencies.frequency >= {hundred_pmw}
            ORDER BY frequencies.word
            """
        ):
            print(row[0])


if __name__ == "__main__":
    main()
