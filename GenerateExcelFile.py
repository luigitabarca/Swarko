import xlsxwriter
import mysql.connector
from datetime import date
from datetime import datetime

# log in to db
mydb = mysql.connector.connect(
  host="localhost",
  user="luigi",
  password="rainacid01",
  database="mydatabase"
)


today=str(date.today())

# select data from db
mycursor = mydb.cursor()
mycursor.execute("SELECT  data, ora, substanta, greutatea FROM inregistrari WHERE data LIKE'"+ today +"'")
myresult = mycursor.fetchall()

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('RaportCantarire.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
cell_format1 = workbook.add_format()
cell_format1.set_num_format('0')

# Write some data headers.
worksheet.write('A1', 'Data', bold)
worksheet.write('B1', 'Ora', bold)
worksheet.write('C1', 'Substanta', bold)
worksheet.write('D1', 'Greutatea', bold)

# Some data we want to write to the worksheet.
greutateatotala = dict()
greutateatotala['Acetat Butil']=0
greutateatotala['MEK']=0
greutateatotala['MIBK']=0
greutateatotala['Toluen']=0
greutateatotala['Acetat Etil']=0
# Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 0

# Iterate over the data and write it out row by row.
for data, ora, substanta, greutatea in  myresult:
    worksheet.write(row, col,     data)
    worksheet.write(row, col + 1, ora)
    worksheet.write(row, col + 2, substanta)
    worksheet.write(row, col + 3, int(greutatea[:-2]), cell_format1)
    row += 1

    greutateatotala[substanta]=greutateatotala[substanta]+int(greutatea[:-2])

# Write a total using a formula.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 3, '=SUM(D2:D'+str(row)+')')


worksheet.write('H1', 'Substanta', bold)
worksheet.write('I1', 'Greutatea', bold)

worksheet.write('H2', 'Acetat Butil')
worksheet.write('I2', greutateatotala['Acetat Butil'])

worksheet.write('H3', 'MEK')
worksheet.write('I3', greutateatotala['MEK'])

worksheet.write('H4', 'MIBK')
worksheet.write('I4', greutateatotala['MIBK'])

worksheet.write('H5', 'Toluen')
worksheet.write('I5', greutateatotala['Toluen'])

worksheet.write('H6', 'Acetat Etil')
worksheet.write('I6', greutateatotala['Acetat Etil'])


workbook.close()