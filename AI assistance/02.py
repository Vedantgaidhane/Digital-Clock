import pyttsx3
import datetime
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()
 
def wish():
    # hour=int(datetime.datetime.now().hour())
    hour = 1
    if hour>=0 and hour<=12:
        speak("shoe prabhat")
    elif hour>=12 and hour<=6:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis , How may i help you!")
    
if __name__=="__main__":
    wish()