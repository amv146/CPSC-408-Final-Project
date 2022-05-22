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
        
        self.geometry("1560x990")
        self.title('Scooby-Doo Database')

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
        self.rowconfigure(0, minsize=20)
        self.rowconfigure(16, minsize=20)

        self.columnconfigure(0, minsize=20)
        self.columnconfigure(7, minsize=20)
        
        title = ttk.Label(self, text="SCOOBY-DOO", font=("Helvetica", 18))
        title.grid(column=3, row=0, sticky=tk.E, padx=5, pady=5)
        title = ttk.Label(self, text="DATABASE", font=("Helvetica", 18))
        title.grid(column=4, row=0, sticky=tk.W, padx=5, pady=5)
        
        self.rowconfigure(2)
        self.buttons()
        self.filters()

        
    # Creating and Placing Buttons 
    def buttons(self):
        self.reset_button = ttk.Button(
            self,
            text='Reset Filters'   
        )
        self.export_button = ttk.Button(
            self,
            text='Export' 
        )
        self.export_button.grid(column=6, row=6,sticky=tk.E)
        
        self.reset_button.grid(column=5, row=5, sticky=tk.E)


    def filters(self):
    #  ROW 2
        filter = ttk.Label(self, text="FILTERS")
        filter.grid(column=1, row=1)

    # ROW 2
        filter_label = ttk.Label(self, text="Series Name:")
        filter_label.grid(column=1, row=2, sticky=tk.E, pady=1)
        series_menu = Menu(self, FilterType.SERIES_NAME)
        series_menu.grid(column=2, row=2, sticky=tk.W, pady=1)

        series_label = ttk.Label(self, text="Season:")
        series_label.grid(column=3, row=2, sticky=tk.E, pady=1)
        season_menu = Menu(self, FilterType.SEASON)
        season_menu.grid(column=4, row=2, sticky=tk.W, pady=1)

    # ROW 3
        filter_label = ttk.Label(self, text="Monster Name:")
        filter_label.grid(column=1, row=3, sticky=tk.E, pady=1)
        monster_name_menu = Menu(self, FilterType.MONSTER_NAME)
        monster_name_menu.grid(column=2, row=3, sticky=tk.W, pady=1)

        series_label = ttk.Label(self, text="Monster Gender:")
        series_label.grid(column=3, row=3, sticky=tk.E, pady=1)
        monster_gender_menu = Menu(self, FilterType.MONSTER_GENDER)
        monster_gender_menu.grid(column=4, row=3, sticky=tk.W, pady=2)

        series_label = ttk.Label(self, text="Monster Species:")
        series_label.grid(column=5, row=3, sticky=tk.E, pady=1)
        monster_species_menu = Menu(self, FilterType.MONSTER_SPECIES)
        monster_species_menu.grid(column=6, row=3, sticky=tk.W, pady=1)

    # ROW 4
        filter_label = ttk.Label(self, text="Culprit Name:")
        filter_label.grid(column=1, row=4, sticky=tk.E, pady=2)
        culprit_name_menu = Menu(self, FilterType.CULPRIT_NAME)
        culprit_name_menu.grid(column=2, row=4, sticky=tk.W, pady=2)

        series_label = ttk.Label(self, text="Culprit Gender:")
        series_label.grid(column=3, row=4, sticky=tk.E, pady=2)
        culprit_gender_menu = Menu(self, FilterType.CULPRIT_GENDER)
        culprit_gender_menu.grid(column=4, row=4, sticky=tk.W, pady=2)

    # ROW 5
        filter_label = ttk.Label(self, text="Actor Name:")
        filter_label.grid(column=1, row=5, sticky=tk.E, pady=2)
        actor_menu = Menu(self, FilterType.ACTOR_NAME)
        actor_menu.grid(column=2, row=5, sticky=tk.W, pady=2)

        series_label = ttk.Label(self, text="Character Name:")
        series_label.grid(column=3, row=5, sticky=tk.E, pady=2)
        character_menu = Menu(self, FilterType.CHARACTER_NAME)
        character_menu.grid(column=4, row=5, sticky=tk.W, pady=2)

     # ROW 6
        filter_label = ttk.Label(self, text="Terrain:")
        filter_label.grid(column=1, row=6, sticky=tk.E, pady=2)
        setting_terrain_menu = Menu(self, FilterType.SETTING_TERRAIN)
        setting_terrain_menu.grid(column=2, row=6, sticky=tk.W, pady=2)

        series_label = ttk.Label(self, text="Place:")
        series_label.grid(column=3, row=6, sticky=tk.E, pady=2)
        setting_place_menu = Menu(self, FilterType.SETTING_PLACE)
        setting_place_menu.grid(column=4, row=6, sticky=tk.W, pady=2)

        self.menus = [series_menu, season_menu, monster_name_menu, monster_gender_menu, monster_species_menu, culprit_name_menu, culprit_gender_menu, actor_menu, character_menu, setting_place_menu, setting_terrain_menu]


    def table(self, df, cols):

        self.tree = Tree(self, cols, dataframe= df)
        self.tree.grid(row=15, column=1, columnspan=6, sticky=tk.NSEW)
        
        # EPISODE DETAILS VARIABLES
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
        
        # BOXES
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
        
        # AGGREGET TOTAL MONSTERS
        self.monster_total = tk.IntVar()
        self.monster_total = 0
        self.monster_total_label = Label(self, text="Total Monsters:")
        self.monster_num_label = Label(self, text= self.monster_total)
        self.monster_total_label.grid(row=20, column=6, sticky=tk.E)
        self.monster_num_label.grid(row=20, column=7, sticky=tk.W)
        
        # TABLE
        self.monster_tree = Tree(self, columns=['monster_name', 'monster_gender', 'monster_type', 'monster_subtype', 'monster_species'], height=2)
        self.monster_tree.grid(row=21, column=1, columnspan=6, sticky=tk.NSEW)
        
        # BOXES
        self.monster_name_label = Label(self, text="Monster Name: ")
        self.monster_name_label.grid(row=22, column=1, sticky=tk.E)
        
        self.monster_entry = Entry(self, textvariable= self.monster_name)
        self.monster_entry.grid(row=22, column=2, sticky=tk.W)
        
        self.monster_real_label = Label(self, text="Monster Real: ")
        self.monster_real_label.grid(row=22, column=3, sticky=tk.E)
        self.monster_real_entry = Entry(self, textvariable= self.monster_real)
        self.monster_real_entry.grid(row=22, column=4, sticky=tk.W)
        
        self.monster_gender_label = Label(self, text="Monster Gender: ")
        self.monster_gender_label.grid(row=22, column=5, sticky=tk.E)
        
        self.monster_gender_entry = Entry(self, textvariable= self.monster_gender)
        self.monster_gender_entry.grid(row=22, column=6, sticky=tk.W)
        
        self.monster_type_label = Label(self, text="Monster Type: ")
        self.monster_type_label.grid(row=24, column=1, sticky=tk.E)
        
        self.monster_type_entry = Entry(self, textvariable= self.monster_type)
        self.monster_type_entry.grid(row=24, column=2, sticky=tk.W)
        
        self.monster_subtype_label = Label(self, text="Monster Subtype: ")
        self.monster_subtype_label.grid(row=24, column=3, sticky=tk.E)
        
        self.monster_subtype_entry = Entry(self, textvariable= self.monster_subtype)
        self.monster_subtype_entry.grid(row=24, column=4, sticky=tk.W)
        
        self.monster_species_label = Label(self, text="Monster Species: ")
        self.monster_species_label.grid(row=24, column=5, sticky=tk.E)
        
        self.monster_species_entry = Entry(self, textvariable= self.monster_species)
        self.monster_species_entry.grid(row=24, column=6, sticky=tk.W)
        
        
    # CULPRITS INFO
        self.culprit_label = Label(self, text="CULPRIT INFO: ")
        self.culprit_label.grid(row=25, column=1)
        
        # AGGREGET TOTAL CULPRITS
        self.culprits_total = tk.IntVar()
        self.culprits_total = 0
        self.culprits_total_label = Label(self, text="Total Culprits:")
        self.culprits_num_label = Label(self, text= self.culprits_total)
        self.culprits_total_label.grid(row=25, column=6, sticky=tk.E)
        self.culprits_num_label.grid(row=25, column=7, sticky=tk.W)
        
        # TABLE
        self.culprits_tree = Tree(self, columns=['culprit_name', 'culprit_gender'], height=2)
        self.culprits_tree.grid(row=26, column=1, columnspan=6, sticky=tk.NSEW)
        
        # BOXES
        self.culprit_name_label = Label(self, text="Culprit Name: ")
        self.culprit_name_label.grid(row=27, column=1, sticky=tk.E)
        
        self.culprit_name_entry = Entry(self, textvariable= self.culprit_name)
        self.culprit_name_entry.grid(row=27, column=2, sticky=tk.W)
        
        self.culprit_gender_label = Label(self, text="Culprit Gender: ")
        self.culprit_gender_label.grid(row=27, column=3, sticky=tk.E)

        
        self.culprit_gender_entry = Entry(self, textvariable= self.culprit_gender)
        self.culprit_gender_entry.grid(row=27, column=4, sticky=tk.W)
        
        self.motive_label = Label(self, text="Motive: ")
        self.motive_label.grid(row=27, column=5, sticky=tk.E)
        self.motive_entry = Entry(self, textvariable= self.motive)
        self.motive_entry.grid(row=27, column=6, sticky=tk.W)
        
    # VOICE ACTOR INFO
        self.episode_label = Label(self, text="VOICE ACTOR INFO: ")
        self.episode_label.grid(row=28, column=1)
        
         # AGGREGET TOTAL CULPRITS
        self.va_total = tk.IntVar()
        self.va_total = 0
        self.va_total_label = Label(self, text="Total Voice Actors:")
        self.va_num_label = Label(self, text= self.va_total)
        self.va_total_label.grid(row=28, column=6, sticky=tk.E)
        self.va_num_label.grid(row=28, column=7, sticky=tk.W)
        
        # TABLE
        self.va_tree = Tree(self, columns=['character_name', 'actor_name'], height=2)
        self.va_tree.grid(row=29, column=1, columnspan=6, sticky=tk.NSEW)
        
        # BOXES
        self.character_name_label = Label(self, text="Character Name: ")
        self.character_name_label.grid(row=30, column=1, sticky=tk.E)
        
        self.character_name_entry = Entry(self, textvariable= self.character_name)
        self.character_name_entry.grid(row=30, column=2, sticky=tk.W)
        
        self.actor_name_label = Label(self, text="Actor Name: ")
        self.actor_name_label.grid(row=30, column=3, sticky=tk.E)
        
        self.actor_name_entry = Entry(self, textvariable= self.actor_name)
        self.actor_name_entry.grid(row=30, column=4, sticky=tk.W)
        
    # SETTING INFO
        self.episode_label = Label(self, text="SETTING INFO: ")
        self.episode_label.grid(row=31, column=1)
        
        # BOXES
        self.setting_terrain_label = Label(self, text="Setting Terrain: ")
        self.setting_terrain_label.grid(row=33, column=1, sticky=tk.E)
        
        self.setting_terrain_entry = Entry(self, textvariable= self.setting_terrain)
        self.setting_terrain_entry.grid(row=33, column=2, sticky=tk.W)
        
        self.setting_place_label = Label(self, text="Setting Place: ")
        self.setting_place_label.grid(row=33, column=3, sticky=tk.E)
        
        self.setting_place_entry = Entry(self, textvariable= self.setting_place)
        self.setting_place_entry.grid(row=33, column=4, sticky=tk.W)
        
        # SPACER
        # spacer_label1 = Label(self, text="")
        # spacer_label2 = Label(self, text="")
        # spacer_label1.grid(column=2, row=33)
        # spacer_label2.grid(column=2,row=10)
        
        
     # BUTTONS
        self.add_record_button = ttk.Button(self, text='Add Record')
        self.delete_record_button = ttk.Button(self, text='Delete Record')
        self.update_record_button = ttk.Button(self, text='Update Record')
        self.clear_button = ttk.Button(self, text='Clear')
        
        self.update_record_button.grid(column=2, row=34, padx=5, pady=5)
        self.delete_record_button.grid(column=3, row=34, padx=5, pady=5)
        self.add_record_button.grid(column=4, row=34, padx=5, pady=5)
        self.clear_button.grid(column=5, row=34, padx=5, pady=5)
        
        return self.tree
    
    def change_entry_text(self, entry: Entry, text: str):
        entry.delete(0, END)
        entry.insert(0, text)
        
    def entry_text(self, entry: Entry):
        return entry.get()
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
