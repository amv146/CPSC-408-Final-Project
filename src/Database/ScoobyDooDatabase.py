import mysql
from mysql import connector
from mysql.connector.cursor import MySQLCursor as Cursor
from os import system
from pandas import DataFrame
import pandas as pd
from src.Database.Database import Database
from src.Utils import *
from src.GUI.Filters import Table
from src.Entities import *


class ScoobyDooDatabase (Database):
  def __init__(self):
      super().__init__('ScoobyDoo')

  def run_all_procedure(self, episode: Episode = Episode(), setting: Setting = Setting(), actor: VoiceActor = VoiceActor(), monster: Monster = Monster(), culprit: Culprit = Culprit()):
    self.refresh_cursor()
    
    sql = '''CALL Query_All({0}, {1}, {2}, {3}, {4}, {5}, {6}, 
                            {7}, {8}, 
                            {9}, {10}, 
                            {11}, {12}, {13}, {14}, {15}, 
                            {16}, {17})'''
                            
    sql = sql.format(null(episode.series_name), null(episode.season), null(episode.title), null(episode.date_aired), null(episode.runtime), null(episode.monster_real), null(episode.motive), 
                     null(setting.setting_terrain), null(setting.setting_place), 
                     null(actor.actor_name), null(actor.character_name), 
                     null(monster.monster_name), null(monster.monster_gender), null(monster.monster_type), null(monster.monster_species), null(monster.monster_subtype), 
                     null(culprit.culprit_name), null(culprit.culprit_gender))
    print(sql)
    result = pd.read_sql(sql, self.database)
    return result

  #
  # BEGIN QUERIES
  #
  
  def query_episodes(self, episode: Episode):
    self.refresh_cursor()
    sql = f'''CALL Query_Episodes({null(episode.series_name)}, {null(episode.season)}, {null(episode.title)}, {null(episode.date_aired)}, {null(episode.runtime)}, {null(episode.monster_real)}, {null(episode.motive)})'''
    result = pd.read_sql(sql, self.database)
    return self.__get_id__(result)
  
  def query_settings(self, setting: Setting):
    self.refresh_cursor()
    sql = f'''CALL Query_Settings({null(setting.setting_terrain)}, {null(setting.setting_place)})'''
      
    result = pd.read_sql(sql, self.database)
    return self.__get_id__(result)
  
  def query_actors(self, actor: VoiceActor):
    self.refresh_cursor()
    sql = f'''CALL Query_Actors({null(actor.actor_name)}, {null(actor.character_name)})'''
        
    result = pd.read_sql(sql, self.database)
    return self.__get_id__(result)

  def query_monsters(self, monster: Monster):
    self.refresh_cursor()
    sql = f'''CALL Query_Monsters({null(monster.monster_name)}, {null(monster.monster_gender)}, {null(monster.monster_type)}, {null(monster.monster_species)}, {null(monster.monster_subtype)})'''
          
    result = pd.read_sql(sql, self.database)
    return self.__get_id__(result)

  def query_culprits(self, culprit: Culprit):
    self.refresh_cursor()
    sql = f'''CALL Query_Culprits({null(culprit.culprit_name)}, {null(culprit.culprit_gender)})'''
          
    result = pd.read_sql(sql, self.database)

    return self.__get_id__(result)
  
  #
  # END QUERIES
  #
  
  
  
  #
  # BEGIN CREATES
  #
  
  def create_episode(self, episode: Episode, setting: Setting, actors: list[VoiceActor], monsters: list[Monster], culprits: list[Culprit]):
    episode_id = self.create_episode_details(episode)
    setting_id = self.create_setting(setting)
    actor_ids = [self.create_actor(actor) for actor in actors]
    monster_ids = [self.create_monster(monster) for monster in monsters]
    culprit_ids = [self.create_culprit(culprit) for culprit in culprits]
    
    self.add_episode_setting(episode_id, setting_id)
    [self.add_episode_actor(episode_id, actor_id) for actor_id in actor_ids]
    [self.add_episode_monster(episode_id, monster_id) for monster_id in monster_ids]
    [self.add_episode_culprit(episode_id, culprit_id) for culprit_id in culprit_ids]
    
    
    pass
    
  
  def create_episode_details(self, episode: Episode) -> int:
    result = self.query_episodes(episode)
    
    
    if result == -1:
      sql = f'''INSERT INTO episode_details(series_name, season, title, date_aired, run_time, monster_real, motive) 
                VALUES ('{episode.series_name}', {episode.season}, '{episode.title}', '{episode.date_aired}', {episode.runtime}, '{episode.monster_real}', '{episode.motive}')'''

      self.commit(sql)

      result = self.query_episodes(episode)

    return result
  
  def create_setting(self, setting: Setting) -> int:
    result = self.query_settings(setting)

    if len(result) == 0:
      # sql = f'''CALL Create_Setting('{setting_terrain}', '{setting_place}')'''
      sql = f'''INSERT INTO settings(setting_terrain, setting_place) 
                VALUES ('{setting.setting_terrain}', '{setting.setting_place}')'''
                  
      self.commit(sql)
      
      result = self.query_settings(setting)

    return result
  
  def create_actor(self, actor: VoiceActor) -> int:
    result = self.query_actors(actor)

    if result == -1:
      sql = f'''INSERT INTO voice_actors(actor_name, character_name) 
                VALUES ('{actor.actor_name}', '{actor.character_name}')'''
      self.commit(sql)

      result = self.query_actors(actor)

    return result

  def create_monster(self, monster: Monster) -> int:
    result = self.query_monsters(monster)

    if result == -1:
      sql = f'''INSERT INTO monsters(monster_name, monster_gender, monster_type, monster_species, monster_subtype) 
                VALUES ('{monster.monster_name}', '{monster.monster_gender}', '{monster.monster_type}', '{monster.monster_species}', '{monster.monster_subtype}')'''
      self.commit(sql)

      result = self.query_monsters(monster)

    return result

  def create_culprit(self, culprit: Culprit) -> int:
    result = self.query_culprits(culprit)
    
    if result == -1:
      sql = f'''INSERT INTO culprits(culprit_name, culprit_gender) 
                VALUES ('{culprit.culprit_name}', '{culprit.culprit_gender}')'''
                
      self.commit(sql)
      
      result = self.query_culprits(culprit)

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

  def add_episode_culprit(self, episode_id: int = 0, culprit_id: int = 0):
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
      return df[str(df.columns[0])].iloc[0]
    except:
      return -1