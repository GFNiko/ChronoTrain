from db.insert_user import AddUser
from source.db.user_from_db import GetUser
from db.report_to_database import SaveReport

"""
Functions toolbox as an adapter between GUI and Database. 
"""


def addUser(user: list) -> None:
    """ Save user in database """
    adduser = AddUser()
    adduser.insert_user(user[0], user[1], user[2])


def get_user(un: str):
    """ Read out user from database """
    getuser = GetUser()
    return getuser.select_user(un)


def save_report(ident: str, report: str, start: str, stopit: str):
    """ Saves daily report to database """
    report_saver = SaveReport()
    report_saver.save(ident, report, start, stopit)
