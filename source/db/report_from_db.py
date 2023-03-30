import sqlite3
from dataclasses import dataclass

from source.logging_logic import log_func
from .db_connect import DbConnection


@dataclass
class GetReport(DbConnection):

    def getreport(self, userid: int) -> list:
        try:
            output = self.cur.execute("""
            SELECT * FROM training WHERE userid = """ + str(userid)).fetchall()
            self.con.commit()
            log_func().debug("Report read from db")

            return output

        except sqlite3.OperationalError as E:
            log_func().error(E)
