from logging import root
import tkinter as tk
from tkinter import Entry, Label, ttk, StringVar, OptionMenu
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
        
        # lr1 = tk.Label()
        
        
        # self.temp_button = ttk.Button(
        #     self,
        #     text = "select button"
        # )
        
        # self.temp_button
        
        # self.temp_label = Label(self, text="")
        # self.temp_label.grid(column=4, row=13)
        
        # self.select_record()
        
        # self.table(pd.DataFrame())
        # self.options()
        
        # showing all the record information 
        
        
    
       
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
        seriesName = tk.StringVar()
        season = tk.StringVar()
        title = tk.StringVar()
        date_aired = tk.StringVar()
        run_time = tk.StringVar()
        monster_real = tk.StringVar()
        monster_name = tk.StringVar()
        monster_gender = tk.StringVar()
        monster_type = tk.StringVar()
        monster_subtype = tk.StringVar()
        monster_species = tk.StringVar()
        motive = tk.StringVar()
        culprit_name = tk.StringVar()
        culprit_gender = tk.StringVar()
        character_name = tk.StringVar()
        actor_name = tk.StringVar()
        setting_terrain = tk.StringVar()
        setting_place = tk.StringVar()
        
        # EPISODE INFO
        episode_label = Label(self, text="EPISODE INFO: ")
        episode_label.grid(row=17, column=1)
        
        series_label = Label(self, text="Series Name: ")
        series_label.grid(row=18, column=1, sticky=tk.E)
        series_entry = Entry(self, textvariable= seriesName)
        series_entry.grid(row=18, column=2, sticky=tk.W)
        
        season_label = Label(self, text="Season: ")
        season_label.grid(row=18, column=3, sticky=tk.E)
        series_entry = Entry(self, textvariable= season)
        series_entry.grid(row=18, column=4, sticky=tk.W)
        
        title_label = Label(self, text="Title: ")
        title_label.grid(row=18, column=5, sticky=tk.E)
        title_entry = Entry(self, textvariable= title)
        title_entry.grid(row=18, column=6, sticky=tk.W)
        
        aired_label = Label(self, text="Date Aired: ")
        aired_label.grid(row=19, column=1, sticky=tk.E)
        aired_entry = Entry(self, textvariable= date_aired)
        aired_entry.grid(row=19, column=2, sticky=tk.W)
        
        run_label = Label(self, text="Run Time: ")
        run_label.grid(row=19, column=3, sticky=tk.E)
        run_entry = Entry(self, textvariable= run_time)
        run_entry.grid(row=19, column=4, sticky=tk.W)
        
        # MONSTERS INFO
        monster_label = Label(self, text="MONSTER INFO: ")
        monster_label.grid(row=20, column=1)
        
        monster_name_label = Label(self, text="Monster Name: ")
        monster_name_label.grid(row=21, column=1, sticky=tk.E)
        monster_entry = Entry(self, textvariable= monster_name)
        monster_entry.grid(row=21, column=2, sticky=tk.W)
        
        monster_real_label = Label(self, text="Monster Real: ")
        monster_real_label.grid(row=21, column=3, sticky=tk.E)
        monster_real_entry = Entry(self, textvariable= monster_real)
        monster_real_entry.grid(row=21, column=4, sticky=tk.W)
        
        monster_gender_label = Label(self, text="Monester Gender: ")
        monster_gender_label.grid(row=21, column=5, sticky=tk.E)
        monster_gender_entry = Entry(self, textvariable= monster_gender)
        monster_gender_entry.grid(row=21, column=6, sticky=tk.W)
        
        monster_type_label = Label(self, text="Monster Type: ")
        monster_type_label.grid(row=22, column=1, sticky=tk.E)
        monster_type_entry = Entry(self, textvariable= monster_type)
        monster_type_entry.grid(row=22, column=2, sticky=tk.W)
        
        monster_subtype_label = Label(self, text="Monster Subtype: ")
        monster_subtype_label.grid(row=22, column=3, sticky=tk.E)
        monster_subtype_entry = Entry(self, textvariable= monster_subtype)
        monster_subtype_entry.grid(row=22, column=4, sticky=tk.W)
        
        monster_species_label = Label(self, text="Monster Species: ")
        monster_species_label.grid(row=22, column=5, sticky=tk.E)
        monster_species_entry = Entry(self, textvariable= monster_species)
        monster_species_entry.grid(row=22, column=6, sticky=tk.W)
        
        
        # CULPRITS INFO
        culprit_label = Label(self, text="CULPRIT INFO: ")
        culprit_label.grid(row=23, column=1)
        
        culprit_name_label = Label(self, text="Culprit Name: ")
        culprit_name_label.grid(row=24, column=1, sticky=tk.E)
        culprit_name_entry = Entry(self, textvariable= culprit_name)
        culprit_name_entry.grid(row=24, column=2, sticky=tk.W)
        
        culprit_gender_label = Label(self, text="Culprit Gender: ")
        culprit_gender_label.grid(row=24, column=3, sticky=tk.E)
        culprit_gender_entry = Entry(self, textvariable= culprit_gender)
        culprit_gender_entry.grid(row=24, column=4, sticky=tk.W)
        
        motive_label = Label(self, text="Motive: ")
        motive_label.grid(row=24, column=5, sticky=tk.E)
        motive_entry = Entry(self, textvariable= motive)
        motive_entry.grid(row=24, column=6, sticky=tk.W)
        
        # VOICE ACTOR INFO
        episode_label = Label(self, text="VOICE ACTOR INFO: ")
        episode_label.grid(row=25, column=1)
        
        character_name_label = Label(self, text="Character Name: ")
        character_name_label.grid(row=26, column=1, sticky=tk.E)
        character_name_entry = Entry(self, textvariable= character_name)
        character_name_entry.grid(row=26, column=2, sticky=tk.W)
        
        actor_name_label = Label(self, text="Actor Name: ")
        actor_name_label.grid(row=26, column=3, sticky=tk.E)
        actor_name_entry = Entry(self, textvariable= actor_name)
        actor_name_entry.grid(row=26, column=4, sticky=tk.W)
        
        # SETTING INFO
        episode_label = Label(self, text="SETTING INFO: ")
        episode_label.grid(row=27, column=1)
        
        setting_terrain_label = Label(self, text="Setting Terrain: ")
        setting_terrain_label.grid(row=28, column=1, sticky=tk.E)
        setting_terrain_entry = Entry(self, textvariable= setting_terrain)
        setting_terrain_entry.grid(row=28, column=2, sticky=tk.W)
        
        setting_place_label = Label(self, text="Setting Place: ")
        setting_place_label.grid(row=28, column=3, sticky=tk.E)
        setting_place_entry = Entry(self, textvariable= setting_place)
        setting_place_entry.grid(row=28, column=4, sticky=tk.W)
        
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
        def select_record():
            # Delete the record details boxes?
            # box.delete(0,END)
            
            # # Grab record number
            # selected = Tree.focus()
            # # Grab record values
            # values = Tree.item(selected, 'values')
            
            selected = self.tree.focus()
            temp_label.config(text = selected)
    
        # Create Binding Click function
        def clicker(e):
            select_record()
        
        
        
        selected = self.tree.focus()
        
        
        # Bindings
        self.tree.bind("<ButtonRelease-1>", clicker)
        
        
        
        return self.tree
    
    
    
    
    
    
    # # NOT DOING ANYTHING / USING!!!!!!
    # def item_selected(self, event):
    #     for selected_item in tree.selection():
    #         item = self.tree.item(selected_item)
    #         record = item['values']
    #         # show a message
    #         showinfo(title='Information', message=','.join(record))
    #         o = Menu(self, FilterType.ACTOR_NAME)

        # # label 1
        # label2 = tk.Label(
        #     self,
        #     text="Relative placement",
        #     # bg='blue',
        #     # fg='white'
        # )

        # label2.place(relx=0.8, rely=0.2, relwidth=0.5, anchor='ne')

        # # # define columns
        # # columns = ('first_name', 'last_name', 'email')

        # # tree = ttk.Treeview(self, columns=columns, show='headings')

        # # contacts = []
        # # for n in range(1, 100):
        # #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
        # # columns = ('Episode_Number', 'Season', 'Monster_Real')

        # # tree = ttk.Treeview(self, columns=columns, show='headings')

        # # tree.heading('Episode_Number', text='Episode Number')
        # # tree.heading('Season', text='Season')
        # # tree.heading('Monster_Real', text='MonsterReal')


        # # define columns
        # columns = ('Episode_Number', 'Season', 'Monster_Real')

        # tree = ttk.Treeview(self, columns=columns, show='headings')

        # tree.heading('Episode_Number', text='Episode Number')
        # tree.heading('Season', text='Season')
        # tree.heading('Monster_Real', text='MonsterReal')

        # contacts = []
        # for n in range(1, 100):
        #     contacts.append((f'Episode {n}', f'1', f'True'))

        # # add data to the treeview
        # for contact in contacts:
        #     tree.insert('', tk.END, values=contact)


        # def item_selected(event):
        #     for selected_item in tree.selection():
        #         item = tree.item(selected_item)
        #         record = item['values']
        #         # show a message
        #         showinfo(title='Information', message=','.join(record))


        # tree.bind('<<TreeviewSelect>>', item_selected)

        # tree.grid(row=4, column=1, sticky='nsew')

        # # add a scrollbar
        # scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        # tree.configure(yscroll=scrollbar.set)
        # scrollbar.grid(row=4, column=2, sticky='ns')


# root = tk.Tk()
# root.title('Scooby-Doo Database')

# window_width = 1000
# window_height = 500

# # get the screen dimension
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # find the center point
# center_x = int(screen_width/2 - window_width / 2)
# center_y = int(screen_height/2 - window_height / 2)

# # set the position of the window to the center of the screen
# root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=3)
# root.columnconfigure(2, weight=1)
# root.columnconfigure(3, weight=1)

# label = ttk.Label(root)
# label.config(text='Hi, there')
# label.pack()

# # Test code
# label = ttk.Label(root)
# label.config(text='Episode Filters')
# label.pack()




# BUTTON CODE?
    # def button_clicked():
    #     print('Button clicked')

    # button = ttk.Button(root, text='Click Me', command=button_clicked)
    # button.pack()
    

if __name__ == "__main__":
    app = App()
    app.mainloop()
