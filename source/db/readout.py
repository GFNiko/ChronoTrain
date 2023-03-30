import sqlite3
from dataclasses import dataclass
from .db_connect import DbConnection

@dataclass
class ReadOut(DbConnection):

    def reader(self) -> str:
        try:
            readout = self.cur.execute('''SELECT * FROM user''').fetchall()
            self.con.commit()
            print("Query successful executed")
            return readout

        except sqlite3.OperationalError:
            print("Error, try again please")
        #
        # finally:
        #     self.con.close()
