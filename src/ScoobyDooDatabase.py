import mysql
from mysql import connector
from sqlite3 import Cursor
from os import system

from Database import Database


class ScoobyDooDatabase (Database):
  def __init__(self):
      super().__init__('ScoobyDoo')
  
  def run_sql_file(self):
    command = """mysql -u %s -p"%s" --host %s --port %s %s < %s""" %('root', self.get_password(), 'localhost', '3061', 'ScoobyDoo', '../data/database_setup.sql')
    system(command)


  