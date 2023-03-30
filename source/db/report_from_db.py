from .db_connect import DbConnection
from dataclasses import dataclass


@dataclass
class GetReport(DbConnection):

    def getreport(self, userid: int) -> list:
        output = self.cur.execute("""
        SELECT * FROM training WHERE userid = """ + str(userid)).fetchmany(7)

        # print(output)

        self.con.commit()

        return output
