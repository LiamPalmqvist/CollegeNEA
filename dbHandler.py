import sqlite3

con = sqlite3.connect("test.db")

cur = con.cursor()

cur.execute('DROP TABLE tblJudoka')
cur.execute('DROP TABLE tblAttendance')

cur.execute('''CREATE TABLE IF NOT EXISTS tblJudoka (
memberID INT PRIMARY KEY NOT NULL, 
name VARCHAR (30) NOT NULL, 
address VARCHAR (50) NOT NULL, 
pgName VARCHAR (30), 
memPhoneNum VARCHAR (10) UNIQUE, 
pgPhoneNum1 VARCHAR (10) UNIQUE, 
pgPhoneNum2 VARCHAR (10) UNIQUE, 
licNum VARCHAR (30) UNIQUE NOT NULL, 
expDate DATETIME NOT NULL, 
grade VARCHAR (20) NOT NULL, 
lastGradDate DATETIME NOT NULL, 
directDebActive BOOLEAN NOT NULL DEFAULT (0), 
emContact1Name VARCHAR (30), 
emContact1Rel VARCHAR (30), 
emContact1Num VARCHAR (10), 
emContact1LandLine VARCHAR (20), 
emContact2Name VARCHAR (30), 
emContact2Rel VARCHAR (30), 
emCOntact2Num VARCHAR (10), 
emCOntact2LandLine VARCHAR (20)
);''')

cur.execute('''CREATE TABLE IF NOT EXISTS tblAttendance(
sessionID int not null PRIMARY key,
sessionDate date not null,
member int,
FOREIGN key(member) REFERENCES tblJudoka(memberid)
);''')

con.commit()

cur.execute('''insert into tblJudoka(memberid, name, address, memphonenum, licnum, expdate, grade, lastgraddate, directdebactive)
values(0, 'Liam', 'Little Foxes, Hermitage Lane, RH19 4DR', 07949296074, 328947239, 2021-12-24, '2nd Kyu', 2021-06-27, 1);''')

cur.execute('''insert into tblAttendance (sessionid, sessiondate, member)
values (0, 2021-05-13, 0);''')

con.commit()
