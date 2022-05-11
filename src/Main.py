
from os import wait
from time import sleep
from Filters import *
from GUI.Tree import Tree
from GUI.gui import App
from Database.ScoobyDooDatabase import ScoobyDooDatabase
from mysql import connector
from subprocess import Popen, PIPE, STDOUT
import subprocess
from sqlite3 import Cursor
import tkinter as tk
from Utils import *
from GUI.Menu import Menu
import warnings
import tkinter as ttk
from tkinter import OptionMenu, StringVar, Frame
from FilterHandler import FilterHandler

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

actor_menu = Menu(app, FilterType.ACTOR_NAME)
season_menu = Menu(app, FilterType.SEASON)
menus = [actor_menu, season_menu]
actor_menu.grid(column=1, row=1, sticky=tk.W, padx=1, pady=1)
season_menu.grid(column=2, row=1, sticky=tk.W, padx=1, pady=1)
filter_handler = FilterHandler(main_db)
main_cols = ['title', 'series_name', 'season']

tree = Tree(app, df, main_cols)
tree.grid(column = 1, row = 3, sticky=tk.W)

print(main_db.read_sql('SELECT * FROM Episode_Details WHERE Season = 4'))
def __on_select__(menu: Menu):
  filter_handler.change_filter_value( menu.filter_type, menu.options.get())
  df = filter_handler.__get_options_df__()[main_cols]
  print(df)
  df = df.drop_duplicates()
  tree.change_table(df)
  
  print(menu.filter_type)
  for menu2 in menus:
    if (menu.options.get() == ' ' or menu.options.get() == '') or menu2 != menu:
      menu2.add_options()


for menu in menus:
  menu.add_options()
  menu.options.trace_add('write', lambda *args, men = menu: __on_select__(men))

# app.table(df)
# print(df)
# print(filter_handler.filters.__str__())

# filter_handler.change_filter_value(FilterType.SEASON, '4')
# filter_handler.change_filter_value(FilterType.CULPRIT_GENDER, 'Male')
# filter_handler.change_filter_value(FilterType.CULPRIT_GENDER, '')



# app.tree.change_table(df)
app.mainloop()


# root = tk.Tk()
# root.title('PandasTable Example')

# frame = tk.Frame(root)
# frame.pack(fill='both', expand=True)

# pt = Table(frame, dataframe=df)
# pt.show()
# root.mainloop()