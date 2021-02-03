import sys
import os

# initialzing
if os.path.isfile('./data.txt'):
    f = open('data.txt')
    login = f.read()
    trypass = ""
    location = ""
    leftovers = ""
    changepass = ""
# aks the user the secret phrase to access if it's the first time skip this step
    while (trypass != login) :
        trypass = input("Enter your password : ")
        if (trypass != login):
            print("Incorrect !")
        else :
            print("Correct !")
#
    location = input("What is the location ? : ")
    leftovers = input("Is there any leftovers ? : ")

    os.system('cls')
    while changepass != "Yes" or changepass != "No":
        changepass = input("Do you want to change your password ? : (Yes/No) ")
        if changepass == "Yes":
            password = input("Type your new password : ")
            sys.exit()
        elif changepass == "No":
            sys.exit()
else :
    login = input("pswrd")
    f = open('data.txt', 'w+')
    f.write(login)
    f.close()

