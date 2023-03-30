from GUI.login_gui import Login
from db.create_db import CreateTables
from source.logging_logic import log_func

""" Set the level of logging 0: NOTSET, 10: DEBUG,
20: INFO, 30: WARNING, 40: ERROR, 50: CRITICAL """
LOGGING_LEVEL = 10

log_func(LOGGING_LEVEL)


def create_tables():
    """ Checks for database existence and
        creates dependent tables, if not found. """
    create_tb = CreateTables()
    create_tb.create_user_table()
    create_tb.create_report_table()


def main():
    """ Main Function """
    create_tables()

    # Create GUI window, in the login screen
    gui = Login()
    gui.login_area()
    gui.root.mainloop()


if __name__ == '__main__':
    log_func().info("Program run")
    main()
