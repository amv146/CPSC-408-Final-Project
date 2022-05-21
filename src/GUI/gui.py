import tkinter as tk
from tkinter import ttk, StringVar, OptionMenu
from tkinter.messagebox import showinfo

from src.GUI.Tree import Tree
from src.GUI.Menu import Menu
from src.GUI.Filters import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1430x700")
        self.title('Scooby-Doo Database')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=2)
        self.columnconfigure(4, weight=2)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=1) 
        
        ## set minimal size for row 9 and column 9
        self.rowconfigure(0, minsize=30)
        self.rowconfigure(16, minsize=30)

        self.columnconfigure(0, minsize=20)
        self.columnconfigure(6, minsize=20)
        

        self.rowconfigure(2)

        self.filters()
        # self.table(pd.DataFrame())
        # self.options()


    def filters(self):
        filter = ttk.Label(self, text="Filters")
        filter.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        
        self.reset_button = ttk.Button(
            self,
            text='Reset Filters',
            
        )
        self.reset_button.grid(column=3, row=14, sticky=tk.W, padx=5, pady=5)

        # ROW 1

        # episode = ttk.Label(self, text="Episode Filters")
        # episode.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

        filter_label = ttk.Label(self, text="Series Name:")
        filter_label.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
        series_menu = Menu(self, FilterType.SERIES_NAME)
        series_menu.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Season:")
        series_label.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)
        season_menu = Menu(self, FilterType.SEASON)
        season_menu.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)

        # ROW 2

        # episode = ttk.Label(self, text="Monster Filters")
        # episode.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

        filter_label = ttk.Label(self, text="Monster Name:")
        filter_label.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
        monster_name_menu = Menu(self, FilterType.MONSTER_NAME)
        monster_name_menu.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Monster Gender:")
        series_label.grid(column=2, row=4, sticky=tk.W, padx=5, pady=5)
        monster_gender_menu = Menu(self, FilterType.MONSTER_GENDER)
        monster_gender_menu.grid(column=2, row=5, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Monster Species:")
        series_label.grid(column=3, row=4, sticky=tk.W, padx=5, pady=5)
        monster_species_menu = Menu(self, FilterType.MONSTER_SPECIES)
        monster_species_menu.grid(column=3, row=5, sticky=tk.W, padx=5, pady=5)

        # ROW 3

        # episode = ttk.Label(self, text="Culprit Filters")
        # episode.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)

        filter_label = ttk.Label(self, text="Culprit Name:")
        filter_label.grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)
        culprit_name_menu = Menu(self, FilterType.CULPRIT_NAME)
        culprit_name_menu.grid(column=1, row=8, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Culprit Gender:")
        series_label.grid(column=2, row=7, sticky=tk.W, padx=5, pady=5)
        culprit_gender_menu = Menu(self, FilterType.CULPRIT_GENDER)
        culprit_gender_menu.grid(column=2, row=8, sticky=tk.W, padx=5, pady=5)

        # ROW 4

        # episode = ttk.Label(self, text="Voice Actor Filters")
        # episode.grid(column=1, row=9, sticky=tk.W, padx=5, pady=5)

        filter_label = ttk.Label(self, text="Actor Name:")
        filter_label.grid(column=1, row=10, sticky=tk.W, padx=5, pady=5)
        actor_menu = Menu(self, FilterType.ACTOR_NAME)
        actor_menu.grid(column=1, row=11, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Character Name:")
        series_label.grid(column=2, row=10, sticky=tk.W, padx=5, pady=5)
        character_menu = Menu(self, FilterType.CHARACTER_NAME)
        character_menu.grid(column=2, row=11, sticky=tk.W, padx=5, pady=5)

        # ROW 4

        # episode = ttk.Label(self, text="Setting Filters")
        # episode.grid(column=1, row=12, sticky=tk.W, padx=5, pady=5)

        filter_label = ttk.Label(self, text="Terrain:")
        filter_label.grid(column=1, row=13, sticky=tk.W, padx=5, pady=5)
        setting_terrain_menu = Menu(self, FilterType.SETTING_TERRAIN)
        setting_terrain_menu.grid(column=1, row=14, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Place:")
        series_label.grid(column=2, row=13, sticky=tk.W, padx=5, pady=5)
        setting_place_menu = Menu(self, FilterType.SETTING_PLACE)
        setting_place_menu.grid(column=2, row=14, sticky=tk.W, padx=5, pady=5)

        # series_label = ttk.Label(self, text="Run Time:")
        # series_label.grid(column=3, row=1, sticky=tk.W, padx=5, pady=5)
        # menu = Menu(self, FilterType.)
        # menu.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
        self.menus = [series_menu, season_menu, monster_name_menu, monster_gender_menu, monster_species_menu, culprit_name_menu, culprit_gender_menu, actor_menu, character_menu, setting_place_menu, setting_terrain_menu]


    # def options(self):
        # o.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)



    def table(self, df, cols):

        self.tree = Tree(self, df, cols)
        self.tree.grid(row=15, column=1, columnspan=5, sticky=tk.NSEW)
        # scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        # self.tree.configure(yscroll=scrollbar.set)
        # scrollbar.grid(row=15, column=5, sticky='ns')


        return self.tree

    def item_selected(self, event):
        for selected_item in tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))
            o = Menu(self, FilterType.ACTOR_NAME)

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
