import sqlite3
from dataclasses import dataclass


@dataclass
class DbConnection:
    con: sqlite3 = sqlite3.connect("db/training.db")
    cur: con = con.cursor()
