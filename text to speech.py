#Created by Abhra Kanti Dubey
#Import pyttsx3 
#pip install pyttsx3

import tkinter as tk
from tkinter import *
import pyttsx3


engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



root=tk.Tk()
root.title("TEXT TO SPEECH")
root.geometry("600x200")
root.config(background="#67E6DC")
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def translate():
	audio=text1.get()
	speak(audio)

welcome=Label(
	root,
	text="TEXT TO SPEECH BY ABHRA",
	font=("Arial",20,"bold"),
	bg="#45CE30",
	fg="black",
	).pack()

enter_text=Label(
	root,
	text="ENTER YOUR TEXT BELOW",
	font=("Arial",18,"bold"),
	bg="#FFF222",
	fg="black",
	relief=GROOVE
	).pack(padx=5,pady=5)

text1=StringVar()

text_area=Entry(
	root,
	font="Arial 18",
	width=30,
	textvariable=text1,
	).pack(padx=3,pady=5)

trans=Button(
	root,
	text="SPEAK",
	font=("Verdana",15,"bold"),
	bg="yellow",
	fg="RED",
	relief=SOLID,
	command=translate).pack(padx=5,pady=10)


root.mainloop()
