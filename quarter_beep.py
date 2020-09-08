import sys
import os
import time
import subprocess
import numpy
from numpy.ma.core import array
import winsound

hourarr = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
minarr = [0, 15, 30, 45]

while True:
        int_hour_call = int(time.strftime('%H'))
        int_minute_call = int(time.strftime('%M'))

        if (int_hour_call in hourarr) and (int_minute_call in minarr):
                winsound.PlaySound('D:\Documents Bulk\Sounds\windows_8_unlock.mp3')
                time.sleep(60)
        if (int_minute_call not in minarr):
                time.sleep(5)
        if (int_hour_call not in hourarr):
                time.sleep()