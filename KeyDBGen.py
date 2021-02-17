import sqlite3, random, time
def gen_key(): #generate random 6 number key
    number = random.randint(100000, 999999)
    return int(number)
def tme(): # Generate local time and return it
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time
class MyData:
    def __init__(self, name_first=None, name_last=None, ID=None):
        self.name_first = name_first
        self.name_last = name_last 
        self.ID = ID
        global conn # Makes the connection global in code
        conn = sqlite3.connect('temp_key.db') # creates connection to DB we have named 'temp_key'
        global cur # Makes the cursor global in code
        cur = conn.cursor()
    @staticmethod
    def QuickRecovery(name_first, name_last, ID):
        return "Name: {} {}, UID: {}".format(name_first, name_last, ID)# Format is easier way of inserting data into string
    @staticmethod #static method = not related to self in the class.
    def GenKey(name_first=None, name_last=None):
        if type(name_first) == type(name_last): #Cheat the check with the simple type check
            cur.execute('''CREATE TABLE IF NOT EXISTS gen_keys
             (first, last, key, time)''') # creates the table for DB
            cur.execute("INSERT OR REPLACE INTO gen_keys VALUES (?, ?, ?, ?)", (name_first, name_last, gen_key(), tme())) # Adds the values to that table. Generates Time and Key on the spot
            conn.commit() # Submits that data to the DB server/File/Table
        else:
            print("Fail")
Start = MyData()
Start.GenKey("Nolan", "Taft")

#NOTE: The '(?, ?, ?, ?)' in line 26 allows us to input variables into the SQLITE3 table, '{}' format doesnt work.
