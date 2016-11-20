import psycopg2

class DBManager:
    global conn
    global cur

    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname=Project user=postgres password=0000")
            print("Connection established")
            self.cur = self.conn.cursor()
        except:
            print("I am unable to connect to the database")
            print(psycopg2.Error)
    def executeSQL(self, sql):
        print("Trying {0}".format(sql))
        try:
            self.cur.execute("""{0}""".format(sql))
            rows = self.cur.fetchall()
            print("Made {0}".format(sql))
            return rows
        except psycopg2.Error as e:
            print("I can't {0}".format(sql))
            print(e)
    def sendSQL(self,sql):
        print("Trying {0}".format(sql))
        try:
            self.cur.execute("""{0}""".format(sql))
            self.conn.commit()
            print("Made {0}".format(sql))
        except psycopg2.Error as e:
            print("I can't {0}".format(sql))
            print(e)