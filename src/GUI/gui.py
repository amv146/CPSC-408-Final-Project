from logging import root
import tkinter as tk
from tkinter import END, Entry, Label, ttk, StringVar, OptionMenu
from tkinter.messagebox import showinfo

from numpy import character

from src.GUI.Tree import Tree
from src.GUI.Menu import Menu
from src.GUI.Filters import *

class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        

        self.geometry("1500x850")
        self.title('Scooby-Doo Database')
        # self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=2)
        self.columnconfigure(4, weight=2)
        self.columnconfigure(5, weight=2)
        self.columnconfigure(6, weight=2)
        self.columnconfigure(7, weight=1) 
        
        ## set minimal size for row 9 and column 9
        self.rowconfigure(0, minsize=30)
        self.rowconfigure(16, minsize=30)

        self.columnconfigure(0, minsize=20)
        self.columnconfigure(6, minsize=20)
        

        self.rowconfigure(2)
        self.buttons()
        self.filters()

        
        
    
       
    # Creating and Placing Buttons 
    def buttons(self):
        self.reset_button = ttk.Button(
            self,
            text='Reset Filters'   
        )
        
        self.reset_button.grid(column=6, row=5, padx=5, pady=5)


    def filters(self):
        filter = ttk.Label(self, text="FILTERS")
        filter.grid(column=1, row=0, padx=5, pady=5)

        # ROW 1

        # episode = ttk.Label(self, text="Episode Filters")
        # episode.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

        filter_label = ttk.Label(self, text="Series Name:")
        filter_label.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        series_menu = Menu(self, FilterType.SERIES_NAME)
        series_menu.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Season:")
        series_label.grid(column=3, row=1, sticky=tk.E, padx=5, pady=5)
        season_menu = Menu(self, FilterType.SEASON)
        season_menu.grid(column=4, row=1, sticky=tk.W, padx=5, pady=5)

        # ROW 2

        # episode = ttk.Label(self, text="Monster Filters")
        # episode.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

        filter_label = ttk.Label(self, text="Monster Name:")
        filter_label.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
        monster_name_menu = Menu(self, FilterType.MONSTER_NAME)
        monster_name_menu.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Monster Gender:")
        series_label.grid(column=3, row=2, sticky=tk.E, padx=5, pady=5)
        monster_gender_menu = Menu(self, FilterType.MONSTER_GENDER)
        monster_gender_menu.grid(column=4, row=2, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Monster Species:")
        series_label.grid(column=5, row=2, sticky=tk.E, padx=5, pady=5)
        monster_species_menu = Menu(self, FilterType.MONSTER_SPECIES)
        monster_species_menu.grid(column=6, row=2, sticky=tk.W, padx=5, pady=5)

        # ROW 3

        # episode = ttk.Label(self, text="Culprit Filters")
        # episode.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)

        filter_label = ttk.Label(self, text="Culprit Name:")
        filter_label.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        culprit_name_menu = Menu(self, FilterType.CULPRIT_NAME)
        culprit_name_menu.grid(column=2, row=3, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Culprit Gender:")
        series_label.grid(column=3, row=3, sticky=tk.E, padx=5, pady=5)
        culprit_gender_menu = Menu(self, FilterType.CULPRIT_GENDER)
        culprit_gender_menu.grid(column=4, row=3, sticky=tk.W, padx=5, pady=5)

        # ROW 4

        # episode = ttk.Label(self, text="Voice Actor Filters")
        # episode.grid(column=1, row=9, sticky=tk.W, padx=5, pady=5)

        filter_label = ttk.Label(self, text="Actor Name:")
        filter_label.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
        actor_menu = Menu(self, FilterType.ACTOR_NAME)
        actor_menu.grid(column=2, row=4, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Character Name:")
        series_label.grid(column=3, row=4, sticky=tk.E, padx=5, pady=5)
        character_menu = Menu(self, FilterType.CHARACTER_NAME)
        character_menu.grid(column=4, row=4, sticky=tk.W, padx=5, pady=5)

        # ROW 4

        # episode = ttk.Label(self, text="Setting Filters")
        # episode.grid(column=1, row=12, sticky=tk.W, padx=5, pady=5)

        filter_label = ttk.Label(self, text="Terrain:")
        filter_label.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
        setting_terrain_menu = Menu(self, FilterType.SETTING_TERRAIN)
        setting_terrain_menu.grid(column=2, row=5, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Place:")
        series_label.grid(column=3, row=5, sticky=tk.E, padx=5, pady=5)
        setting_place_menu = Menu(self, FilterType.SETTING_PLACE)
        setting_place_menu.grid(column=4, row=5, sticky=tk.W, padx=5, pady=5)

        # series_label = ttk.Label(self, text="Run Time:")
        # series_label.grid(column=3, row=1, sticky=tk.W, padx=5, pady=5)
        # menu = Menu(self, FilterType.)
        # menu.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
        self.menus = [series_menu, season_menu, monster_name_menu, monster_gender_menu, monster_species_menu, culprit_name_menu, culprit_gender_menu, actor_menu, character_menu, setting_place_menu, setting_terrain_menu]


    # def options(self):
        # o.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)



    def table(self, df, cols):

        self.tree = Tree(self, df, cols)
        self.tree.grid(row=15, column=1, columnspan=6, sticky=tk.NSEW)
        # scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        # self.tree.configure(yscroll=scrollbar.set)
        # scrollbar.grid(row=15, column=5, sticky='ns')
        
        # PRINTS SELECTED ROW TO SCREEN
        temp_label = Label(self, text="")
        temp_label.grid(column=2, row=16)
        
        # EPISODE DETAILS
        self.seriesName = tk.StringVar()
        self.season = tk.StringVar()
        self.title = tk.StringVar()
        self.date_aired = tk.StringVar()
        self.run_time = tk.StringVar()
        self.monster_real = tk.StringVar()
        self.monster_name = tk.StringVar()
        self.monster_gender = tk.StringVar()
        self.monster_type = tk.StringVar()
        self.monster_subtype = tk.StringVar()
        self.monster_species = tk.StringVar()
        self.motive = tk.StringVar()
        self.culprit_name = tk.StringVar()
        self.culprit_gender = tk.StringVar()
        self.character_name = tk.StringVar()
        self.actor_name = tk.StringVar()
        self.setting_terrain = tk.StringVar()
        self.setting_place = tk.StringVar()
        
        # EPISODE INFO
        self.episode_label = Label(self, text="EPISODE INFO: ")
        self.episode_label.grid(row=17, column=1)
        
        self.series_label = Label(self, text="Series Name: ")
        self.series_label.grid(row=18, column=1, sticky=tk.E)
        self.series_entry = Entry(self, textvariable= self.seriesName)
        self.series_entry.grid(row=18, column=2, sticky=tk.W)
        
        self.season_label = Label(self, text="Season: ")
        self.season_label.grid(row=18, column=3, sticky=tk.E)
        self.season_entry = Entry(self, textvariable= self.season)
        self.season_entry.grid(row=18, column=4, sticky=tk.W)
        
        self.title_label = Label(self, text="Title: ")
        self.title_label.grid(row=18, column=5, sticky=tk.E)
        self.title_entry = Entry(self, textvariable= self.title)
        self.title_entry.grid(row=18, column=6, sticky=tk.W)
        
        self.aired_label = Label(self, text="Date Aired: ")
        self.aired_label.grid(row=19, column=1, sticky=tk.E)
        self.aired_entry = Entry(self, textvariable= self.date_aired)
        self.aired_entry.grid(row=19, column=2, sticky=tk.W)
        
        self.run_label = Label(self, text="Run Time: ")
        self.run_label.grid(row=19, column=3, sticky=tk.E)
        self.run_entry = Entry(self, textvariable= self.run_time)
        self.run_entry.grid(row=19, column=4, sticky=tk.W)
        
        # MONSTERS INFO
        self.monster_label = Label(self, text="MONSTER INFO: ")
        self.monster_label.grid(row=20, column=1)
        
        self.monster_name_label = Label(self, text="Monster Name: ")
        self.monster_name_label.grid(row=21, column=1, sticky=tk.E)
        self.monster_entry = Entry(self, textvariable= self.monster_name)
        self.monster_entry.grid(row=21, column=2, sticky=tk.W)
        
        self.monster_real_label = Label(self, text="Monster Real: ")
        self.monster_real_label.grid(row=21, column=3, sticky=tk.E)
        self.monster_real_entry = Entry(self, textvariable= self.monster_real)
        self.monster_real_entry.grid(row=21, column=4, sticky=tk.W)
        
        self.monster_gender_label = Label(self, text="Monester Gender: ")
        self.monster_gender_label.grid(row=21, column=5, sticky=tk.E)
        self.monster_gender_entry = Entry(self, textvariable= self.monster_gender)
        self.monster_gender_entry.grid(row=21, column=6, sticky=tk.W)
        
        self.monster_type_label = Label(self, text="Monster Type: ")
        self.monster_type_label.grid(row=22, column=1, sticky=tk.E)
        self.monster_type_entry = Entry(self, textvariable= self.monster_type)
        self.monster_type_entry.grid(row=22, column=2, sticky=tk.W)
        
        self.monster_subtype_label = Label(self, text="Monster Subtype: ")
        self.monster_subtype_label.grid(row=22, column=3, sticky=tk.E)
        self.monster_subtype_entry = Entry(self, textvariable= self.monster_subtype)
        self.monster_subtype_entry.grid(row=22, column=4, sticky=tk.W)
        
        self.monster_species_label = Label(self, text="Monster Species: ")
        self.monster_species_label.grid(row=22, column=5, sticky=tk.E)
        self.monster_species_entry = Entry(self, textvariable= self.monster_species)
        self.monster_species_entry.grid(row=22, column=6, sticky=tk.W)
        
        
        # CULPRITS INFO
        self.culprit_label = Label(self, text="CULPRIT INFO: ")
        self.culprit_label.grid(row=23, column=1)
        
        self.culprit_name_label = Label(self, text="Culprit Name: ")
        self.culprit_name_label.grid(row=24, column=1, sticky=tk.E)
        self.culprit_name_entry = Entry(self, textvariable= self.culprit_name)
        self.culprit_name_entry.grid(row=24, column=2, sticky=tk.W)
        
        self.culprit_gender_label = Label(self, text="Culprit Gender: ")
        self.culprit_gender_label.grid(row=24, column=3, sticky=tk.E)
        self.culprit_gender_entry = Entry(self, textvariable= self.culprit_gender)
        self.culprit_gender_entry.grid(row=24, column=4, sticky=tk.W)
        
        self.motive_label = Label(self, text="Motive: ")
        self.motive_label.grid(row=24, column=5, sticky=tk.E)
        self.motive_entry = Entry(self, textvariable= self.motive)
        self.motive_entry.grid(row=24, column=6, sticky=tk.W)
        
        # VOICE ACTOR INFO
        self.episode_label = Label(self, text="VOICE ACTOR INFO: ")
        self.episode_label.grid(row=25, column=1)
        
        self.character_name_label = Label(self, text="Character Name: ")
        self.character_name_label.grid(row=26, column=1, sticky=tk.E)
        self.character_name_entry = Entry(self, textvariable= self.character_name)
        self.character_name_entry.grid(row=26, column=2, sticky=tk.W)
        
        self.actor_name_label = Label(self, text="Actor Name: ")
        self.actor_name_label.grid(row=26, column=3, sticky=tk.E)
        self.actor_name_entry = Entry(self, textvariable= self.actor_name)
        self.actor_name_entry.grid(row=26, column=4, sticky=tk.W)
        
        # SETTING INFO
        self.episode_label = Label(self, text="SETTING INFO: ")
        self.episode_label.grid(row=27, column=1)
        
        self.setting_terrain_label = Label(self, text="Setting Terrain: ")
        self.setting_terrain_label.grid(row=28, column=1, sticky=tk.E)
        self.setting_terrain_entry = Entry(self, textvariable= self.setting_terrain)
        self.setting_terrain_entry.grid(row=28, column=2, sticky=tk.W)
        
        self.setting_place_label = Label(self, text="Setting Place: ")
        self.setting_place_label.grid(row=28, column=3, sticky=tk.E)
        self.setting_place_entry = Entry(self, textvariable= self.setting_place)
        self.setting_place_entry.grid(row=28, column=4, sticky=tk.W)
        
        # SPACER
        spacer_label1 = Label(self, text="")
        spacer_label2 = Label(self, text="")
        spacer_label1.grid(column=2, row=29)
        spacer_label2.grid(column=2,row=10)
        
        
        # BUTTONS
        self.add_record_button = ttk.Button(
            self,
            text='Add Record' 
        )
        self.delete_record_button = ttk.Button(
            self,
            text='Delete Record' 
        )
        self.update_record_button = ttk.Button(
            self,
            text='Update Record' 
        )
        self.export_button = ttk.Button(
            self,
            text='Export' 
        )
        self.clear_button = ttk.Button(
            self,
            text='Clear' 
        )
        
        self.update_record_button.grid(column=2, row=30, padx=5, pady=5)
        self.delete_record_button.grid(column=3, row=30, padx=5, pady=5)
        self.add_record_button.grid(column=4, row=30, padx=5, pady=5)
        self.clear_button.grid(column=5, row=30, padx=5, pady=5)
        
        self.export_button.grid(column=6, row=16, padx=5, pady=5)
        
        
        
        # Select Records
        # def select_record():
        #     # Delete the record details boxes?
        #     # box.delete(0,END)
            
        #     # # Grab record number
        #     # selected = Tree.focus()
        #     # # Grab record values
        #     # values = Tree.item(selected, 'values')
            
        #     selected = self.tree.focus()
        #     item = self.tree.item(selected)
        #     print(item)
        #     temp_label.config(text = selected)
            
        # Create Binding Click function
        
        return self.tree
    
    def change_entry_text(self, entry: Entry, text: str):
        entry.delete(0, END)
        entry.insert(0, text)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
