import cv2
import xml.etree.ElementTree as ET
import numpy as np
import os


def get_skin_color(xml: str):
    """Get skin color from xml file"""
    tree = ET.parse(xml)
    root = tree.getroot()

    for meta in root.findall('meta'):
        for task in meta.findall('task'):
            for labels in task.findall('labels'):
                for label in labels.findall('label'):
                    if label.find('name').text == 'Skin':
                        h = label.find('color').text.lstrip('#')
                        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def get_point(label: str, image_name: str, xml: str):
    """Gets the coordinates for the masks and returns a dictionary with all the faces of the polygon"""
    tree = ET.parse(xml)
    root = tree.getroot()
    ignore = dict()
    skin = dict()
    key_for_ignore = 0
    key_for_skin = 0
    pts = []
    for i in root.findall('image'):
        if i.attrib['name'].split('/')[-1] == image_name:
            for j in i.findall('polygon'):
                pts = []
                if j.attrib['label'] == 'Ignore':
                    for cord in j.attrib['points'].split(';'):
                        pts.append(list(map(float, cord.split(','))))
                    key_for_ignore += 1
                    ignore[key_for_ignore] = pts

                if j.attrib['label'] == 'Skin':
                    for cord in j.attrib['points'].split(';'):
                        pts.append(list(map(float, cord.split(','))))
                    key_for_skin += 1
                    skin[key_for_skin] = pts
    if label == 'Skin':
        return skin
    elif label == 'Ignore':
        return ignore


def get_black_img(image: str, labels: list, xml: str):
    """Gets a mask on a black background"""
    image_name = image.split('\\')[-1]
    pic = cv2.imread(image, -1)
    img = np.zeros(pic.shape, dtype='uint8')
    color = get_skin_color(xml)
    for label in labels:
        if label == 'Skin':
            pts = get_point(label='Skin', image_name=image_name, xml=xml)
            for i, j in pts.items():
                pts = np.array(j, np.int32)
                cv2.fillPoly(img, pts=[pts], color=color)
        elif label == 'Ignore':
            pts = get_point(label='Ignore', image_name=image_name, xml=xml)
            for i, j in pts.items():
                pts = np.array(j, np.int32)
                cv2.fillPoly(img, pts=[pts], color=(0, 0, 0))

    return cv2.imwrite(f'D:\Python\Repo\-TrainingDataSolutions\ex2\\black_image_with_mask\\{image_name}', img)


def get_mask_for_ignore(image: str, labels: list, xml: str):
    """Gets the mask to ignore on the original background"""
    image_name = image.split('\\')[-1]
    pic = cv2.imread(image, -1)
    mask = np.zeros(pic.shape, dtype='uint8')
    channel_count = pic.shape[2]
    ignore_mask_color = (255,) * channel_count
    for label in labels:
        if label == 'Ignore':
            pts = get_point(label='Ignore', image_name=image_name, xml=xml)
            for i, j in pts.items():
                pts = np.array(j, np.int32)
                cv2.fillPoly(mask, pts=[pts], color=ignore_mask_color)

    return mask


def get_orig_img_with_mask(image: str, labels: list, xml: str):
    """Gets a mask on original background"""
    image_name = image.split('\\')[-1]
    pic = cv2.imread(image, -1)
    mask = get_mask_for_ignore(image, labels=labels, xml=xml)
    img = cv2.bitwise_and(pic.copy(), mask)
    color = get_skin_color(xml)
    for label in labels:
        if label == 'Skin':
            pts = get_point(label='Skin', image_name=image_name, xml=xml)
            for i, j in pts.items():
                pts = np.array(j, np.int32)
                cv2.fillPoly(pic, pts=[pts], color=color)
        elif label == 'Ignore':
            pts = get_point(label='Ignore', image_name=image_name, xml=xml)
            for i, j in pts.items():
                pts = np.array(j, np.int32)
                cv2.fillPoly(pic, pts=[pts], color=(0, 0, 0))
    pic = cv2.add(pic, img)

    return cv2.imwrite(f'D:\Python\Repo\-TrainingDataSolutions\ex2\orig_image_with_mask\\{image_name}', pic)


if __name__ == '__main__':
    """Searches for all jpg files in the specified area"""
    for root, dirs, files in os.walk('D:\Python\Repo\-TrainingDataSolutions\ex2\images'):
        for file in files:
            if file.endswith(".jpg"):
                path_file = os.path.join(root, file)
                get_orig_img_with_mask(image=path_file, labels=['Skin', 'Ignore'], xml='masks.xml')
                get_black_img(image=path_file, labels=['Skin', 'Ignore'], xml='masks.xml')
