import xml.etree.ElementTree as ET

tree = ET.parse('xxx.xml')

root = tree.getroot()

print(root.tag)

for i in root:
    #print(i.tag)
    for j in i:
        print(j.tag)
        #print(j.attrib)
        print(j.text)


for i in root.iter('price'):
    print(i.tag, i.text)


for i in root.iter('calories'):
    print(i.text)