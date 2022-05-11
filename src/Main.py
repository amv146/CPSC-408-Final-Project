
from os import wait
from time import sleep
from Filters import *
from GUI.gui import App
from Database.ScoobyDooDatabase import ScoobyDooDatabase
from mysql import connector
from subprocess import Popen, PIPE, STDOUT
import subprocess
from sqlite3 import Cursor
import tkinter as tk
from Utils import *
import warnings
from pandastable import Table
import tkinter as ttk
from tkinter import OptionMenu, StringVar, Frame

warnings.filterwarnings('ignore')
main_db: ScoobyDooDatabase = ScoobyDooDatabase()
main_db.run_sql_file('database_setup.sql')
main_db.run_sql_file('procedures.sql')


df = main_db.read_sql('SELECT * FROM Voice_Actors')
# print(list(df.columns))
# for row_index in range(0, len(df)):
#   print(list(df.iloc[row_index]))
df = main_db.run_all_procedure()
app = App()
# app.table(df)
# print(df)
filter_handler = FilterHandler(main_db)
# print(filter_handler.filters.__str__())

filter_handler.change_filter_value(FilterType.SEASON, '4')
filter_handler.change_filter_value(FilterType.CULPRIT_GENDER, 'Male')
filter_handler.change_filter_value(FilterType.CULPRIT_GENDER, '')



# app.tree.change_table(df)
app.mainloop()


# root = tk.Tk()
# root.title('PandasTable Example')

# frame = tk.Frame(root)
# frame.pack(fill='both', expand=True)

# pt = Table(frame, dataframe=df)
# pt.show()
# root.mainloop()