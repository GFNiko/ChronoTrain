import sqlite3
import tkinter as tk
from dataclasses import dataclass

import ttkbootstrap as tb
from ttkbootstrap.constants import *

from source.data_parser import get_user, addUser
from source.secure_password import check_password, gen_password_hash
from .chronotrain import ChronoTrainGUI
from .main_area import Notebook


@dataclass
class AddUser(ChronoTrainGUI):
    registry_frame = tb.Frame(ChronoTrainGUI.root)
    registry_frame.pack(pady=20)

    def add_user_frame(self):

        def clear_entries() -> None:
            identnr_entry.delete(0, END)
            usern_entry.delete(0, END)
            passw_entry.delete(0, END)
            passw_repeat_entry.delete(0, END)

        def check_empty() -> bool:
            return (len(identnr_entry.get()) < 1
                    or len(usern_entry.get()) < 1
                    or len(passw_entry.get()) < 1
                    or len(passw_repeat_entry.get()) < 1)

        def success():
            success_frame = tb.Frame(self.root)
            success_lbl = tb.Label(success_frame,
                                   text="Erfolgreich gespeichert",
                                   bootstyle=SUCCESS,
                                   font=("Helvetica", 22))
            success_lbl.pack()
            success_frame.pack()
            self.root.after(1500, success_frame.destroy)

        def parse_registry() -> None:
            self.wrong_pass_frame = tb.Frame(self.root)
            self.wrong_pass_frame.place(relx=0.5, rely=0.8, anchor=CENTER)
            self.wrong_pass_frame.lift()
            wrong_pass_lbl = tb.Label(self.wrong_pass_frame,
                                      text='',
                                      font='calibri',
                                      bootstyle=DANGER)

            if passw_entry.get() != passw_repeat_entry.get() or check_empty():
                wrong_pass_lbl.config(text="Falsche Eingabe!")
                wrong_pass_lbl.pack()

            else:
                try:
                    addUser([identnr_entry.get(), usern_entry.get(), gen_password_hash(passw_entry.get())])
                    self.registry_frame.destroy()
                    success()
                    self.ls = Login()
                    self.ls.build_frame()
                    self.ls.login_area()
                except sqlite3.IntegrityError:
                    wrong_pass_lbl.config(text="Identnummern sind nur Zahlen!")
                    wrong_pass_lbl.pack()

        # # Create new Frame and destroy login Frame

        Login.login_frame.destroy()

        # labels
        main_title_lbl = tb.Label(self.registry_frame,
                                  text="User hinzufügen",
                                  bootstyle=INFO,
                                  font=('Calibri', 16),
                                  justify='center')
        main_title_lbl.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

        identnr_lbl = tb.Label(self.registry_frame,
                               text="Identnummer: ",
                               font='Calibri')
        identnr_lbl.grid(column=0, row=1)

        username_lbl = tb.Label(self.registry_frame,
                                text="Username: ",
                                font='Calibri')
        username_lbl.grid(column=0, row=2, pady=20)

        password_lbl = tb.Label(self.registry_frame,
                                text="Passwort: ",
                                font='Calibri')
        password_lbl.grid(column=0, row=3)

        passw_repeat_lbl = tb.Label(self.registry_frame,
                                    text="Password wiederholen: ",
                                    font='Calibri')
        passw_repeat_lbl.grid(column=0, row=4, pady=20)

        # Entries
        identnr_entry = tb.Entry(self.registry_frame)
        identnr_entry.grid(column=1, row=1)

        usern_entry = tb.Entry(self.registry_frame)
        usern_entry.grid(column=1, row=2)

        passw_entry = tb.Entry(self.registry_frame, foreground='green', show="*")
        passw_entry.grid(column=1, row=3)

        passw_repeat_entry = tb.Entry(self.registry_frame, foreground='green', show='*')
        passw_repeat_entry.grid(column=1, row=4)

        # Buttons
        clear_btn = tb.Button(self.registry_frame,
                              text="Löschen",
                              bootstyle=(WARNING, OUTLINE),
                              command=clear_entries)
        clear_btn.grid(column=0, row=5, pady=20)

        save_btn = tb.Button(self.registry_frame,
                             text="Speichern",
                             bootstyle=(SUCCESS, OUTLINE),
                             command=lambda: parse_registry())
        save_btn.grid(column=1, row=5, sticky='EW')


@dataclass()
class Login(ChronoTrainGUI):
    login_frame = tk.Frame(ChronoTrainGUI.root)
    login_frame.pack()
    add_user = None
    pass_entry = None
    username_entry = None

    def build_frame(self):
        self.login_frame = tk.Frame(ChronoTrainGUI.root)
        self.login_frame.pack(pady=20)

    def add_user_call(self):
        self.add_user = AddUser()
        self.add_user.add_user_frame()
        self.destroy_frame()

    def destroy_frame(self):
        self.login_frame.destroy()

    def credentials_check(self) -> None:
        try:
            user = get_user(self.username_entry.get())
            self.ident_nr = user[0]
            passwd = user[1]
            if check_password(passwd, gen_password_hash(passwd)):
                self.login_frame.destroy()
                ma = Notebook()
                ma.input_area(self.ident_nr)
                ma.output_area(self.ident_nr)
                self.failed.config(text="")
            else:
                self.failed.place(relx=0.5, rely=0.5, y=120, anchor=CENTER)

        except TypeError:
            self.failed.place(relx=0.5, rely=0.5, y=120, anchor=CENTER)

    def login_area(self):

        self.failed = tb.Label(self.root,
                               text="Login inkorrekt. Bitte erneut eingeben!",
                               bootstyle=DANGER,
                               font=('Calibri', 16))

        # Labels
        login_lbl = tb.Label(self.login_frame,
                             text="Login",
                             font=("Calibri", 16),
                             bootstyle=INFO)
        login_lbl.grid(column=0, row=1, columnspan=2)

        username_lbl = tb.Label(self.login_frame,
                                text="Username: ",
                                font="Calibri")
        username_lbl.grid(column=0, row=3, pady=20)

        pass_lbl = tb.Label(self.login_frame,
                            text="Passwort: ",
                            font="Calibri")
        pass_lbl.grid(column=0, row=4)

        # Entries
        self.username_entry = tb.Entry(self.login_frame)
        self.username_entry.grid(column=1, row=3)

        self.pass_entry = tb.Entry(self.login_frame, foreground="green", show="*")
        self.pass_entry.grid(column=1, row=4)

        """ Buttons """
        # Login
        login_btn = tb.Button(self.login_frame,
                              text="Login",
                              bootstyle=(SUCCESS, OUTLINE),
                              command=self.credentials_check)
        login_btn.grid(column=0, row=5, pady=20)

        # Registry
        reg_btn = tb.Button(self.login_frame,
                            text="Account beantragen",
                            bootstyle=(WARNING, OUTLINE),
                            command=self.add_user_call)
        reg_btn.grid(column=1, row=5)
