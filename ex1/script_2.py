import xml.etree.ElementTree as ET
import os


def class_filter(files):
    file = files.split('\\')[-1]
    tree = ET.parse(file)
    root = tree.getroot()

    class_dict = {}
    for meta in root.findall('meta'):
        for task in meta.findall('task'):
            for labels in task.findall('labels'):
                for label in labels.findall('label'):
                    for name in label.findall('name'):
                        class_dict[name.text] = 0

    for image in root.findall('image'):
        if image.find('box') is not None:
            for box in image.findall('box'):
                class_dict[box.attrib['label']] += 1
        if image.find('polygon') is not None:
            for polygon in image.findall('polygon'):
                class_dict[polygon.attrib['label']] += 1

    print(f"Файл {file} имеет {len(class_dict)} классa:")
    for k, v in class_dict.items():
        print(f"В классе {k}: {v} фигур")
    print()


for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(".xml"):
            path_file = os.path.join(root, file)
            class_filter(path_file)
