import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\sayom\OneDrive\Documents\Database3.accdb;')
    print("Database is connected")

    ID = 6
    Fullname = 'Legaspi, Mart Joven C.'
    Address = 'Pasig'
    Contact = 457742040
    Birthdate = '20/02/1993'
    Sem = 80
    record = connection.cursor()
    record.execute('INSERT INTO Table1 (ID, Fullname, Address, Contact, Birthdate, Sem) VALUES (?,?,?,?,?,?)', (ID, Fullname, Address, Contact, Birthdate, Sem))
    record.commit()
    print("Database is added")

except pyodbc.Error as e:
    print("Error in Connection")