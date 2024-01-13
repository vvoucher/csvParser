import time
from time import strftime

def delay_terminal(dt):
    sleepTime = dt
    now = strftime("%H:%M:%S")
    print(now,"To okno zamknie się za ", sleepTime,"sekund")
    time.sleep(sleepTime)