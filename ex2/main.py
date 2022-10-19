import cv2
import xml.etree.ElementTree as ET
import numpy as np
import os


def get_point(image):
    image_name = image.split('\\')[-1]
    print(image_name)
    pic = cv2.imread(f'D:\Python\Repo\-TrainingDataSolutions\ex2\images\\{image_name}')
    img = np.zeros(pic.shape[:], dtype='uint8')
    ignore_img = np.zeros(pic.shape[:], dtype='uint8')
    tree = ET.parse('masks.xml')
    root = tree.getroot()
    color = (115, 51, 128)
    isClosed = True
    thickness = 2
    for i in root.findall('image'):
        if i.attrib['name'].split('/')[-1] == image_name:
            for j in i.findall('polygon'):
                pts = []
                if j.attrib['label'] == 'Ignore':
                    color = (0, 0, 0)
                    for cord in j.attrib['points'].split(';'):
                        cord = list(map(float, cord.split(',')))
                        pts.append(cord)
                    pts = np.array(pts, np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    # cv2.polylines(img, [pts], isClosed, color, thickness)
                    cv2.fillPoly(ignore_img, pts=[pts], color=color)
                    cv2.fillPoly(pic, pts=[pts], color=color)
                    cv2.fillPoly(img, pts=[pts], color=color)
                    # continue
                if j.attrib['label'] == 'Skin':
                    color = (115, 51, 128)
                    for cord in j.attrib['points'].split(';'):
                        cord = list(map(float, cord.split(',')))
                        pts.append(cord)
                    pts = np.array(pts, np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    # cv2.polylines(image, [pts], isClosed, color, thickness)
                    cv2.fillPoly(pic, pts=[pts], color=color)
                    cv2.fillPoly(img, pts=[pts], color=color)
    # new_img_with_mask = cv2.bitwise_or(pic, pic, mask=ignore_img)
    # cv2.imshow("res", new_img_with_mask)
    cv2.imwrite(f'D:\Python\Repo\-TrainingDataSolutions\ex2\\black_image_with_mask\\{image_name}', img)
    cv2.imwrite(f'D:\Python\Repo\-TrainingDataSolutions\ex2\orig_image_with_mask\\{image_name}', pic)
    # cv2.imshow("res", new_img_with_mask)
    # cv2.waitKey(0)




for root, dirs, files in os.walk('images'):
    for file in files:
        if file.endswith(".jpg"):
            path_file = os.path.join(root, file)
            get_point(path_file)

# get_point('D:\Python\Repo\-TrainingDataSolutions\ex2\images\\0814b919-6cea-4092-b5d6-eb17d8ffa08c.jpg')

