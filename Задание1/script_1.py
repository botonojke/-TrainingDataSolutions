# import os
#
# for root, dirs, files in os.walk(".//"):
#     for file in files:
#         if file.endswith(".xml"):
#             path_file = os.path.join(root, file)
#             print(path_file)

import xml.etree.ElementTree as ET

# file_name = input('Please enter file name path: ')
files = ['annotations.xml', 'annotations-2.xml', 'annotations-3.xml']


def total_stats(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    all_image = 0
    image_with = 0
    image_without = 0
    all_figure = 0
    screen = []
    max_screen = ''
    min_screen = ''
    x = 0
    y = 99999999999999999999
    max_name = ""
    min_name = ""
    # Поиск всех изображений
    for i in root.findall('image'):
        all_image += 1

        scree = int(i.get('width')) * int(i.get('height'))
        # print(f"{scree} = {i.get('width')}:{i.get('height')}")
        if scree > x:
            x = scree
            max_name = f"{i.get('name')}"
            max_screen = f"{i.get('width')}:{i.get('height')}"
        if y > scree:
            y = scree
            min_name = f"{i.get('name')}"
            min_screen = f"{i.get('width')}:{i.get('height')}"

        screen.append(f"{i.get('width')}:{i.get('height')}")

        # Поиск всех фигур
        for j in i:
            if i.find('box') is not None or i.find('polygon') is not None:
                all_figure += 1
        # Поиск размеченных изображений
        if i.findall('box') or i.findall('polygon'):
            image_with += 1
        # Поиск не размеченных изображений
        else:
            image_without += 1
    if image_without != 0:
        print(f"В файле {file_name}\n"
              f"Всего изображений: {all_image}\n"
              f"Не размечено изображений: {image_without}\n"
              f"Всего изображений размечено: {image_with}\n"
              f"Всего фигур {all_figure}\n"
              f"Самое большое изображение {max_screen}, таких изображений в файле {screen.count(max_screen)}\n"
              f"Пример: {max_name}\n"
              f"Самое маленькое изображение {min_screen}, таких изображений в файле {screen.count(min_screen)}\n"
              f"Пример: {min_name}\n")
    else:
        print(f"В файле {file_name}\n"
              f"Всего изображений: {all_image}\n"
              f"Изображений размечено: {image_with}\n"
              f"Всего фигур {all_figure}\n"
              f"Самое большое изображение {max_screen}, таких изображений в файле {screen.count(max_screen)}\n"
              f"Пример: {max_name}\n"
              f"Самое маленькое изображение {min_screen}, таких изображений в файле {screen.count(min_screen)}\n"
              f"Пример: {min_name}\n")


for file in files:
    total_stats(file)
