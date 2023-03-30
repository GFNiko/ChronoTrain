from dataclasses import dataclass
from tkinter import *

import ttkbootstrap as tb
from ttkbootstrap import Querybox
from ttkbootstrap.constants import *

from .chronotrain import ChronoTrainGUI
from source.create_pdf import PDF
from source.data_parser import *

import datetime as dt


@dataclass
class Notebook(ChronoTrainGUI):
    notebook_tabs = tb.Notebook(ChronoTrainGUI.root, bootstyle=DARK)
    notebook_tabs.pack()

    def input_area(self, identnr) -> None:

        input_frame = Frame(ChronoTrainGUI.root)
        input_frame.pack()

        def time_now() -> None:
            time2 = (dt.datetime.now().time().replace(microsecond=0),
                     dt.date.today().strftime("%d.%m.%Y"))
            current_datetime.configure(text=time2)
            input_frame.after(200, time_now)

        def validate_entry(var):
            text = daily_report_text.get('1.0', 'end-1c')
            if len(text) < 50:
                stop_recording_btn.configure(state='disabled')
            else:
                stop_recording_btn.configure(state='normal')

        def parse_start_time() -> None:
            global input_start_time
            input_start_time = dt.datetime.now().time().replace(microsecond=0)
            start_recording_btn.configure(state='disabled')
            daily_report_text.configure(state='normal')

        def kill_program():
            self.root.destroy()

        def end_frame():
            ending_frame = Frame(self.root, bg='black')
            ending_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            closing_lbl = tb.Label(ending_frame,
                                   justify='center',
                                   text="Vielen Dank.\nEinen schönen Feierabend!",
                                   bootstyle=WARNING,
                                   font=("Helvetica", 22))
            closing_lbl.pack()

        def report_to_db() -> None:
            save_report(identnr,
                        daily_report_text.get('1.0', 'end-1c'),
                        str(input_start_time),
                        str(dt.datetime.now().time().replace(microsecond=0)))
            end_frame()
            self.root.after(2000, kill_program)

        # User Identification Number
        user_lbl = tb.Label(input_frame,
                            text=f"User: {identnr}",
                            bootstyle=LIGHT,
                            font=("Calibri", 12))
        user_lbl.grid(column=0, row=0, sticky='w', pady=5, padx=5)

        # Subtitle Label
        datetime_lbl = tb.Label(input_frame,
                                text="Zeiterfassung & Bericht",
                                bootstyle=INFO,
                                font=("Calibri", 18))
        datetime_lbl.grid(column=1, row=1, columnspan=3)

        # Time and Date
        current_datetime = tb.Label(input_frame,
                                    text=(dt.datetime.now().time().replace(microsecond=0),
                                          dt.date.today().strftime("%d.%m.%Y")),
                                    bootstyle=SECONDARY,
                                    font=("Calibri"))
        current_datetime.grid(column=4, row=0)

        """ Report input area """
        # Label frame from left positioned labels
        lbl_frame = LabelFrame(input_frame, relief='flat', labelanchor='e')
        lbl_frame.grid(column=0, row=3)

        # Title and subtitle labels left of text area
        daily_report_lbl = tb.Label(lbl_frame,
                                    text="Tagesbericht:",
                                    bootstyle=SECONDARY,
                                    font=('Helvetica', 12),
                                    justify='right')
        daily_report_lbl.pack()
        daily_report_sublbl = tb.Label(lbl_frame,
                                       text='Mindestens 50 Zeichen',
                                       bootstyle=SECONDARY,
                                       justify='right')
        daily_report_sublbl.pack()

        # Input character counter function call and report input field
        text_var = StringVar()
        text_var.trace('w', validate_entry)
        daily_report_text = Text(input_frame,
                                 width=60,
                                 height=6,
                                 wrap='word',
                                 state='disabled')
        daily_report_text.bind('<KeyRelease>', validate_entry)
        daily_report_text.grid(column=1, row=3, columnspan=3, sticky='w')

        # Buttons
        start_recording_btn = tb.Button(input_frame,
                                        text="Zeiterfassung starten",
                                        bootstyle=SECONDARY,
                                        command=lambda: parse_start_time())
        start_recording_btn.grid(column=1, row=2, columnspan=3, pady=10)

        stop_recording_btn = tb.Button(input_frame,
                                       text="Zeiterfassung beenden",
                                       bootstyle=(SUCCESS, OUTLINE),
                                       state='disabled',
                                       command=lambda: report_to_db())
        stop_recording_btn.grid(column=1, row=4, columnspan=3, pady=10)

        time_now()
        self.notebook_tabs.add(input_frame, text="Eingabe")

    """" Main Output Area """
    def output_area(self, identnr) -> None:
        output_frame = Frame(ChronoTrainGUI.root)
        output_frame.pack(expand=True)

        def start_date_frame() -> None:
            global output_start_time
            cal_start = Querybox()
            output_start_time = cal_start.get_date()

        def end_date_frame() -> None:
            cal_end = Querybox()
            end_time = cal_end.get_date()
            if output_start_time is not None and end_time is not None:
                timeframe_lbl.config(text=f"Zeitraum: "
                                          f"{output_start_time.strftime('%d.%m.%Y')} - "
                                          f"{end_time.strftime('%d.%m.%Y')}")

        def call_pdf_creator():
            pdf = PDF()
            pdf.add_page(orientation="landscape")
            pdf.set_font('Times', size=12)
            pdf.set_margins(10, 20)
            pdf.body(identnr)

        def cancel_selection():
            timeframe_lbl.config(text="")

        # Labels
        user_lbl = tb.Label(output_frame,
                            text=f"User: {identnr}",
                            bootstyle=LIGHT,
                            font=("Calibri", 12))
        user_lbl.grid(column=0, row=0, sticky='w', pady=5, padx=5)

        info_lbl = tb.Label(output_frame,
                            text="Ausgabe in PDF",
                            bootstyle=INFO,
                            font=("Calibri", 18))
        info_lbl.grid(column=0, row=1, columnspan=4)

        period_lbl = tb.Label(output_frame,
                              text="Zeitraum",
                              bootstyle=INFO,
                              font=("Calibri", 14))
        period_lbl.grid(column=1, row=2, rowspan=2)

        begin_lbl = tb.Label(output_frame,
                             text="Startzeitpunkt",
                             bootstyle=LIGHT,
                             font=("Calibri", 12))
        begin_lbl.grid(column=2, row=2)

        end_lbl = tb.Label(output_frame,
                           text="Endzeitpunkt",
                           bootstyle=LIGHT,
                           font=("Calibri", 12))
        end_lbl.grid(column=2, row=3)

        timeframe_lbl = tb.Label(output_frame,
                                 text="",
                                 bootstyle=LIGHT,
                                 font=("Calibri", 12))
        timeframe_lbl.grid(column=2, row=4, columnspan=2, pady=10)

        placeholder_lbl = tb.Label(output_frame, text="")
        placeholder_lbl.grid(column=4, row=1)

        # Buttons
        begin_selector_btn = tb.Button(output_frame,
                                       text="Zeitpunkt wählen",
                                       bootstyle=(SECONDARY, OUTLINE),
                                       command=lambda: start_date_frame())
        begin_selector_btn.grid(column=3, row=2, pady=10)

        end_selector_btn = tb.Button(output_frame,
                                     text="Zeitpunkt wählen",
                                     bootstyle=(SECONDARY, OUTLINE),
                                     command=lambda: end_date_frame())
        end_selector_btn.grid(column=3, row=3)

        print_pdf_btn = tb.Button(output_frame,
                                  text="PDF drucken",
                                  bootstyle=(SUCCESS, OUTLINE),
                                  command=lambda: call_pdf_creator())
        print_pdf_btn.grid(column=1, row=5)

        cancel_btn = tb.Button(output_frame,
                               text="Eingabe zurücksetzen",
                               bootstyle=(WARNING, OUTLINE),
                               command=cancel_selection)
        cancel_btn.grid(column=3, row=5)

        # Add to Root Notebook
        self.notebook_tabs.add(output_frame, text="Ausgabe")
