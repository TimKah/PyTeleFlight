import psycopg2

class DBManager:
    def __init__(self, name):
        try:
            self.conn = psycopg2.connect("dbname=25655 user=postgres password=0000")
        except psycopg2.Error as e:
            print("I am unable to connect to the database")
            print(e)
            print(e.pgcode)
            print(e.pgerror)
            print(traceback.format_exc())