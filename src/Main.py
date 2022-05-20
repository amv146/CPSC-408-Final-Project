
from os import wait
from time import sleep
from GUI.Filters import *
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
from GUI.FilterHandler import FilterHandler

warnings.filterwarnings('ignore')
main_db: ScoobyDooDatabase = ScoobyDooDatabase()
# main_db.run_sql_file('database_setup.sql')
# main_db.run_sql_file('procedures.sql')

main_db.create_culprit('test culprit 9', 'male')
main_db.create_episode('test series 9', 9, 'test 9', 'test date 9', 9, 'FALSE', 'test motive 9')

print(main_db.query_episodes(series_name='test series 9', season=9, title='test 9'))

main_db.add_episode_culprit(1, main_db.query_culprits('test culprit 9', 'male')[0])
main_db.database.commit()
print(main_db.query_episodes(series_name='test series 9', season=9, title='test 9'))

df = main_db.read_sql('SELECT * FROM Voice_Actors')
# print(list(df.columns))
# for row_index in range(0, len(df)):
#   print(list(df.iloc[row_index]))
df = main_db.run_all_procedure()
app = App()

actor_menu = Menu(app, FilterType.ACTOR_NAME)
season_menu = Menu(app, FilterType.SEASON)
# actor_menu.grid(column=1, row=1, sticky=tk.W, padx=1, pady=1)
# season_menu.grid(column=2, row=1, sticky=tk.W, padx=1, pady=1)
filter_handler = FilterHandler(main_db)
reset_val = False

def reset():
  filter_handler.reset_filter_values()
  df = filter_handler.__get_options_df__()
  df = df[main_cols].drop_duplicates()
  app.tree.change_table(df)
  for menu in app.menus:
    menu.reset_val = True
    menu.options.set(' ')
    menu.add_options()
main_cols = ['title', 'series_name', 'season', 'date_aired', 'run_time', 'setting_place', 'setting_terrain']
app.table(df, main_cols)
app.reset_button.configure(command = reset)


def __on_select__(menu: Menu):
  if (menu.reset_val):
    menu.reset_val = False
    return
  filter_handler.change_filter_value( menu.filter_type, menu.options.get())
  df = filter_handler.__get_options_df__()
  df = df[main_cols].drop_duplicates()
  app.tree.change_table(df)

  for menu2 in app.menus:
    if (menu.options.get() == ' ' or menu.options.get() == '') or menu2 != menu:
      menu2.add_options()

for menu in app.menus:
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
