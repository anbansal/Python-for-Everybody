import sqlite3


class sqlDatabase:
    con = None
    cur = None
    name = ''

    def __init__(self, nam='Tracks'):
        self.name = nam
        self.con = sqlite3.connect('music.sqlite')
        self.cur = self.con.cursor()
        cmd = 'DROP TABLE IF EXISTS '+self.name
        self.cur.execute(cmd)
        cmd = 'CREATE TABLE '+self.name+' (title TEXT, plays INTEGER)'
        self.cur.execute(cmd)

    def __del__(self):
        self.cur.close()

    def insertIntoDB(self, string):
        self.cur.execute(string)
        self.con.commit()

    def showDB(self, string):
        print("Tracks: ")
        self.cur.execute(string)
        for row in self.cur:
            print(row)

    def delDB(self, string='DELETE FROM Tracks'):
        self.cur.execute(string)
        self.con.commit()
