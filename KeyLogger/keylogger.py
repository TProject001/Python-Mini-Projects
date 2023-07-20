import pynput
from pynput.keyboard import Key,Listener
def on_press(key):
    print("{} key pressed".format(key))
def on_released(key):
    if key==key.esc:
        return false   # return true  #same result (i have dout)
with Listener(on_press=on_press , on_released=on_released) as listener:
    listener.join()
