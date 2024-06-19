from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet


class receipt_error(Exception):
    pass


class make_receipt:
    def __init__(self, lst):
        self.DATA = [lst]
        print(self.DATA)

    def make_table(self, lst):
        self.DATA.append(lst)

    def build(self):
        pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

        styles = getSampleStyleSheet()

        title_style = styles["Heading1"]
        subtitle_style = styles["BodyText"]

        title_style.alignment = 1
        subtitle_style.alignment = 1

        title = Paragraph("Ved Patel", title_style)
        title2 = Paragraph("Built with ved patel api", subtitle_style)

        style = TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 1, colors.black),
                ("GRID", (0, 0), (4, 4), 1, colors.black),
                ("BACKGROUND", (0, 0), (3, 0), colors.gray),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ]
        )

        table = Table(self.DATA, style=style)

        pdf.build([title, table, title2])

        print("builded")
