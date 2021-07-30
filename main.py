import dbHandler
from tkinter import *
from tkinter.ttk import *
import sqlite3


class MainView(Tk):

    def __init__(self):
        Tk.__init__(self)
        window = Frame(self)

        window.pack(side=TOP, fill=BOTH, expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # Defining the config within the master window
        Tk.configure(self, bg="ivory2")
        Tk.title(self, "Judo Databasing System")
        Tk.option_add(self, '*Font', 'helvetica 14')
        Tk.option_add(self, '*Background', 'ivory2')
        Tk.geometry(self, '800x700+600+300')
        # End of defining the config within the master window


if __name__ == "__main__":
    app = MainView()
    app.mainloop()
