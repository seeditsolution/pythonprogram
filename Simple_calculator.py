from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    # print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
        pass
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root=Tk()
root.geometry("200x400")
root.title("Calculator")
root.maxsize(200,400)
root.config(bg="black")
root.wm_iconbitmap("download.ico")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 20 bold",bg="white",fg="black")
screen.pack(fill=X,ipadx=6,pady=4,padx=6)

f1=Frame(root,bg="black",width=10)
f1.pack()
b=Button(f1,text="7",padx=6,pady=4,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=6,pady=4)
b.bind("<Button-1>",click)

b=Button(f1,text="8",padx=6,pady=4,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=6,pady=4)
b.bind("<Button-1>",click)

b=Button(f1,text="9",padx=6,pady=4,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=6,pady=4)
b.bind("<Button-1>",click)

f1=Frame(root,bg="black")
f1.pack()
b=Button(f1,text="4",padx=6,pady=4,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=6,pady=4)
b.bind("<Button-1>",click)

b=Button(f1,text="5",padx=6,pady=4,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=6,pady=4)
b.bind("<Button-1>",click)

b=Button(f1,text="6",padx=6,pady=4,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=6,pady=4)
b.bind("<Button-1>",click)

f1=Frame(root,bg="black")
f1.pack()
b=Button(f1,text="1",padx=6,pady=4,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=6,pady=4)
b.bind("<Button-1>",click)

b=Button(f1,text="2",padx=6,pady=4,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=6,pady=4)
b.bind("<Button-1>",click)

b=Button(f1,text="3",padx=6,pady=4,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=6,pady=4)
b.bind("<Button-1>",click)

f1=Frame(root,bg="black")
f1.pack()
b=Button(f1,text="0",padx=6.1,pady=4,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=6.2,pady=4)
b.bind("<Button-1>",click)

b=Button(f1,text="+",padx=5.6,pady=4,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=5.5,pady=3)
b.bind("<Button-1>",click)

b=Button(f1,text="-",padx=6.5,pady=3,font="lucida 16 bold",bg="orange")
b.pack(side=LEFT,padx=6,pady=3)
b.bind("<Button-1>",click)

f1=Frame(root,bg="black")
f1.pack()
b=Button(f1,text="*",padx=6.5,pady=3,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=6.3,pady=4)
b.bind("<Button-1>",click)

b=Button(f1,text="/",padx=7,pady=3,font="lucida 16 bold",bg="orange")
b.pack(side=LEFT,padx=7,pady=3)
b.bind("<Button-1>",click)

b=Button(f1,text="%",padx=2.5,pady=4,font="lucida 14 bold",bg="orange")
b.pack(side=LEFT,padx=6.1,pady=5)
b.bind("<Button-1>",click)

f1=Frame(root,bg="black")
f1.pack()
b=Button(f1,text="C",padx=6.3,pady=6,font="lucida 13 bold",bg="orange")
b.pack(side=LEFT,padx=6.1,pady=3)
b.bind("<Button-1>",click)

b=Button(f1,text=".",padx=6.8,pady=0.7,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=6.8,pady=3)
b.bind("<Button-1>",click)

b=Button(f1,text="=",padx=6.1,pady=1,font="lucida 15 bold",bg="orange")
b.pack(side=LEFT,padx=6.3,pady=3)
b.bind("<Button-1>",click)


root.mainloop()
