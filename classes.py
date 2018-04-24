import xml.etree.cElementTree as ET
from models import *
import MySQLdb as my
import sql

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
        if drug.find('{http://www.drugbank.ca}direct-print').text and drug.find('{http://www.drugbank.ca}kingdom').text and drug.find('{http://www.drugbank.ca}superclass').text and drug.find('{http://www.drugbank.ca}class').text and drug.find('{http://www.drugbank.ca}drugbank-id').text:
            return (True , DrugClass(drug.find('{http://www.drugbank.ca}direct-print').text , drug.find('{http://www.drugbank.ca}kingdom').text , drug.find('{http://www.drugbank.ca}superclass').text , drug.find('{http://www.drugbank.ca}class').text , drug.find('{http://www.drugbank.ca}drugbank-id').text))
        return False

    def check_drugtarget(self , drug):
        targets = drug.find('{http://www.drugbank.ca}targets')
        for target in targets:
            if drug.find('{http://www.drugbank.ca}position').text and drug.find('{http://www.drugbank.ca}name').text and drug.find('{http://www.drugbank.ca}drugbank-id').text and drug.find('{http://www.drugbank.ca}id').text:
                return (True, DrugTarget(drug.find('{http://www.drugbank.ca}position').text , drug.find('{http://www.drugbank.ca}name').text , drug.find('{http://www.drugbank.ca}drugbank-id').text , drug.find('{http://www.drugbank.ca}id').text))
        return False
    
    def check_interactions(self , drug):
        if drug.find('{http://www.drugbank.ca}id').text and drug.find('{http://www.drugbank.ca}name').text and drug.find('{http://www.drugbank.ca}drugbank-id').text and drug.find('{http://www.drugbank.ca}description').text:
            return (True, DrugInteractions(drug.find('{http://www.drugbank.ca}id').text , drug.find('{http://www.drugbank.ca}name').text , drug.find('{http://www.drugbank.ca}drugbank-id').text , drug.find('{http://www.drugbank.ca}description').text))
        return False
    
    #TODO: Modify this function to check for all - Drug , DrugClass , DrugTarget, Interactions
    def initialize_classes(self , tree):
        root = tree.getroot()
        for drug in root.getchildren():
            check , value = self.check_drug(drug)
            check1 , value1 = self.check_drugclass(drug)
            if check:
                sql.DumpToSQL().insert_drug(value)
            if check1:
                sql.DumpToSQL().insert_drug(value1)

