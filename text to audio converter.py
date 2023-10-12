from tkinter import *
from gtts import gTTS
import os

def submit():
    data=ery.get()
    Text=data
    language="en"

    output=gTTS(text=Text,lang=language,slow=False)

    output.save("output.mp3")

    os.system("start output.mp3")


box=Tk()
box.title("Text to audio converter")
box.geometry("600x600")

lab=Label(box,text="Text 2 Audio converter",bg="purple",fg="white",font=("algerian",25,"bold"))
lab.pack(fill=X)

lab1=Label(box,text="Enter words to speak :",bg="purple",fg="white",font=("times",15,"bold"))
lab1.pack(side="left")

ery=Entry(box,width=30,font=("times",20,"bold"),bg="lightblue",fg="white",selectbackground="red",selectforeground="black")
ery.pack(side='right')

bt=Button(box,text="submit",font=("times",15),width=10,padx=30,pady=10,bg="green",fg="white",command=submit)
bt.pack(side="bottom")
