#!/bin/python3
import random

# create a list of characters to choose from
# containing letters, numbers and punctuation characters
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ123457890!#$@_+,?[]().-&*'

password = ''  # start with an empty variable

for c in range(10):
    password += random.choice(chars)
print(password)
