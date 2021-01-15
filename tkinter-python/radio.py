from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Radio Buttons')
root.iconbitmap('images\cra.ico')

#r = IntVar()
#r.set("0")

MODES =[
    ("Pep","Pep"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pep")


for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=pizza.get())
    myLabel.pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda : clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda : clicked(r.get())).pack()
#r = StringVar()
#RadioButton(root, text="Option 1", variable=r, value="1").pack()
#myLabel = Label(root, text=pizza.get())
#myLabel.pack()


myButton = Button(root, text="Click Me!", command=lambda : clicked(pizza.get())).pack()

root.mainloop()