import xml.etree.ElementTree as ET
import os


def get_images(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    images = root.findall('image')
    return images


def get_all_figure(images: list[ET.Element]):
    figure = []
    for image in images:
        figure.extend(image.iterfind('*'))
    return figure


def get_annotated_images(images: list[ET.Element]):
    annotated_images = 0
    for image in images:
        if image.findall('box') or image.findall('polygon'):
            annotated_images += 1
    return annotated_images


def get_screen_size(image: ET.Element):
    height = int(image.get('height'))
    width = int(image.get('width'))
    size = height * width
    return size


def get_max_min_screen(images: list[ET.Element]):
    max_screen = {}
    min_screen = {}
    screens = [get_screen_size(image) for image in images]
    for image in images:
        if get_screen_size(image) == max(screens):
            max_screen[f"{image.get('width')}:{image.get('height')}"] = image.get('name')
        elif get_screen_size(image) == min(screens):
            min_screen[f"{image.get('width')}:{image.get('height')}"] = image.get('name')
    return max_screen, min_screen


def total_stats(file_name):
    images = get_images(file_name=file_name)
    file = file_name.split('\\')[-1]
    screens = [get_screen_size(image) for image in images]
    not_annotated_images = len(images) - get_annotated_images(images=images)
    if get_max_min_screen(images=images)[1] != {}:
        largest_image = list(get_max_min_screen(images=images)[0].keys())[0]
        smallest_image = list(get_max_min_screen(images=images)[1].keys())[0]
        name_smallest_image = get_max_min_screen(images=images)[1][smallest_image]
        name_largest_image = get_max_min_screen(images=images)[0][largest_image]
    else:
        smallest_image = list(get_max_min_screen(images=images)[0].keys())[0]
        largest_image = list(get_max_min_screen(images=images)[0].keys())[0]
        name_smallest_image = get_max_min_screen(images=images)[0][smallest_image]
        name_largest_image = get_max_min_screen(images=images)[0][largest_image]

    if not_annotated_images != 0:
        return f"В файле {file}\n" \
               f"Всего изображений: {len(images)}\n" \
               f"Не размечено изображений: {not_annotated_images}\n" \
               f"Всего изображений размечено: {get_annotated_images(images=images)}\n" \
               f"Всего фигур {len(get_all_figure(images=images))}\n" \
               f"Самое большое изображение {largest_image}, таких изображений в файле {screens.count(max(screens))}\n" \
               f"Пример: {name_largest_image}\n" \
               f"Самое маленькое изображение {smallest_image}, таких изображений в файле {screens.count(min(screens))}\n" \
               f"Пример: {name_smallest_image}\n\n"
    else:
        return f"В файле {file}\n" \
               f"Всего изображений: {len(images)}\n" \
               f"Всего изображений размечено: {get_annotated_images(images=images)}\n" \
               f"Всего фигур {len(get_all_figure(images=images))}\n" \
               f"Самое большasdasое изображение {largest_image}, таких изображений в файле {screens.count(max(screens))}\n" \
               f"Пример: {name_largest_image}\n" \
               f"Самое маленькое изображение {smallest_image}, таких изображений в файле {screens.count(min(screens))}\n" \
               f"Пример: {name_smallest_image}\n\n"


with open('script_1.txt', 'w', encoding='utf-8') as fl:
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith("copy.xml"):
                continue
            elif file.endswith(".xml"):
                path_file = os.path.join(root, file)
                fl.writelines(total_stats(path_file))
