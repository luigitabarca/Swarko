from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
import mysql.connector

canvas = Canvas("font-colors.pdf", pagesize=LETTER)



mydb = mysql.connector.connect(
  host="localhost",
  user="luigi",
  password="rainacid01",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM inregistrari")

myresult = mycursor.fetchall()
i=9.0
for x in myresult:
    a=str(x)
    canvas.drawString(2 * inch, i * inch, a)
    i=i-0.2
canvas.save()
