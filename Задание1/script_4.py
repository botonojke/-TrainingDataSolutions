import xml.etree.ElementTree as ET

file_name = input('Please enter file name path: ')

def chenge_file(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    for (id, image) in enumerate(root.findall('image')):
        image.set('id', str(id))
        image.set('name', f"{image.attrib['name'].split('/')[-1].split('.')[0]}.png")

    file = file_name.split('\\')[-1].split('.')[0]
    tree.write(f"{file}-copy.xml", encoding='utf-8')

if __name__ == "__main__":
    chenge_file(file_name)

