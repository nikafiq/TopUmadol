import os
import pyocr
from picprocessor import *
import pandas as pd
import openpyxl
import tkinter

#linking OCR program path
path='Tesseract-OCR/'
os.environ['PATH'] = os.environ['PATH'] + path
pyocr.tesseract.TESSERACT_CMD = r'Tesseract-OCR/Tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

#creating empty list
fannum =[]
playerlist = []

#read linked images and return it as text
def imgocr(img):
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    text = tool.image_to_string(img, lang="jpn", builder=builder)
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace(' ', '')
    return text

#Extracting fan number from text
def fan_num(text):
    p = re.compile('[0-9]+')
    num = p.findall(text)
    num2 = []
    for i in range(len(num)):
        if len(num[i]) >= 7:
            num2.append(num[i])
    return  num2

#Extracting player list from text
def player_list(text):
    player = text.split("\n")
    playerlist = []
    if len(player) == 7:
        for i in range(0, len(player), 4):
            playerlist.append(player[i])
    elif len(player) == 6:
        for i in range(0, len(player), 3):
            playerlist.append(player[i])
    else:
        for i in range(0, len(player), 5):
            playerlist.append(player[i])
    return playerlist

def list_fan():
    global fannum, playerlist
    for i in glob.iglob('pic/crop/*.png'):
        img = Image.open(i)
        text = imgocr(img)
        num = fan_num(text)
        player = player_list(text)
        for x in num:
            fannum.append(x)
        for x in player:
            playerlist.append(x)

def daily_folder():
    for i in glob.glob('pic/crop/'):
        for j in glob.glob(i+'*png'):
            list_fan(j)
            print(fannum)
            print(playerlist)

def add_df():
    global playerlist, fannum
    path = 'out.xlsx'
    pathexist = os.path.exists(path)
    if pathexist == False:
        df = {'IGN': playerlist,'Day1': fannum}
        df = pd.DataFrame(df,columns=['IGN','Day1'])
        df.to_excel('out.xlsx')
    else:
        df = pd.read_excel('out.xlsx',index_col=0)
        newname = 'Day'+f'{len(df.columns)}'
        df[newname] = fannum
        df.to_excel('out.xlsx')
    fannum = []
    playerlist = []

def run_ss():
    ss_crop()
    list_fan()

def export_data():
    add_df()
    move_files()

#initialize gui
window_main = tkinter.Tk()
window_main.title("TopUmadol - Fan Counter")
window_main.geometry('400x200')
scan_button = tkinter.Button(window_main, text="Start scanning", command=run_ss)
scan_button.config(width=20, height=2)
export_button = tkinter.Button(window_main, text="Export data", command=export_data)
export_button.config(width=20, height=2)

scan_button.pack()
export_button.pack()
window_main.mainloop()

#ss_crop()
#list_fan()
#add_df()
#move_files()
#print(playerlist)
#print(fannum)