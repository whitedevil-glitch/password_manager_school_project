from cgi import test
import sqlite3
import random

master_pwd = input("Enter your master-password please: ")

if master_pwd == "123":
    print("\n succesfully logged in! \n")
else:
    print("Invalid!")
    quit()

# Logo


def logo():

    print('''

        ██╗░░░██╗░█████╗░██╗░░░██╗██╗░░░░░████████╗  
        ██║░░░██║██╔══██╗██║░░░██║██║░░░░░╚══██╔══╝  
        ╚██╗░██╔╝███████║██║░░░██║██║░░░░░░░░██║░░░  
        ░╚████╔╝░██╔══██║██║░░░██║██║░░░░░░░░██║░░░  
        ░░╚██╔╝░░██║░░██║╚██████╔╝███████╗░░░██║░░░  
        ░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚══════╝░░░╚═╝░░░  
        
            THE VAULT (ULTIMATE PASSWORD MANAGER)

                          WELCOME :)  
    ''')


# SQL CONNECTION AND TABLE CREATION
conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER UNIQUE NOT NULL,
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT,
    phone INTEGER NOT NULL
);
''')

# Generating Function


def gen():
    # password strength
    max_len = int(input("Enter No. of Characters (12-26): "))
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
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol  # abcd
    for x in range(max_len - 4):  # user number - 4 = result
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

    password = ""
    for x in temp_pass:
        password = password + x

    print("generated password: ", password)

    ask = input(
        "Would you like to add/save this new password to the database? (yes/no): ")
    if ask == "yes":
        id1 = int(input("Enter ID Number: "))
        name1 = input("Username to save this password: ")
        serv = input("Enter service: ")
        mai = input("Enter email: ")
        numbe = int(input("Enter phone number: "))
        sql = """INSERT INTO users  (id, service, username, password, email, phone) 
                 VALUES (?, ?, ?, ?, ?, ?);"""
        val = (id1, serv, name1 , password , mai, numbe)
        cursor.execute(sql, val)
        conn.commit()
    else:
        print("Alright!")


# Add Function
def add():
    id2 = int(input("Enter ID Number: "))
    ser = input("Enter Service name: ")
    name = input("Account Username: ")
    pwd = input("Account Password: ")
    mail = input("Enter Email Address: ")
    numb = int(input("Enter Phone Number: "))

    cursor.execute(f'''
        INSERT INTO users (id, service, username, password, email, phone)
        VALUES ('{id2}', '{ser}', '{name}', '{pwd}', '{mail}', '{numb}')
    ''')
    conn.commit()

# View All Services

def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

# Retrieve / Search Function
def search():
    ask = int(input("1. Search with Username, 2. Search with Email, 3. Search with Service (1,2,3): " + "\n"))
    if ask == 1:
        usr1 = input("Enter Username: ")
        sql1 = ('''select password from users where username = ?;''')
        val1 = (usr1,)
        cursor.execute(sql1, val1)
        for (password) in cursor:
            print("Your Password is: ", password)
    elif ask == 2:
        usr2 = input("Enter Email Address: ")
        sql2 = ('''select username, password from users where email = ?;''') 
        val2 = (usr2,)
        cursor.execute(sql2, val2)
        for (username, password) in cursor:
            print("Username: " + username + "\npassword: " + password + "\n")
    elif ask == 3:
        usr3 = input("Enter Service: ")
        sql3 = ('''select username, password from users where service = ?;''')
        val3 = (usr3,)
        cursor.execute(sql3, val3)
        for (username, password) in cursor.fetchall():
            print("\n" + "Username: " + username + "\npassword: " + password + "\n")
    else:
        print("Not Found!")

# Forgot Password Function
def forgot():
    print("You Lost Your Password? No Worries We Got You :) ")
    ask = input("Enter your Email: ")
    sql = "SELECT phone FROM users WHERE email = ?"
    val = (ask, )
    cursor.execute(sql, val)
    for (email, phone) in cursor():
        print("Email: ", email, "Your Recovery Phone Number: ", phone)
    else:
        print("Not Found!")    

# Delete Function


def delete():
    ask = input("Enter service: ")
    removeItem = "DELETE FROM users WHERE service = ? "
    cursor.execute(removeItem, (ask,))
    conn.commit()
    print(cursor.rowcount, "item removed")

# Update Function
def update():
    ask = input("Which data you want to update? (phone, usr, service, password, email): ")
    ask.lower()
    if ask == "phone":
        ask1 = input("enter username: ")
        ask2 = int(input("enter new phone number: "))
        sql = 'update users set phone = ? where username = ?;'
        val = (ask2, ask1, )
        cursor.execute(sql, val)
        conn.commit()
        print(" UPDATED !!! ")
    else:
        print("Please Check Your Input!")
    if ask == "usr":
        ask1 = input("enter old username: ")
        ask2 = input("enter new username: ")
        sql = 'update users set username = ? where username = ?;'
        val = (ask2, ask1, )
        cursor.execute(sql, val)
        conn.commit()
        print(" UPDATED !!! ")
    else:
        print("Please Check Your Input!")
    if ask == "service":
        ask1 = input("enter username: ")
        ask2 = input("enter new service: ")
        sql = 'update users set service = ? where username = ?;'
        val = (ask2, ask1, )
        cursor.execute(sql, val)
        conn.commit()
        print(" UPDATED !!! ")
    else:
        print("Please Check Your Input!")
    if ask == "password":
        ask1 = input("enter username: ")
        ask2 = input("enter new password: ")
        sql = 'update users set password = ? where username = ?;'
        val = (ask2, ask1, )
        cursor.execute(sql, val)
        conn.commit()
        print(" UPDATED !!! ")
    else:
        print("Please Check Your Input!")
    if ask == "email":
        ask1 = input("enter username: ")
        ask2 = input("enter new email: ")
        sql = 'update users set email = ? where username = ?;'
        val = (ask2, ask1, )
        cursor.execute(sql, val)
        conn.commit()
        print(" UPDATED !!! ")
    else:
        print("Please Check Your Input!")
        
# Main Menu

def menu():
    print("|--------------------------------|")
    print("| 1: Generate: |")
    print("| 2: Add: |")
    print("| 3: Retrieve a password: |")
    print("| 4: Forgot Password: |")
    print("| 5: View all services: |")
    print("| 6: Delete a DATA (with id): |")
    print("| 7: UPDATE DATA: |")
    print("| 8: EXIT: |")
    print("|-------------------------------|\n")


logo()
while True:
    menu()
    opt = int(input("Enter Option"))
    if opt == 1:
        gen()
    elif opt == 2:
        add()
    elif opt == 3:
        search()
    elif opt == 4:
        forgot()
    elif opt == 5:
        show_services()
    elif opt == 6:
        delete()
    elif opt == 7:
        update()
    elif opt == 8:
        print(r"                                                            ")
        print(r"THANK YOU FOR USING *THE VAULT* ( Ultimate Password Manager ) ") 
        print(r"                                                            ")
        break
