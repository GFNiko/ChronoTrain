import sqlite3
from dataclasses import dataclass
from .db_connect import DbConnection
import logging


logging.basicConfig(filename="../db.log", level=logging.DEBUG)
logger = logging.getLogger()

@dataclass
class ReadOut(DbConnection):

    def reader(self) -> str:
        try:
            readout = self.cur.execute('''SELECT * FROM user''').fetchall()
            self.con.commit()
            logger.info("Query successful executed")
            return readout

        except sqlite3.OperationalError as E:
            logger.error(E)
