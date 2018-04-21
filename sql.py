import MySQLdb as my
import json

class DumpToSQL:
    db = None

    def __init__(self):
        with open('local_settings.json') as jsonfile:
            data = json.load(jsonfile)
            host = data['host']
            username = data['user']
            password = data['password']
            database = data['database']
        self.db = my.connect(host=host , user=username , password=password , db=database, use_unicode=True)
    
    def insert_drug(self , drug):
        cursor = self.db.cursor()
        u = drug.name
        v = drug.id
        try:
            sql = "INSERT INTO DRUG(name , id) VALUES (\"" + u + "\",\"" + v + "\");"
            cursor.execute(sql)
            self.db.commit()
        except UnicodeEncodeError:
            print("Could Not Insert Unicode " + u + " " + v)
        except TypeError:
            print("Could Not Insert Type " + u + " " + v)
        finally:
            cursor.close()
            self.db.close()
        
    # 1. You will get an object of the respective class with every insert operation invoked. Write code to add them taking into reference insert_drug() from above
    # 2. To find what elements needed to be added, look at classes.py and also refer to the XML

    def insert_druginteraction(self, druginteraction):
        print()

    def insert_drugclass(self , drugclass):
        print()

    def insert_drugtarget(self , drugtarget):
        print()