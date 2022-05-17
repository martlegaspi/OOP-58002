import pyodbc
try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\sayom\OneDrive\Documents\Database3.accdb;')
    print("Database is connected")

    Address = 'Navotas'
    user_id = 1

    Sem = 100
    user_id = 10
    record = connection.cursor()
    record.execute('update Table1 SET Address=? WHERE id=?',(Address,user_id))
    record.execute('update Table1 SET Sem=? WHERE id=?', (Sem, user_id))
    record.commit()
    print("Database is updated")


except pyodbc.Error as e:
    print("Error in Connection")
