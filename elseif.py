#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program checks if a number is positive or not


def main():
    # This function show if a number is positive or not

    user_input = int(input("Enter an integer: "))
    print("")

    if user_input < 0:
        print("negative number")
    elif user_input > 0:
        print("positive number")
    elif user_input == 0:
        print("0")
    else:
        print("no idea")


if __name__ == "__main__":
    main()
