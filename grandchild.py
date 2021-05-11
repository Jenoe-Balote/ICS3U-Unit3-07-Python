#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program determines if you can date my grandchild

import string


def main():
    # this function runs the better "Number Guessing Game"

    # input
    print("Can you date my grandchild?")
    print("Respond with 1 for yes and 2 for no:")
    number_rich = str(input("Are you rich? "))
    number_attractive = str(input("Are you good looking? "))

    # process and output
    try:
        number_rich = int(number_rich)
        number_attractive = int(number_attractive)
        if number_rich == 1 or number_attractive == 1:
            print("Congrats! You may date my grandchild!")
        elif number_rich == 2 or number_attractive == 2: 
            print("Stay away from my grandchild!")
    except Exception:
        print("{} is invalid data.".format(number_rich and number_attractive))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
