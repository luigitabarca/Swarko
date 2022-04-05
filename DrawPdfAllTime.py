from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import PageBreak
import mysql.connector
from datetime import date
canvas = Canvas("font-colors.pdf", pagesize=LETTER)



mydb = mysql.connector.connect(
  host="localhost",
  user="luigi",
  password="rainacid01",
  database="mydatabase"
)

mycursor = mydb.cursor()

#calculeaza data curenta si filtreaza datele

mycursor.execute("SELECT * FROM inregistrari")

myresult = mycursor.fetchall()
i=10.0
count=0
for x in myresult:
    a=str(x)
    canvas.drawString(2 * inch, i * inch, a)
    i=i-0.2
    count=count+1
    if count == 40:
        canvas.showPage()
        count=0
        i=10.0
    
canvas.save()
