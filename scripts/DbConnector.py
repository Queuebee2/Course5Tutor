# Author        Queuebee2
# iteration     idk


#importants
import mysql.connector
from base64 import b64decode as magic_wizardry


# load basic credentials (add DbCreds to .gitignore!!!!!!!!)
try:
    from DbCreds import HOST_DEFAULT, USER_DEFAULT, DATABASE_DEFAULT
except ModuleNotFoundError:
    raise ModuleNotFoundError ("It seems there is no DbCreds.py file"+
                               " available. Try creating it manually,") 
                            

GLOBAL_FIREBALL = False # we need a fireball, conjured by a magician.
                        # keep False unless the secret has been revealed.



class DbConnector():
    """ An object to help communicate with a (my)SQL Database"""
    def __init__(self,  host=HOST_DEFAULT, fireball=GLOBAL_FIREBALL,
                        user=USER_DEFAULT, db=DATABASE_DEFAULT):
        
        # setup initial static attributes
        self.host = host
        self.__magic = fireball
        if not self.__magic:
            # get magic
            self.__magic = self._DbConnector__wizardman()
        self.user = user
        self.db = db

        # variable attributes
        self.connected = False


        # startup
        print("trying to setup a db connection now!")
        
        self._connect()
    

    def select_results(self, limit = 100):
        """ hardcoded select to just select current results"""

#!TODO  add parameter to set table
        default_table = "PROTEIN"
        
        self.cursor.execute("SELECT * FROM " + default_table + " LIMIT " + str(limit +";"))

        results = self.cursor.fetchall()

        return results

            
            
    def insert(self, query, values):
        """
        a simple SQL insert values into the connected database
        
        example query:
           "insert into PROTEIN (id, MSA_id, length, header)"

        example values:
            [000000, 000000, 000000, 00000]
        
        """
        
        self.cursor.execute(query, values)
        self.connection.commit()
        print(self.cursor.rowcount, 'record inserted')
        # can't be implemented yet, default values haven't been established
        # it's recommended to set default values on the database side 
        # so the script doesn't haveto generate them for every missing value.

        # extra:
        # add another function to return string query from**kwargs
        # this could be done like ``self.Query_id = blastresult[0]``


    def insert_many_to_many(self, table_value_dict):
        """
        Insert data into a many-to-many relationship
        """

#!TODO  finish this function
#!UFF
        pass
    

        
    def _connect(self):
        # connect to database
        print("trying to connect...")
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                password=self._DbConnector__magic,
                user=self.user,
                db=self.db)

            self.cursor = self.connection.cursor()
            self.connected = True
            print("connection achieved")
        except:
            self.connected = False
            print("No connection established! Did you set the db " + \
                  "connector globals correctly?")
    

    def __wizard_helper(self, bunny):
        # a wizard never explains where his/her props hide
        return bunny.decode("utf-8")
        
    def __wizardman(self):
        # a wizard never reveals it's secret methods
        print("conjuring a fireball...")

        try:
            from DbCreds import joke       
        except:
            print('no joke, no magic')
            raise NoJokeError\

        lmfao = magic_wizardry(joke)

        fireball = self._DbConnector__wizard_helper(lmfao)

        print("Hocus pocus pilatus pas! Wingardium leviosa! " + \
              "Expecto Patronum!")
        print("Gabindo Purchai Camerinthum Carlem Aber.")

        return fireball


class NoJokeError(Exception):
    pass

if __name__ == '__main__':
    app = DbConnector()
else:
    print('imported db_insert')
