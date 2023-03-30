import os.path

from GUI.login_gui import Login
from db.create_db import CreateTables
from source.db.db_connect import DbConnection


def create_tables():
    """ Checks for database existence and
        creates dependent tables, if not found. """
    # if not os.path.isfile('db/training.db'):
    create_tb = CreateTables()
    create_tb.create_user_table()
    create_tb.create_report_table()
    # else:
    #     print("tables already exist")


def main():
    """ Main Function """
    create_tables()

    # Create GUI window, in the login screen
    gui = Login()
    gui.login_area()
    gui.root.mainloop()


if __name__ == '__main__':
    main()
