import sqlite3
from .db_connect import DbConnection
from dataclasses import dataclass


@dataclass
class CreateTables(DbConnection):

    def create_user_table(self):
        try:
            self.cur.execute("""
            CREATE TABLE user (
            userid INTEGER PRIMARY KEY NOT NULL,
            username TEXT NOT NULL UNIQUE,
            passwd TEXT NOT NULL,
            registrydate DATETIME)
            """)
            self.con.commit()
            print("user table created without any errors")

        except sqlite3.OperationalError:
            print("Table user already exists")

    def create_report_table(self):
        try:
            self.cur.execute("""
            CREATE TABLE training (
            report TEXT NOT NULL,
            dateofcreation DATE NOT NULL,
            userid INTEGER,
            ttstart TIME NOT NULL,
            ttstop TIME NOT NULL,
            FOREIGN KEY (userid) REFERENCES user(userid)
            )
            """)
            self.con.commit()
            print("report table created without any errors")

        except sqlite3.OperationalError:
            print("Table training already exists")

        # finally:
        #     self.con.close()


