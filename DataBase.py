from datetime import date
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="luigi",
  password="rainacid01",
  database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("show databases;")

# mycursor.execute("CREATE TABLE inregistrari (id INT AUTO_INCREMENT PRIMARY KEY, ora VARCHAR(255), data VARCHAR(255), greutatea VARCHAR(255))")

sql = "INSERT INTO inregistrari (ora, data, greutatea) VALUES (%s, %s, %s)"
now=datetime.now()
dt_string = now.strftime(" %H:%M:%S")
val = (dt_string, date.today(), "355kg")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

# mycursor.execute("SELECT * FROM inregistrari")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)