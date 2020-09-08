from os import path
from pydub import AudioSegment

src = 'D:\Documents Bulk\GitHub\quarterly_beep\windows_8_unlock.mp3'
dst = 'D:\Documents Bulk\GitHub\quarterly_beep\windows_8_unlock.wav'

sound = AudioSegment.from_mp3(src)
sound.export(dst, format='wav')
