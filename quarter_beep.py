from asyncio import subprocess
import subprocess
import time
from playsound import playsound

def quarter_beep():
    playsound('D:\Documents Bulk\Sounds\windows_8_unlock.mp3')

hour_call = time.strftime('%H')
minute_call = time.strftime('%M')

if int(hour_call) in range(0,8):
        if int(minute_call) == 00 or 15 or 30 or 45:
                print(hour_call+':'+minute_call)
                quarter_beep()
                time.sleep(870)
        else:
                time.sleep(1)
else:
        time.sleep(50370)