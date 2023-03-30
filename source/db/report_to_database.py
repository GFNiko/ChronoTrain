import datetime as dt
import sqlite3
from dataclasses import dataclass

from source.logging_logic import log_func
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

            log_func().debug("Report saved to db")

        except sqlite3.OperationalError as E:
            log_func().error(E)
