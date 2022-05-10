import mysql
from mysql import connector
from sqlite3 import Cursor
from os import system
from pandas import DataFrame
import pandas as pd
from Database.Database import Database
from Utils import *


class ScoobyDooDatabase (Database):
  def __init__(self):
      super().__init__('ScoobyDoo')
  
  def run_sql_file(self): 
    command = """mysql -u %s -p"%s" --host %s --port %s %s < %s""" %('root', self.get_password(), 'localhost', '3061', 'ScoobyDoo', get_project_root().__str__() + '/data/database_setup.sql')
    system(command)

  def run_all_procedure(self, series_name: str = '', season: int = 0, title: str = '', date_aired: str = '', runtime: int = 0, monster_real: str = '', motive: str = '', setting_terrain: str = '', setting_place: str = '', actor_name: str = '', character_name: str = '', monster_name: str = '', monster_gender: str = '', monster_type: str = '', monster_species: str = '', monster_subtype: str = '', culprit_name: str = '', culprit_gender: str = ''): 
    sql = 'CALL Query_All({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17})'.format(null(series_name), null(season), null(title), null(date_aired), null(runtime), null(monster_real), null(motive), null(setting_terrain), null(setting_place), null(actor_name), null(character_name), null(monster_name), null(monster_gender), null(monster_type), null(monster_species), null(monster_subtype), null(culprit_name), null(culprit_gender))
    print(sql)
    result = pd.read_sql(sql, self.database)
    return result

  