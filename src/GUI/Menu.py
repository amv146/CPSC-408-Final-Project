import tkinter as tk
from tkinter import Misc, OptionMenu, StringVar
from typing import Any, Callable


class Menu(OptionMenu):
  def __init__(self, master: Misc | None, variable: StringVar, value: str, *values: str, command: Callable[[StringVar], Any] | None = ...) -> None:
      super().__init__(master, variable, value, *values, command=command)
      
  