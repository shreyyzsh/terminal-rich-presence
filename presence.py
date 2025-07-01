
import time
import psutil
from pypresence import Presence

CLIENT_ID = 1355846448343683203

def checkTerminalStatus():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'iTerm2':
            return True
    return False


timeOfStart = time.time()

while checkTerminalStatus():
    
    try:
        rpc = Presence(CLIENT_ID)
        rpc.connect()  
        rpc.update(
            start=timeOfStart,
            state="On iTerm2",
            large_image="iterm-big",
            small_image=None,
            large_text=None,
            details="Running zsh"
        )
        #print("Connected Successfully.")
        time.sleep(30)
    
    except:
        print("Connection Failed.")
        pass
    
    
        
