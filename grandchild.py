#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program determines if you can date my grandchild



def main():
    # this function runs the better "Number Guessing Game"

    # input
    print("Can you date my grandchild?")
    print("Respond with 1 for yes and 2 for no:")
    rich = int(input("Are you rich? "))
    attractive =  int(input("Are you good looking? "))
    print("")

    # process and output
    if rich == 1 or attractive == 1:
        print("Congrats! You may date my grandchild!")
    elif rich == 2 or attractive == 2:
        print("Stay away from my grandchild!")
    else:
        print("What?")


if __name__ == "__main__":
    main()
