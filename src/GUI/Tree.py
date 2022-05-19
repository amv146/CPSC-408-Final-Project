import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import pandas as pd
from tkinter.ttk import Treeview
from pandas import DataFrame
import re

class Tree(Treeview):
  def __init__(self, app, dataframe: DataFrame, columns: list[str]) -> None:
    self.columns: list[str] = columns
    self.dataframe = dataframe

    super().__init__(app, columns=self.columns, show='headings')
    
    self.make_headings()
    self.set_headings()
    
    self.change_table(self.dataframe)
    
    

  def make_headings(self):
    pattern = r'([^_]+)+'
    headings = []
    for col in self.columns:
      groups = re.findall(pattern, col)
      heading = ""
      for group in groups:
        heading += str.upper(group[0]) + group[1:]
        if group != groups[len(groups) - 1]:
          heading += ' '
      headings.append(heading)
      
    self.headings = headings
    
  def change_table(self, df: DataFrame):
    df = df[self.columns].drop_duplicates()
    for child in self.get_children():
      self.delete(child)
    self.set_rows(df)
    self.dataframe = df
    
  def set_rows(self, df: DataFrame):
    for row_index in range(0, len(df)):
      row = list(df.iloc[row_index])
      self.insert('', tk.END, values=row)
    
  def set_headings(self):
    for i in range(len(self.headings)):
      self.heading(self.columns[i], text=self.headings[i])
    
        