import xml.etree.ElementTree as ET
from models import *
import MySQLdb as my
import sql
import time

class XMLParser:
    def parse_element_tree(self , filename):
        tree = ET.parse(filename)
        return tree

class DataExtractor:

    # Finding the elements should always happen along with the XMLNS. Syntax: object.find('{http://www.drugbank.ca}colname')

    # Checks Every Drug. If every required value is present, it returns true, along with a new object of the Drug class
    def check_drug(self , drug):
        if drug.find('{http://www.drugbank.ca}name').text and drug.find('{http://www.drugbank.ca}drugbank-id').text:
            return (True , Drug(drug.find('{http://www.drugbank.ca}name').text , drug.find('{http://www.drugbank.ca}drugbank-id').text))
        return False

    #To find what elements to search for, refer to models.py and also their respective names in the XML file
    def check_drugclass(self , drug):
        direct_parent = "Not Available"
        kingdom = "Not Available"
        super_class = "Not Available"
        subclass = "Not Available"
        class_ = "Not Available"
        flag = 0
        id = drug.find('{http://www.drugbank.ca}drugbank-id').text
        for child in drug.findall('{http://www.drugbank.ca}classification'):
            '''
            print(child.tag , child.find(child.tag).text)
            '''
            if child.find('{http://www.drugbank.ca}kingdom').text:
                kingdom = child.find('{http://www.drugbank.ca}kingdom').text
            if child.find('{http://www.drugbank.ca}direct-parent').text:
                direct_parent = child.find('{http://www.drugbank.ca}direct-parent').text
            if child.find('{http://www.drugbank.ca}superclass').text:
                super_class = child.find('{http://www.drugbank.ca}superclass').text
            if child.find('{http://www.drugbank.ca}subclass').text:
                subclass = child.find('{http://www.drugbank.ca}subclass').text
            if child.find('{http://www.drugbank.ca}class').text:
                class_ = child.find('{http://www.drugbank.ca}class').text
        return (True , DrugClass(direct_parent=direct_parent , kingdom=kingdom , class_=class_ , sub_class=subclass, super_class=super_class , id=id))

    def check_drugtarget(self , drug):
        targets = drug.find('{http://www.drugbank.ca}targets')
        name = "Not Available"
        id = drug.find('{http://www.drugbank.ca}drugbank-id').text
        position = "0"
        organism = "Not Available"
        drugbank_id = "Not Available"
        array = []
        for beep in targets.findall('{http://www.drugbank.ca}target'):
            for child in beep:
                if child.tag == '{http://www.drugbank.ca}name':
                    name = child.text
                if child.tag == '{http://www.drugbank.ca}organism':
                    organism = child.text
                if child.tag == '{http://www.drugbank.ca}id':
                    drugbank_id = child.text
                if beep.attrib.get('position'):
                    position = beep.attrib.get('position')
                else:
                    position = "0"
            target = DrugTarget(position=position, name=name, id=id, drugbank_id=drugbank_id , organism=organism)
            array.append(target)
        return (True , array)


    def check_interactions(self , drug):
        interactions = drug.find('{http://www.drugbank.ca}drug-interactions')
        id = drug.find('{http://www.drugbank.ca}drugbank-id').text
        array = []
        for beep in interactions.findall('{http://www.drugbank.ca}drug-interaction'):
            drugbank_id = "Not Available"
            name_ = "Not Available"
            description = "Not Available"
            for child in beep:
                if child.tag == '{http://www.drugbank.ca}drugbank-id':
                    drugbank_id = child.text
                if child.tag == '{http://www.drugbank.ca}name':
                    name_ = child.text
                if child.tag == '{http://www.drugbank.ca}description':
                    description = child.text
            array.append(DrugInteractions(id , drugbank_id , name_ , description))

        return (True, array)
    
    def initialize_classes(self , tree):
        root = tree.getroot()
        for drug in root.getchildren():
            check , value = self.check_drug(drug)
            if check:
                print("$" , value.name , value.id)
                sql.DumpToSQL().insert_drug(value)
        
        for drug in root.getchildren():
            check3 , value3 = self.check_drugtarget(drug)

            if check3:
                for value1 in value3:
                    value1.print()
                sql.DumpToSQL().insert_drugtarget(value3)
            '''
            check1 , value1 = self.check_drugclass(drug)
            check2 , value2 = self.check_interactions(drug)
            
            
            if check1:
                print("#" , value1.id , value1.class_ , value1.sub_class , value1.super_class , value1.kingdom)
                sql.DumpToSQL().insert_drugclass(value1)

            if check2:
                for value1 in value2:
                    print("###" , value1.id , value1.drugbank_id , value1.name , value1.description)
                sql.DumpToSQL().insert_druginteraction(value2)
            '''