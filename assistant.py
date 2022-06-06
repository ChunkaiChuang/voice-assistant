import speech_recognition as sr   # speech to text
import os 
from pygame import mixer
from gtts import gTTS



def bot_listen():
    recog=sr.Recognizer()
    with sr.Microphone() as source:
        audioData = recog.listen(source)
    try:
        text=recog.recognize_google(audioData, language='zh-tw')
        return text
    except:
        return 
        
question = bot_listen()
print(question)

mixer.init()
if not os.path.isfile('tmp.mp3'):
    tts=gTTS(text=' ', lang='zh-tw')
    tts.save('tmp.mp3')
    print('已產生不重要的影音檔 tmp.mp3')

def bot_speak(text, lang):
    try:
        mixer.music.load('tmp.mp3')
        tts=gTTS(text=text, lang=lang)
        tts.save('speak.mp3')
        mixer.music.load('speak.mp3')
        mixer.music.play()
        while(mixer.music.get_busy()):
            continue
        
    except:
        print('Failed')
        
if question=='臭妹妹':
    bot_speak('我是超級臭妹妹','zh-tw')
