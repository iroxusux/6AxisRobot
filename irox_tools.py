import os

def ClearConsole():
    clear = lambda: os.system('clear')
    clear()
    

def Toggle(event, toggle, one_shot):
    if not toggle:
        one_shot = False
    
    if (one_shot == False) and (toggle == True):
        one_shot = True
        if event:
            event = False
            return event, one_shot
        if not event:
            event = True
            return event, one_shot
    return event, one_shot