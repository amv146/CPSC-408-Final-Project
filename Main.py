from datetime import datetime
import os
from src.Entities import *
from src.GUI.Filters import *
from src.GUI.Tree import Tree
from src.GUI.gui import App
from src.GUI.Menu import Menu
from src.GUI.FilterHandler import FilterHandler
from src.Database.ScoobyDooDatabase import ScoobyDooDatabase
from src.Utils import *
from zipfile import ZipFile

import warnings
warnings.filterwarnings('ignore')

main_db: ScoobyDooDatabase = ScoobyDooDatabase()

df = main_db.read_sql('SELECT * FROM Voice_Actors')
df = main_db.run_all_procedure()

app = App()

filter_handler = FilterHandler(main_db)
reset_val = False
main_cols = ['title', 'series_name', 'season', 'date_aired', 'run_time', 'setting_place', 'setting_terrain']



def on_select(e, app: App, main_db: ScoobyDooDatabase):
  item = app.tree.item(app.tree.focus())
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
    print(monsters, monster)
    # monsters.append(Monster(monster_name= monster['monster_name'].iloc[0], monster_gender = monster['monster_gender'].iloc[0], monster_type = monster['monster_type'].iloc[0], monster_species= monster['monster_species'].iloc[0], monster_subtype= monster['monster_subtype'].iloc[0]))
  app.monster_tree.change_table(monsters, drop_duplicates=False)
  
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
  app.culprits_tree.change_table(culprits, drop_duplicates=False)
  
    
    
  
  
  episode = Episode(series_name= episode_details['series_name'].iloc[0], season= episode_details['season'].iloc[0], title = episode_details['title'].iloc[0], date_aired=episode_details['date_aired'].iloc[0], runtime= episode_details['run_time'].iloc[0], monster_real= episode_details['monster_real'].iloc[0], motive = episode_details['motive'].iloc[0])
  setting = Setting(setting_place= setting_details['setting_place'].iloc[0], setting_terrain= setting_details['setting_terrain'].iloc[0])
  
  app.change_entry_text(app.series_entry, episode.series_name)
  app.change_entry_text(app.season_entry, str(episode.season))
  app.change_entry_text(app.run_entry, str(episode.runtime))
  app.change_entry_text(app.motive_entry, episode.motive)
  app.change_entry_text(app.monster_real_entry, episode.monster_real)
  app.change_entry_text(app.aired_entry, episode.date_aired)
  app.change_entry_text(app.title_entry, episode.title)
  
  app.change_entry_text(app.setting_place_entry, setting.setting_place)
  app.change_entry_text(app.setting_terrain_entry, setting.setting_terrain)
  
  num_monsters_sql = f'SELECT COUNT(*) AS num_monsters FROM episode_monsters WHERE episode_id = {episode_id}'
  num_monsters = main_db.read_sql(num_monsters_sql)['num_monsters'].iloc[0]
  print(num_monsters_sql, num_monsters)
  app.monster_num_label.config(text=num_monsters)
  
  num_culprits_sql = f'SELECT COUNT(*) AS num_culprits FROM episode_culprits WHERE episode_id = {episode_id}'
  num_culprits = main_db.read_sql(num_culprits_sql)['num_culprits'].iloc[0]
  app.culprits_num_label.config(text=num_culprits)
  
  num_actors_sql = f'SELECT COUNT(*) AS num_actors FROM episode_actors WHERE episode_id = {episode_id}'
  num_actors = main_db.read_sql(num_actors_sql)['num_actors'].iloc[0]
  app.va_num_label.config(text=num_actors)
  
def add_record(e, app: App, main_db: ScoobyDooDatabase):
  
  episode = Episode(series_name= app.series_entry.get(), season= int(app.season_entry.get()), title = app.title_entry.get(), date_aired= app.aired_entry.get(), runtime= int(app.run_entry.get()), monster_real= app.monster_real_entry.get(), motive = app.motive_entry.get())
  
  setting = Setting(setting_place= app.setting_place_entry.get(), setting_terrain= app.setting_terrain_entry.get())
  
  actor = VoiceActor(character_name= app.character_name_entry.get(), actor_name= app.actor_name_entry.get())
  monster = Monster(monster_name = app.monster_entry.get(), monster_gender = app.monster_gender_entry.get(), monster_type = app.monster_type_entry.get(), monster_species= app.monster_species_entry.get(), monster_subtype= app.monster_subtype_entry.get())
  culprit = Culprit(culprit_name= app.culprit_name_entry.get(), culprit_gender= app.culprit_gender_entry.get())
  
  main_db.create_episode(episode, setting, [actor], [monster], [culprit])
  
  reset(app)
  
def update_record(e, app: App, main_db: ScoobyDooDatabase):
  item = app.tree.item(app.tree.focus())
  episode_name = (item['values'][0])

  episode_sql = f'SELECT * FROM episode_details WHERE title = \'{episode_name}\''
  episode_details = main_db.read_sql(episode_sql)
  episode_id = episode_details['episode_id'].iloc[0]
  
  episode = Episode(episode_id = episode_id, series_name= app.series_entry.get(), season= int(app.season_entry.get()), title = app.title_entry.get(), date_aired= app.aired_entry.get(), runtime= int(app.run_entry.get()), monster_real= app.monster_real_entry.get(), motive = app.motive_entry.get())
    
  setting = Setting(setting_place= app.setting_place_entry.get(), setting_terrain= app.setting_terrain_entry.get())
    
  actor = VoiceActor(character_name= app.character_name_entry.get(), actor_name= app.actor_name_entry.get())
  monster = Monster(monster_name = app.monster_entry.get(), monster_gender = app.monster_gender_entry.get(), monster_type = app.monster_type_entry.get(), monster_species= app.monster_species_entry.get(), monster_subtype= app.monster_subtype_entry.get())
  culprit = Culprit(culprit_name= app.culprit_name_entry.get(), culprit_gender= app.culprit_gender_entry.get())
    
  main_db.update_episode(episode, setting, actor, monster, culprit)
  
  reset(app)
  

def delete_record(e, app: App, main_db: ScoobyDooDatabase):
  item = app.tree.item(app.tree.focus())
  episode_name = (item['values'][0])
  episode_sql = f'SELECT * FROM episode_details WHERE title = \'{episode_name}\''
  episode_details = main_db.read_sql(episode_sql)
  episode_id = episode_details['episode_id'].iloc[0]
  
  main_db.delete_episode(episode_id)
  clear(e, app)
  reset(app)
  
  
  
  # app.seriesName = df['series_name']

def clear(e, app: App):
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
  
  app.va_tree.reset()
  app.culprits_tree.reset()
  app.monster_tree.reset()

  app.va_num_label.config(text=0)
  app.monster_num_label.config(text=0)
  app.culprits_num_label.config(text=0)
  
def reset(app: App):
  filter_handler.reset_filter_values()
  df = filter_handler.__get_options_df__()
  df = df[main_cols].drop_duplicates()
  app.tree.change_table(df)
  for menu in app.menus:
    menu.reset_val = True
    menu.options.set(' ')
    menu.add_options()

def export(e, app: App, main_db: ScoobyDooDatabase):
  episode_details_sql = 'SELECT episode_id, series_name, season, title, date_aired, run_time, monster_real, motive FROM episode_details WHERE is_deleted = 0'
  episode_details_df = main_db.read_sql(episode_details_sql)
  
  settings_sql = 'SELECT setting_id, setting_terrain, setting_place FROM settings WHERE is_deleted = 0'
  settings_df = main_db.read_sql(settings_sql)
  
  monsters_sql = 'SELECT monster_id, monster_name, monster_gender, monster_type, monster_subtype, monster_species FROM monsters WHERE is_deleted = 0'
  monsters_df = main_db.read_sql(monsters_sql)
  
  culprits_sql = 'SELECT culprit_id, culprit_name, culprit_gender FROM culprits WHERE is_deleted = 0'
  culprits_df = main_db.read_sql(culprits_sql)
  
  actors_sql = 'SELECT actor_id, character_name, actor_name FROM voice_actors WHERE is_deleted = 0'
  actors_df = main_db.read_sql(actors_sql)
  
  episode_actors_sql = 'SELECT episode_id, actor_id FROM episode_actors WHERE is_deleted_episode_actors = 0'
  episode_actors_df = main_db.read_sql(episode_actors_sql)
  
  episode_culprits_sql = 'SELECT episode_id, culprit_id FROM episode_culprits WHERE is_deleted_episode_culprits = 0'
  episode_culprits_df = main_db.read_sql(episode_culprits_sql)
  
  episode_monsters_sql = 'SELECT episode_id, monster_id FROM episode_monsters WHERE is_deleted_episode_monsters = 0'
  episode_monsters_df = main_db.read_sql(episode_monsters_sql)
  
  os.makedirs('Exports/Temp', exist_ok=True)
  
  episode_details_df.to_csv('Exports/Temp/Episode Details.csv')
  settings_df.to_csv('Exports/Temp/Settings.csv')
  monsters_df.to_csv('Exports/Temp/Monsters.csv')
  culprits_df.to_csv('Exports/Temp/Culprits.csv')
  actors_df.to_csv('Exports/Temp/Voice Actors.csv')
  episode_actors_df.to_csv('Exports/Temp/Episode Actors.csv')
  episode_culprits_df.to_csv('Exports/Temp/Episode Culprits.csv')
  episode_monsters_df.to_csv('Exports/Temp/Episode Monsters.csv')
  
  curr_date_time = datetime.now().strftime('%m-%d %H:%M:%S')
  zipObj = ZipFile(f'Exports/Tables Export {curr_date_time}.zip', 'w')
  
  zipObj.write('Exports/Temp/Episode Details.csv', arcname='Episode Details.csv')
  zipObj.write('Exports/Temp/Settings.csv', arcname= 'Settings.csv')
  zipObj.write('Exports/Temp/Monsters.csv', arcname= 'Monsters.csv')
  zipObj.write('Exports/Temp/Culprits.csv', arcname='Culprits.csv')
  zipObj.write('Exports/Temp/Voice Actors.csv', arcname='Voice Actors.csv')
  zipObj.write('Exports/Temp/Episode Actors.csv', arcname='Episode Actors.csv')
  zipObj.write('Exports/Temp/Episode Culprits.csv', arcname= 'Episode Culprits.csv')
  zipObj.write('Exports/Temp/Episode Monsters.csv', arcname= 'Episode Monsters.csv')
  
  zipObj.close()
  
  os.system('rm -rf Exports/Temp')
  
  
  
  
  pass

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
app.reset_button.bind("<ButtonRelease-1>", lambda e, app = app, main_db = main_db: delete_record(e, app, main_db))

        
        
app.tree.bind("<ButtonRelease-1>", lambda e, app = app, db = main_db: on_select(e, app, db)) 
app.delete_record_button.bind("<ButtonRelease-1>", lambda e, app = app, main_db = main_db: delete_record(e, app, main_db))
app.add_record_button.bind("<ButtonRelease-1>", lambda e, app = app, db = main_db: add_record(e, app, db))
app.clear_button.bind("<ButtonRelease-1>", lambda e, app = app: clear(e, app))
app.update_record_button.bind("<ButtonRelease-1>", lambda e, app = app, db = main_db: update_record(e, app, db))
app.export_button.bind("<ButtonRelease-1>", lambda e, app = app, db = main_db: export(e, app, db))
# Bindings
        


for menu in app.menus:
  menu.add_options()
  menu.options.trace_add('write', lambda *args, men = menu: __on_select__(men))

app.mainloop()