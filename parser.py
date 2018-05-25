from classes import XMLParser , DataExtractor
from sql import DumpToSQL
import xml.etree.ElementTree
import json
                
def main():
    tree = XMLParser().parse_element_tree("/home/sparker0i/fulldatabase.xml")
    dump = DumpToSQL()
    DataExtractor().initialize_classes(tree , dump)
    dump.terminate()

if __name__ == "__main__":
    main()