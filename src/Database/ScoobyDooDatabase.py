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
      try:
        sql = f'''INSERT INTO episode_details(series_name, season, title, date_aired, run_time, monster_real, motive) 
                  VALUES ('{episode.series_name}', {episode.season}, '{episode.title}', '{episode.date_aired}', {episode.runtime}, '{episode.monster_real}', '{episode.motive}')'''

        self.commit(sql)

        result = self.query_episodes(episode)
      
      except connector.Error as error:
        print("failed create: {}".format(error))
        self.rollback()

    return result
  
  def create_setting(self, setting: Setting) -> int:
    result = self.query_settings(setting)

    if result == -1:
      try:
        sql = f'''INSERT INTO settings(setting_terrain, setting_place) 
                  VALUES ('{setting.setting_terrain}', '{setting.setting_place}')'''
                    
        self.commit(sql)
        
        result = self.query_settings(setting)
      
      except connector.Error as error:
        print("failed create: {}".format(error))
        self.rollback()

    return result
  
  def create_actor(self, actor: VoiceActor) -> int:
    result = self.query_actors(actor)

    if result == -1:
      try:
        sql = f'''INSERT INTO voice_actors(actor_name, character_name) 
                  VALUES ('{actor.actor_name}', '{actor.character_name}')'''
        self.commit(sql)

        result = self.query_actors(actor)

      except connector.Error as error:
        print("failed create: {}".format(error))
        self.rollback()

    return result

  def create_monster(self, monster: Monster) -> int:
    result = self.query_monsters(monster)

    if result == -1:
      try:
        sql = f'''INSERT INTO monsters(monster_name, monster_gender, monster_type, monster_species, monster_subtype) 
                  VALUES ('{monster.monster_name}', '{monster.monster_gender}', '{monster.monster_type}', '{monster.monster_species}', '{monster.monster_subtype}')'''
        self.commit(sql)

        result = self.query_monsters(monster)
      
      except connector.Error as error:
        print("failed create: {}".format(error))
        self.rollback()

    return result

  def create_culprit(self, culprit: Culprit) -> int:
    result = self.query_culprits(culprit)
    
    if result == -1:
      try:
        sql = f'''INSERT INTO culprits(culprit_name, culprit_gender) 
                  VALUES ('{culprit.culprit_name}', '{culprit.culprit_gender}')'''
                  
        self.commit(sql)
      
        result = self.query_culprits(culprit)
      
      except connector.Error as error:
        print("failed create: {}".format(error))
        self.rollback()


    return result
  
  #
  # END CREATES
  #


  #
  # BEGIN ADDS
  #
  
  def add_episode_setting(self, episode_id: int = 0, setting_id: int = 0):
    self.refresh_cursor()
    
    try:
      sql = f'''UPDATE episode_details
                SET setting_id = {setting_id}
                WHERE episode_id = {episode_id};
      '''
      
      self.commit(sql)

    except connector.Error as error:
        print("failed add: {}".format(error))
        self.rollback()

  def add_episode_actor(self, episode_id: int = 0, actor_id: int = 0):
    self.refresh_cursor()

    try:
      sql = f'''INSERT INTO episode_actors (episode_id, actor_id)
                VALUES ({episode_id}, {actor_id});
      '''
      
      self.commit(sql)

    except connector.Error as error:
        print("failed add: {}".format(error))
        self.rollback()

  def add_episode_monster(self, episode_id: int = 0, monster_id: int = 0):
    self.refresh_cursor()
    try:
      sql = f'''INSERT INTO episode_monsters (episode_id, monster_id)
                VALUES ({episode_id}, {monster_id});'''
      
      self.commit(sql)

    except connector.Error as error:
        print("failed add: {}".format(error))
        self.rollback()

  def add_episode_culprit(self, episode_id: int = 0, culprit_id: int = 0):
    self.refresh_cursor()
    
    try:
      sql = f'''INSERT INTO episode_culprits (episode_id, culprit_id)
                VALUES ({episode_id}, {culprit_id});
      '''
      
      self.commit(sql)

    except connector.Error as error:
        print("failed add: {}".format(error))
        self.rollback()
    
  #
  # END ADDS
  #

  #
  # BEGIN UPDATES
  #
  
  def update_episode(self, episode: Episode, setting: Setting, actor: VoiceActor, monster: Monster, culprit: Culprit):
    self.update_episode_details(episode, episode.episode_id)
    
    setting_id = self.create_setting(setting)
    self.update_episode_setting(episode.episode_id, setting_id)
    
    if not (monster.monster_gender == '' and monster.monster_name == '' and monster.monster_species == '' and monster.monster_type == '' and monster.monster_subtype == ''):
      monster_id = self.create_monster(monster)
      self.add_episode_monster(episode.episode_id, monster_id)
    
    if not (culprit.culprit_gender == '' and culprit.culprit_gender == ''):
      culprit_id = self.create_culprit(culprit)
      self.add_episode_culprit(episode.episode_id, culprit_id)
    
    if not (actor.actor_name == '' and actor.character_name == ''):
      actor_id = self.create_actor(actor)
      self.add_episode_actor(episode.episode_id, actor_id)
    

  def update_episode_details(self, episode: Episode, episode_id: int = 0):
    self.refresh_cursor()
    
    try:
      sql = f'''UPDATE episode_details
                SET series_name = '{episode.series_name}',
                    season = {episode.season},
                    title = '{episode.title}',
                    date_aired = '{episode.date_aired}',
                    run_time = {episode.runtime},
                    monster_real = '{episode.monster_real}',
                    motive = '{episode.motive}'
                WHERE episode_id = {episode_id};
      '''
      print(sql)
      
      self.commit(sql)

    except connector.Error as error:
        print("failed update: {}".format(error))
        self.rollback()
  
  def update_episode_setting(self, episode_id: int, setting_id: int):
    self.refresh_cursor()
    
    try:
      sql = f'''UPDATE episode_details
                SET setting_id = {setting_id}
                WHERE episode_id = {episode_id};
      '''
      
      self.commit(sql)

    except connector.Error as error:
        print("failed update: {}".format(error))
        self.rollback()

  def update_setting(self, setting: Setting, setting_id: int = 0):
    self.refresh_cursor()
    
    try:
      sql = f'''UPDATE settings
                SET setting_terrain = '{setting.setting_terrain}',
                    setting_place = '{setting.setting_place}'
                WHERE setting_id = {setting_id};
      '''
      
      self.commit(sql)
    
    except connector.Error as error:
        print("failed update: {}".format(error))
        self.rollback()

  def update_actor(self, actor: VoiceActor, actor_id: int = 0):
    self.refresh_cursor()
    
    try:
      sql = f'''UPDATE voice_actors
                SET actor_name = '{actor.actor_name}',
                    character_name = '{actor.character_name}'
                WHERE actor_id = {actor_id};
      '''
      
      self.commit(sql)

    except connector.Error as error:
        print("failed update: {}".format(error))
        self.rollback()

  def update_monster(self, monster: Monster, monster_id: int = 0):
    self.refresh_cursor()
    
    try:
      sql = f'''UPDATE monsters
                SET monster_name = '{monster.monster_name}',
                    monster_gender = '{monster.monster_gender}',
                    monster_type = '{monster.monster_type}',
                    monster_subtype = '{monster.monster_subtype}',
                    monster_species = '{monster.monster_species}'
                WHERE monster_id = {monster_id};
      '''

      self.commit(sql)

    except connector.Error as error:
        print("failed update: {}".format(error))
        self.rollback()

  def update_culprit(self, culprit: Culprit, culprit_id: int = 0):
    self.refresh_cursor()
    
    try:
      sql = f'''UPDATE culprits
                SET culprit_name = '{culprit.culprit_name}',
                    culprit_gender = '{culprit.culprit_gender}'
                WHERE culprit_id = {culprit_id};
      '''

      self.commit(sql)
    
    except connector.Error as error:
        print("failed update: {}".format(error))
        self.rollback()

  #
  # END UPDATES
  #

  #
  # BEGIN DELETES
  #

  def delete_episode(self, episode_id: int = 0):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE episode_details
                SET is_deleted = 1
                WHERE episode_id = {episode_id};
      '''

      self.commit(sql)
    
    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

    self.delete_episode_actor(episode_id)
    self.delete_episode_monster(episode_id)
    self.delete_episode_culprit(episode_id)

  def delete_setting(self, setting_id: int = 0):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE settings
                SET is_deleted = 1
                WHERE setting_id = {setting_id};
      '''
      self.commit(sql)

    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

    self.delete_setting_episode(setting_id)

  def delete_actor(self, actor_id: int = 0):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE voice_actors
                SET is_deleted = 1
                WHERE actor_id = {actor_id};
      '''

      self.commit(sql)

    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

    self.delete_actor_episode(actor_id)

  def delete_monster(self, monster_id: int = 0):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE monsters
                SET is_deleted = 1
                WHERE monster_id = {monster_id};
      '''

      self.commit(sql)
    
    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

    self.delete_monster_episode(monster_id)
  
  def delete_culprit(self, culprit_id: int = 0):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE culprits
                SET is_deleted = 1
                WHERE culprit_id = {culprit_id};
      '''

      self.commit(sql)

    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

    self.delete_culprit_episode(culprit_id)


  # 
  # BEGIN SINGLE DELETES
  # 

  def delete_single_episode_actor(self, episode_id: int, actor_id: int):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE episode_actors
                SET is_deleted_episode_actors = 1
                WHERE episode_id = {episode_id}
                  AND actor_id = {actor_id};
      '''

      self.commit(sql)

    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

  def delete_single_episode_monster(self, episode_id: int, monster_id: int):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE episode_monsters
                SET is_deleted_episode_monsters = 1
                WHERE episode_id = {episode_id}
                  AND monster_id = {monster_id};
      '''

      self.commit(sql)

    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()
  
  def delete_single_episode_culprit(self, episode_id: int, culprit_id: int):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE episode_culprits
                SET is_deleted = 1
                WHERE episode_id = {episode_id}
                  AND culprit_id = {culprit_id};
      '''

      self.commit(sql)

    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

  # 
  # END SINGLE DELETES
  # 

  # 
  # BEGIN DELETE LINKING TABLES
  # 

  def delete_setting_episode(self, setting_id: int = 0):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE episode_details
                SET setting_id = NULL
                WHERE setting_id = {setting_id};
      '''

      self.commit(sql)
    
    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

  def delete_episode_actor(self, episode_id: int = 0):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE episode_actors
                SET is_deleted_episode_actors = 1
                WHERE episode_id = {episode_id};
      '''

      self.commit(sql)
    
    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

  def delete_actor_episode(self, actor_id: int = 0):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE episode_actors
                SET is_deleted_episode_actors = 1
                WHERE actor_id = {actor_id};
      '''

      self.commit(sql)

    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

  def delete_episode_monster(self, episode_id: int = 0):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE episode_monsters
                SET is_deleted_episode_monsters = 1
                WHERE episode_id = {episode_id};
      '''

      self.commit(sql)
    
    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

  def delete_monster_episode(self, monster_id: int = 0):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE episode_monsters
                SET is_deleted_episode_monsters = 1
                WHERE monster_id = {monster_id};
      '''

      self.commit(sql)
    
    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

  def delete_episode_culprit(self, episode_id: int = 0):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE episode_culprits
                SET is_deleted_episode_culprits = 1
                WHERE episode_id = {episode_id};
      '''

      self.commit(sql)
    
    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

  def delete_culprit_episode(self, culprit_id: int = 0):
    self.refresh_cursor()

    try:
      sql = f'''UPDATE episode_culprits
                SET is_deleted_episode_culprits = 1
                WHERE culprit_id = {culprit_id};
      '''

      self.commit(sql)
    
    except connector.Error as error:
        print("failed delete: {}".format(error))
        self.rollback()

  # 
  # END DELETE LINKING TABLES
  # 

  #
  # END DELETES
  #

    
  def __get_params__(self, locals: dict):
    return {key: null(value) for key, value in locals.items()}
  
  def __get_id__(self, df: DataFrame):
    try:
      return df[str(df.columns[0])].iloc[0]
    except:
      return -1