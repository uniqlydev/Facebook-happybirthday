import pyautogui as pg
import time
import random
import json as js


def GetMessage(birthday_quotes):
    # Randomly select from msg then remove it
    msg = random.choice(birthday_quotes['quotes'])
    birthday_quotes['quotes'].remove(msg)
    return msg

def OpenJson(jsonFilename):
    with open(jsonFilename) as file:
        return js.load(file)
    

config = OpenJson("config.json")



# Update these settings in config.json
# Loading the config files
postXY = (config['postXY']['x'],config['postXY']['y']) 
postXY_Assurance = (config['postXY_Assurance']['x'],config['postXY_Assurance']['y'])
postButton = (config['postButton']['x'],config['postButton']['y'])
birthday_quotes = OpenJson("quotes.json")

length = len(birthday_quotes['quotes'])
counter = 0 # Counter for the number of posts

time.sleep(5)

while True:
    pg.click(postXY[0],postXY[1]) # Press the post textbox
    time.sleep(0.5)
    pg.click(postXY_Assurance[0],postXY_Assurance[1]) # Press the text box for assurance
    pg.typewrite(GetMessage(birthday_quotes))
    pg.typewrite(f" -  {counter+1}/{length}")
    pg.click(postButton[0],postButton[1]) # Press the post button
    time.sleep(2.5)
    pg.hotkey('command','r',interval=0.25) # Close the window
    counter += 1
    time.sleep(3600) # Refresh the page may take time.

