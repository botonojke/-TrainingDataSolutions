import cv2
import xml.etree.ElementTree as ET
import numpy as np
import os


def get_point(image):
    image_name = image.split('\\')[-1]
    pic = cv2.imread(f'D:\Python\Repo\-TrainingDataSolutions\ex2\images\\{image_name}', -1)
    pick = pic.copy()
    img = np.zeros(pic.shape, dtype='uint8')
    mask = np.zeros(pic.shape, dtype='uint8')
    channel_count = pic.shape[2]
    ignore_mask_color = (255,) * channel_count
    tree = ET.parse('masks.xml')
    root = tree.getroot()
    color = (115, 51, 128)
    thickness = 2
    for i in root.findall('image'):
        if i.attrib['name'].split('/')[-1] == image_name:
            for j in i.findall('polygon'):
                pts = []
                if j.attrib['label'] == 'Ignore':
                    color = (250, 50, 83)
                    for cord in j.attrib['points'].split(';'):
                        cord = list(map(float, cord.split(',')))
                        pts.append(cord)
                    pts = np.array(pts, np.int32)
                    cv2.fillPoly(pic, pts=[pts], color=(0, 0, 0))
                    cv2.fillPoly(img, pts=[pts], color=(0, 0, 0))
                    cv2.fillPoly(mask, pts=[pts], color=ignore_mask_color)

                if j.attrib['label'] == 'Skin':
                    color = (115, 51, 128)
                    for cord in j.attrib['points'].split(';'):
                        cord = list(map(float, cord.split(',')))
                        pts.append(cord)
                    pts = np.array(pts, np.int32)
                    cv2.fillPoly(pic, pts=[pts], color=color)
                    cv2.fillPoly(img, pts=[pts], color=color)

    pickk = cv2.bitwise_and(pick, mask)
    new_img = cv2.add(pic, pickk)
    cv2.imwrite(f'D:\Python\Repo\-TrainingDataSolutions\ex2\\black_image_with_mask\\{image_name}', img)
    cv2.imwrite(f'D:\Python\Repo\-TrainingDataSolutions\ex2\orig_image_with_mask\\{image_name}', new_img)


for root, dirs, files in os.walk('images'):
    for file in files:
        if file.endswith(".jpg"):
            path_file = os.path.join(root, file)
            get_point(path_file)
