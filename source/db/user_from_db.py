import sqlite3
from dataclasses import dataclass

from .db_connect import DbConnection


@dataclass
class GetUser(DbConnection):

    def select_user(self, un: str):
        try:
            user = self.cur.execute("""SELECT userid, passwd
                             FROM user WHERE username=?""",
                                    [un]).fetchone()
            self.con.commit()
            return user

        except sqlite3.OperationalError:
            print("Oh No! Something went wrong! Please try again!")
