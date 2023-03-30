import os.path

from db.create_db import CreateTables
from db.readout import ReadOut
from GUI.login_gui import Login
# from GUI.main_area import Notebook


def create_tables():
    """ Checks for database existence and
        creates dependent tables, if not found. """
    if not os.path.isfile('db/training.db'):
        create_tb = CreateTables()
        create_tb.create_user_table()
        create_tb.create_report_table()


def check_for_user():
    """ Debugging module -> print all users,
        and it's elements from 'user' table. """


    readit = ReadOut()
    for entry in readit.reader():
        print(entry)
        # for x, y in enumerate(entry):
        #     print(f"{entry_list[x]}: {y}")
        print("\n")


def main():
    """ Main Function """
    create_tables()
    # check_for_user()

    # Create GUI window, in the login screen
    gui = Login()
    gui.login_area()
    gui.root.mainloop()

    # Create GUI window, in the main screen, with dummy ident number
    # nb = Notebook()
    # nb.input_area(9847583)
    # nb.output_area(9847583)
    # nb.root.mainloop()


if __name__ == '__main__':
    main()
