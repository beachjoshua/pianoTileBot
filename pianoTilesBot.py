import keyboard
import mss
import cv2
import numpy
from time import time, sleep
import pyautogui

pyautogui.PAUSE = 0

print("Press 's' to start.")
print("Press 'q' to quit.")
keyboard.wait('s')
left = True
sct = mss.mss()
dimensions = {
        'left': 10,
        'top': 1000,
        'width': 850,
        'height': 500
    }

x,y = 700, 1200
tile = cv2.imread('tile3.png')
w = tile.shape[1]
h = tile.shape[0]


#fpsTime = time()
#spyautogui.FAILSAFE = False
fpsTime = time()
while True:
    if keyboard.is_pressed('q'):
        break
    scr = numpy.array(sct.grab(dimensions))
    #Cut off alpha
    scrRemove = scr[:,:,:3]
    result = cv2.matchTemplate(scrRemove, tile, cv2.TM_CCOEFF_NORMED)
    
    _, maxVal, _, maxLoc = cv2.minMaxLoc(result)
    print(f"Max Val: {maxVal} Max Loc: {maxLoc}")
    src = scr.copy()
    if maxVal >= 0.9:
        #print("NOWSWITCHC\n")
        scr = cv2.rectangle(scr, maxLoc, (maxLoc[0] + w, maxLoc[1] + h), (0,255,255), 2)
        #sleep(.12)
        x = maxLoc[0]+w//2
        y = maxLoc[1]+dimensions['top']
        pyautogui.click(x=x, y=y)
    
    cv2.imshow('Screen Shot', scr)
    cv2.waitKey(1)
    
    #sleep(.12)
    print('FPS: {}'.format(1 / (time() - fpsTime)))
    fpsTime = time()