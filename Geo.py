### desbems ###
### 2021 ###
from os import system
import os
import sys
import bcrypt
import sqlite3
from prettytable import from_db_cursor
# initializing and creating db if not present
connection = sqlite3.connect('location.db')
cursor = connection.cursor()
# creating tables
command1 = """CREATE TABLE IF NOT EXISTS locations(id integer primary key, real_loc TEXT, leftovers TEXT)"""
cursor.execute(command1)

################### Definitions #################################
def changeLoc(): #SQL command creating a row
        location = input("What is the location ? : ")
        leftovers = input("Is it still there ? : ")
        cursor.execute("insert into locations (real_loc, leftovers) values (?, ?)", (location, leftovers))
        connection.commit()

def printLoc(): #SQL command for printing the db
        cursor.execute('SELECT * FROM locations')
        x = from_db_cursor(cursor)
        print(x)
def passwordgen(password, salt):
        f = open('data.txt', 'wb')
        hashed_password = bcrypt.hashpw(password, salt)
        f.write(hashed_password)
        f.close()
##################################################################

correct = False
loop = 0
# loop to create a password if not it isn't present
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
                printLoc()
# shows all the informations and asks if change is wished
                answer = input("Do you want to change something ? ")
                if answer.upper() == "YES":
                    answer2 = 0
                    while answer2 > 4 or answer2 < 1:
                        print("Change location ..........(1) ")
                        print("Add a new location .......(2) ")
                        print("Change password ..........(3) ")
                        print("Exit......................(4) ")
                        answer2 = int(input())
                    if answer2 == 1:
                        system('cls')
                        printLoc()
                        row = int(input("What is the row you want to change ?"))
                        location = input("What is the location ? : ")
                        leftovers = input("Is it still there ? : ")
                        system('cls')
                        # SQL command : Updating a row
                        cursor.execute("UPDATE locations SET real_loc = (?) WHERE id = (?)", (location, row))
                        cursor.execute("UPDATE locations SET leftovers = (?) WHERE id = (?)", (leftovers, row))
                        printLoc()
                        connection.commit()
                    elif answer2 == 2:
                        system('cls')
                        printLoc()
                        changeLoc()
                        system('cls')
                    elif answer2 == 3:
                        password = input("Enter your new password : ").encode('utf8')
                        salt = bcrypt.gensalt()
                        passwordgen(password, salt)
                        system('cls')
                    elif answer2 == 4:
                        sys.exit()
                else:
                    sys.exit()
# aks the user the secret phrase to access if it's the first time skip this step
    else:
        password = input("Please type your new password : ").encode('utf8')
        salt = bcrypt.gensalt()
        passwordgen(password, salt)
        changeLoc()
        system('cls')
