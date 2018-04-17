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
        self.db = my.connect(host , username , password , database , charset="utf8mb4", use_unicode=True)
    
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
        