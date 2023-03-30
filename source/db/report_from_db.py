import sqlite3

from .db_connect import DbConnection
from dataclasses import dataclass
import logging


logging.basicConfig(filename="../db.log", level=logging.DEBUG)
logger = logging.getLogger()


@dataclass
class GetReport(DbConnection):

    def getreport(self, userid: int) -> list:
        try:
            output = self.cur.execute("""
            SELECT * FROM training WHERE userid = """ + str(userid)).fetchone()
            self.con.commit()
            logger.info("Report successful returned from db")

            return output

        except sqlite3.OperationalError as E:
            logger.error(E)

