import xml.etree.cElementTree as ET

tree = ET.parse('fulldatabase.xml')
drugbank = tree.getroot()

for drug in drugbank.iter('{http://www.drugbank.ca}drug'):
    print(drug.find('{http://www.drugbank.ca}name').text)
