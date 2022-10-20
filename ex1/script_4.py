import xml.etree.ElementTree as ET
import os


def chenge_file(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    for (id, image) in enumerate(root.findall('image')):
        image.set('id', str(id))
        image.set('name', f"{image.attrib['name'].split('/')[-1].split('.')[0]}.png")

    file = file_name.split('\\')[-1].split('.')[0]
    tree.write(f"{file}-copy.xml", encoding='utf-8')

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(".xml"):
            path_file = os.path.join(root, file)
            chenge_file(path_file)

