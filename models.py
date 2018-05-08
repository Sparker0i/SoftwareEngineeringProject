class Drug:
    def __init__(self , name , id):
        self.name = name
        self.id = id
        
class DrugClass:
    def __init__(self , direct_parent , kingdom , super_class , class_ , sub_class, id):
        self.direct_parent = direct_parent
        self.kingdom = kingdom
        self.super_class = super_class
        self.class_ = class_
        self.sub_class = sub_class
        self.id = id

#id refers to the drug 
class DrugTarget:
    def __init__(self , position , id , drugbank_id, name , organism):
        self.position = position
        self.id = id #One that refers to the Root drug
        self.drugbank_id = drugbank_id #One that refers to the target of the current Drug
        self.name = name
        self.organism = organism

    def print(self):
        print("##" , self.position , self.id , self.drugbank_id , self.name , self.organism)

class DrugInteractions:
    def __init__(self , id , drugbank_id , name , description):
        self.id = id
        self.drugbank_id = drugbank_id
        self.name = name
        self.description = description

