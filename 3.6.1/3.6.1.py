from lxml import etree
from xml.etree import ElementTree

# rootlist = "<cube color=\"blue\"><cube color=\"red\"><cube color=\"green\"></cube></cube><cube color=\"red\"></cube></cube>"
rootlist = input()
tree = ElementTree.fromstring(rootlist)

dict_result = {"red": 0, "blue": 0, "green": 0}

def recursev_try(root, level):
    level += 1
    dict_result[root.attrib["color"]] += level
    for childe in root:
        recursev_try(childe, level)

recursev_try(tree, 0)

print(dict_result["red"], dict_result["green"], dict_result["blue"])

