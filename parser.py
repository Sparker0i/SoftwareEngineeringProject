import xml.etree.cElementTree as ET

tree = ET.parse('/home/sparker0i/fulldatabase.xml')
drugbank = tree.getroot()

for drug in drugbank.getchildren():
    print(drug.find('{http://www.drugbank.ca}name').text)
