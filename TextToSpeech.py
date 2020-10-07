#create a .txt file(text123.txt here) and enter the text that should be converted into speech.
#save the .txt file in the same directory where this .py program is saved.


from gtts import gTTS
import os
import re
f=open('text123.txt')
f=f.read()
audio=gTTS(text=f,lang='en',slow=True)
audio.save('text123.wav')
os.system('text123.wav')
