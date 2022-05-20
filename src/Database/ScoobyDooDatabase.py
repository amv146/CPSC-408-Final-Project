import mysql
from mysql import connector
from mysql.connector.cursor import MySQLCursor as Cursor
from os import system
from pandas import DataFrame
import pandas as pd
from Database.Database import Database
from Utils import *
from GUI.Filters import Table


class ScoobyDooDatabase (Database):
  def __init__(self):
      super().__init__('ScoobyDoo')
  
  def run_sql_file(self, file: str): 
    command = """mysql -u %s -p"%s" --host %s %s < %s""" %('adminroot', 'Chapman408!', 'chapman-univ.mysql.database.azure.com', 'scooby_doo', get_project_root().__str__() + '/data/' + file)
    system(command)
  

    
  def read_sql(self, sql: str) -> DataFrame:
    self.refresh_cursor()
    return pd.read_sql(sql, self.database)

  def run_all_procedure(self, series_name: str = '', season: int = 0, title: str = '', date_aired: str = '', runtime: int = 0, monster_real: str = '', motive: str = '', 
                        setting_terrain: str = '', setting_place: str = '', 
                        actor_name: str = '', character_name: str = '', 
                        monster_name: str = '', monster_gender: str = '', monster_type: str = '', monster_species: str = '', monster_subtype: str = '', 
                        culprit_name: str = '', culprit_gender: str = ''): 
    self.refresh_cursor()
    sql = '''CALL Query_All({0}, {1}, {2}, {3}, {4}, {5}, {6}, 
                            {7}, {8}, 
                            {9}, {10}, 
                            {11}, {12}, {13}, {14}, {15}, 
                            {16}, {17})'''
    sql = sql.format(null(series_name), null(season), null(title), null(date_aired), null(runtime), null(monster_real), null(motive), 
                     null(setting_terrain), null(setting_place), 
                     null(actor_name), null(character_name), 
                     null(monster_name), null(monster_gender), null(monster_type), null(monster_species), null(monster_subtype), 
                     null(culprit_name), null(culprit_gender))
    result = pd.read_sql(sql, self.database)
    return result

  def query_settings(self, setting_terrain: str = '', setting_place: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Settings('{setting_terrain}', '{setting_place}')'''
    
    result = pd.read_sql(sql, self.database)
    return result
  
  def query_episodes(self, series_name: str = '', season: int = 0, title: str = '', date_aired: str = '', runtime: int = 0, monster_real: str = '', motive: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Episodes('{series_name}', {season}, '{title}', '{date_aired}', {runtime}, '{monster_real}', '{motive}')'''
      
    result = pd.read_sql(sql, self.database)
    return result
  
  def query_actors(self, actor_name: str = '', character_name: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Actors('{actor_name}', '{character_name}')'''
        
    result = pd.read_sql(sql, self.database)
    return result

  def query_monsters(self, monster_name: str = '', monster_gender: str = '', monster_type: str = '', monster_species: str = '', monster_subtype: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Monsters('{monster_name}', '{monster_gender}', '{monster_type}', '{monster_species}', '{monster_subtype}')'''
          
    result = pd.read_sql(sql, self.database)
    return result

  def query_culprits(self, culprit_name: str = '', culprit_gender: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Culprits('{culprit_name}', '{culprit_gender}')'''
          
    result = pd.read_sql(sql, self.database)
    return result

  def create_setting(self, setting_terrain: str = '', setting_place: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Settings('{setting_terrain}', '{setting_place}')'''
    
    result = pd.read_sql(sql, self.database)

    if len(result) == 0:
      sql = f'''CALL Create_Setting('{setting_terrain}', '{setting_place}')'''
      result = pd.read_sql(sql, self.database)

    return result
  
  def create_episode(self, series_name: str = '', season: int = 0, title: str = '', date_aired: str = '', runtime: int = 0, monster_real: str = '', motive: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Episodes('{series_name}', {season}, '{title}', '{date_aired}', {runtime}, '{monster_real}', '{motive}')'''
      
    result = pd.read_sql(sql, self.database)

    if len(result) == 0:
      sql = f'''CALL Create_Episode('{series_name}', {season}, '{title}', '{date_aired}', {runtime}, '{monster_real}', '{motive}')'''
      result = pd.read_sql(sql, self.database)

    return result
  
  def create_actor(self, actor_name: str = '', character_name: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Actors('{actor_name}', '{character_name}')'''
        
    result = pd.read_sql(sql, self.database)

    if len(result) == 0:
      sql = f'''CALL Create_Actor('{actor_name}', '{character_name}')'''
      result = pd.read_sql(sql, self.database)

    return result

  def create_monster(self, monster_name: str = '', monster_gender: str = '', monster_type: str = '', monster_species: str = '', monster_subtype: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Monsters('{monster_name}', '{monster_gender}', '{monster_type}', '{monster_species}', '{monster_subtype}')'''
          
    result = pd.read_sql(sql, self.database)

    if len(result) == 0:
      sql = f'''CALL Create_Monster('{monster_name}', '{monster_gender}', '{monster_type}', '{monster_species}', '{monster_subtype}')'''
      result = pd.read_sql(sql, self.database)

    return result

  def create_culprit(self, culprit_name: str = '', culprit_gender: str = ''):
    result = self.query_culprits(culprit_name, culprit_gender)

    print(len(result))
    if len(result) == 0:
      print("made it")
      self.refresh_cursor()
      sql = f'''CALL Create_Culprit('{culprit_name}', '{culprit_gender}')'''
      self.database.commit()
      print(sql)
      # result = pd.read_sql(sql, self.database)
      result = self.query_culprits(culprit_name, culprit_gender)

    return result

  def add_episode_setting(self, episode_id: str = '', setting_id: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Add_Setting({episode_id}, {setting_id})'''

  def add_episode_actor(self, episode_id: str = '', actor_id: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Add_Actor({episode_id}, {actor_id})'''

  def add_episode_monster(self, episode_id: str = '', monster_id: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Add_Monster({episode_id}, {monster_id})'''

  def add_episode_culprit(self, episode_id: str = '', culprit_id: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Add_Culprit({episode_id}, {culprit_id})'''