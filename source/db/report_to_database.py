import datetime as dt
import sqlite3
from dataclasses import dataclass

from .db_connect import DbConnection


@dataclass
class SaveReport(DbConnection):

    def save(self, userid, report, start, stop):
        input_dict = {
            "report": report,
            'today': str(dt.datetime.now().strftime('%Y-%m-%d')),
            "userid": userid,
            "start": start,
            "stop": stop}

        try:
            self.cur.execute("""INSERT INTO training VALUES (
            :report, :today, :userid, :start, :stop)""", input_dict)
            self.con.commit()

        except sqlite3.OperationalError:
            print("Oh No! A wild Error appeared")
