import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\MJ\Download(D)\Database1.accdb;')
    print("Database is connected")



except pyodbc.Error as e:
    print("Error in Connection")