import psycopg2

class DBManager:
    def __init__(self, name):
        try:
            self.conn = psycopg2.connect("dbname=Project user=postgres password=0000")
            print("Connection established")
            self.cur = self.conn.cursor()
            
            try:
                self.cur.execute("""SELECT * from {0}""".format("users"))
            except:
                print("I can't SELECT from users")

            rows = self.cur.fetchall()
            print("We have {0} rows".format(len(rows)))
            
            print("{0} - {1}".format(rows[0][1].replace(" ",""), len(rows[0][1].replace(" ",""))))
        except psycopg2.Error as e:
            print("I am unable to connect to the database")
            print(e)
            print(e.pgcode)
            print(e.pgerror)
            print(traceback.format_exc())