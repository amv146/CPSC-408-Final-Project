import mysql
from mysql import connector
from sqlite3 import Cursor
import pandas as pd
from pandas import DataFrame
from enum import Enum

class FilterType(Enum):
  SERIES_NAME = 'series_name',
  SEASON = 'name', # Dependent on series_name
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

class Table(Enum):
  
  
class Filter:
  def __init__(self, type: FilterType, disable_list: list[FilterType], update_list: list[FilterType]) -> None:
    self.type = type
    self.disable_list = []
    self.update_list = []
      
class FilterHandler:
  def __init__(self) -> None:
    pass