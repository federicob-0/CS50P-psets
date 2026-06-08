from fpdf import FPDF, Align


class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", size=50, style="B")
        self.cell(text="CS50 Shirtificate", center=True, h=70)


def main():
    name = input("Name: ").strip()
    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png", x=Align.C, y=75, w=pdf.epw)
    pdf.set_font("Helvetica", size=24, style="B")
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(text=f"{name} took CS50", center=True, h=260)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
