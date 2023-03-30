import sqlite3
from dataclasses import dataclass

@dataclass
class DbConnection:
    con: sqlite3 = sqlite3.connect("db/training.db")
    cur: con = con.cursor()

    def close(self):
        if self.cur:
            self.cur.close()
        if self.con:
            self.con.close()
