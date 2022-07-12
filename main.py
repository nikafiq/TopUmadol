import os
from PIL import Image
import pyocr

path='C:\\Program Files\\Tesseract-OCR\\'
os.environ['PATH'] = os.environ['PATH'] + path

pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files/Tesseract-OCR\Tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

img = Image.open("test_image\\test.png")

builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img, lang="jpn", builder=builder)

print(text)
print(type(text))