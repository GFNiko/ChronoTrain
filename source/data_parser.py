import datetime as dt

from db.insert_user import AddUser
from db.readout import ReadOut
from source.db.user_from_db import GetUser
from db.report_to_database import SaveReport


def parse_end_time(end: dt.datetime) -> str:
    # global end_time
    end_time = end
    return end_time.strftime("%H:%M:%S")


def parse_report(report: str) -> None:
    print(report)
    parse_end_time(dt.datetime.now())


def addUser(user: list) -> None:
    adduser = AddUser()
    adduser.insert_user(user[0], user[1], user[2])
    # adduser.close()


def readOutAll() -> None:
    readout = ReadOut()
    readout.reader()
    readout.close()


def get_user(un: str, pw: str) -> bool:
    getuser = GetUser()
    user = getuser.select_user(un)

    try:
        return user[0][2] == pw

    except IndexError:
        return False


def get_user_ident(un: str) -> str:
    get_ident = GetUser()
    return get_ident.select_user(un)[0][0]


def save_report(ident: str, report: str, start: str, stopit: str):
    report_saver = SaveReport()
    report_saver.save(ident, report, start, stopit)
