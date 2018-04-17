import MySQLdb as my

class DumpToSQL:
    db = None

    def __init__(self):
        self.db = my.connect("localhost" , "root" , "THE PASSWORD HERE" , "DRUGBANK", charset="utf8mb4", use_unicode=True)

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
        