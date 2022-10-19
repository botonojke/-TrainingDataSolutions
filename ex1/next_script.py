# import xml.etree.ElementTree as ET
#
#
# def parse():
#     tree = ET.parse('annotations.xml')
#     root = tree.getroot()
#     all_images = 0
#     width_heigth = {} # Словарь разрешений
#     for child in root:
#         # Считаем кол-во изображений
#         if child.tag == 'image':
#             all_images += 1
#             if f"{int(child.attrib['width']) * int(child.attrib['height'])}" in width_heigth:
#                 width_heigth[f"{int(child.attrib['width']) * int(child.attrib['height'])}"] += 1
#             else:
#                 width_heigth[f"{int(child.attrib['width']) * int(child.attrib['height'])}"] = 1
#
#             # print(f"{child.attrib['name']} -  {child.attrib['width']}:{child.attrib['height']}")
#             # for image_child in child:
#             #     if image_child.tag == 'polygon' or image_child.tag == 'box':
#             #         image_with += 1
#     for i, j in width_heigth.items():
#         print(f"Изображений с разрешением {i} - {j} штук")
#     # print(image_child.tag, image_child.attrib)
#     print(f"Всего изображений {all_images}")
#
#
# parse()


x = None
print(x)
if x > 10:
    x = 10
print(x)