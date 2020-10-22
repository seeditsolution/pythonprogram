import PySimpleGUI as sg
import webbrowser as wb
from datetime import *

sg.theme('GreenMono') 
sg.ChangeLookAndFeel('GreenMono')

layout = [[sg.Text('Persistent window')],
          [sg.Text('Value A'),sg.InputText(key='-IN-'),sg.Text('Value A'),sg.InputText(key='-IN2-')],
          [sg.Button('Read'), sg.Exit()],
         [sg.Text('Enter Url'),sg.InputText(key='-URL-'),sg.Button('open')]]   

date_ = datetime.now()
now_ = date_.split(' ')
window = sg.Window('Window that stays open', layout, now_[0]) 

event, values = window.read()

text_input, text2 = values['-IN-'], values['-IN2-']
sg.popup('You entered', text_input, text2)

url = values['-URL-']
wb.open(url)
window.close()
