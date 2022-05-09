import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__(self)

        self.geometry("1000x500")
        self.title('Scooby-Doo Database')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        self.selection()
        self.table()
    
    def selection(self):
        filter_label = ttk.Label(self, text="Filters")
        filter_label.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        series_label = ttk.Label(self, text="Series Name:")
        series_label.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
    
    def table(self):

        columns = ('first_name', 'last_name', 'email')
        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')

        tree.bind('<<TreeviewSelect>>', self.item_selected)
        tree.grid(row=3, column=1, sticky=tk.NSEW)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=3, column=2, sticky='ns')

        # generate sample data
        contacts = []
        for n in range(1, 100):
            contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview
        for contact in contacts:
            tree.insert('', tk.END, values=contact)

        return tree

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))

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
