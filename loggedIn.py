import tkinter as tk
from tkinter.ttk import *
import dbHandler
import custom


class MainView(tk.Toplevel):

    def __init__(self, username):
        super().__init__()
        window = Frame(self)

        window.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # Defining the config within the master window
        tk.Tk.configure(self, bg="ivory2")
        tk.Tk.title(self, "JDS")
        tk.Tk.option_add(self, '*Font', 'helvetica 14')
        tk.Tk.option_add(self, '*Background', 'ivory2')
        tk.Tk.geometry(self, '800x700+600+300')
        # End of defining the config within the master window

        # Setting up notebooks using tkinter.ttk

        tabControl = Notebook(window)
        Notebook(master=None)

        tab1 = Frame(tabControl)
        tabControl.add(tab1, text='Home Page')

        tab2 = Frame(tabControl)
        tabControl.add(tab2, text='Competitions')

        tab3 = Frame(tabControl)
        tabControl.add(tab3, text='Profile')

        user = dbHandler.getSingleUser(username)
        if user[-2] == 1:
            tab4 = Frame(tabControl)
            tabControl.add(tab4, text='Register')

        tabControl.pack(expand=1, fill=tk.BOTH)

        ### Setting up the Home Page

        # Main tab page to fill bg colour
        tab1Fill = tk.Frame(tab1)
        tab1Fill.config(bg='#E0D8DA')
        tab1Fill.pack(expand=1, fill=tk.BOTH)

        # Frame 1
        tab1Frame1 = tk.Frame(tab1Fill)
        tab1Frame1.config(bg='#E0D8DA')
        tab1Frame1.pack(expand=1, fill=tk.X, anchor=tk.N)

        image = tk.PhotoImage(file='assets/pfps/' + user[-1])
        lblIcon = tk.Label(tab1Frame1, bg='#E0D8DA', relief='flat')
        lblIcon.config(image=image)
        lblIcon.image = image
        lblIcon.pack(side=tk.LEFT, padx=10, pady=10)

        lblWelcome = tk.Label(tab1Frame1)
        lblWelcome.config(text="Welcome, "+username, font='Helvetica 30', bg='#E0D8DA')
        lblWelcome.pack(side=tk.LEFT)

        ### Setting up the Competitions Page

        # Main tab page to fill bg colour
        tab2Fill = tk.Frame(tab2)
        tab2Fill.config(bg='#E0D8DA')
        tab2Fill.pack(expand=1, fill=tk.BOTH)

        ### Setting up the Profile Page

        # Main tab page to fill bg colour
        tab3Fill = tk.Frame(tab3)
        tab3Fill.config(bg='#E0D8DA')
        tab3Fill.pack(expand=1, fill=tk.BOTH)

        # Frame 1
        tab3Frame1 = tk.Frame(tab3Fill)
        tab3Frame1.config(bg='#E0D8DA')
        tab3Frame1.pack(expand=1, fill=tk.X, anchor=tk.N)

        lblWelcome = tk.Label(tab3Frame1)
        lblWelcome.config(text="Edit profile", font='Helvetica 30', bg='#E0D8DA')
        lblWelcome.pack(side=tk.LEFT)

        # Frame 2
        tab3Frame2 = tk.Frame(tab3Fill)
        tab3Frame2.config(bg='#E0D8DA')
        tab3Frame2.pack(expand=1, fill=tk.X, anchor=tk.N)

        image = tk.PhotoImage(file='assets/pfps/' + user[-1])
        lblIcon = tk.Label(tab3Frame2, bg='#E0D8DA', relief='flat')
        lblIcon.config(image=image)
        lblIcon.image = image
        lblIcon.pack(side=tk.LEFT, padx=10, pady=10)

        ### Setting up the Register Page

        # Main tab page to fill bg colour
        tab4Fill = tk.Frame(tab4)
        tab4Fill.config(bg='#E0D8DA')
        tab4Fill.pack(expand=1, fill=tk.BOTH)


def run(username):
    app = MainView(username)
    app.iconbitmap('assets/logographic.ico')
    app.mainloop()


if __name__ == '__main__':
    app = MainView("admin")
    app.iconbitmap('assets/logographic.ico')
    app.mainloop()
