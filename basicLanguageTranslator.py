from random import choices
from googletrans import Translator
from gtts import gTTS
from tkinter import *

window=Tk()
window.geometry('800x400')
window.config(bg="black")

set_bg=PhotoImage(file="aiden4k.png")

lable_1=Label(window,image=set_bg)

lable_1.place(x=-100,y=-100)

e1=Entry(window,bg="white",fg="black",font=("Arial",25,"bold"))
e1.place(x=20,y=20)

def convert_language():
    a1=e1.get()
    t1=Translator()
    t2=click_option.get()

    if t2=="English":
        convert="en"
    elif t2=="Hindi":
        convert="hi"
    elif t2=="German":
        convert="de"
    elif t2=="French":
        convert="fr"
    elif t2=="Spanish":
        convert="es"
    elif t2=="Russian":
        convert="ru"
    elif t2=="Japanese":
        convert="ja"
    elif t2=="Chinese":
        convert="zh-cn"

    trans_text=t1.translate(a1,dest=convert)
    trans_text=trans_text.text

    ob1=gTTS(text=trans_text,slow=False,lang=convert)
    lable_2.config(text=trans_text)

choices=[
    "English",
    "Hindi",
    "German",
    "French",
    "Spanish",
    "Russian",
    "Japanese",
    "Chinese",
]

click_option=StringVar()
click_option.set("Select Language")

list_drop=OptionMenu(window,click_option,*choices)
list_drop.configure(background="green",foreground="white",font=("Ariel",15,"bold"))
list_drop.place(x=400,y=20)

lable_2=Label(window,text="\t\t\t\t\t\t",bg="black",fg="white",font=("Ariel",40,"bold"))
lable_2.place(x=0,y=120)
lable_2=Label(window,text="Translated Text",bg="black",fg="white",font=("Ariel",40,"bold"))
lable_2.place(x=180,y=120)

Button_1=Button(window,text="Translate",bg="red",fg="white",font=("Ariel",25,"bold"),command=convert_language)
Button_1.place(x=220,y=200)


window.mainloop()

