import KeyDBGen, DBReader
Run = KeyDBGen.MyData()
Run.GenKey("First Name", "Last Name")
READ = DBReader.Read("temp_key.db")
print(READ)
