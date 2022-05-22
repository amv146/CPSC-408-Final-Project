from typing import final
from mysql import connector
from mysql.connector.cursor import MySQLCursor as Cursor
import pandas as pd
from pandas import DataFrame
from mysql.connector import CMySQLConnection
from src.Utils import *

class Database:
  def __init__(self, database_name: str):
    self.database_name: str = database_name
    self.connect()
    
  def get_cursor(self) -> Cursor:
    return self.database.cursor(buffered=True) 
    
  def read_sql(self, sql: str) -> DataFrame:
    self.refresh_cursor()
    return pd.read_sql(sql, self.database)
  
  def commit(self, sql: str):
    self.refresh_cursor()
    self.cursor.execute(sql)
    self.database.commit()
    self.refresh_cursor()

  def rollback(self):
    self.refresh_cursor()
    self.database.rollback()
    self.refresh_cursor()
  
  def refresh_cursor(self):
    try:
      self.cursor.close()
    except:
      pass
    finally:
      self.database.reconnect()
      self.cursor: Cursor = self.database.cursor(buffered=True)
    
  def connect(self):
    db: CMySQLConnection = connector.connect(host='chapman-univ.mysql.database.azure.com', 
      user='adminroot',
      password='Chapman408!', 
      database='scooby_doo',
      client_flags= [connector.ClientFlag.SSL]
    )
    self.database = db
    self.cursor: Cursor = self.database.cursor(buffered=True)

    if db != None:
      self.database = db
    