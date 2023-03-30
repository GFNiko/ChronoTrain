import sqlite3
from dataclasses import dataclass
from .db_connect import DbConnection
import logging


logging.basicConfig(filename="../db.log", level=logging.DEBUG)
logger = logging.getLogger()


@dataclass
class CreateTables(DbConnection):

    def create_user_table(self):
        try:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS user (
                                    userid INTEGER PRIMARY KEY NOT NULL,
                                    username TEXT NOT NULL UNIQUE,
                                    passwd TEXT NOT NULL,
                                    registrydate DATETIME)""")
            self.con.commit()

        except sqlite3.OperationalError as E:
            logger.error(f"Error {E}")

    def create_report_table(self):
        try:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS training (
                                report TEXT NOT NULL,
                                dateofcreation DATE NOT NULL,
                                userid INTEGER,
                                ttstart TIME NOT NULL,
                                ttstop TIME NOT NULL,
                                FOREIGN KEY (userid) REFERENCES user(userid))""")
            self.con.commit()

        except sqlite3.OperationalError as E:
            logger.error(E)
