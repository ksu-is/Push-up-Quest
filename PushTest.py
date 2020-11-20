from tkinter import Tk, END, Entry, Label, StringVar, INSERT, Button, Text, Listbox
import pygame

window = Tk()
window.title("Push-up Quest")

pygame.mixer.init()

def Music():
    pygame.mixer.music.load("Not_Weeb_Music.mp3")
    pygame.mixer.music.play(loops=0)

#Question for user
question = Label(window, text="Name")
question.grid(row=0,column=0)

question = Label(window, text="Sex (M/F)")
question.grid(row=0,column=2)

question = Label(window, text="Age")
question.grid(row=1,column=0)

question = Label(window, text="Weight")
question.grid(row=1,column=2)

#User input here
name_text=StringVar()
answer1 = Entry(window, textvariable=name_text)
answer1.grid(row=0, column=1)


gender_text=StringVar()
answer2 = Entry(window, textvariable=gender_text)
answer2.grid(row=0, column=3)


age_text=StringVar()
answer3 = Entry(window, textvariable=age_text)
answer3.grid(row=1, column=1)


weight_text=StringVar()
answer4 = Entry(window, textvariable=weight_text)
answer4.grid(row=1, column=3)

#Box
box1 = Text(window, height=6, width=40, borderwidth=3)
box1.grid(row=2, column=0, rowspan=6, columnspan=2)

def Calculate():

    box1.delete('1.0', END)
    box1.insert(INSERT,"\n"+"Hello, " + str(name_text.get()))
    pushup_calorie = 0.36

    if str(gender_text.get()) == "M":
        
        if int(age_text.get()) < 18:
            if int(weight_text.get()) < 140:
                pushups_done = 26
                box1.insert(INSERT,"\n" + "Your quest today is 26 push-ups" )
            elif int(weight_text.get()) < 180:
                pushups_done = 27
                box1.insert(INSERT,"\n" + "Your quest today is 27 push-ups" )
            else:
                pushups_done = 25
                box1.insert(INSERT,"\n" + "Your quest today is 25 push-ups" )
            
        elif int(age_text.get()) < 24:
            if int(weight_text.get()) < 140:
                pushups_done = 23
                box1.insert(INSERT,"\n" + "Your quest today is 23 push-ups" )
            elif int(weight_text.get()) < 180:
                pushups_done = 24
                box1.insert(INSERT,"\n" + "Your quest today is 24 push-ups" )
            else:
                pushups_done = 22
                box1.insert(INSERT,"\n" + "Your quest today is 22 push-ups" )

        elif int(age_text.get()) < 34:
            if int(weight_text.get()) < 140:
                pushups_done = 18
                box1.insert(INSERT,"\n" + "Your quest today is 18 push-ups" )
            elif int(weight_text.get()) < 180:
                pushups_done = 19
                box1.insert(INSERT,"\n" + "Your quest today is 19 push-ups" )
            else:
                pushups_done = 17
                box1.insert(INSERT,"\n" + "Your quest today is 17 push-ups" )

        elif int(age_text.get()) < 44:
            if int(weight_text.get()) < 140:
                pushups_done = 15
                box1.insert(INSERT,"\n" + "Your quest today is 15 push-ups" )
            elif int(weight_text.get()) < 180:
                pushups_done = 16
                box1.insert(INSERT,"\n" + "Your quest today is 16 push-ups" )
            else:
                pushups_done = 14
                box1.insert(INSERT,"\n" + "Your quest today is 14 push-ups" )

        elif int(age_text.get()) < 54:
            if int(weight_text.get()) < 140:
                pushups_done = 13
                box1.insert(INSERT,"\n" + "Your quest today is 13 push-ups" )
            elif int(weight_text.get()) < 180:
                pushups_done = 14
                box1.insert(INSERT,"\n" + "Your quest today is 14 push-ups" )
            else:
                pushups_done = 12
                box1.insert(INSERT,"\n" + "Your quest today is 12 push-ups" )

        elif int(age_text.get()) < 63:
            if int(weight_text.get()) < 140:
                pushups_done = 11
                box1.insert(INSERT,"\n" + "Your quest today is 11 push-ups" )
            elif int(weight_text.get()) < 180:
                pushups_done = 12
                box1.insert(INSERT,"\n" + "Your quest today is 12 push-ups" )
            else:
                pushups_done = 10
                box1.insert(INSERT,"\n" + "Your quest today is 10 push-ups" )
        
        else:
            box1.insert(INSERT,"\n" + "Your too old for this quest")
        
    elif str(gender_text.get()) == "F":

        if int(age_text.get()) < 18:
            if int(weight_text.get()) < 120:
                pushups_done = 16
                box1.insert(INSERT,"\n" + "Your quest today is 16 push-ups" )
            elif int(weight_text.get()) < 160:
                pushups_done = 17
                box1.insert(INSERT,"\n" + "Your quest today is 17 push-ups" )
            else:
                pushups_done = 15
                box1.insert(INSERT,"\n" + "Your quest today is 15 push-ups" )

        elif int(age_text.get()) < 24:
            if int(weight_text.get()) < 120:
                pushups_done = 17
                box1.insert(INSERT,"\n" + "Your quest today is 17 push-ups" )
            elif int(weight_text.get()) < 160:
                pushups_done = 18
                box1.insert(INSERT,"\n" + "Your quest today is 18 push-ups" )
            else:
                pushups_done = 16
                box1.insert(INSERT,"\n" + "Your quest today is 16 push-ups" )

        elif int(age_text.get()) < 34:
            if int(weight_text.get()) < 120:
                pushups_done = 15
                box1.insert(INSERT,"\n" + "Your quest today is 15 push-ups" )
            elif int(weight_text.get()) < 160:
                pushups_done = 16
                box1.insert(INSERT,"\n" + "Your quest today is 16 push-ups" )
            else:
                pushups_done = 14
                box1.insert(INSERT,"\n" + "Your quest today is 14 push-ups" )

        elif int(age_text.get()) < 44:
            if int(weight_text.get()) < 120:
                pushups_done = 12
                box1.insert(INSERT,"\n" + "Your quest today is 12 push-ups" )
            elif int(weight_text.get()) < 160:
                pushups_done = 13
                box1.insert(INSERT,"\n" + "Your quest today is 13 push-ups" )
            else:
                pushups_done = 11
                box1.insert(INSERT,"\n" + "Your quest today is 11 push-ups" )

        elif int(age_text.get()) < 54:
            if int(weight_text.get()) < 120:
                pushups_done = 10
                box1.insert(INSERT,"\n" + "Your quest today is 10 push-ups" )
            elif int(weight_text.get()) < 160:
                pushups_done = 11
                box1.insert(INSERT,"\n" + "Your quest today is 11 push-ups" )
            else:
                pushups_done = 9
                box1.insert(INSERT,"\n" + "Your quest today is 9 push-ups" )

        elif int(age_text.get()) < 63:
            if int(weight_text.get()) < 120:
                pushups_done = 8
                box1.insert(INSERT,"\n" + "Your quest today is 8 push-ups" )
            elif int(weight_text.get()) < 160:
                pushups_done = 9
                box1.insert(INSERT,"\n" + "Your quest today is 9 push-ups" )
            else:
                pushups_done = 7
                box1.insert(INSERT,"\n" + "Your quest today is 7 push-ups" )

        else: 
            box1.insert(INSERT,"\n" + "Your too old for this quest" )
        
    else:
        box1.insert(INSERT,"\n" + "Please fill the box." )
    

    def Done():

        push1 = str(pushups_done * pushup_calorie)
        box1.insert(INSERT,"\n" + "\n" + "Total calorie burn: " + push1)


    button2 = Button(window,text="Quest Done?", width=12, command=Done)
    button2.grid(row=4, column=3)

def Close():
    exit()

#Button
button1 = Button(window,text="Calculate", width=12, command=Calculate)
button1.grid(row=3, column=3)

button3 = Button(window,text="Close", width=12, command=Close)
button3.grid(row=6, column=3)

button3 = Button(window,text="Music", width=12, command=Music)
button3.grid(row=5, column=3)

window.mainloop()