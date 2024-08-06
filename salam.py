import os
os.chdir(r'The path of the folder where the text files are locatedمسیر پوشه ای که فایل های متن توش قرار داره')
d=(os.listdir())

for i in d:
    with open(i,'a') as f:
        f.write('-------------------------------------------------------------------------')

with open('tamam moton', 'a', encoding="utf-8") as c:
    for i in d:
        with open (i,'r', encoding="utf-8") as s:
            c.write(s.read())
            c.write('\n')
