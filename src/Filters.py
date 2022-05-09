import mysql
from mysql import connector
from sqlite3 import Cursor
import pandas as pd
from pandas import DataFrame
from enum import Enum

class FilterType(Enum):
  SERIES_NAME = 1,
  SEASON = 2, # Dependent on series_name
  DATE_AIRED = 3, # Dependent on series_name, season
  ACTOR_NAME = 4,
  CHARACTER_NAME = 5,
  MONSTER_NAME = 6, # Dependent on monster_gender, monster_species
  MONSTER_GENDER = 7, # Dependent on monster_name, monster_species
  MONSTER_SPECIES = 8, # Dependent on monster_name, monster_gender
  CULPRIT_NAME = 9, # Dependent on culprit_gender
  CULPRIT_GENDER = 10, # Dependent on culprit_name
  SETTING_TERRAIN = 11, # Dependent on setting_place
  SETTING_PLACE = 12 # Dependent on setting_terrain