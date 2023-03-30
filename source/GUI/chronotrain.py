from dataclasses import dataclass

import ttkbootstrap as tb
from ttkbootstrap.constants import *


def center_window(screen_width: int,
                  screen_height: int,
                  width: int = 600,
                  height: int = 400
                  ) -> str:
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    return '%dx%d+%d+%d' % (width, height, x, y)


@dataclass
class ChronoTrainGUI:

    root = tb.Window(themename='solar')
    root.title("ChronoTrain")
    root.geometry(center_window(root.winfo_screenwidth(),
                                root.winfo_screenheight(),
                                700, 600))

    spacer = tb.Label(root,
                      text="_____________",
                      bootstyle=DARK)
    spacer.pack(pady=20)

    main_title = tb.Label(root,
                          text='ChronoTrain',
                          font=('Helvetica', 26),
                          bootstyle=SUCCESS)
    main_title.pack()

    subtitle = tb.Label(root,
                        text="by Huddeij SoftWorks",
                        font="Calibri",
                        bootstyle="SECONDARY")
    subtitle.pack()

    spacer = tb.Label(root,
                      text="_____________",
                      bootstyle=DARK)
    spacer.pack()

    failed = None
    ident_nr = None
