from src.Entities import *
from src.GUI.Filters import *
from src.GUI.Tree import Tree
from src.GUI.gui import App
from src.GUI.Menu import Menu
from src.GUI.FilterHandler import FilterHandler
from src.Database.ScoobyDooDatabase import ScoobyDooDatabase
from src.Utils import *


import warnings
warnings.filterwarnings('ignore')

main_db: ScoobyDooDatabase = ScoobyDooDatabase()

df = main_db.read_sql('SELECT * FROM Voice_Actors')
df = main_db.run_all_procedure()

app = App()

filter_handler = FilterHandler(main_db)
reset_val = False
main_cols = ['title', 'series_name', 'season', 'date_aired', 'run_time', 'setting_place', 'setting_terrain']


def clicker(e):
    on_select(app.tree.item(app.tree.focus()))

def on_select(item):
  episode_name = (item['values'][0])
  print(episode_name)
  episode_sql = f'SELECT * FROM episode_details WHERE title = \'{episode_name}\''
  episode_details = main_db.read_sql(episode_sql)
  setting_id = df['setting_id'].iloc[0]
  setting_sql = f'SELECT * FROM settings WHERE setting_id = {setting_id}'
  setting_details = main_db.read_sql(setting_sql)
  
  episode = Episode(series_name= episode_details['series_name'].iloc[0], season= episode_details['season'].iloc[0], title = episode_details['title'].iloc[0], date_aired=episode_details['date_aired'].iloc[0], runtime= episode_details['run_time'].iloc[0], monster_real= episode_details['monster_real'].iloc[0], motive = episode_details['motive'].iloc[0])
  setting = Setting(setting_place= setting_details['setting_terrain'].iloc[0], setting_terrain= setting_details['setting_place'].iloc[0])
  
  app.change_entry_text(app.series_entry, episode.series_name)
  app.change_entry_text(app.season_entry, str(episode.season))
  app.change_entry_text(app.run_entry, str(episode.runtime))
  app.change_entry_text(app.motive_entry, episode.motive)
  app.change_entry_text(app.monster_real_entry, episode.monster_real)
  app.change_entry_text(app.aired_entry, episode.date_aired)
  app.change_entry_text(app.title_entry, episode.title)
  
  app.change_entry_text(app.setting_place_entry, setting.setting_place)
  app.change_entry_text(app.setting_terrain_entry, setting.setting_terrain)

def delete_record(e):
  item = app.tree.item(app.tree.focus())
  episode_name = (item['values'][0])
  episode_sql = f'SELECT * FROM episode_details WHERE title = \'{episode_name}\''
  episode_details = main_db.read_sql(episode_sql)
  episode_id = episode_details['episode_id'].iloc[0]
  
  main_db.delete_episode(episode_id)
  
  
  
  # app.seriesName = df['series_name']


def reset():
  filter_handler.reset_filter_values()
  df = filter_handler.__get_options_df__()
  df = df[main_cols].drop_duplicates()
  app.tree.change_table(df)
  for menu in app.menus:
    menu.reset_val = True
    menu.options.set(' ')
    menu.add_options()

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
    

app.table(df, main_cols)
app.reset_button.configure(command = reset)

        
        
app.tree.bind("<ButtonRelease-1>", clicker) 
app.delete_record_button.bind("<ButtonRelease-1>", delete_record)
        
        
# Bindings
        


for menu in app.menus:
  menu.add_options()
  menu.options.trace_add('write', lambda *args, men = menu: __on_select__(men))

app.mainloop()