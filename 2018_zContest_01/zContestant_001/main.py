#! usr/bin/env python3
import os

# If not exists, file will be created.
FILE = "shopping_list.txt"

def banner(text, icon):
    '''Increases visibility of text'''
    row = icon * (len(text) + 6)
    print("\n" + row + "\n   " + text + "   \n" + row)

def read_all():
    '''Returns all lines'''
    with open (FILE, "r") as fh:
        data = fh.readlines()
        for num, line in enumerate(data, 1):
            print(str(num) + ") " + line + "\n")

def write_line():
    '''Appends a line to the end of file'''
    entry = input("Please type your item: ")
    quantity = input("How many? ")
    entry += ", " + quantity + "\n"
    with open (FILE, "a") as fh:
        fh.writelines(entry)

def update_line():
    '''Rewrites the file with an updated value'''
    with open (FILE, "r") as fh:
        data = fh.readlines()
    line = input("Please pick a line number: ")
    try:
        line_int = int(line) - 1
    except ValueError:
        banner("ERROR: Numbers only", "~")
        return
    if line_int > len(data) or line == "0":
        banner("ERROR: Not an existing line number", "~")
        return
    new_input = input("New item: ")
    quantity = input("How many? ")
    new_input += ", " + quantity

    data[int(line_int)] = new_input + "\n"
    with open (FILE, "w") as fh:
        for item in data:
            fh.writelines(item)

def delete_line():
    '''Deletes one line from list'''
    with open(FILE, "r") as fh:
        data = fh.readlines()
    line = input("Please pick a line number to delete: ")
    try:
        line_int = int(line) - 1
    except ValueError:
        banner("ERROR: Numbers only", "~")
        return
    if line_int > len(data) or line == "0":
        banner("ERROR: Not an existing line number", "~")
        return
    del data[line_int]
    with open(FILE, "w") as fh:
        for item in data:
            fh.writelines(item)

def menu():
    '''User interface'''
    while True:
        print("\n")
        try:
            read_all()
        except FileNotFoundError:
            print("\nNo list to show yet. Type '1' to enter items")

        banner("(1) Add Item | (2) Update Entry | (3) Delete Entry | (4) Clear List | (0) Quit", "-")

        user_choice = input("Please pick a number: ")

        if user_choice == "1":
            write_line()
        elif user_choice == "2":
            update_line()
        elif user_choice == "3":
            delete_line()
        elif user_choice == "4":
            os.remove(FILE)
        elif user_choice == "0":
            print("\n{:*^84}".format(" Goodbye! See You Next Time! ") + "\n")
            break
        else:
            banner("ERROR: Invalid choice, Try again", "~")


if __name__ == "__main__":

    print("\n{:*^84}".format(" Welcome to Your Shopping List! "))
    menu()
