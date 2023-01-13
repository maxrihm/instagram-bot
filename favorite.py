import os
import colorama

while True:
    new_user = input("Enter user's link: ")
    add_line = False
    clear = lambda: os.system('cls')
    clear()

    with open("account_favorite_list.txt", "r+") as f:
        if new_user in f.read():
            print('\033[31m' + "user already in list")
            print('\033[39m')
        else:
            f.write(new_user+"\n")
            print('\033[32m' + "user added in list")
            print('\033[39m')
