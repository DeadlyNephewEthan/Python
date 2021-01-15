from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Image Frames')

#frame = LabelFrame(root, text="This the frame", padx=5, pady=5)
frame = LabelFrame(root, padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="...or here!")
b2.grid(row=1, column=1)
b.grid(row=0, column=0)





root.mainloop()
