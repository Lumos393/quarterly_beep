import sys
import os
from pickle import FALSE
import time
import subprocess
from playsound import playsound
from datetime import datetime
import decouple

mornran = range(0, 8)
dayran = range(8, 19)
nightran = range(19, 24)
minarr = [0, 15, 30, 45]

hour_call = time.strftime('%H')
int_hour_call = int(time.strftime('%H'))
minute_call = time.strftime('%M')
int_minute_call = int(time.strftime('%M'))

print(hour_call + ':' + minute_call)

for x in dayran:
        if int_minute_call in minarr:
                print(hour_call, minute_call)
                playsound('D:\Documents Bulk\Sounds\windows_8_unlock.mp3')
                time.sleep(870)
        if((int_hour_call in (range(0, 8) or range(19, 24))) and ((int_minute_call in minarr) == FALSE)):
                print('Waiting...')
                time.sleep(1) or range(0, 8)
        if int_hour_call in (mornran or nightran):
                print('Nighty night')
                time.sleep(1)