from tkinter import *

window = Tk()
window.title("Push-up Quest")

#Question for user
question = Label(window, text="Age")
question.grid(row=0,column=0)

question = Label(window, text="Gender")
question.grid(row=0,column=2)

question = Label(window, text="Height")
question.grid(row=1,column=0)

question = Label(window, text="Weight")
question.grid(row=1,column=2)

#User input here
age_text=StringVar()
answer1 = Entry(window, textvariable=age_text)
answer1.grid(row=0, column=1)


gender_text=StringVar()
answer2 = Entry(window, textvariable=gender_text)
answer2.grid(row=0, column=3)


height_text=StringVar()
answer3 = Entry(window, textvariable=height_text)
answer3.grid(row=1, column=1)


weight_text=StringVar()
answer4 = Entry(window, textvariable=weight_text)
answer4.grid(row=1, column=3)

#Box
box1 = Text(window, height=6, width=35, borderwidth=3)
box1.grid(row=2, column=0, rowspan=6, columnspan=2)

def Calculate():
    box1.insert(INSERT,str(height_text.get()))
    

def Close():
    exit()

#Button
button1 = Button(window,text="Calculate", width=12, command=Calculate)
button1.grid(row=3, column=3)

button2 = Button(window,text="Close", width=12, command=Close)
button2.grid(row=5, column=3)


window.mainloop()