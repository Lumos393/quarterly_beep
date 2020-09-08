from os import path
from pydub import AudioSegment

src = 'D:\Documents Bulk\Sounds\windows_8_unlock.mp3'
dst = 'D:\Documents Bulk\Sounds\windows_8_unlock.wav'

sound = AudioSegment.from_mp3(src)
sound.export(dst, format='wav')
