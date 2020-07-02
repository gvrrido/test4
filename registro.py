# Truzz Blogg | Python + Tkinter | How to create a GUI
# How to create a registration form using Python + Tkinter

# Let's import tkinter
from tkinter import *


# import tkinter as tk

# Manipulate data from registration fields
def send_data():
    username_info = username.get() #NOMBRE
    password_info = password.get()
    fullname_info = fullname.get()
    age_info = str(age.get())
    print("Nombre","   Apellido    ","  Rut    " , "   Edad   ")
    print(username_info,"\t", password_info,"\t", fullname_info,"\t", age_info)

    #  Open and write data to a file
    file = open("user.txt" or "user.xlsx", "a")
    file.write(username_info)
    file.write("\t")
    file.write(password_info)
    file.write("\t ")
    file.write(fullname_info)
    file.write(" \t ")
    file.write(age_info)
    file.write("\t\n ")
    file.close()
    print()
    print(" Usuario Registrado. Nombre: {} | Rut: {}   ".format(username_info, fullname_info))

    #  Delete data from previous event
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    fullname_entry.delete(0, END)
    age_entry.delete(0, END)


# Create new instance - Class Tk()
mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Python")
mywindow.resizable(False, False)
mywindow.config(background="#213141")
main_title = Label(text="Alonso.apps", font=("Cambria", 14), bg="#56CD63", fg="black", width="500",
                   height="2")
main_title.pack()

# Define Label Fields
username_label = Label(text="Nombres", bg="#FFEEDD")
username_label.place(x=22, y=70)
password_label = Label(text="Apellidos", bg="#FFEEDD")
password_label.place(x=22, y=130)
fullname_label = Label(text="Rut", bg="#FFEEDD")
fullname_label.place(x=22, y=190)
age_label = Label(text="Edad", bg="#FFEEDD")
age_label.place(x=22, y=250)

# Get and store data from users
username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()

username_entry = Entry(textvariable=username, width="40")
password_entry = Entry(textvariable=password, width="40")
fullname_entry = Entry(textvariable=fullname, width="20")
age_entry = Entry(textvariable=age, width="5")

username_entry.place(x=22, y=100)
password_entry.place(x=22, y=160)
fullname_entry.place(x=22, y=220)
age_entry.place(x=22, y=280)

# Submit Button
submit_btn = Button(mywindow, text="REGISTRAR", width="30", height="2", command=send_data, bg="#00CD63")
submit_btn.place(x=22, y=320)

mywindow.mainloop()