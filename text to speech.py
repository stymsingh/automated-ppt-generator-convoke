from gtts import gTTS
import os
tts = gTTS(text='Good morning satyam and kanika, welcome to hashhacks', lang='hi')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
 