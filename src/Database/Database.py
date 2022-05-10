from mysql import connector
from sqlite3 import Cursor
import pandas as pd
from pandas import DataFrame
from mysql.connector import CMySQLConnection
import base64
from Utils import *

class Database:
  def __init__(self, database_name: str):
    self.database_name: str = database_name
    self.connect('localhost', '3306')
    
  def get_cursor(self) -> Cursor:
    return self.database.cursor(buffered=True) 
    
  def read_sql(self, sql: str) -> DataFrame:
    return pd.read_sql(sql, self.database)
  
  def refresh_cursor(self):
    self.cursor.close()
    self.database.reconnect()
    self.cursor = self.database.cursor(buffered=True)
    
  def try_connect(self, host: str, user: str, password: str, port: str, schema: str = "") -> CMySQLConnection | None:
    if schema == "":
      try:
        db = connector.connect(host=host, 
          user=user, 
          password=password, 
          port=port,
          auth_plugin='mysql_native_password') 
        return db
      except:
        return None
    else:
      try:
        db = connector.connect(host=host, 
          user=user, 
          password=password, 
          port=port,
          auth_plugin='mysql_native_password',
          database=schema) 
        return db
      except:
        return None
    
    
  def connect(self, host: str, port: str):
    password = self.get_password()
    db: CMySQLConnection | None = None
    if (password != None):
      db = self.try_connect(host, 'root', password, port)
    while db == None:
      password = input("Please input your MySQL password to connect\n")
      db = self.try_connect(host, 'root', password, port)
    self.database = db
    self.cursor = self.database.cursor(buffered=True)
    self.store_password(str(password))
    
    self.try_create_schema(self.cursor)
    db = self.try_connect(host, 'root', str(password), '3306', self.database_name)
    if db != None:
      self.database = db
    
      
      
  def try_create_schema(self, cursor: Cursor):
    cursor.execute("CREATE SCHEMA IF NOT EXISTS ScoobyDoo;")

  def store_password(self, password: str):
    encoded = base64.b64encode(password.encode('utf-8'))
    with open(get_project_root().__str__() + '/data/data.txt', 'w+') as file:
      file.write(str(encoded, 'utf-8'))
    
  def get_password(self) -> str | None:
    try:
      with open(get_project_root().__str__() + '/data/data.txt') as file:
        password = file.read()
    except:
      return None
    if (password == None or password == ""):
      return None
    return str(base64.b64decode(password).decode('utf-8'))
