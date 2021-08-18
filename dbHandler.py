import sqlite3

import loggedIn

db = 'databaseJudoka.db'


### Setting up the databases on first boot
def main():
    con = sqlite3.connect(db)

    cur = con.cursor()

    cur.execute('DROP TABLE IF EXISTS tblJudoka')
    cur.execute('DROP TABLE IF EXISTS tblAttendance')
    cur.execute('DROP TABLE IF EXISTS tblMember')
    cur.execute('DROP TABLE IF EXISTS tblComp')

    cur.execute('''CREATE TABLE IF NOT EXISTS tblJudoka (
    memberID           INTEGER      PRIMARY KEY
                                    UNIQUE
                                    NOT NULL,
    name               VARCHAR (30) NOT NULL,
    address            VARCHAR (50) NOT NULL,
    pgName             VARCHAR (30),
    memPhoneNum        VARCHAR (10) UNIQUE,
    pgPhoneNum1        VARCHAR (10) UNIQUE,
    pgPhoneNum2        VARCHAR (10) UNIQUE,
    licNum             VARCHAR (30) UNIQUE
                                    NOT NULL,
    expDate            DATE         CONSTRAINT [dd-MM-yy] NOT NULL,
    grade              VARCHAR (20) NOT NULL,
    lastGradDate       DATE         CONSTRAINT [dd-MM-yy] NOT NULL,
    directDebActive    BOOLEAN      NOT NULL
                                    DEFAULT (0),
    emContact1Name     VARCHAR (30),
    emContact1Rel      VARCHAR (30),
    emContact1Num      VARCHAR (10),
    emContact1LandLine VARCHAR (20),
    emContact2Name     VARCHAR (30),
    emContact2Rel      VARCHAR (30),
    emCOntact2Num      VARCHAR (10),
    emCOntact2LandLine VARCHAR (20),
    belongsTo          INT,
    FOREIGN KEY (
        belongsTo
    )
    REFERENCES tblMember (memberid)
);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS tblAttendance (
    sessionID   INTEGER NOT NULL
                        PRIMARY KEY
                        UNIQUE,
    sessionDate DATE    NOT NULL,
    member      INT,
    FOREIGN KEY (
        member
    )
    REFERENCES tblJudoka (memberid) 
);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS tblMember (
    memberID      INTEGER       NOT NULL
                                PRIMARY KEY
                                UNIQUE,
    username      VARCHAR (20),
    email         VARCHAR (30),
    password      VARCHAR (20),
    isAdmin       INTEGER       NOT NULL,
    profilePhoto  VARCHAR (20)
);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS tblComp (
    compID        INTEGER       NOT NULL
                                PRIMARY KEY AUTOINCREMENT
                                UNIQUE,
    compDate      DATE          NOT NULL,
    listOfJudokas VARCHAR (255) 
);
''')

    con.commit()

    cur.execute('''insert into tblJudoka(memberID, name, address, memphonenum, licnum, expdate, grade, lastgraddate, directdebactive, belongsTo)
    values  (0, 'Liam', 'Little Foxes, Hermitage Lane, RH19 4DR', 07949296074, 328947239, '2021-12-24', '3rd Kyu', '2021-06-27', 1, 0);''')

    cur.execute('''insert into tblAttendance (sessionid, sessiondate, member)
    values  (0, '2021-05-13', 0);''')

    cur.execute('''insert into tblMember(memberID, username, email, password, isAdmin, profilePhoto)
    values  (0, 'LiamPalmqvist', 'liam.palmqvist@icloud.com', 'password', 1, 'LiamPalmqvist.png'),
            (1, 'admin', 'admin@admin.com', 'password', 1, 'admin.png'),
            (2, 'nonAdmin', 'nonadmin@admin.com', 'password', 0, 'nonAdmin.png');''')
    con.commit()


### Getting the users and outputting a list
def getUsers() -> list:
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('SELECT username, email, password, memberID, isAdmin, profilePhoto FROM tblMember')
    users = cur.fetchall()

    return users


### Getting a single user and outputting that user's data as a list
def getSingleUser(username) -> list:
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(
        "SELECT username, email, password, memberID, isAdmin, profilePhoto FROM tblMember WHERE username = '{}'".format(username))
    user = cur.fetchone()

    return user


### Setting checks to make sure username and password are or aren't taken

# Logging in with a username and password
def logIn(username, other, login) -> bool:
    if (username, other) == ('username', 'password'):
        return True

    users = getUsers()

    if login:
        for i in users:
            if (username, other) == (i[0], i[2]):
                return True
        return False

    # Signing up with username, password and e-mail
    else:
        for i in users:
            if username == i[0] or other == i[1]:
                return True
        return False


### Signing up
def signUp(username, email, password):
    users = getUsers()
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('''insert into tblMember(memberID, username, email, password, isAdmin, profilePhoto)
            values('{}', '{}', '{}', '{}', 0, '{}');'''.format((users[-1][-3] + 1), username, email, password, username+'.png'))
    # This formats the string using the parameters specified
    con.commit()
    loggedIn.saveImage(username, True)


# Running if __name__ == __main__
if __name__ == '__main__':
    main()
