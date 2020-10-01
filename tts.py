import pyttsx3
engine = pyttsx3.init()
speak=input("enter any text you want to listen ")
engine.say(speak)
engine.runAndWait()