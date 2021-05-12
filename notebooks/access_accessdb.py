import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\lgProgam\DataSet\Brazilian E-Commerce Public Dataset by Olist\eCommerce_BRZ.accdb;')


   
#for row in cursor.fetchall():
#    print (row)