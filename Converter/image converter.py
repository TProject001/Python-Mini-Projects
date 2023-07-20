from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image

root=Tk()

root.geometry("400x400")
root.title("Image Converter App")

def jpg_to_png():
    a=fd.askopenfilename()
    if(a.endswith(".jpg")):
        file_name=int(input("Enter file name : "))
        Image.open(a).save(file_name+".png")
    else:
        Label_2=Label(root,text="Error!",width=20,fg="Red",font=("bold",15))
        Label_2.place(x=80,y=280)

def jpg_to_pdf():
    a=fd.askopenfilename()
    if(a.endswith(".jpg")):
        file_name=int(input("Enter file name : "))
        Image.open(a).save(file_name+".pdf",resolution=100.0)
    else:
        Label_2=Label(root,text="Error!",width=20,fg="Red",font=("bold",15))
        Label_2.place(x=80,y=280)

Label_1=Label(root,text="Browse a file",width=20,font=("bold",15))
Label_1.place(x=80,y=80)

Button(root,text="Jpg to Png",width=20,height=2,bg="brown",fg="white",command=jpg_to_png).place(x=120,y=120)
Button(root,text="Jpg to Pdf",width=20,height=2,bg="brown",fg="white",command=jpg_to_pdf).place(x=120,y=220)

root.mainloop()
