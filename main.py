import sys
import os

# initialzing
password = "123"
trypass = ""
location = ""
leftovers = ""
changepass = ""
# aks the user the secret phrase to access if it's the first time skip this step
while (trypass != password) :
    trypass = input("Enter your password : ")
    if (trypass != password):
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
