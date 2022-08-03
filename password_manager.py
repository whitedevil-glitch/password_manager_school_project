import random #random module for generating pass
import os #for removal of passwrd txt 

#Master Password Code

master_pwd = input("Enter your master-password please: ")

if master_pwd == "123":
    print("\n succesfully logged in! \n")
else:
    print("Invalid!")
    quit()


# Generating Function

def gen():
    max_len = 12 #password strength
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOWCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                          'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                          'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '~', '>',
               '*', '(', ')', '<']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOWCASE_CHARACTERS + SYMBOLS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOWCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol #abcd
    for x in range(max_len - 4): # 12-4 = 8
        temp_pass = temp_pass + random.choice(COMBINED_LIST)


    password = ""
    for x in temp_pass:
        password = password + x

    print("generated password: ", password)


    ask = input(
        "Would you like to add/save this new password with a username? (yes/no): ")
    if ask == "yes":
        name1 = input("Username to save this password: ")
        with open("passwords.txt", "a") as f:
            f.write(name1 + "|" + password + "\n")
    else:
        print("Alright!")



# VIew Function

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, ", Password: ", passw)

# Add Function

def add():
    name = input("Account Username: ")
    pwd = input("Account Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

# Deleting Function

def rem():
    abc = input("Do you want to remove everything from database? (y/n): ")
    if abc == "y":
        os.remove("passwords.txt")
    elif abc == "n":
        efg = input("Enter the username which is to be removed from database: ")
        with open("passwords.txt", "r") as t:
            for i in t.readlines():
                if i == efg:
                    t.remove(i)
                else:
                    pass
    else:
        print("Invalid operation! ")

#Main Menu

while True:
    mode = input(
        "Would you like to generate a new password or add a new password or view existing one or remove (gen, add, view, del, q to quit): ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "gen":
        gen()
    elif mode == "del":
        rem()
    else:
        print("Invalid Mode!")
        continue
