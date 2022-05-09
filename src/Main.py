
from ScoobyDooDatabase import ScoobyDooDatabase
from mysql import connector
from subprocess import Popen, PIPE, STDOUT
import subprocess
from sqlite3 import Cursor
import tkinter as tk
from pandastable import Table

main_db: ScoobyDooDatabase = ScoobyDooDatabase()
main_db.run_sql_file()


df = main_db.read_sql('SELECT * FROM Voice_Actors')

root = tk.Tk()
root.title('PandasTable Example')

frame = tk.Frame(root)
frame.pack(fill='both', expand=True)

pt = Table(frame, dataframe=df)
pt.show()
root.mainloop()