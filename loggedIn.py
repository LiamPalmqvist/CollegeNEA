import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter.font import *
from PIL import Image, ImageTk

import custom
import dbHandler


def saveImage(username, newUser):
    if newUser:
        filename = 'assets/pfps/default.png'
    else:
        filename = askopenfilename()

    im = Image.open(filename)
    im = im.resize((100, 100), Image.ANTIALIAS)
    im.save('assets/pfps/' + username + '.png', "PNG")


class MainView(tk.Toplevel):

    def __init__(self, username):
        super().__init__()
        self.daemon = True
        window = Frame(self)

        window.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # Defining the config within the master window
        tk.Tk.configure(self, bg="ivory2")
        tk.Tk.title(self, "JDS")
        tk.Tk.option_add(self, '*Font', 'helvetica 14')
        tk.Tk.option_add(self, '*Background', '#E0D8DA')
        tk.Tk.geometry(self, '800x700+600+300')
        # End of defining the config within the master window

        # Setting up notebooks using tkinter.ttk

        tabControl = Notebook(window)
        Notebook(master=None)

        tab1 = Frame(tabControl)
        tabControl.add(tab1, text='Home Page')

        tab2 = Frame(tabControl)
        tabControl.add(tab2, text='Competitions')

        tab3 = tk.Frame(tabControl)
        tabControl.add(tab3, text='Profile')

        user = dbHandler.getSingleUser(username)
        if user[-2] == 1:
            tab4 = Frame(tabControl)
            tabControl.add(tab4, text='Register')
            # Main tab page to fill bg colour
            tab4Fill = tk.Frame(tab4)
            tab4Fill.config(bg='#E0D8DA')
            tab4Fill.pack(expand=1, fill=tk.BOTH)

        tabControl.pack(expand=1, fill=tk.BOTH)

        self.frames = {}

        for i in (JudokaFrame, ProfileFrame):
            frame = i(tab3, self, username=username)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame(ProfileFrame)

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
        self.lblIcon = tk.Label(tab1Frame1, bg='#E0D8DA', relief='flat')
        self.lblIcon.config(image=image)
        self.lblIcon.image = image
        self.lblIcon.pack(side=tk.LEFT, padx=10, pady=10)

        lblWelcome = tk.Label(tab1Frame1)
        lblWelcome.config(text="Welcome, " + username, font='Helvetica 30', bg='#E0D8DA')
        lblWelcome.pack(side=tk.LEFT)

        ### Setting up the Competitions Page

        # Main tab page to fill bg colour
        tab2Fill = tk.Frame(tab2)
        tab2Fill.config(bg='#E0D8DA')
        tab2Fill.pack(expand=1, fill=tk.BOTH)

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class JudokaFrame(Frame):

    def __init__(self, parent, controller, username):
        ### Initialisation script
        userID = dbHandler.getUserId(username)
        Frame.__init__(self, parent)
        frame = tk.Frame(self, bg='#E0D8DA')
        frame.pack(expand=tk.TRUE, fill=tk.BOTH)

        tempFrame = tk.Frame(self, bg='#E0D8DA')
        tempFrame.pack(expand=True, fill=tk.BOTH)
        text = tk.Label(tempFrame)
        text.config(text="PLACEHOLDER", fg='#E0D8DA', bg='#E0D8DA', font='Helvetica 500')
        text.pack()

        judokas = dbHandler.getJudoka(userID)
        print(judokas)
        listLabels = ['Name', 'Address', 'Phone Number', 'Licence number', 'Expiry Date', 'Grade', 'Date of last '
                                                                                                   'grading']

        buttonFrame = tk.Frame(frame)
        buttonFrame.config(height=500)
        buttonFrame.pack(expand=True, side=tk.BOTTOM, fill=tk.BOTH)
        judokaDisp = tk.Frame(frame)
        judokaDisp.pack(expand=True, fill=tk.BOTH)

        for i in range(len(listLabels)):
            label = tk.Label(judokaDisp)
            font = Font(label, label.cget('font'))
            font.config(underline=True)
            label.config(text=listLabels[i], bg='#E0D8DA', justify='center', wraplength=150, font=font)
            label.grid(row=1, column=i)

        for i in range(len(judokas)):
            for f in range(len(judokas[i])-3):
                label = tk.Label(judokaDisp)
                label.config(text=judokas[i][f+1], wraplength=150, justify='center', bg='#E0D8DA')
                label.grid(row=i+2, column=f)
        print(judokas)

        # Switching Button
        switchButton = tk.Button(frame)
        switchButton.config(text="EDIT PROFILE", command=lambda: controller.showFrame(ProfileFrame), width=18,
                            bg='#E94949',
                            fg='#EEEDEF', font='helvetica 20', relief=tk.FLAT)
        switchButton.place(x=30, y=590)


class ProfileFrame(tk.Frame):

    def updateImage(self, username):
        filename = askopenfilename()

        im = Image.open(filename)
        im = im.resize((100, 100), Image.ANTIALIAS)
        im.save('assets/pfps/' + username + '.png', "PNG")
        im = ImageTk.PhotoImage(image=im)

        self.updTxtLbl.config(fg='#E94949')
        print("Changed")

    def updatePassword(self, username):
        if self.pwd.get() == dbHandler.getSingleUser(username)[2]:
            if self.newPwd.get() != self.confPwd.get():

                self.pwdReport.config(text="New passwords do not match", fg='#E94949')
            else:
                self.pwdReport.config(text="Success, password changed!", fg='#77DD77')
        else:
            print(False, "Old password does not match")
            self.pwdReport.config(text="Old password does not match", fg='#E94949')

    ### Initialisation script
    def __init__(self, parent, controller, username):
        Frame.__init__(self, parent)
        frame = tk.Frame(self, bg='#EEEDEF')
        frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        userInfo = dbHandler.getSingleUser(username)

        # Main tab page to fill bg colour
        tab3Fill = tk.Frame(frame)
        tab3Fill.config(bg='#E0D8DA')
        tab3Fill.pack(expand=tk.TRUE, fill=tk.BOTH)

        # Frame 1
        tab3Frame1 = tk.Frame(tab3Fill)
        tab3Frame1.config(bg='#E0D8DA')
        tab3Frame1.pack(expand=1, fill=tk.BOTH)

        lblWelcome = tk.Label(tab3Frame1)
        lblWelcome.config(text="Edit profile", font='Helvetica 30', bg='#E0D8DA')
        lblWelcome.place(x=20, y=20)

        # The profile photo section

        image = tk.PhotoImage(file='assets/pfps/' + userInfo[-1])
        userSettingsIcon = tk.Label(tab3Frame1, bg='#E0D8DA', relief='flat')
        userSettingsIcon.config(image=image)
        userSettingsIcon.image = image
        userSettingsIcon.place(x=58, y=90)

        self.updTxtLbl = tk.Label(tab3Frame1)
        self.updTxtLbl.config(text="Changes will only take effect after application restart", fg='#E0D8DA', bg='#E0D8DA')
        self.updTxtLbl.place(x=20, y=225)

        imageButton = Button(tab3Frame1)
        imageButton.config(text="Upload image", command=lambda: self.updateImage(username))
        imageButton.place(x=68, y=200)

        # The username/password section

        lblUsername = tk.Label(tab3Frame1)
        lblUsername.config(text="Username:", bg='#E0D8DA', relief='flat')
        lblUsername.place(x=200, y=100)

        lblCurUsr = tk.Label(tab3Frame1)
        lblCurUsr.config(text=userInfo[0], bg='#E0D8DA', relief='flat')
        lblCurUsr.place(x=300, y=100)

        lblEmail = tk.Label(tab3Frame1)
        lblEmail.config(text="E-Mail:", bg='#E0D8DA', relief='flat')
        lblEmail.place(x=200, y=140)

        lblCurMail = tk.Label(tab3Frame1)
        lblCurMail.config(text=userInfo[1], bg='#E0D8DA', relief='flat')
        lblCurMail.place(x=300, y=140)

        lblEditPwd = tk.Label(tab3Frame1)
        lblEditPwd.config(text="Edit Password", font='Helvetica 30', bg='#E0D8DA', relief='flat')
        lblEditPwd.place(x=20, y=250)

        self.pwd = custom.EntryWithPassword(tab3Frame1, 'Current Password')
        self.pwd.place(x=30, y=310)

        self.newPwd = custom.EntryWithPassword(tab3Frame1, 'New Password')
        self.newPwd.place(x=30, y=350)

        self.confPwd = custom.EntryWithPassword(tab3Frame1, 'Confirm Password')
        self.confPwd.place(x=30, y=390)

        changePwd = Button(tab3Frame1)
        changePwd.config(text="Change", command=lambda: self.updatePassword(username))
        changePwd.place(x=30, y=440)

        self.pwdReport = tk.Label(tab3Frame1)
        self.pwdReport.config(text='', font='Helvetica 30', bg='#E0D8DA', fg='#E0D8DA')
        self.pwdReport.place(x=30, y=490)

        # Switching Button
        switchButton = tk.Button(frame)
        switchButton.config(text="EDIT JUDOKA", command=lambda: controller.showFrame(JudokaFrame), width=18, bg='#E94949',
                            fg='#EEEDEF', font='helvetica 20', relief=tk.FLAT)
        switchButton.place(x=30, y=590)


def run(username):
    app = MainView(username)
    app.iconbitmap('assets/logographic.ico')
    app.mainloop()


if __name__ == '__main__':
    app = MainView("admin")
    app.iconbitmap('assets/logographic.ico')
    app.mainloop()
