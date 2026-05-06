import pyodbc

try:
    # Connect to the 'company' database
    connection = pyodbc.connect('DRIVER={SQL Server};' +
                                'server=DESKTOP-8B4115O;' +
                                'database=company;' +
                                'Trusted_Connection=yes')
    connection.autocommit = True

    cursor = connection.cursor()

    # First, ensure the table exists
    create_table_sql = """
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'EMPLOYEE1')
    BEGIN
        CREATE TABLE EMPLOYEE1 (
            id INT PRIMARY KEY,
            name NVARCHAR(50)
        )
    END
    """
    cursor.execute(create_table_sql)

    # Insert data into EMPLOYEE1 table
    cursor.execute("INSERT INTO EMPLOYEE1(id, name) VALUES(1, 'Rahul')")
    cursor.execute("INSERT INTO EMPLOYEE1(id, name) VALUES(2, 'Janvi')")
    cursor.execute("INSERT INTO EMPLOYEE1(id, name) VALUES(3, 'Karan')")
    cursor.execute("INSERT INTO EMPLOYEE1(id, name) VALUES(4, 'Shubham')")

    connection.commit()
    print("Data inserted successfully!")

except pyodbc.Error as ex:
    print("Connection or execution failed", ex)

finally:
    if connection:
        connection.close()
