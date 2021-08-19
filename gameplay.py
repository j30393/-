import pyautogui 
import time
import win32api , win32con
def presskey(key):
    win32api.keybd_event(key,0,0,0)
    time.sleep(0.01)
    win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0)

def press_spontaneously(key1,key2):
    win32api.keybd_event(key1,0,0,0)
    win32api.keybd_event(key2,0,0,0)
    time.sleep(0.01)
    win32api.keybd_event(key1,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(key2,0,win32con.KEYEVENTF_KEYUP,0)
    
while 1:
    p1 = 0
    p2 = 0
    try:
        p1 = pyautogui.pixel(595,415)[1]
        p2 = pyautogui.pixel(610,382)[1]
    except:
        p1 = pyautogui.pixel(595,415)[1]
        p2 = pyautogui.pixel(610,382)[1]       
    if(p1 in range(180,195)):
        if(p2 in range(180,195)):
            presskey(ord('D'))
        else:
            press_spontaneously(ord('D'),ord('K'))
    elif(p1 in range(65,75)):
        if(p2 in range(65,75)):
            presskey(ord('J'))
        else:
            press_spontaneously(ord('J'),ord('F')) 
    elif(p1 in range(115,125)):
        presskey(ord('D'))
        presskey(ord('J'))
    else:
        pass
        