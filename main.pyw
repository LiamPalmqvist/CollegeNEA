import tkinter as tk
from tkinter.ttk import *
import dbHandler
import loggedIn
from custom import EntryWithPlaceholder


class MainWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        window = Frame(self)

        window.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # Defining the config within the master window
        tk.Tk.title(self, "Judo Databasing System")
        tk.Tk.option_add(self, '*Font', 'helvetica 20')
        tk.Tk.geometry(self, '350x550+600+300')
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

    ### Checking if login matches any logins in the sqlite db
    def loginAttempt(self):
        match = dbHandler.logIn(self.username.get(), self.password.get(), True)
        print(match)
        if match:
            loggedIn.run(self.username.get())
        else:
            self.wrongAnswer.config(fg='#E94949')

    ### Initialisation script
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        frame = tk.Frame(self, bg='#EEEDEF')
        frame.pack(expand=tk.TRUE, fill=tk.BOTH)

        ### Setting up the top frame for the logo and the text
        topFrame = tk.Frame(frame, bg='#E0D8DA')
        topFrame.pack(side=tk.TOP, fill=tk.X)

        # Making images appear
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
        ### Finishing the logo and text

        # Added another picture because it was much easier to make it in PhotoShop
        image = tk.PhotoImage(file='assets/login.png')
        lblIcon = tk.Label(frame, bg='#EEEDEF', relief='flat')
        lblIcon.config(image=image)
        lblIcon.image = image
        lblIcon.pack(padx=0, pady=10)

        # Entering your account stuff
        frame1 = Frame(frame)
        frame1.pack(expand=tk.TRUE)

        self.username = EntryWithPlaceholder(frame1, 'username')
        self.username.grid(row=0, column=1)

        placeholder = tk.Label(frame1)
        placeholder.config(text="placeholder", fg='#EEEDEF', font='helvetica 10')
        placeholder.grid(row=1, column=1)

        self.password = EntryWithPlaceholder(frame1, 'password')
        self.password.grid(row=2, column=1)

        # Logging in
        placeholder = tk.Label(frame)
        placeholder.config(text="placeholder", fg='#EEEDEF', font='helvetica 10')
        placeholder.pack()

        login = tk.Button(frame)
        login.config(text="ENTER", command=lambda: self.loginAttempt(), width=18, bg='#E94949', fg='#EEEDEF', font='helvetica 20', relief=tk.FLAT)
        login.pack()

        placeholder = tk.Label(frame)
        placeholder.config(text="placeholder", fg='#EEEDEF', font='helvetica 10')
        placeholder.pack()

        # Switching Button
        switchButton = tk.Button(frame)
        switchButton.config(text="SIGN UP", command=lambda: controller.show_frame(SignupWindow), width=18, bg='#E94949', fg='#EEEDEF', font='helvetica 20', relief=tk.FLAT)
        switchButton.pack()

        self.wrongAnswer = tk.Label(frame)
        self.wrongAnswer.config(text='''The username or password you 
entered was incorrect''', fg='#EEEDEF', pady=10, font=('lmpRegular', 14))
        self.wrongAnswer.pack()

        spacer1 = Frame(frame)
        spacer1.pack(expand=tk.TRUE)


class SignupWindow(Frame):

    def signUp(self):
        match = dbHandler.logIn(self.username.get(), self.email.get(), False)
        if not match:
            dbHandler.signUp(self.username.get(), self.email.get(), self.password.get())

        self.wrongAnswer.config(fg='#E94949')
        print(self.username.get(), self.email.get(), self.password.get())

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

        image = tk.PhotoImage(file='assets/signUp.png')
        lblIcon = tk.Label(frame, bg='#EEEDEF', relief='flat')
        lblIcon.config(image=image)
        lblIcon.image = image
        lblIcon.pack(padx=0, pady=10)

        # Entering your account stuff
        frame1 = Frame(frame)
        frame1.pack(expand=tk.TRUE)

        self.username = EntryWithPlaceholder(frame1, 'username')
        self.username.grid(row=0, column=0)

        self.email = EntryWithPlaceholder(frame1, 'e-mail')
        self.email.grid(row=1, column=0)

        self.password = EntryWithPlaceholder(frame1, 'password')
        self.password.grid(row=2, column=0)

        placeholder = tk.Label(frame)
        placeholder.config(text="placeholder", fg='#EEEDEF', font='helvetica 10')
        placeholder.pack()

        login = tk.Button(frame)
        login.config(text="ENTER", command=lambda: self.signUp(), width=18, bg='#E94949', fg='#EEEDEF',
                     font='helvetica 20', relief=tk.FLAT)
        login.pack()

        placeholder = tk.Label(frame)
        placeholder.config(text="placeholder", fg='#EEEDEF', font='helvetica 10')
        placeholder.pack()

        # Switching Button
        switchButton = tk.Button(frame)
        switchButton.config(text="LOG IN", command=lambda: controller.show_frame(LoginWindow), width=18, bg='#E94949',
                            fg='#EEEDEF', font='helvetica 20', relief=tk.FLAT)
        switchButton.pack()

        self.wrongAnswer = tk.Label(frame)
        self.wrongAnswer.config(text='''The username or password you 
entered was incorrect''', fg='#EEEDEF', pady=10, font=('lmpRegular', 14))
        self.wrongAnswer.pack()

        spacer1 = Frame(frame)
        spacer1.pack(expand=tk.TRUE)


if __name__ == "__main__":
    app = MainWindow()
    app.iconbitmap('assets/logographic.ico')
    app.mainloop()
