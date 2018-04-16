import xml.etree.cElementTree as ET
from models import *
import MySQLdb as my
import sql

class XMLParser:
    def parse_element_tree(self , filename):
        tree = ET.parse(filename)
        return tree

class DataExtractor:
    
    def check_drug(self , drug):
        if drug.find('{http://www.drugbank.ca}name').text and drug.find('{http://www.drugbank.ca}drugbank-id').text:
            return (True , Drug(drug.find('{http://www.drugbank.ca}name').text , drug.find('{http://www.drugbank.ca}drugbank-id').text))
        return False
    
    def initialize_classes(self , tree):
        root = tree.getroot()
        for drug in root.getchildren():
            check , value = self.check_drug(drug)
            if check:
                sql.DumpToSQL().insert_drug(value)
            