from models import *
from classes import *
                
def main():
    tree = XMLParser().parse_element_tree("/home/sparker0i/fulldatabase.xml")
    DataExtractor().initialize_classes(tree)

if __name__ == "__main__":
    main()