import sqlite3

import datetime as dt
from dataclasses import dataclass
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

            print("Query successful executed")

        except sqlite3.OperationalError:
            print("Error, try again please")
