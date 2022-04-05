from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
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
azi=date.today()
azi=str(azi)
mycursor.execute("SELECT * FROM inregistrari WHERE data LIKE'"+ azi +"'")

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
