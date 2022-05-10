
from os import wait
from time import sleep
from GUI.gui import App
from Database.ScoobyDooDatabase import ScoobyDooDatabase
from mysql import connector
from subprocess import Popen, PIPE, STDOUT
import subprocess
from sqlite3 import Cursor
import tkinter as tk
from Utils import *
from pandastable import Table

main_db: ScoobyDooDatabase = ScoobyDooDatabase()
main_db.run_sql_file()


df = main_db.read_sql('SELECT * FROM Voice_Actors')
# print(list(df.columns))
# for row_index in range(0, len(df)):
#   print(list(df.iloc[row_index]))
df = main_db.read_sql('SELECT * FROM Voice_Actors')
app = App()
app.table(df)
print(get_project_root())
app.tree.change_table(df)
app.mainloop()


# root = tk.Tk()
# root.title('PandasTable Example')

# frame = tk.Frame(root)
# frame.pack(fill='both', expand=True)

# pt = Table(frame, dataframe=df)
# pt.show()
# root.mainloop()