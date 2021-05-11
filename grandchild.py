#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program is the better "Number Guessing Game"

import random
import string
random_number = random.randint(0, 9)


def main():
    # this function runs the better "Number Guessing Game"

    # input
    print("Can you date my grandchild?")
    print("Respond with 1 for yes and 2 for no:")
    rich = int(input("Are you rich? "))
    attractive =  int(input("Are you good looking? "))
    print("")

    # process and output
    try:
        if rich == 1 or attractive == 1:
            print("Congrats! You may date my grandchild!")
        elif rich == 2 or attractive == 2:
            print("Stay away from my grandchild!")
    except Exception:
        print("What?")
    finally:
        print("Thanks for answering truthfully!")


if __name__ == "__main__":
    main()
