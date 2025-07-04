
import time
import psutil
from pypresence import Presence

CLIENT_ID = 1355846448343683203

def checkTerminalStatus():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'iTerm2':
            return True
    return False

def checkDiscordStatus():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'Discord':
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
        
        time.sleep(30)
    
    except:
        if not checkDiscordStatus():
            print('Discord Not Detected. Restart iTerm2 after opening discord.')
        else:
            print('Connection Failed.')
        
        break
            
        
    
    
        
