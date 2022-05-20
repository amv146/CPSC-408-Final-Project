import tkinter as tk
from tkinter import Misc, OptionMenu, StringVar
from typing import Any, Callable

from GUI.Filters import *

class Menu(OptionMenu):
  def __init__(self, master, filter_type: FilterType):
      self.options = StringVar(master, '')
      super().__init__(master, self.options, '')
      self.filter_type = filter_type
      self.filter = filter_dict[self.filter_type]
      self.reset_val = False





  def add_options(self):
    self.remove_all() # remove all options
    for opt in [' '] + self.filter.options:
      self['menu'].add_command(label=opt, command=lambda value=opt: self.options.set(str(value)))

  def remove_all(self):
    self['menu'].delete(0,'end')
