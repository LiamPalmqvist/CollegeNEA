import tkinter as tk
from tkinter.ttk import *
import sqlite3
from PIL import ImageTk, Image
import dbHandler
import loggedIn


class MainWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        window = Frame(self)

        window.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # Defining the config within the master window
        tk.Tk.title(self, "Judo Databasing System")
        tk.Tk.option_add(self, '*Font', 'helvetica 14')
        tk.Tk.geometry(self, '350x400+600+300')
        # End of defining the config within the master window

        self.frames = {}

        for i in (LoginWindow, SignupWindow):
            frame = i(window, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginWindow)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class LoginWindow(Frame):

    def loginAttempt(self):
        match = dbHandler.logIn(self.username.get(), self.password.get())
        print(match)
        if match:
            loggedIn.run(self.username.get())

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        frame = tk.Frame(self, bg='#EEEDEF')
        frame.pack(expand=tk.TRUE, fill=tk.BOTH)

        topFrame = tk.Frame(frame, bg='#E0D8DA')
        topFrame.pack(side=tk.TOP, fill=tk.X)

        # Making an image appear
        image = tk.PhotoImage(file='assets/logo desaturated (Custom).png')
        lblIcon = tk.Label(topFrame, bg='#E0D8DA', relief='flat')
        lblIcon.config(image=image)
        lblIcon.image = image
        lblIcon.pack(side=tk.LEFT, padx=10, pady=10)

        image = tk.PhotoImage(file='assets/keisenJudo (Custom).png')
        lblIcon = tk.Label(topFrame, bg='#E0D8DA', relief='flat')
        lblIcon.config(image=image)
        lblIcon.image = image
        lblIcon.pack(side=tk.LEFT, padx=0, pady=10)

        image = tk.PhotoImage(file='assets/login.png')
        lblIcon = tk.Label(frame, bg='#EEEDEF', relief='flat')
        lblIcon.config(image=image)
        lblIcon.image = image
        lblIcon.pack(padx=0, pady=10)

        # Entering your account stuff
        frame1 = Frame(frame)
        frame1.pack(expand=tk.TRUE)

        usernameText = tk.Label(frame1)
        usernameText.config(text="Username:")
        usernameText.grid(row=0, column=0)

        self.username = Entry(frame1)
        self.username.grid(row=0, column=1)

        passwordText = tk.Label(frame1)
        passwordText.config(text="Password:")
        passwordText.grid(row=1, column=0)

        self.password = Entry(frame1, show='•')
        self.password.grid(row=1, column=1)

        # Logging in
        login = Button(frame)
        login.config(text="ENTER", command=lambda: self.loginAttempt())
        login.pack()

        # Switching Button
        switchButton = Button(frame)
        switchButton.config(text="SIGN UP", command=lambda: controller.show_frame(SignupWindow))
        switchButton.pack()

        spacer1 = Frame(frame)
        spacer1.pack(expand=tk.TRUE)


class SignupWindow(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        frame = Frame(self)
        frame.pack(expand=tk.TRUE)

        # Switching Button
        switchButton = Button(frame)
        switchButton.config(text="Back", command=lambda: controller.show_frame(LoginWindow))
        switchButton.grid(row=0, column=0)


if __name__ == "__main__":
    app = MainWindow()
    app.iconbitmap('assets/logographic.ico')
    app.mainloop()
