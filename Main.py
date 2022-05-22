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
  app.change_entry_text(app.monster_type_entry, '')
  app.change_entry_text(app.monster_subtype_entry, '')
  app.change_entry_text(app.monster_species_entry, '')
  app.change_entry_text(app.monster_type_entry, '')
  
  app.change_entry_text(app.culprit_name_entry, '')
  app.change_entry_text(app.culprit_gender_entry, '')
  
  app.change_entry_text(app.actor_name_entry, '')
  app.change_entry_text(app.character_name_entry, '')
  episode_name = (item['values'][0])

  episode_sql = f'SELECT * FROM episode_details WHERE title = \'{episode_name}\''
  episode_details = main_db.read_sql(episode_sql)
  episode_id = episode_details['episode_id'].iloc[0]
  
  setting_id = episode_details['setting_id'].iloc[0]
  setting_sql = f'SELECT * FROM settings WHERE setting_id = {setting_id}'
  setting_details = main_db.read_sql(setting_sql)
  
  episode_monster_sql = f'SELECT monster_id FROM episode_monsters WHERE episode_id = {episode_id}'
  monster_ids = list(main_db.read_sql(episode_monster_sql)['monster_id'])
  monsters: DataFrame = pd.DataFrame()
  for monster_id in monster_ids:
    monster_sql = f'SELECT * FROM monsters WHERE monster_id = {monster_id}'
    monster = main_db.read_sql(monster_sql)
    monsters = pd.concat([monsters, monster])
    # monsters.append(Monster(monster_name= monster['monster_name'].iloc[0], monster_gender = monster['monster_gender'].iloc[0], monster_type = monster['monster_type'].iloc[0], monster_species= monster['monster_species'].iloc[0], monster_subtype= monster['monster_subtype'].iloc[0]))
  
  episode_actor_sql = f'SELECT actor_id FROM episode_actors WHERE episode_id = {episode_id}'
  actor_ids = list(main_db.read_sql(episode_actor_sql)['actor_id'])
  actors: DataFrame = pd.DataFrame()
  for actor_id in actor_ids:
    actor_sql = f'SELECT * FROM voice_actors WHERE actor_id = {actor_id}'
    actor = main_db.read_sql(actor_sql)
    actors = pd.concat([actors, actor])
  app.va_tree.change_table(actors)
  
  episode_culprit_sql = f'SELECT culprit_id FROM episode_culprits WHERE episode_id = {episode_id}'
  culprit_ids = list(main_db.read_sql(episode_culprit_sql)['culprit_id'])
  culprits: DataFrame = pd.DataFrame()
  for culprit_id in culprit_ids:
    culprit_sql = f'SELECT * FROM culprits WHERE culprit_id = {culprit_id}'
    culprit = main_db.read_sql(culprit_sql)
    culprits = pd.concat([culprits, culprit])
  app.culprits_tree.change_table(culprits)
  
    
    
  
  
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
  
def add_record(e):
  episode = Episode(series_name= app.series_entry.get(), season= int(app.season_entry.get()), title = app.title_entry.get(), date_aired= app.aired_entry.get(), runtime= int(app.run_entry.get()), monster_real= app.monster_real_entry.get(), motive = app.motive_entry.get())
  
  setting = Setting(setting_place= app.setting_place_entry.get(), setting_terrain= app.setting_terrain_entry.get())
  
  actor = VoiceActor(character_name= app.character_name_entry.get(), actor_name= app.actor_name_entry.get())
  monster = Monster(monster_name = app.monster_entry.get(), monster_gender = app.monster_gender_entry.get(), monster_type = app.monster_type_entry.get(), monster_species= app.monster_species_entry.get(), monster_subtype= app.monster_subtype_entry.get())
  culprit = Culprit(culprit_name= app.culprit_name_entry.get(), culprit_gender= app.culprit_gender_entry.get())
  
  main_db.create_episode(episode, setting, [actor], [monster], [culprit])
  
  reset()
  
def update_record(e):
  episode = Episode(series_name= app.series_entry.get(), season= int(app.season_entry.get()), title = app.title_entry.get(), date_aired= app.aired_entry.get(), runtime= int(app.run_entry.get()), monster_real= app.monster_real_entry.get(), motive = app.motive_entry.get())
    
  setting = Setting(setting_place= app.setting_place_entry.get(), setting_terrain= app.setting_terrain_entry.get())
    
  actor = VoiceActor(character_name= app.character_name_entry.get(), actor_name= app.actor_name_entry.get())
  monster = Monster(monster_name = app.monster_entry.get(), monster_gender = app.monster_gender_entry.get(), monster_type = app.monster_type_entry.get(), monster_species= app.monster_species_entry.get(), monster_subtype= app.monster_subtype_entry.get())
  culprit = Culprit(culprit_name= app.culprit_name_entry.get(), culprit_gender= app.culprit_gender_entry.get())
    
  main_db.update_episode(episode, setting, actor, monster, culprit)
  

def delete_record(e):
  item = app.tree.item(app.tree.focus())
  episode_name = (item['values'][0])
  episode_sql = f'SELECT * FROM episode_details WHERE title = \'{episode_name}\''
  episode_details = main_db.read_sql(episode_sql)
  episode_id = episode_details['episode_id'].iloc[0]
  
  main_db.delete_episode(episode_id)
  
  reset()
  
  
  
  # app.seriesName = df['series_name']

def clear(e):
  app.change_entry_text(app.series_entry, '')
  app.change_entry_text(app.season_entry, '')
  app.change_entry_text(app.run_entry, '')
  app.change_entry_text(app.motive_entry, '')
  app.change_entry_text(app.monster_real_entry, '')
  app.change_entry_text(app.aired_entry, '')
  app.change_entry_text(app.title_entry, '')
    
  app.change_entry_text(app.setting_place_entry, '')
  app.change_entry_text(app.setting_terrain_entry, '')
  
  app.change_entry_text(app.monster_type_entry, '')
  app.change_entry_text(app.monster_subtype_entry, '')
  app.change_entry_text(app.monster_species_entry, '')
  app.change_entry_text(app.monster_type_entry, '')
  
  app.change_entry_text(app.culprit_name_entry, '')
  app.change_entry_text(app.culprit_gender_entry, '')
  
  app.change_entry_text(app.actor_name_entry, '')
  app.change_entry_text(app.character_name_entry, '')

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
app.add_record_button.bind("<ButtonRelease-1>", add_record)
app.clear_button.bind("<ButtonRelease-1>", clear)
        
# Bindings
        


for menu in app.menus:
  menu.add_options()
  menu.options.trace_add('write', lambda *args, men = menu: __on_select__(men))

app.mainloop()