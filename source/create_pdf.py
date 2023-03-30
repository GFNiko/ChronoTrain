from fpdf import FPDF

from db.report_from_db import GetReport


def _get_report(identnr: int):
    get_report = GetReport()
    return get_report.getreport(identnr)


class PDF(FPDF):

    def __init__(self):
        super().__init__()
        self.data_dict = None

    def header(self):
        self.set_font('helvetica', 'B', 15)
        self.cell(80)
        self.cell(50, 10, "ChronoTrain", align='C')
        self.set_font('helvetica', '', 13)
        self.ln(10)
        self.cell(100, 10, "Ausgabe ausgewählter Berichte: ", align='C')
        self.ln(10)

    def body(self, identnr):
        raw_data = _get_report(identnr)
        key_list = ["Report", "Datum", "Ident Nr.", "Startzeit", "Endzeit"]

        data_dict = {key_list[i]: [entry[i] for entry in raw_data]
                     for i in range(len(key_list))}

        # print(data_dict)

        # Define column widths
        col_widths = [self.w * 5 / 10] + [self.w / 10] * 4

        # Add headers to table
        for key in data_dict:
            self.cell(col_widths[list(data_dict.keys()).index(key)], 10, key, border=1)

        # Add data to table
        self.ln()
        for row in range(len(list(data_dict.values())[0])):
            for value in data_dict.values():
                self.cell(col_widths[
                              list(data_dict.values()).index(value)
                          ], 10, str(value[row]), border=1)
            self.ln()

        # Output PDF
        self.output('../table.pdf')
        print("Erfolgreich gespeichert")

    def footer(self):
        img = '../media/logo.png'
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, 'Huddeij Softworks @2023', align='C')
        self.image(img, x=10, y=275, w=20)
