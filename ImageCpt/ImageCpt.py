# A screenshot-capturing toy
# Author: Icey

# You may have to run the following line in your terminal to install PIL:
# pip install pillow

# BTW I'm not sure if python has win32api initially.

import win32api,win32gui,win32con,time
from PIL import ImageGrab

# Label Definition
label = "Name of Target Window"

# Loops Definition
loops = 404

# Getting Handle
hdl = win32gui.FindWindow(None,label)

# Special Position Definition
nxtpos = (423, 65)
luapos = (752,118)
rdapos = (1453,1012)

# Set window to the front
win32gui.SetForegroundWindow(hdl)

# Loop & Screenshot
for i in range(pages):
    img = ImageGrab.grab(bbox=(752,118,1453,1012))
    img.save("%d.jpg"%i)

    win32api.SetCursorPos(nxtpos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
    time.sleep(0.5)
    
    
