import re
from collections import Counter

# file = input("Please input full path to file: ")
# file = f"D:\Python\Education\DataSolution\Тестовое задание\Задание1\annotations.xml"
files = ['annotations.xml', 'annotations-2.xml', 'annotations-3.xml']


def parse_xml(file_name):
    with open(file_name) as xml_file:
        xml = xml_file.read()

        pattern = r"<\w+ "

        how_many_tags = Counter(re.findall(pattern, xml))

        clear = {}

        for i in how_many_tags:
            key = i[1:].strip()
            clear[key] = how_many_tags[i]
        print(f'In file {file_name}:')
        for i, j in clear.items():
            if i == 'image':
                continue
            else:
                print(f'{i} = {j}')


for file in files:
    parse_xml(file)
