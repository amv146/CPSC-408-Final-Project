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

  #
  # BEGIN QUERIES
  #
  
  def query_episodes(self, series_name: str = '', season: int = 0, title: str = '', date_aired: str = '', runtime: int = 0, monster_real: str = '', motive: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Episodes({null(series_name)}, {null(season)}, {null(title)}, {null(date_aired)}, {null(runtime)}, {null(monster_real)}, {null(motive)})'''
    result = pd.read_sql(sql, self.database)
    return self.__get_id__(result)
  
  def query_settings(self, setting_terrain: str = '', setting_place: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Settings({null(setting_terrain)}, {null(setting_place)})'''
      
    result = pd.read_sql(sql, self.database)
    return self.__get_id__(result)
  
  def query_actors(self, actor_name: str = '', character_name: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Actors({null(actor_name)}, {null(character_name)})'''
        
    result = pd.read_sql(sql, self.database)
    return self.__get_id__(result)

  def query_monsters(self, monster_name: str = '', monster_gender: str = '', monster_type: str = '', monster_species: str = '', monster_subtype: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Monsters({null(monster_name)}, {null(monster_gender)}, {null(monster_type)}, {null(monster_species)}, {null(monster_subtype)})'''
          
    result = pd.read_sql(sql, self.database)
    return self.__get_id__(result)

  def query_culprits(self, culprit_name: str = '', culprit_gender: str = ''):
    self.refresh_cursor()
    sql = f'''CALL Query_Culprits({null(culprit_name)}, {null(culprit_gender)})'''
          
    result = pd.read_sql(sql, self.database)

    return self.__get_id__(result)
  
  #
  # END QUERIES
  #
  
  
  
  #
  # BEGIN CREATES
  #

  def create_setting(self, setting_terrain: str = '', setting_place: str = ''):
    result = self.query_settings(setting_terrain, setting_place)

    if len(result) == 0:
      # sql = f'''CALL Create_Setting('{setting_terrain}', '{setting_place}')'''
      sql = f'''INSERT INTO settings(setting_terrain, setting_place) 
                VALUES ('{setting_terrain}', '{setting_place}')'''
                
      self.commit(sql)
    
      result = self.query_settings(setting_terrain, setting_place)

    return result
  
  def create_episode(self, series_name: str = '', season: int = 0, title: str = '', date_aired: str = '', runtime: int = 0, monster_real: str = '', motive: str = ''):
    result = self.query_episodes(series_name, season, title, date_aired, runtime, monster_real, motive)
    
    if result == -1:
      sql = f'''INSERT INTO episode_details(series_name, season, title, date_aired, run_time, monster_real, motive) 
                VALUES ('{series_name}', {season}, '{title}', '{date_aired}', {runtime}, '{monster_real}', '{motive}')'''

      self.commit(sql)

      result = self.query_episodes(series_name, season, title, date_aired, runtime, monster_real, motive)

    return result
  
  def create_actor(self, actor_name: str = '', character_name: str = ''):
    result = self.query_actors(actor_name, character_name)

    if result == -1:
      sql = f'''INSERT INTO voice_actors(actor_name, character_name) 
                VALUES ('{actor_name}', '{character_name}')'''
      self.commit(sql)

      result = self.query_actors(actor_name, character_name)

    return result

  def create_monster(self, monster_name: str = '', monster_gender: str = '', monster_type: str = '', monster_species: str = '', monster_subtype: str = ''):
    result = self.query_monsters(monster_name, monster_gender, monster_type, monster_species, monster_subtype)

    if result == -1:
      sql = f'''INSERT INTO monsters(monster_name, monster_gender, monster_type, monster_species, monster_subtype) 
                VALUES ('{monster_name}', '{monster_gender}', '{monster_type}', '{monster_species}', '{monster_subtype}')'''
      self.commit(sql)

      result = self.query_monsters(monster_name, monster_gender, monster_type, monster_species, monster_subtype)

    return result

  def create_culprit(self, culprit_name: str = '', culprit_gender: str = ''):
    result = self.query_culprits(culprit_name, culprit_gender)
    
    if result == -1:
      sql = f'''INSERT INTO culprits(culprit_name, culprit_gender) 
                VALUES ('{culprit_name}', '{culprit_gender}')'''
                
      self.commit(sql)
      
      result = self.query_culprits(culprit_name, culprit_gender)

    return result
  
  #
  # END CREATES
  #


  #
  # BEGIN ADDS
  #
  
  def add_episode_setting(self, episode_id: int = 0, setting_id: int = 0):
    self.refresh_cursor()
    
    sql = f'''UPDATE episode_details
              SET setting_id = {setting_id}
              WHERE episode_id = {episode_id};
    '''
    
    self.commit(sql)

  def add_episode_actor(self, episode_id: int = 0, actor_id: int = 0):
    self.refresh_cursor()
    
    sql = f'''UPDATE episode_actors
              SET setting_id = {actor_id}
              WHERE episode_id = {episode_id};
    '''
    
    self.commit(sql)

  def add_episode_monster(self, episode_id: int = 0, monster_id: int = 0):
    self.refresh_cursor()
    
    sql = f'''INSERT INTO episode_monsters (episode_id, monster_id)
              VALUES ({episode_id}, {monster_id});'''
    
    self.commit(sql)

  def add_episode_culprit(self, episode_id: int = 0, culprit_id:int = 0):
    self.refresh_cursor()
    
    sql = f'''INSERT INTO episode_culprits (episode_id, culprit_id)
              VALUES ({episode_id}, {culprit_id});
    '''
    
    self.commit(sql)
    
  #
  # END ADDS
  #
    
  def __get_params__(self, locals: dict):
    return {key: null(value) for key, value in locals.items()}
  
  def __get_id__(self, df: DataFrame):
    try:
      return df[df.columns[0]].iloc[0]
    except:
      return -1