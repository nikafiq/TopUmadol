import os, pyocr, tkinter, win32gui, threading, datetime, openpyxl
from picprocessor import *
import pandas as pd
from tkinter import *
from PIL import ImageGrab, Image, ImageTk
from urllib.request import urlopen
# if "pip install win32gui" doesn't work, try using "pip install pywin32"

def ocr_path():
    global path, tool, tools
    path = 'Tesseract-OCR/'
    pathexist = os.path.exists(path)
    if pathexist:
        path = 'Tesseract-OCR/'
        os.environ['PATH'] = os.environ['PATH'] + path
        pyocr.tesseract.TESSERACT_CMD = r'Tesseract-OCR/Tesseract.exe'
        tools = pyocr.get_available_tools()
        tool = tools[0]
    else:
        path = tkFileDialog.askdirectory()
ocr_path()

#creating empty list
fannum =[]
playerlist = []

#setting screenshot variable
counter = 0
now = datetime.datetime.now()
today = f'{now:%Y%m%d}'

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

def printit():
    global counter, time_gap, ss_update, t
    try:
        umawin = win32gui.FindWindow(None, r'umamusume')
    except (win32gui.error):
        ss_display.configure(text="Screenshot stopped, game windows not found")
        t.cancel()
    t = threading.Timer(time_gap, printit)
    t.start()
    counter += 1
    win32gui.SetForegroundWindow(umawin)
    dimensions = win32gui.GetWindowRect(umawin)
    image = ImageGrab.grab(dimensions)
    image.save("pic/"f"{today}_" + "ss_" + f"{str(counter).zfill(2)}" + ".png")
    ss_display.configure(text="Took screenshot %d" % counter)
    # print("Took screenshot " + f"{counter}")
    if counter == 15:
        t.cancel()
        counter = 0
        ss_display.configure(text="Finished taking screenshot")

def run_ss():
    ss_crop()
    list_fan()

def export_data():
    add_df()
    move_files()

def gettime():
    global time_gap
    time_gap = float(timevar.get())
    return time_gap

def ss():
    time_gap = gettime()
    printit()

def stop_ss():
    global counter
    t.cancel()
    counter = 0
    ss_display.configure(text="Screenshot stopped")

#initialize gui
window_main = tkinter.Tk()
window_main.title("TopUmadol - Fan Counter")
window_main.geometry('300x340')
timer_text = Label(text= "Set the screenshot gap speed")
img = Image.open(urlopen("https://drive.google.com/uc?export=view&id=1BW7yA1awU8ck59DUcIv1gMbxW4lSZ0xf"))
icon = ImageTk.PhotoImage(img)
window_main.wm_iconphoto(False, icon)
ss_display = Label(window_main, text="")

#spinbox setting
timevar = StringVar(window_main)
timevar.set("2.5")
timer_spinbox = Spinbox(window_main, from_=0, to=5, increment=0.5, state="readonly", textvariable=timevar)

ss_button = tkinter.Button(window_main, text="Take screenshot", command=ss)
ss_button.config(width=20, height=2)
ss_stop_button = tkinter.Button(window_main, text="Force stop screenshot", command=stop_ss)
ss_stop_button.config(width=20, height=2)
scan_button = tkinter.Button(window_main, text="Scan screenshot", command=run_ss)
scan_button.config(width=20, height=2)
export_button = tkinter.Button(window_main, text="Export data", command=export_data)
export_button.config(width=20, height=2)
ss_display.pack()


#running the program
timer_text.pack(pady= 5)
timer_spinbox.pack(pady= 5) #spinbox button
ss_button.pack(pady= 10)
ss_stop_button.pack(pady=10)
scan_button.pack(pady= 10)
export_button.pack(pady= 10)
window_main.mainloop()
create_input_folder()

#ss_crop()
#list_fan()
#add_df()
#move_files()
#print(playerlist)
#print(fannum)