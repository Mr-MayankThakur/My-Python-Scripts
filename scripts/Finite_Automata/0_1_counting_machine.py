# -*- coding: utf-8 -*-
"""
Machine which counts the total number of 1s and 0s in the given string over the input alphabets {0, 1}.

Requirements:
    -> Python 3.0 or higher

Usage:
    -> Simply run this script with python and follow on screen instructions.
"""
__script_name__ = "Machine counting total 0s and 1s"
__version__ = "1.0.0"
__author__ = "Mayank Thakur"
__date__ = "12-09-2020"

def counter_machine(input_string, counts):
    if input_string == '':
        return counts

    current_value = input_string[0]

    if current_value == '0':
        counts[0] += 1
    elif current_value == '1':
        counts[1] += 1
    else:
        raise(TypeError("Invalid Value found in the string: {}".format(current_value)))

    return counter_machine(input_string[1:], counts)


if __name__ == "__main__":

    print("0s and 1s Counter Machine")
    print("Enter q to exit.")
    while True:
        user_input_string = input("Please Enter a string: ")

        if user_input_string.lower() == 'q':
            print("Exiting...\nHave a Nice Day!!")
            break

        # setting initial counts
        total = {0: 0, 1: 0}
        try:
            total = counter_machine(user_input_string, total)
            print("Found {} 1s and {} 0s\n".format(total[1], total[0]))

        except TypeError as e:
            print(e)


