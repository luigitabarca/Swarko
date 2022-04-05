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
#mycursor.execute("DROP TABLE inregistrari")
# mycursor.execute("CREATE TABLE inregistrari (id INT AUTO_INCREMENT PRIMARY KEY, ora VARCHAR(255), data VARCHAR(255), greutatea VARCHAR(255), substanta VARCHAR(255))")
for i in range(100):
  sql = "INSERT INTO inregistrari (ora, data, greutatea, substanta) VALUES (%s, %s, %s, %s)"
  now=datetime.now()
  dt_string = now.strftime(" %H:%M:%S")
  val = (dt_string, date.today(), "55kg","Toluen")
  mycursor.execute(sql, val)

  val = (dt_string, date.today(), "65kg","Acetat Butil")
  mycursor.execute(sql, val)

  val = (dt_string, date.today(), "75kg","MEK")
  mycursor.execute(sql, val)

  val = (dt_string, date.today(), "85kg","MIBK")
  mycursor.execute(sql, val)

  val = (dt_string, date.today(), "95kg","Acetat Etil")
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")

# mycursor.execute("SELECT * FROM inregistrari")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)