#pip install pyautogui
import pyautogui

#pip install pytesseract
import pytesseract

import os

#pip install PIL
from PIL import Image

import random

import time

i=0

# https://github.com/UB-Mannheim/tesseract/wiki 

#Download tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe (64 bit) resp.

while True:

    screenshot = pyautogui.screenshot(region=(0,778, 1376, 776))

    file_name=str(i)+".png"

    screenshot.save(file_name)

    print("Scan ",file_name)

    i+=1

    pytesseract.pytesseract.tesseract_cmd=r"path_where_you_install_the_file\tesseract.exe"

    img=Image.open(file_name)

    scan_text=pytesseract.image_to_string(img)

    get_text=scan_text.split()

    target_text=["alex","Alex","alex.","ALEX.","Alex?","Alex.","l x","lx","L X""Lx","Lx.","lx."]

    output = ["hmm","net slow","yes","yes sir","sir sona jache na","sir arekbar repeat korun","net kub slow","hmmm"]

    choice=random.choice(output)

    for target in get_text:

        if target in target_text:

            pyautogui.click(x=1525, y=1023)

            pyautogui.write(choice)#, interval=0.25) 

            pyautogui.press('enter') 

            time.sleep(4)

            print("ok we got it")

            continue

    os.remove(file_name)

    print("Destroy ",file_name)

    
