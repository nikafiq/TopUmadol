import os
from PIL import Image
import pyocr
import re

path='C:\\Program Files\\Tesseract-OCR\\'
os.environ['PATH'] = os.environ['PATH'] + path

pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files/Tesseract-OCR\Tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

img = Image.open("test_image\\umamusume 2022_04_16 0_05_05.png")

builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img, lang="jpn", builder=builder)

text = text.replace(',','')
text = text.replace('.','')
p = re.compile('[0-9]+')
num = p.findall(text)

with open('text.txt','w') as txt:
    txt.write(text)

with open('num.txt','w') as txt:
    for item in num:
        txt.write("%s\n" % item)

print(text)
print(type(text),end="/n/n")
print(num)