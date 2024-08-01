from fpdf import FPDF
ask_name = input("Name: ")
new_text = ask_name+ " took CS50"

pdf = FPDF(orientation="P", unit="mm", format="A4")

#adds a page
pdf.add_page()
#sets the universal font
pdf.set_font("Times", size=50)
#adds image from file
pdf.image("shirtificate.png",x='C', y = 50, w=175, h=175)
pdf.set_y(20)
#adds cell containing title text
pdf.cell(0, 0, "CS50 Shirtificate", border = 0, align='C')
#moves cursor to new position before making new cell
pdf.set_y(100)

pdf.set_font("Times", size=30)
pdf.cell(0, 0, new_text, border = 0, align='C')
pdf.output("Brandon.pdf")

