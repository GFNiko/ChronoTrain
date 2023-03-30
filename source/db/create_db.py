import sqlite3
from dataclasses import dataclass
from .db_connect import DbConnection
from source.logging_logic import log_func

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

            log_func().debug("Table 'user' created or already existent")

        except sqlite3.OperationalError as E:
            log_func().error(f"Error {E}")

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
            log_func().debug("Table 'training' created or already existent")

        except sqlite3.OperationalError as E:
            log_func().error(E)
