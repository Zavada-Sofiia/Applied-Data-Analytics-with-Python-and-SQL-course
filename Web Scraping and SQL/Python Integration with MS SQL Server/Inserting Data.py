# insert.py

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

# insert_gui.py

import pyodbc
import customtkinter

# Setup appearance for the GUI
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("300x500")
app.title("Insert into Table")

# Entry for table name, ID, and name
entry_table_name = customtkinter.CTkEntry(app, placeholder_text="Table name")
entry_table_name.place(relx=0.2, rely=0.1)

entry_id = customtkinter.CTkEntry(app, placeholder_text="ID")
entry_id.place(relx=0.2, rely=0.2)

entry_name = customtkinter.CTkEntry(app, placeholder_text="Name")
entry_name.place(relx=0.2, rely=0.3)


def insert():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'server=DESKTOP-8B4115O;' +
                                    'database=company;' +
                                    'Trusted_Connection=yes')
        connection.autocommit = True
        cursor = connection.cursor()

        # Format the SQL query with proper syntax
        sql_query = f"INSERT INTO {entry_table_name.get()} (id, name) VALUES (?, ?)"

        # Execute the query and pass parameters
        cursor.execute(sql_query, (int(entry_id.get()), entry_name.get()))

        # Update the UI
        info_label.configure(text="INSERT COMPLETED!")
        cursor.commit()
        cursor.close()

    except pyodbc.IntegrityError as ex:
        # Catch duplicate key errors (ID already exists)
        print("Duplicate entry for ID", ex)
        info_label.configure(text="Insert Failed! Duplicate ID.")

    except pyodbc.Error as ex:
        print("Connection Failed", ex)
        info_label.configure(text="Insert Failed!")


# Button to trigger the insert operation
insert_button = customtkinter.CTkButton(app, text="INSERT", command=insert, fg_color="green")
insert_button.place(relx=0.2, rely=0.4)

# Label to display the status
info_label = customtkinter.CTkLabel(app, text="Company")
info_label.place(relx=0.2, rely=0.5)

# Start the GUI application
app.mainloop()
