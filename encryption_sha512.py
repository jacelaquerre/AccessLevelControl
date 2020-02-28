# Jace Laquerre


import csv
import hashlib
import secrets

def main():
    print("Welcome to the password-protected system.")
    print("To create a new Account, please register.")
    print("If you already have an account, type 'n' to login")
    authenticate()

def authenticate():
    try:
        login = False
        # csv file name
        filename = "userProfiles.csv"
        badAns = True
        while badAns:
            register = input("Need to register (y/n)?")
            if register == "y":
                user = input("Create a username: ")
                badPass1 = True
                while badPass1:
                    password = input("Create a password: ")
                    length = len(password)
                    badAns = False
                    # pass validation if between 8-25 characters
                    if (length < 7) or (length > 26):
                        print("Password must be between 8-25 characters.")
                        badPass1 = True
                    # Check if there is a digit in the password
                    if not any(char.isdigit() for char in password):
                        print("Password should have at least one numeral.")
                    # Check if there is a digit in the password
                        badPass1 = True
                    if not any(char.isalpha() for char in password):
                        print("Password should have at least one letter.")
                        badPass1 = True
                    else:
                        badPass1 = False

                        # Create Hash and Salt
                        salt = secrets.token_hex(4)
                        saltedPass = password + salt
                        newPass = encrypt(saltedPass)
                        row = [user, salt, newPass, 1]
                        with open(filename, 'a') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                        print("Account Information Saved.")
                        register = input("Need to register (y/n)?")
            if register == "n":
                badPass = True
                badAns = False
                while badPass:
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    # reading csv file
                    csvfile = open(filename)
                    csvreader = csv.reader(csvfile)

                    for row in csvreader:
                        if row[0] == username:
                            userInput = encrypt(password + row[1])
                            if userInput == row[2]:
                                login = True
                                levelStr = row[3]
                                level = int(levelStr)
                                break

                    if login:
                        badPass = False
                        print("You have logged in successfully.")
                        showMenu(level)
                        # Close file
                        csvfile.close()
                    else:
                        print("Incorrect Login Information.")
                        badPass = True
            else:
                badPass = True
                print("Please type 'n' or 'y'.")

    except IOError:
        print('Sorry, no such file exists.')

def showMenu(level):
    print("Login successful.")
    print("Press 1 for time-reporting")
    print("Press 2 for Accounting")
    print("Press 3 for Engineering")
    print("Press 4 for system control")

    badChoice = True
    while badChoice:
        choice = input("Enter Choice: ")
        if choice == "1":
            timeReporting(level)
            badChoice = False
        elif choice == "2":
            accounting(level)
            badChoice = False
        elif choice == "3":
            engineering(level)
            badChoice = False
        elif choice == "4":
            systemControl(level)
            badChoice = False
        else:
            print("That's not one of the options, please choose again.")
            badChoice = True

def encrypt(saltedPass):
    hash = hashlib.sha512(saltedPass.encode()).hexdigest()
    return hash

def timeReporting(level):
    if level > 0:
        print("You have now accessed the time-reporting application.")
    else:
        print("You are not authorized to access this area.")

def accounting(level):
    if level > 1:
        print("You have now accessed the accounting application.")
    else:
        print("You are not authorized to access this area.")

def engineering(level):
    if level > 1:
        print("You have now accessed the engineering application.")
    else:
        print("You are not authorized to access this area.")

def systemControl(level):
    if level > 2:
        print("You have now accessed the system control application.")
    else:
        print("You are not authorized to access this area.")

main()
