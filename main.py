import sys
import os
import bcrypt



def changeloc(location, leftovers):
        lo = open('misc.txt', 'w')
        lo.write(location)
        lo.write("\n")
        lo.write(leftovers)
        lo.write("\n")
        lo.close()
def passwordGen(password, salt):
    f = open('data.txt', 'wb')
    hashed_password = bcrypt.hashpw(password, salt)
    f.write(hashed_password)
    f.close()

# initializing

correct = False
loop = 0
while loop != 2:
    if os.path.isfile('./data.txt'):
        f = open('data.txt', 'r+')
        login = f.read()
        trypass = ""
        location = ""
        leftovers = ""
        changepass = ""

# loop until password is not a match
        valid = False
        while valid != True:
            trypass = input("Enter your password : ")
            valid = bcrypt.checkpw(trypass.encode('utf8'), login.encode('utf8'))
            if valid != True:
                print("Incorrect !")

            else:
                print("Correct !")
                os.system('cls')
                lo = open('misc.txt', 'r')
                locshow = lo.readlines()
                print(locshow)

                answer = input("Do you want to change something ?")
                if answer == "yes":
                    location = input("What is the location ? : ")
                    leftovers = input("\nIs there any leftovers ? : ")
                    changeloc(location, leftovers)
        os.system('cls')
        while changepass != "Yes" or changepass != "No" or changepass != "yes" or changepass != "no":
            changepass = input("Do you want to change your password ? : (Yes/No) ")
            if changepass == "Yes" or changepass == "yes":
                password = input("pswrd").encode('utf8')
                salt = bcrypt.gensalt()
                passwordGen(password, salt)
                sys.exit()
            elif changepass == "No" or changepass == "no":
                loop = 2
                sys.exit()
# aks the user the secret phrase to access if it's the first time skip this step
    else:
        password = input("pswrd").encode('utf8')
        salt = bcrypt.gensalt()
        passwordGen(password, salt)
        location = input("What is the location ? : ")
        leftovers = input("\nIs there any leftovers ? : ")
        changeloc(location, leftovers)

