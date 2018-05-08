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
        except Exception:
            print("Could Not Insert Exception " + u + " " + v + " " + w + " " + x + " " + y)
        finally:
            cursor.close()
            self.db.close()
        
    # 1. You will get an object of the respective class with every insert operation invoked. Write code to add them taking into reference insert_drug() from above
    # 2. To find what elements needed to be added, look at classes.py and also refer to the XML

    def insert_druginteraction(self, druginteractions):
        cursor = self.db.cursor()
        for druginteraction in druginteractions:
            u = druginteraction.id
            v = druginteraction.drugbank_id
            w = druginteraction.name
            x = druginteraction.description
            try:
                sql = "INSERT INTO DRUG_INTERACTIONS(id,drugbank_id,name,description) VALUES (\"" + u + "\",\"" + v + "\",\""+ w + "\",\""+ x + "\");"
                cursor.execute(sql)
                self.db.commit()
            except UnicodeEncodeError:
                print("Could Not Insert Unicode " + u + " " + v + " " + w + " " + x)
            except TypeError:
                print("Could Not Insert Type " + u + " " + v + " " + w + " " + x)
            except Exception:
                print("Could Not Insert Exception " + u + " " + v + " " + w + " " + x + " " + y)
        cursor.close()
        self.db.close()

    def insert_drugclass(self , drugclass):
        cursor = self.db.cursor()
        u = drugclass.direct_parent
        v = drugclass.kingdom
        w = drugclass.super_class
        x = drugclass.class_
        y = drugclass.sub_class
        z = drugclass.id
        try:
            sql = "INSERT INTO DRUG_CLASS(directparent,kingdom,superclass,class,subclass,id) VALUES (\"" + u + "\",\"" + v + "\",\""+ w + "\",\""+ x +"\",\"" + y +"\",\""+ z + "\");"
            cursor.execute(sql)
            self.db.commit()
        except UnicodeEncodeError:
            print("Could Not Insert Unicode " + u + " " + v + " " + w + " " + x + " " + y + " " + z)
        except TypeError:
            print("Could Not Insert Type " + u + " " + v + " " + w + " " + x + " " + y + " " + z)
        except Exception:
                print("Could Not Insert Exception " + u + " " + v + " " + w + " " + x + " " + y)
        finally:
            cursor.close()
            self.db.close()

    def insert_drugtarget(self , drugtargets):
        cursor = self.db.cursor()
        for drugtarget in drugtargets:
            u = drugtarget.position
            v = drugtarget.id
            w = drugtarget.drugbank_id
            x = drugtarget.name
            y = drugtarget.organism        
            try:
                sql = "INSERT INTO DRUG_TARGET(position ,id,drugbank_id,name,organism) VALUES (\"" + u + "\",\"" + v + "\",\""+ w + "\",\""+ x +"\",\"" + y + "\");"
                cursor.execute(sql)
                self.db.commit()
            except UnicodeEncodeError:
                print("Could Not Insert Unicode " + u + " " + v + " " + w + " " + x + " " + y)
            except TypeError:
                print("Could Not Insert Type " + u + " " + v + " " + w + " " + x + " " + y)
            except Exception:
                print("Could Not Insert Exception " + u + " " + v + " " + w + " " + x + " " + y)
        cursor.close()
        self.db.close()
