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
            trypass = input("Enter your password :\n")


            if (trypass != login):
                print("Incorrect !")
            else :
                print("Correct !")
        f.close()
        location = input("What is the location ? : ")
        f = open('data.txt', 'a')
        f.write("\n")
        f.write(location)
        f.write("\n")
        leftovers = input("\nIs there any leftovers ? : ")
        f.write(leftovers)
        f.write("\n")
        f.close()



        os.system('cls')
        while changepass != "Yes" or changepass != "No":
            changepass = input("Do you want to change your password ? : (Yes/No) ")
            if changepass == "Yes":
                password = input("Type your new password : ")
                sys.exit()
            elif changepass == "No":
                loop = 2
                sys.exit()

    else :
        login = input("pswrd")
        f = open('data.txt', 'a')
        f.write(login)

        f.close()


