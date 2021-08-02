from tkinter import *
from tkinter.ttk import *
import main
import sys


class MainView(Tk):

    def __init__(self, username):
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

        # Setting up notebooks using tkinter.ttk

        tabControl = Notebook(window)
        Notebook(master=None)

        tab1 = Frame(tabControl)
        tabControl.add(tab1, text='Main Page')

        tab2 = Frame(tabControl)
        tabControl.add(tab2, text='Register')

        tab3 = Frame(tabControl)
        tabControl.add(tab3, text='Competitions')

        tabControl.pack(expand=1, fill=BOTH)

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
