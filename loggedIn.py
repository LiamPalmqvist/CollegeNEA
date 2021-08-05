import tkinter as tk
from tkinter.ttk import *


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

        if username == 'admin':
            tab2 = Frame(tabControl)
            tabControl.add(tab2, text='Register')

        tab3 = Frame(tabControl)
        tabControl.add(tab3, text='Competitions')

        tabControl.pack(expand=1, fill=tk.BOTH)

        getText = Label(tab1)
        getText.config(text=username)
        getText.pack()


def run(username):
    loginSuccess = MainView(username)
    loginSuccess.iconbitmap('assets/logographic.ico')
    loginSuccess.mainloop()


if __name__ == '__main__':
    loginSuccess = MainView("LiamPalmqvist")
    loginSuccess.mainloop()
