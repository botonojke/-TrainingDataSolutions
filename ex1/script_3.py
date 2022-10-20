import re
from collections import Counter
import os




def parse_xml(file_name):
    with open(file_name) as xml_file:
        xml = xml_file.read()

        pattern = r"<\w+ "

        how_many_tags = Counter(re.findall(pattern, xml))

        clear = {}
        file = file_name.split('\\')[-1]
        for i in how_many_tags:
            key = i[1:].strip()
            clear[key] = how_many_tags[i]
        print(f"In file {file}:")
        for i, j in clear.items():
            if i == 'image':
                continue
            else:
                print(f'{i} = {j}')


for root, dirs, files in os.walk('.'):
    for file in files:
        # if file.endswith("copy.xml"):
        #     continue
        if file.endswith(".xml"):
            path_file = os.path.join(root, file)
            parse_xml(path_file)
