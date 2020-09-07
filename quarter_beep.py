from asyncio import subprocess
import subprocess
import time
from time import sleep
from playsound import playsound


time_call = time.strftime('%H.%M')

def quarter_beep():
        playsound('D:\Documents Bulk\Sounds\windows_8_unlock.mp3')