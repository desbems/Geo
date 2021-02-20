from tkinter import *
import bcrypt

# Initialisation
root = Tk()
root.title("GeoProject")
root.geometry("400x300")
password = "123"
gpass = Label(root, text="Good password")
bpass = Label(root, text="Bad password")
#
def passCheck():
	trypass = inputPassword.get()
	if trypass == password:
		gpass.pack()
		btnOk.place_forget()
		inputPassword.place_forget()

	else:
		bpass.pack()



# Phase 1 : Password Checking / Creation
inputPassword = Entry(root)
inputPassword.place(x=0, y=0)
btnOk = Button(root, text="Enter your password", command=passCheck)
btnOk.place(x=0, y=30)



# print Window
root.mainloop()