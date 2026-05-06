import customtkinter
import pyodbc
import tkinter

from database import create_button, info_label
from main import entry_table

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry("500x500")
app.title('CREATE TABLE')

entry_table_name = customtkinter.CTkEntry(app, placeholder_text='TABLE NAME', width=190)
entry_table_name.place(relx=0.1, rely=0.1)

entry_column1 = customtkinter.CTkEntry(app, placeholder_text='Column 1', width=190)
entry_column1.place(relx=0.1, rely=0.2)

entry_column2 = customtkinter.CTkEntry(app, placeholder_text='Column 2', width=190)
entry_column2.place(relx=0.1, rely=0.3)


def create():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'server=DESKTOP-8B4115O;' +
                                    'database=company;' +
                                    'Trusted_Connection=yes')
        connection.autocommit = True
        sql_stmt = (f"CREATE TABLE {entry_table_name.get()} ("
                    f"{entry_column1.get()} {radio_var_col1.get()}, "
                    f"{entry_column2.get()} {radio_var_col2.get()})")

        connection.execute(sql_stmt)
        info_label.configure(text="Table created")
    except pyodbc.Error as ex:
        print("connection failed", ex)
        info_label.configure(text="connection failed")


create_button = customtkinter.CTkButton(app, text="Create", command=create)
create_button.place(relx=0.1, rely=0.4)

radio_var_col1 = tkinter.StringVar(value="")
col1_rd_varchar50 = customtkinter.CTkRadioButton(app,
                                                 text="varchar(50)",
                                                 variable=radio_var_col1,
                                                 value="varchar(50)")
col1_rd_varchar50.place(relx=0.5, rely=0.2)
col1_rd_int = customtkinter.CTkRadioButton(app,
                                           text="integer",
                                           variable=radio_var_col1,
                                           value="integer")
col1_rd_int.place(relx=0.7, rely=0.2)

radio_var_col2 = tkinter.StringVar(value="")
col2_rd_varchar50 = customtkinter.CTkRadioButton(app,
                                                 text="varchar(50)",
                                                 variable=radio_var_col2,
                                                 value="varchar(50)")
col2_rd_varchar50.place(relx=0.5, rely=0.3)
col2_rd_int = customtkinter.CTkRadioButton(app,
                                           text="integer",
                                           variable=radio_var_col2,
                                           value="integer")
col2_rd_int.place(relx=0.7, rely=0.3)

info_label = customtkinter.CTkLabel(app, text="company")
info_label.place(relx=0.1, rely=0.6)
app.mainloop()
