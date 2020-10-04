import speech_recognition as pr
import webbrowser
pr.Microphone(device_index=1)
r=pr.Recognizer()
r.energy_threshold=5000
with pr.Microphone() as source:
    print("Say something")
    au=r.listen(source)
    try:
        t=r.recognize_google(au)
        t=hello
        print("You said :() ".format(text))
        url="https://www.google.com/search?q="
        aurl=url+t
        webbrowser.open(aurl)
    except:
        print("Say again")
