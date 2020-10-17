# binding Events

from tkinter import *
def hello(event):
     print('Double click to exit')

def quit(event):
     print('caught a double click,leaving')
     import sys; sys.exit()

Widget = Button(None,text='Hello event world')
Widget.pack()
Widget.bind('<Button-1>',hello)
Widget.bind('<Double-1>',quit)
Widget.mainloop()
