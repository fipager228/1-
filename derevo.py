from tkinter import *
import random

tree = Tk()

tree.title('. . .')
icon = PhotoImage(file='icon_tree.png')
tree.iconphoto(True, icon)

tree.geometry('500x400+500+220')
tree.resizable(width=False, height=False)
tree.config(bg="#000000")

tre = 0

def nazhal_na_knopku():
    chance = random.randint(1, 8)
    if chance <= 2:
        knopka.destroy()

        img_man = PhotoImage(file="man.png")
        label_derevo.config(image=img_man)
        label_derevo.image = img_man
        label_derevo.place(relx=0.5, rely=0.5, anchor=CENTER)
        label_derevo.bind("<Button-1>", na_derevo)
    else:
        pass

def na_derevo(event):
    global tre
    tre = tre + 1

    if tre == 1:
        label_slovo.config(text="дерево")
        label_slovo.place(relx=0.5, rely=0.85, anchor=CENTER)
        tree.after(1500, ubrat_slovo)

    elif tre == 2:
        label_slovo.config(text="возьми это")
        label_slovo.place(relx=0.5, rely=0.85, anchor=CENTER)
        tree.after(2000, pokazat_yaico)

def ubrat_slovo():
    label_slovo.config(text="")

def pokazat_yaico():
    label_slovo.config(text="вы получили яйцо")
    tree.after(3000, konec)

def konec():
    label_slovo.config(text="")
    tree.after(3000, tree.destroy)

knopka = Button(tree, text=":D", font=("Fixedsys", 16), command=nazhal_na_knopku)
knopka.place(relx=0.5, rely=0.5, anchor=CENTER)

label_derevo = Label(tree, bg="black")

label_slovo = Label(tree, text="", font=("Fixedsys", 16), fg="white", bg="black")

tree.mainloop()
