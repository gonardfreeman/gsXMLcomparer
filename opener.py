import os

ROOT_PATH=os.path.dirname(__file__)
for filename in os.listdir(ROOT_PATH):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(ROOT_PATH, filename)
    tree = ET.parse(fullname)