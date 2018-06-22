#!/bin/python3
import random

# create a list of characters to choose from
# containing letters, numbers and punctuation characters
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ123457890!#$@_+,?[]().-&*^%'

# print header
header = 'Password Generator'
print('\nPassword Generator')
print('=' * len(header) + "\n")
# Ask the user to input a password length, and store it in a variable
length = input('password length? ')
length = int(length)  # turn the user's input into a whole number

# Ask the user to input how many passwords want generated, and store it in a variable
amount = input('number of passwords? ')
amount = int(amount)  # turn the user's input into a whole number

for p in range(amount):
    password = ''  # start with an empty variable

    for c in range(length):  # using the `length` variable to repeat as many times as the user entered.
        password += random.choice(chars)
    print(password)
