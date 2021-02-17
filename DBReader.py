import sqlite3
def ReturnDB():
        try:
            c.execute("SELECT * FROM gen_keys")
            print(c.fetchall())
        except Exception as e:
            print(("ERROR :2: {}").format(str(e)))
class Read:
    def __init__(self, db):
        try:
            connection = sqlite3.connect(str(db))
            global c
            c = connection.cursor()
            ReturnDB()
        except Exception as e:
           print(("ERROR :1: {}").format(str(e)))
