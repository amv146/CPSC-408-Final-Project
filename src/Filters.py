import mysql
from mysql import connector
from sqlite3 import Cursor
import pandas as pd
from pandas import DataFrame
from enum import Enum
from Database.ScoobyDooDatabase import ScoobyDooDatabase
from pandas.core.series import Series
from tkinter import OptionMenu

class FilterType(str, Enum):
  SERIES_NAME = 'series_name',
  SEASON = 'season', # Dependent on series_name
  DATE_AIRED = 'date_aired', # Dependent on series_name, season
  ACTOR_NAME = 'actor_name',
  CHARACTER_NAME = 'character_name',
  MONSTER_NAME = 'monster_name', # Dependent on monster_gender, monster_species
  MONSTER_GENDER = 'monster_gender', # Dependent on monster_name, monster_species
  MONSTER_SPECIES = 'monster_species', # Dependent on monster_name, monster_gender
  CULPRIT_NAME = 'culprit_name', # Dependent on culprit_gender
  CULPRIT_GENDER = 'culprit_gender', # Dependent on culprit_name
  SETTING_TERRAIN = 'setting_terrain', # Dependent on setting_place
  SETTING_PLACE = 'setting_place' # Dependent on setting_terrain
  
  def __str__(self):
    return str(self.value)

class Table(str, Enum):
  EPISODE_DETAILS = 'Episode_Details',
  VOICE_ACTORS = 'Voice_Actors',
  MONSTERS = 'Monsters',
  CULPRITS = 'Culprits',
  SETTINGS = 'Settings'
  
  def __str__(self):
    return str(self.value)
  
  
class Filter:
  def __init__(self, type: FilterType, table: Table, applied_value: str = '', disable_list: list[FilterType] = [], update_list: list[FilterType] = []):
    self.type = type
    self.table = table
    self.applied_value = applied_value
    self.disable_list = disable_list
    self.update_list = update_list
    
    self.options = []
    
  def __repr__(self) -> str:
    result = f'({self.type} {self.options})'
    return result


FILT_SERIES_NAME =  Filter(type=FilterType.SERIES_NAME, table=Table.EPISODE_DETAILS,
         disable_list=[
    
         ]
  )
FILT_SEASON = Filter(type=FilterType.SEASON, table = Table.EPISODE_DETAILS,
         disable_list=[
    
         ]
  )
FILT_DATE_AIRED = Filter(type=FilterType.DATE_AIRED, table = Table.EPISODE_DETAILS,
         disable_list=[
    
         ]
  )
FILT_ACTOR_NAME =  Filter(type=FilterType.ACTOR_NAME, table = Table.VOICE_ACTORS,
         disable_list=[
    
         ]
  )
FILT_CHARACTER_NAME = Filter(type=FilterType.CHARACTER_NAME, table = Table.VOICE_ACTORS,
         disable_list=[
    
         ]
  )
FILT_MONSTER_NAME = Filter(type=FilterType.MONSTER_NAME, table = Table.MONSTERS,
         disable_list=[
    
         ]
  )
FILT_MONSTER_GENDER = Filter(type=FilterType.MONSTER_GENDER, table = Table.MONSTERS,
         disable_list=[
    
         ]
  )
FILT_MONSTER_SPECIES = Filter(type=FilterType.MONSTER_SPECIES, table = Table.MONSTERS,
         disable_list=[
    
         ]
  )
FILT_CULPRIT_NAME = Filter(type=FilterType.CULPRIT_NAME, table = Table.CULPRITS,
         disable_list=[
    
         ]
  )
FILT_CULPRIT_GENDER = Filter(type=FilterType.SERIES_NAME, table = Table.CULPRITS, 
         disable_list=[
    
         ]
  )
FILT_SETTING_TERRAIN = Filter(type=FilterType.SERIES_NAME, table = Table.SETTINGS,
         disable_list=[
    
         ]
  )
FILT_SETTING_PLACE = Filter(type=FilterType.SERIES_NAME, table = Table.SETTINGS,
         disable_list=[
    
         ]
  )

filter_dict: dict[FilterType, Filter] = {
  FilterType.SERIES_NAME: FILT_SERIES_NAME,
  FilterType.SEASON: FILT_SEASON,
  FilterType.DATE_AIRED: FILT_DATE_AIRED,
  FilterType.ACTOR_NAME: FILT_ACTOR_NAME,
  FilterType.CHARACTER_NAME: FILT_CHARACTER_NAME,
  FilterType.MONSTER_NAME: FILT_MONSTER_NAME,
  FilterType.MONSTER_GENDER: FILT_MONSTER_GENDER,
  FilterType.MONSTER_SPECIES: FILT_MONSTER_SPECIES,
  FilterType.CULPRIT_NAME: FILT_CULPRIT_NAME,
  FilterType.CULPRIT_GENDER: FILT_CULPRIT_GENDER,
  FilterType.SETTING_TERRAIN: FILT_SETTING_TERRAIN,
  FilterType.SETTING_PLACE: FILT_SETTING_PLACE
}