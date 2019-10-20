import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DbConnector import DbConnector

myDB = DbConnector()
identifiery = 16
try:
    myDB.commit_query(f"INSERT INTO PROTEIN VALUES ({identifiery}, 5, 'hhgtsghsfg', 'tagtgtgatgatg')")
except Exception as e:
    print(type(e))
    identifiery += 1
    myDB.commit_query(f"INSERT INTO PROTEIN VALUES ({identifiery}, 5, 'hhgtsghsfg', 'tagtgtgatgatg')")


#myDB.insert("INSERT INTO PROTEIN (`id`, `MSA_id`, `header`, `sequence`)", [14, 5, 'hhgtsghsfg', 'tagtgtgatgatg'])
myDB.update_row("PROTEIN", 13, {"MSA_id":1337, "header":">headeryboi1", "sequence":"atcctg"})


print(myDB.select_results())