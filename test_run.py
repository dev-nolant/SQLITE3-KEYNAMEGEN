import KeyDBGen, DBReader
Run = KeyDBGen.MyData()
Run.GenKey("Nolan", "Taft")
READ = DBReader.Read("temp_key.db")
print(READ)