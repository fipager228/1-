from pydoc import text
from tkinter import *
import tkinter as ttk

import time
from PIL import Image, ImageTk

schetch = 0

image2 = Image.open("веталя2.png")
vet2 = ImageTk.PhotoImage(image2)


image = Image.open("веталя1.png")
vet = ImageTk.PhotoImage(image)





def klicer():
    bg = ttk.Label(room, image=vet)
    bg.place(x=0, y=0, relwidth=1, relheight=1)

    bg.image = vet

    schet1 = ttk.Label(text=schetch, font=("Minecraftia",25))
    schet1.place(relx=0.5, rely=0.7, anchor="n")

    klk = ttk.Button(text='Клик!',
                      font=("Minecraftia", 27),
                      bg='#8fa9e8',
                      fg='#28326c',
                      activebackground='#9eabc9',
                      activeforeground='#151c43',
                      bd=0,
                      relief="flat",
                      cursor='circle',
                      command=klik)
    klk.place(relx=0.5, rely=0.5, anchor="n")

    ppc = ttk.Button(text='ППЦ',
                     font=("Minecraftia", 34),
                     bg='#8fa9e8',
                     fg='#28326c',
                     activebackground='#9eabc9',
                     activeforeground='#151c43',
                     bd=0,
                     relief="flat",
                     cursor='circle',
                     command=popc)

def klik():
    bg = ttk.Label(room, image=vet2)
    bg.place(x=0, y=0, relwidth=1, relheight=1)
    bg.image2 = vet2
    time.sleep(0.1)
    bg.image = vet

room = Tk()

def popc():
    pass

room.title('Мини игры')
room.geometry(f'800x750+{(room.winfo_screenwidth()-800)//2}+{(room.winfo_screenheight()-800)//2}')

room.resizable(width=0, height=0)



klki = ttk.Button(text='Кликер',
                  font=("Minecraftia", 34),
                  bg='#8fa9e8',
                  fg='#28326c',
                  activebackground='#9eabc9',
                  activeforeground='#151c43',
                  bd=0,
                  relief="flat",
                  cursor='circle',
                  command=klicer)

ppc = ttk.Button(text='ППЦ',
                  font=("Minecraftia", 34),
                  bg='#8fa9e8',
                  fg='#28326c',
                  activebackground='#9eabc9',
                  activeforeground='#151c43',
                  bd=0,
                  relief="flat",
                  cursor='circle',
                  command=popc)

klki.place(relx=0.25, y=30, anchor="n")
ppc.place(relx=0.75, y=30, anchor="n")



room.mainloop()