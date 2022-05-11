import tkinter as tk
from tkinter import ttk, StringVar, OptionMenu
from tkinter.messagebox import showinfo

from GUI.Tree import Tree
import pandas as pd
from GUI.Menu import Menu
from GUI.Filters import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x700")
        self.title('Scooby-Doo Database')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=3)
        self.columnconfigure(4, weight=3)
        self.columnconfigure(5, weight=1)
        
        self.rowconfigure(2)

        self.filters()
        self.table(pd.DataFrame())

    
    def filters(self):
        filter = ttk.Label(self, text="Filters")
        filter.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        
        # ROW 1
        
        episode = ttk.Label(self, text="Episode Filters")
        episode.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        
        filter_label = ttk.Label(self, text="Series Name:")
        filter_label.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
        menu = Menu(self, FilterType.SERIES_NAME)
        menu.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Season:")
        series_label.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)
        menu = Menu(self, FilterType.SEASON)
        menu.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)
        
        # ROW 2
        
        episode = ttk.Label(self, text="Monster Filters")
        episode.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)
        
        filter_label = ttk.Label(self, text="Monster Name:")
        filter_label.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
        menu = Menu(self, FilterType.MONSTER_NAME)
        menu.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Monster Gender:")
        series_label.grid(column=2, row=4, sticky=tk.W, padx=5, pady=5)
        menu = Menu(self, FilterType.MONSTER_GENDER)
        menu.grid(column=2, row=5, sticky=tk.W, padx=5, pady=5)
        
        series_label = ttk.Label(self, text="Monster Species:")
        series_label.grid(column=3, row=4, sticky=tk.W, padx=5, pady=5)
        menu = Menu(self, FilterType.MONSTER_SPECIES)
        menu.grid(column=3, row=5, sticky=tk.W, padx=5, pady=5)
        
        # ROW 3
        
        episode = ttk.Label(self, text="Culprit Filters")
        episode.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)
        
        filter_label = ttk.Label(self, text="Culprit Name:")
        filter_label.grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)
        menu = Menu(self, FilterType.CULPRIT_NAME)
        menu.grid(column=1, row=8, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Culprit Gender:")
        series_label.grid(column=2, row=7, sticky=tk.W, padx=5, pady=5)
        menu = Menu(self, FilterType.CULPRIT_GENDER)
        menu.grid(column=2, row=8, sticky=tk.W, padx=5, pady=5)
        
        # ROW 4
        
        episode = ttk.Label(self, text="Voice Actor Filters")
        episode.grid(column=1, row=9, sticky=tk.W, padx=5, pady=5)
        
        filter_label = ttk.Label(self, text="Actor Name:")
        filter_label.grid(column=1, row=10, sticky=tk.W, padx=5, pady=5)
        menu = Menu(self, FilterType.ACTOR_NAME)
        menu.grid(column=1, row=11, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Character Name:")
        series_label.grid(column=2, row=10, sticky=tk.W, padx=5, pady=5)
        menu = Menu(self, FilterType.CULPRIT_NAME)
        menu.grid(column=2, row=11, sticky=tk.W, padx=5, pady=5)
        
        # ROW 4
        
        episode = ttk.Label(self, text="Setting Filters")
        episode.grid(column=1, row=12, sticky=tk.W, padx=5, pady=5)
        
        filter_label = ttk.Label(self, text="Terrain:")
        filter_label.grid(column=1, row=13, sticky=tk.W, padx=5, pady=5)
        menu = Menu(self, FilterType.SETTING_TERRAIN)
        menu.grid(column=1, row=14, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Place:")
        series_label.grid(column=2, row=13, sticky=tk.W, padx=5, pady=5)
        menu = Menu(self, FilterType.SETTING_PLACE)
        menu.grid(column=2, row=14, sticky=tk.W, padx=5, pady=5)
        
        # series_label = ttk.Label(self, text="Run Time:")
        # series_label.grid(column=3, row=1, sticky=tk.W, padx=5, pady=5)
        # menu = Menu(self, FilterType.)
        # menu.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
        
    

    # def options(self):
        # o.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        
        
    def table(self, df):

        self.tree = Tree(self, df)
        self.tree.grid(row=15, column=1, columnspan=4, sticky=tk.NSEW)
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=15, column=5, sticky='ns')


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
