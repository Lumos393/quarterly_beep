from pickle import FALSE
import time
from playsound import playsound
import pause
from datetime import datetime

mornran = range(0, 8)
dayran = range(8, 19)
nightran = range(19, 24)
minarr = [0, 15, 30, 45]

hour_call = time.strftime('%H')
int_hour_call = int(time.strftime('%H'))
minute_call = time.strftime('%M')
int_minute_call = int(time.strftime('%M'))

print(hour_call + ':' + minute_call)

for int_hour_call in dayran:
        if int_minute_call in minarr:  
                print(hour_call, minute_call)
                playsound('D:\Documents Bulk\Sounds\windows_8_unlock.mp3')
                time.sleep(870)
        elif((int_hour_call in (range(0, 8) or range(19, 24))) and ((int_minute_call in minarr) == FALSE)):
                print('Waiting...')
                time.sleep(1) or range(0, 8)
else:
        if int_hour_call in (mornran or nightran):
                print('Long sleep...')
                time.sleep(1)