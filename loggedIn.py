import tkinter as tk
from tkinter.ttk import *

import dbHandler


class MainView(tk.Tk):

    def __init__(self, username):
        tk.Tk.__init__(self)
        window = Frame(self)

        window.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # Defining the config within the master window
        tk.Tk.configure(self, bg="ivory2")
        tk.Tk.title(self, "Judo Databasing System")
        tk.Tk.option_add(self, '*Font', 'helvetica 14')
        tk.Tk.option_add(self, '*Background', 'ivory2')
        tk.Tk.geometry(self, '800x700+600+300')
        # End of defining the config within the master window

        # Setting up notebooks using tkinter.ttk

        tabControl = Notebook(window)
        Notebook(master=None)

        tab1 = Frame(tabControl)
        tabControl.add(tab1, text='Main Page')

        tab2 = Frame(tabControl)
        tabControl.add(tab2, text='Competitions')

        user = dbHandler.getSingleUser(username)
        if user[-1] == 1:
            tab3 = Frame(tabControl)
            tabControl.add(tab3, text='Register')

        tab4 = Frame(tabControl)
        tabControl.add(tab4, text='Profile')
        tabControl.config()

        tabControl.pack(expand=1, fill=tk.BOTH)

        getText = Label(tab1)
        getText.config(text=username)
        getText.pack()


def run(username):
    app = MainView(username)
    app.iconbitmap('assets/logographic.ico')
    app.mainloop()


if __name__ == '__main__':
    app = MainView("admin")
    app.mainloop()
