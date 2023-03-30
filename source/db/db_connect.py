import sqlite3
from dataclasses import dataclass

from source.logging_logic import log_func


@dataclass
class DbConnection:
    try:
        con: sqlite3 = sqlite3.connect("db/training.db")
        cur: con = con.cursor()
    except sqlite3.OperationalError as E:
        log_func().error(E)

    def close(self):
        if self.cur:
            self.cur.close()
        if self.con:
            self.con.close()
