import psycopg2

class DBManager:
    global conn
    global cur

    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname=Project user=postgres password=0000")
            print("Connection with database established")
            self.cur = self.conn.cursor()
        except:
            print("Unable to connect to the database")
            print(psycopg2.Error)
    def executeSQL(self, sql):
        print("Trying {0}".format(sql))
        try:
            self.cur.execute("""{0}""".format(sql))
            rows = self.cur.fetchall()
            print("SQL fetched all")
            return rows
        except psycopg2.Error as e:
            print("Can't execute SQL")
            print(e)
    def sendSQL(self,sql):
        print("Trying {0}".format(sql))
        try:
            self.cur.execute("""{0}""".format(sql))
            self.conn.commit()
            print("SQL commited")
        except psycopg2.Error as e:
            print("Can't send SQL")
            print(e)