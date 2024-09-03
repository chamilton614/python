import pyautogui
import time
import random

while True:
    # x = random.randint(0,1000)
    # y = random.randint(0,1000)
    # pyautogui.moveTo(x,y)
    pyautogui.click()
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    # print('Clicked at ' + str(result) + ' ('  + str(x) + ', ' + str(y) + ')')
    print('Clicked at ' + str(result) + ')')
    time.sleep(90)