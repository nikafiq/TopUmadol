import os.path
from PIL import Image
import glob
import re
import shutil

# Opens a image in RGB mode
#im = Image.open("pic/umamusume 2022_07_21 17_51_05.png")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
#width, height = im.size

# Setting the points for cropped image
#left = 150
#top = (height-30) / 2
#right = width - 150
#bottom = 3 * height / 4

# Cropped image of above dimension
# (It will not change original image)
#im1 = im.crop((left, top, right, bottom))

# Shows the image in image viewer
#im1.save("pic/crop/img.png","png")

#cropping
def image_crop(x):
    width, height = x.size

    left = 150
    top = (height - 30) / 2
    right = width - 150
    bottom = 3 * height / 4

    im1 = x.crop((left, top, right, bottom))
    return im1

#changing glob format to enumerate
def glob_enumerate(x):
    p = re.compile('[0-9]+')
    a = p.findall(x)
    s = [str(integer) for integer in a]
    a_string = "".join(s)
    y = int(a_string)
    return y

#renaming cropped pictures
def ss_crop():
    path = 'pic/crop'
    pathexist = os.path.exists(path)
    if not pathexist:
        os.makedirs(path)
        #print('Created /crop directory because it does not exist',end='\n\n')
    for i in glob.iglob("pic/*.png"):
        im=Image.open(i)
        j = glob_enumerate(i)
        image_crop(im).save(f'pic/crop/img{j}.png','png')


def make_unique_filename(file_path):
    duplicate = 0
    base, extension = os.path.splitext(file_path)
    while os.path.exists(file_path):
        duplicate += 1
        file_path = f'{base}{duplicate}'
    return file_path

def move_files():
    path = 'pic/day0'
    pathexist = os.path.exists(path)
    if pathexist:
        newname = make_unique_filename(path)
        os.makedirs(newname)
        for images in glob.iglob('pic/*png'):
            shutil.move(images,newname)
        shutil.move('pic/crop',newname)
    else:
        os.makedirs(path)
        for images in glob.iglob('pic/*png'):
            shutil.move(images,path)
        shutil.move('pic/crop',path)
