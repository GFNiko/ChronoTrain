import datetime as dt
import sqlite3
from dataclasses import dataclass

from source.logging_logic import log_func
from .db_connect import DbConnection


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

            log_func().debug(f"User {username} created")

        except sqlite3.OperationalError as E:
            log_func().error(E)
