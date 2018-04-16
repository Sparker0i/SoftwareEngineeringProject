import xml.etree.cElementTree as ET

class Drug:
    name = "Name"
    id = "Id"

    def init(self , name , id):
        self.name = name
        self.id = id
        
class DrugClass:
    direct_parent = "directParent"
    kingdom = "kingdom"
    super_class = "superClass"
    class_ = "class_"
    sub_class = "sub_class"
    id = "id"

    def init(self , direct_parent , kingdom , super_class , class_ , sub_class):
        self.direct_parent = direct_parent
        self.kingdom = kingdom
        self.super_class = super_class
        self.class_ = class_
        self.sub_class = sub_class
        self.id = id

class XMLParser:
    def parse_element_tree(self , filename):
        tree = ET.parse(filename)
        return tree

class DataExtractor:
    def initialize_classes(self , tree):
        for drug in tree.getchildren():
            if drug.find('{http://www.drugbank.ca}name').text and drug.find('{http://www.drugbank.ca}cas-number').text:
                print(drug.find('{http://www.drugbank.ca}name').text, " " , drug.find('{http://www.drugbank.ca}cas-number').text)