from tkinter import*


def bttnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def bttnClear():
    global operator
    operator = ""
    text_input.set("")

def bttnEquals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

calc = Tk()
calc.title("Calculator")
operator = ""
text_input = StringVar()

textDisplay = Entry(calc, font = ('arial', 20, 'bold'), textvariable = text_input, bd = 30, insertwidth = 4, bg = 'powder blue', justify = 'right').grid(columnspan = 4)


#=============================================FIRST ROW==========================================================================#
button_7 = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '7', bg = 'powder blue', command = lambda:bttnClick(7)).grid(row = 1, column = 0)

button_8 = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '8', bg = 'powder blue', command = lambda:bttnClick(8)).grid(row = 1, column = 1)

button_9 = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '9', bg = 'powder blue', command = lambda:bttnClick(9)).grid(row = 1, column = 2)

Addition_button = Button(calc, padx = 16,pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '+', bg = 'powder blue', command = lambda:bttnClick('+')).grid(row = 1, column = 3)

#===============================================SECOND ROW==========================================================================#

button_4 = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '4', bg = 'powder blue', command = lambda:bttnClick(4)).grid(row = 2, column = 0)

button_5 = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '5', bg = 'powder blue', command = lambda:bttnClick(5)).grid(row = 2, column = 1)

button_6 = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '6', bg = 'powder blue', command = lambda:bttnClick(6)).grid(row = 2, column = 2)

Subtraction_button = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '-', bg = 'powder blue', command = lambda:bttnClick('-')).grid(row = 2, column = 3)

#===============================================THIRD ROW==========================================================================#

button_3 = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '3', bg = 'powder blue', command = lambda:bttnClick(3)).grid(row = 3, column = 0)

button_2 = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '2', bg = 'powder blue', command = lambda:bttnClick(2)).grid(row = 3, column = 1)

button_1 = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '1', bg = 'powder blue', command = lambda:bttnClick(1)).grid(row = 3, column = 2)

Multiplication_button = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '*', bg = 'powder blue', command = lambda:bttnClick('*')).grid(row = 3, column = 3)


#===============================================THIRD ROW==========================================================================#

button_0 = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '0', bg = 'powder blue', command = lambda:bttnClick(0)).grid(row = 4, column = 0)

button_Clear = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = 'Clr', bg = 'powder blue', command = bttnClear).grid(row = 4, column = 1)

button_Equals = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '=', bg = 'powder blue', command = bttnEquals).grid(row = 4, column = 2)

Division_button = Button(calc, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '/', bg = 'powder blue', command = lambda:bttnClick('/')).grid(row = 4, column = 3)




calc.mainloop()