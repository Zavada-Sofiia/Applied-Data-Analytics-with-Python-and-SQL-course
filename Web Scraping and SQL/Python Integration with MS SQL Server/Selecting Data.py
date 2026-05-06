import pyodbc
import customtkinter

try:
    connection = pyodbc.connect('DRIVER={SQL Server};' +
                                'server=DESKTOP-8B4115O;' +
                                'database=company;' +
                                'Trusted_Connection=yes')
    cursor = connection.cursor()

    cursor.execute("select * from employee1")

    for data in cursor:
        print(data[0],data[1])

except pyodbc.Error as ex:
    print("Failed!",ex)
