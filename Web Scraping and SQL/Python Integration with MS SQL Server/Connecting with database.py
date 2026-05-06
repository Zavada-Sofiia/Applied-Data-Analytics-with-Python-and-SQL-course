import pyodbc
import customtkinter

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("200x300")
app.title('Create-Connect MS Database')

entry_database = customtkinter.CTkEntry(app, placeholder_text="Database Name")
entry_database.place(relx=0.1, rely=0.1)


def create_db():
    try:
        # Open connection to SQL Server
        connection = pyodbc.connect('DRIVER={SQL Server};'
                                    'server=DESKTOP-8B4115O;'
                                    'database=master;'
                                    'Trusted_Connection=yes')
        connection.autocommit = True

        # Get the database name from the entry and format the query correctly
        database_name = entry_database.get().strip()

        # Ensure that the database name is not empty
        if database_name:
            connection.execute(f'CREATE DATABASE [{database_name}]')
            info_label.configure(text="Database Created")
        else:
            info_label.configure(text="Database Name cannot be empty")

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="Database Creation failed")


create_button = customtkinter.CTkButton(app, text="Create",
                                        command=create_db, fg_color="green")
create_button.place(relx=0.1, rely=0.2)


def connect_db():
    try:
        # Open connection to the database with user-provided name
        connection = pyodbc.connect('DRIVER={SQL Server};'
                                    'server=DESKTOP-8B4115O;'
                                    f'database={entry_database.get().strip()};'
                                    'Trusted_Connection=yes')

        info_label.configure(text="Connection successful")
    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="Connection failed")


connect_button = customtkinter.CTkButton(app, text="Connect",
                                         command=connect_db, fg_color="blue")
connect_button.place(relx=0.1, rely=0.3)

info_label = customtkinter.CTkLabel(app, text="")
info_label.place(relx=0.1, rely=0.4)

app.mainloop()
