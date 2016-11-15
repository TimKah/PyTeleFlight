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
    def executeSQL(sql):
        try:
            self.cur.execute("""{0}""".format(sql))
            rows = cur.fetchall()
        except:
            print("I can't {0}".format(sql))