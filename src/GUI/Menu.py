import tkinter as tk
from tkinter import Misc, OptionMenu, StringVar
from typing import Any, Callable
from GUI.Filters import *

class Menu(OptionMenu):
  def __init__(self, master: Misc | None, filter_type: FilterType) -> None:
      super().__init__(master, StringVar(master), '')
      self.filter_type = filter_type
      
  