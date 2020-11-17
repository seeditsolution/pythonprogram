import os
import pyttsx3
import datetime

today = datetime.date.today()

pyttsx3.speak("Hello user, please provide your name")
a = input("Enter your name : ")
print()
print("Hello "+ a)
pyttsx3.speak("Hello"+a)
pyttsx3.speak("I am Jarvis")
pyttsx3.speak("I am an AI Assistant and can perform a few tasks for you !")
print("I am Jarvis and I am an AI Assitant and can perform a few tasks for you !")
pyttsx3.speak("Today's Date is :")
pyttsx3.speak(today)
print("Today's Date is :")
print(today)


pyttsx3.speak("I will help you to, open Chrome, Windows Media Player, Calculator, Notepad, Control Panel, Settings. If you want, I can also open Lightroom , Spotify or Zoom App for you")
pyttsx3.speak("So, tell me"+a+"what can I do for you ? ")


while True:
 p=input("Kindly give me a task to perform :  ")
 p=p.lower()
 
 
 if(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("run" in p) or ("execute" in p) or ("open" in p))
and (("chrome" in p) or ("browser" in p) or ("search engine" in p) or ("google" in p))):
     pyttsx3.speak("Opening Google Chrome")
     os.system("chrome")

 

 elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("run" in p) or ("execute" in p) or ("open" in
p)) and (("player" in p) or ("media player" in p) or ("audio player" in p) or ("video player" in p))):
     pyttsx3.speak("Opening Windows Media Player")
     os.system("wmplayer")



 elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("run" in p) or ("execute" in p) or ("open" in
p)) and (("editor" in p) or ("notepad" in p) or ("text editor" in p) or ("writer" in p))):
     pyttsx3.speak("Opening Notepad")
     os.system("notepad")


 elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("open" in p) or ("run" in p) or ("execute" in
p)) and (("control panel" in p) or ("hardware settings" in p) or ("software settings" in p) or ("user control settings" in p)
or ("controlpanel" in p))):
     pyttsx3.speak("Opening Control Panel")
     os.system("control panel")


 elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("open" in p) or ("run" in p) or ("want" in
p)) and (("lightroom" in p) or ("edit" in p) or ("picture" in p))):
     pyttsx3.speak("Opening Adobe Lightroom")
     os.system("lightroom")


 elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("open" in p) or ("run" in p) or ("execute" in
p)) and (("computer settings" in p) or ("settings" in p) or ("pc settings" in p))):
     pyttsx3.speak("Opening System Settings")
     os.system("start ms-settings:")



 elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("open" in p) or ("play" in p) or ("want" in
p)) and (("spotify" in p) or ("music" in p) or ("song" in p))):
     pyttsx3.speak("Opening Spotify")
     os.system("spotify")



 elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("open" in p) or ("play" in p) or ("want" in
p)) and (("calculator" in p) or ("add" in p) or ("subtract" in p) or ("multiply" in p) or ("divide" in p) or ("numbers" in p))):
     pyttsx3.speak("Opening Calculator")
     os.system("calc")



 elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("run" in p) or ("execute" in p) or ("open" in p))
and (("video call" in p) or ("zoom app" in p) or ("zoom" in p) or ("video conference" in p))):
     pyttsx3.speak("Opening Zoom App")
     os.system("zoom")
     


 elif("exit" in p) or ("close" in p) or ("quit" in p):
     pyttsx3.speak("Thank you Sir, goodbye, have a nice day ahead")
     print("Thank you Sir, goodbye, have a nice day ahead.")
     break


 else:
     pyttsx3.speak("I don't know how to do this")
     print("Try again !")
