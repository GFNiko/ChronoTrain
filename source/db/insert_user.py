import datetime as dt
import logging
import sqlite3
from dataclasses import dataclass

from .db_connect import DbConnection

logging.basicConfig(filename="../db.log", level=logging.DEBUG)
logger = logging.getLogger()


@dataclass
class AddUser(DbConnection):

    def insert_user(self, identnr: str, username: str, passwd: str) -> None:
        try:
            input_dict = {"inr": identnr,
                          'un': username,
                          'pw': passwd,
                          'today': dt.datetime.now().strftime('%Y-%m-%d')}

            self.cur.execute("""INSERT INTO user VALUES (
                             :inr, :un, :pw, :today)""",
                             input_dict)
            self.con.commit()

            logger.info(f"User {username} successful created")

        except sqlite3.OperationalError as E:
            logger.error(E)
