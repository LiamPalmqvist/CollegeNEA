import tkinter as tk
from tkinter.font import *
from tkinter.ttk import *
import dbHandler
import loggedIn
from custom import EntryWithPlaceholder, EntryWithPassword


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        super().iconbitmap("assets/logographic.ico")
        window = Frame(self)

        window.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # Defining the config within the master window
        tk.Tk.title(self, "JDS")
        tk.Tk.option_add(self, '*Font', 'helvetica 20')
        self.resizable(False, False)
        tk.Tk.geometry(self, '350x600+600+300')
        # End of defining the config within the master window

        self.frames = {}

        for i in (LoginWindow, SignupWindow, ForgotPassword):
            frame = i(window, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame(LoginWindow)

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class LoginWindow(Frame):

    ### Checking if login matches any logins in the sqlite db
    def loginAttempt(self):
        user = dbHandler.getSingleUser(self.username.get())  # Gets user from db
        print(user)

        try:  # Tries to log in by matching username and password
            if user[2] == self.password.get():
                loggedIn.run(self.username.get())

            else:  # If no error and password doesn't match
                self.wrongAnswer.config(fg='#E94949')

        except TypeError:  # Waits for error from a blank login
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

        image = tk.PhotoImage(file='assets/keisenJudoClub (Custom).png')
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

        self.password = EntryWithPassword(frame1, 'password')
        self.password.grid(row=2, column=1)

        # This is the forgotten password button. It doesn't use a button but instead uses a Label which can be clicked
        forgotPassword = tk.Label(frame1)

        # Custom font for the label
        font = Font(forgotPassword, forgotPassword.cget('font'))
        font.config(underline=True, family="helvetica", size=12)

        forgotPassword.config(text="Forgot password?", fg='blue', font=font, pady=10)
        forgotPassword.grid(row=3, column=1)
        forgotPassword.bind("<Button-1>", lambda e: [print("I was clicked"), controller.showFrame(ForgotPassword)])

        # Logging in
        login = tk.Button(frame)
        login.config(text="ENTER", command=lambda: self.loginAttempt(), width=18, bg='#E94949', fg='#EEEDEF',
                     font='helvetica 20', relief=tk.FLAT)
        login.pack()

        placeholder = tk.Label(frame)
        placeholder.config(text="placeholder", fg='#EEEDEF', font='helvetica 10')
        placeholder.pack()

        # Switching Button
        switchButton = tk.Button(frame)
        switchButton.config(text="SIGN UP", command=lambda: controller.showFrame(SignupWindow), width=18, bg='#E94949',
                            fg='#EEEDEF', font='helvetica 20', relief=tk.FLAT)
        switchButton.pack()

        self.wrongAnswer = tk.Label(frame)
        self.wrongAnswer.config(text='''The username or password you 
entered was incorrect''', fg='#EEEDEF', pady=10, font=('lmpRegular', 14))
        self.wrongAnswer.pack()

        spacer1 = Frame(frame)
        spacer1.pack(expand=tk.TRUE)


class SignupWindow(Frame):

    def signUp(self):

        if self.username.get() == 'username' or self.password.get() == 'password' or self.email.get() == 'e-mail':

            self.wrongAnswer.config(fg='#E94949', text='''Please enter all
of the required information''')

        else:
            match = dbHandler.logIn(self.username.get(), self.email.get(), False)
            if not match:

                dbHandler.signUp(self.username.get(), self.email.get(), self.password.get())
                self.wrongAnswer.config(fg='#77DD77', text='''Success!
Please sign in!''')
            else:

                self.wrongAnswer.config(fg='#E94949', text='''The username or e-mail you 
entered has already been taken''')
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

        image = tk.PhotoImage(file='assets/keisenJudoClub (Custom).png')
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

        self.password = EntryWithPassword(frame1, 'password')
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
        switchButton.config(text="LOG IN", command=lambda: controller.showFrame(LoginWindow), width=18, bg='#E94949',
                            fg='#EEEDEF', font='helvetica 20', relief=tk.FLAT)
        switchButton.pack()

        self.wrongAnswer = tk.Label(frame)
        self.wrongAnswer.config(text='''The username or password you 
entered has already been taken''', fg='#EEEDEF', pady=10, font=('lmpRegular', 14))
        self.wrongAnswer.pack()

        spacer1 = Frame(frame)
        spacer1.pack(expand=tk.TRUE)


# This class allows me to switch to a password forgot section where the
# user will be able to reset their password to a string generated by an algorithm
class ForgotPassword(Frame):

    def resetPassword(self):
        if dbHandler.sendMail(self.email.get()):
            self.confirm.config(fg='#77DD77')
        else:
            self.confirm.config(fg='#E94949', text="""Hmm, it looks like we don't have
this email address in our database,
please try again or sign up.""")

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

        image = tk.PhotoImage(file='assets/keisenJudoClub (Custom).png')
        lblIcon = tk.Label(topFrame, bg='#E0D8DA', relief='flat')
        lblIcon.config(image=image)
        lblIcon.image = image
        lblIcon.pack(side=tk.LEFT, padx=0, pady=10)
        ### Finishing the logo and text

        image = tk.PhotoImage(file='assets/forgot.png')
        lblIcon = tk.Label(frame, bg='#EEEDEF', relief='flat')
        lblIcon.config(image=image)
        lblIcon.image = image
        lblIcon.pack(side=tk.TOP, pady=10)

        # Label for information to the client
        infText = tk.Label(frame)
        infText.config(text='''Please enter your email and
hit "SUBMIT" to reset your
password''', font='helvetica 14')
        infText.pack()

        # Entering your account stuff
        frame1 = Frame(frame)
        frame1.pack(expand=tk.TRUE, pady=10)

        self.email = EntryWithPlaceholder(frame1, 'email')
        self.email.pack()

        placeholder = tk.Label(frame)
        placeholder.config(text="placeholder", fg='#EEEDEF', font='helvetica 3')
        placeholder.pack()

        submitButton = tk.Button(frame)
        submitButton.config(text="SUBMIT", command=lambda: self.resetPassword(), width=18, bg='#E94949',
                            fg='#EEEDEF', font='helvetica 20', relief=tk.FLAT)
        submitButton.pack()

        placeholder = tk.Label(frame)
        placeholder.config(text="placeholder", fg='#EEEDEF', font='helvetica 10')
        placeholder.pack()

        back = tk.Button(frame)
        back.config(text="BACK", command=lambda: controller.showFrame(LoginWindow), width=18, bg='#E94949',
                            fg='#EEEDEF', font='helvetica 20', relief=tk.FLAT)
        back.pack()

        self.confirm = tk.Label(frame)
        self.confirm.config(text='''Your password has been
reset. An email will be sent to you
shortly containing a temporary
password.''', fg='#EEEDEF', pady=30, font=('lmpRegular', 14))
        self.confirm.pack()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
