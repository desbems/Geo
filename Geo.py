### desbems ###
### 2021 ###
from os import system
import os
import sys
import bcrypt
import sqlite3
import getpass
from prettytable import from_db_cursor
# initializing and creating db if not present
connection = sqlite3.connect('location.db')
cursor = connection.cursor()
# creating tables
command1 = """CREATE TABLE IF NOT EXISTS locations(id integer primary key, Locations TEXT, leftovers TEXT)"""
cursor.execute(command1)

################### Definitions ##################################
def changeLoc(): #SQL command creating a row
        location = input("What is the location ? : ")
        leftovers = input("Is it still there ? : ")
        cursor.execute("insert into locations (Locations, leftovers) values (?, ?)", (location, leftovers))
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
def deleteRecord():
        id = input("Which record do you want to delete (type the id) : ")
        cursor.execute("DELETE FROM locations WHERE id = (?)", (id))
        connection.commit()
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
            trypass = getpass.getpass("Enter your password : ")
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
                    while answer2 > 5 or answer2 < 1:
                        print("Change location ..........(1) ")
                        print("Add a new location .......(2) ")
                        print("Change password ..........(3) ")
                        print("Delete a record...........(4) ")
                        print("Exit......................(5) ")
                        answer2 = int(input())
                    if answer2 == 1:
                        system('cls')
                        printLoc()
                        row = int(input("What is the row you want to change ?"))
                        location = input("What is the location ? : ")
                        leftovers = input("Is it still there ? : ")
                        system('cls')
                        # SQL command : Updating a row
                        cursor.execute("UPDATE locations SET Locations = (?) WHERE id = (?)", (location, row))
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
                        printLoc()
                        deleteRecord()
                        system('cls')
                        printLoc()
                    elif answer2 == 5:
                        sys.exit()
                else:
                    sys.exit()
# aks the user the secret phrase to access if it's the first time skip this step
    else:
        password = getpass.getpass("Please type your new password : ").encode('utf8')
        salt = bcrypt.gensalt()
        passwordgen(password, salt)
        changeLoc()
        system('cls')
