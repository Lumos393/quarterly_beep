import sys
import os
import time
import subprocess
import numpy
from numpy.ma.core import array
from playsound import playsound
from datetime import datetime
import decouple

hourarr = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
minarr = [0, 15, 30, 45]

hour_call = time.strftime('%H')
int_hour_call = int(time.strftime('%H'))
minute_call = time.strftime('%M')
int_minute_call = int(time.strftime('%M'))

while True:
        if int_minute_call in minarr:
                print(hour_call, minute_call)
                playsound('D:\Documents Bulk\Sounds\windows_8_unlock.mp3')
                time.sleep(870)
        if((int_hour_call in hourarr) and ((int_minute_call in minarr) == False)):
                print('Waiting...')
        if (int_hour_call in hourarr) == False:
                print('.')