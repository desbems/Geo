from tkinter import *
import bcrypt
import os

# name and size of the gui
root = Tk()
root.title("GeoProject")
root.geometry("400x300")

# Defintions
def passCheck():
	trypass = inputPassword.get()
	if trypass == password:
		gpass.pack()
		btnOk.place_forget()
		inputPassword.place_forget()

	else:
		bpass.pack()


def passwordgen():
    f = open('data.txt', 'wb')
    passw = (newPassword.get()).encode('utf8')
    f.write(passw)
    f.close()

# Initialisation of every buttons and labels !!!!!! not yet placed !!!!!!!!
gpass = Label(root, text="Good password")
bpass = Label(root, text="Bad password")



inputPassword = Entry(root)

btnOk = Button(root, text="Enter your password", command=passCheck)
# Check if it's the first time
if os.path.isfile('./data.txt'):
	pass









else:
	fpass = Label(root, text="Please create your password")
	fpass.pack()
	newPassword = Entry(root)
	newPassword.pack()
	btnCreatePass = Button(root, text="Submit", command=passwordgen)
	btnCreatePass.pack()
	


# print Window
root.mainloop()