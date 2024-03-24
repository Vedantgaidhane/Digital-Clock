import pyttsx3
engine = pyttsx3.init()
engine.say('hiiiii')
engine.runAndWait()
voice=engine.getproperty('voices')
engine=voice.setproperty('voice',voice[0].id)