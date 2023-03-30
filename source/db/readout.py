import sqlite3
from dataclasses import dataclass
from .db_connect import DbConnection
from source.loging_logic import log_func


@dataclass
class ReadOut(DbConnection):

    def reader(self) -> str:
        try:
            readout = self.cur.execute('''SELECT * FROM user''').fetchall()
            self.con.commit()
            log_func().debug("User in db found")
            return readout

        except sqlite3.OperationalError as E:
            log_func().error(E)
