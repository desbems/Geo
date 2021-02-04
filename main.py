import sys
import os

# initialzing
correct = False
loop = 0
while (loop != 2):
    if os.path.isfile('./data.txt'):
        f = open('data.txt', 'r')
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
                os.system('cls')
                lo = open('misc.txt', 'r')
                locshow = lo.readlines()
                print(locshow)

                answer = input("Do you want to change something ?")
                if answer == "yes":
                    lo = open('misc.txt', 'w')
                    location = input("What is the location ? : ")
                    lo.write(location)
                    lo.write("\n")
                    leftovers = input("Is there any leftovers ? : ")
                    lo.write(leftovers)
                    lo.close()
        os.system('cls')
        while changepass != "Yes" or changepass != "No":
            changepass = input("Do you want to change your password ? : (Yes/No) ")
            if changepass == "Yes":
                password = input("Type your new password : ")
                f = f = open('data.txt', 'w')
                f.write(password)
                sys.exit()
            elif changepass == "No":
                loop = 2
                sys.exit()

    else:
        login = input("pswrd")
        f = open('data.txt', 'w')
        f.write(login)
        f.close()
        lo = open('misc.txt', 'a')
        location = input("What is the location ? : ")
        lo.write(location)
        lo.write("\n")
        leftovers = input("\nIs there any leftovers ? : ")
        lo.write(leftovers)
        lo.write("\n")
        lo.close()


