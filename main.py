from selenium import webdriver
from moviepy.editor import *
import time
import cv2





FILE_NAME = "bad_apple.mp4" # file to play

cap = cv2.VideoCapture(FILE_NAME)



delay = 1/VideoFileClip(FILE_NAME).fps


cmd_ = "document.querySelectorAll(\"[data-ix='__x__']\")[__y__].style.background = '__color__';"

driver = webdriver.Chrome("/home/chromedriver")


driver.get("https://github.com/merwin-asm") # Github profile url
time.sleep(40)

def rgb2hex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'



def img_to_js(img):
 
    img = cv2.resize(img, (51, 7),interpolation = cv2.INTER_LINEAR)

    code = ""
    for y in range(0, 7):
        for x in range(0, 51):
            cmd = cmd_.replace("__x__", str(x))
            cmd = cmd.replace("__y__", str(y))
            cmd = cmd.replace("__color__", rgb2hex(img[y][x][2], img[y][x][1], img[y][x][0]))
            code+=cmd
    return code






t__ = time.time()

while(cap.isOpened()):
    z_1 = time.time()
    ret, frame = cap.read()
    if ret == True:
        f_ = img_to_js(frame)
        driver.execute_script(f_)
        z_2 = time.time()
        try:
            time.sleep(delay-(z_2-z_1))
        except:
            pass
    else:
        break



        
print("Time taken : ", time.time()-t__)


driver.close()

