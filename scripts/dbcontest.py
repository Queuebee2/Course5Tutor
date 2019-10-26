from DbConnector import DbConnector


db = DbConnector()

mess = db.exists_protein('testgfId')

print(mess)
