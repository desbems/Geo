import sys
import os
import bcrypt



def changeloc(location, leftovers):
        lo = open('misc.txt', 'w')
        lo.write(location, "\n")
        lo.write(leftovers)
        lo.close()
def passwordgen(password, salt):
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
            if not valid:
                print("Incorrect !")
            else:
                print("Correct !")
                os.system('cls')
                with open('misc.txt', 'r') as reader:
                    locshow = reader.read(1)
                    print(f"The location is : {locshow}")
                    leftshow = reader.read(2)
                    print(f"There is : {leftshow} leftovers")

                answer = input("Do you want to change something ?")
                if answer == "yes" or answer == "yes":
                    answer2 = 0
                    while answer2 > 3 or answer2 < 1:
                        print("Change location ..........(1)")
                        print("Change password ..........(2)")
                        print("Exit......................(3)")
                        answer2 = int(input())
                    if answer2 == 1:
                        location = input("What is the location ? : ")
                        leftovers = input("\nIs there any leftovers ? : ")
                        changeloc(location, leftovers)
                    elif answer2 == 2:
                        password = input("Enter your new password : ").encode('utf8')
                        salt = bcrypt.gensalt()
                        passwordgen(password, salt)

                    elif answer2 ==3:
                        sys.exit()
                else:
                    sys.exit()
# aks the user the secret phrase to access if it's the first time skip this step
    else:
        password = input("Please type your new password : ").encode('utf8')
        salt = bcrypt.gensalt()
        passwordgen(password, salt)
        location = input("What is the location ? : ")
        leftovers = input("\nIs there any leftovers ? : ")
        changeloc(location, leftovers)
