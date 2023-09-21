from tkinter import *
import speech_recognition as sr
import pandas as pd
import random as rand
import re
import os
from gtts import gTTS
from playsound import playsound
import tkinter.messagebox

uc=[]
c=0

# Speech Recognition
def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source, timeout=2)
        # try:
        text = r.recognize_google(audio)
        print(text)
        dataset(text)  
              
        # except: 
        #     tkinter.messagebox.showwarning("Oops!", "Didn't Catch That, Please Try Again!")
    os.remove("country.mp3")          
# Dataset
def dataset(text):  

    df = pd.read_json('country.json')
    l=len(text)
    v='^'+text[l-1]+'[a-z]*'
    country = df.loc[df['name'].str.contains(v, flags=re.I, regex=True)]         
    country_lt = country.values.tolist()
    l2=len(country_lt)
    n=rand.randint(0,(l2-1))
    c=country_lt[n]
    name = c[0]
    l3=len(name)
    if text[0]=='S' or text[0]==name[l3-1]:
        if name in uc or text in uc:
            tkinter.messagebox.showwarning("Oops!", "Name already used!")
            language = 'en'
            myobj = gTTS(text=c[0], lang=language, slow=False) 
            myobj.save("country.mp3") 
        else:
            lab1 = Label(top, text= "###############################################", font=("Poppins Light", 25), bg='#541D69', fg='#541D69')
            lab1.place(x=110,y=180)

            user_a = Label(top, text= text, font=("Poppins Light", 20), bg='#541D69', fg='#FFFFFF')
            user_a.place(x=110,y=180)
            
            lab2 = Label(top, text= "###############################################", font=("Poppins Light", 25), bg='#541D69', fg='#541D69')
            lab2.place(x=100,y=230)
            bot_a = Label(top, text= name, font=("Poppins Light", 20), bg='#541D69', fg='#FFFFFF')
            bot_a.place(x=100,y=230)
            print(name) 
            uc.append(name+",")
            uc.append(text+",")
            language = 'en'
            myobj = gTTS(text=name, lang=language, slow=False)  
            myobj.save("country.mp3") 
            playsound("country.mp3") 

    else:
        return

def words():
    tkinter.messagebox.showinfo("Words Used",uc)

def howto():
    w = Tk()

    # Window Code
    w.geometry("650x390")
    w.minsize(650, 390)
    w.maxsize(650, 390)    
    w.title("Voice Atlas")
    w.config(bg="#541D69")

    l1= Label(w, text= "How To Play", font=("Poppins", 30), bg='#541D69', fg='#FFFFFF')
    l1.place(x=200, y = 10)

    l2= Label(w, text= """1. Press the "Start Listening" button.""", font=("Poppins Light", 20), bg='#541D69', fg='#FFFFFF')
    l2.place(x=20, y=100)
    l3= Label(w, text= "2. Say your country's name", font=("Poppins Light", 20), bg='#541D69', fg='#FFFFFF')
    l3.place(x=20, y=140)
    l4= Label(w, text= "3. The bot displays its counter answer", font=("Poppins Light", 20), bg='#541D69', fg='#FFFFFF')
    l4.place(x=20, y=180)
    l5= Label(w, text= "Continue till either of you runs out of options.", font=("Poppins Light", 20), bg='#541D69', fg='#FFFFFF')
    l5.place(x=20, y=240)

    b1= Button(w, text = "PLAY", font=("Poppins Light", 17), command=w.destroy)
    b1.place(x=250, y=300)

    w.mainloop()

# Main
top = Tk()  

#icon
img = PhotoImage(file='globe.png')
top.call('wm', 'iconphoto', top._w, img)

# Window Code
top.geometry("800x550")
top.minsize(800, 550)
top.maxsize(800, 550)    
top.title("Voice Atlas")

img = PhotoImage(file="background.png")
label = Label(top, image=img)
label.place(x=0, y=0)

b1= Button(top, text = "Start Listening", font=("Poppins Light", 14),relief=RAISED, command=speech)
b1.place(x=330, y=90)


b2= Button(top, text = "Quit", font=("Poppins Light", 10),relief=RAISED, command=top.destroy)
b2.place(x=740, y=490)

b2= Button(top, text = "Words", font=("Poppins Light", 10),relief=RAISED, command=words)
b2.place(x=30, y=490)

b3= Button(top, text = "?", font=("Poppins Light", 8), command=howto)
b3.place(x=780, y=10)

user_l = Label(top, text= "USER: ", font=("Poppins", 14), bg='#541D69', fg='#FFFFFF')
user_l.place(x=50,y=190)
bot_l = Label(top, text= "BOT: ", font=("Poppins", 14), bg='#541D69', fg='#FFFFFF')
bot_l.place(x=50,y=240)
top.mainloop()
