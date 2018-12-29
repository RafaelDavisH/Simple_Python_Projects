"""
This game simple game guessing program was found at raywendirlich.com site
in the article https://www.raywenderlich.com/2379-programming-for-teens-beginning-python-tutorial
The sole purpose of rewriting this guess is to have reference for a young community program
where teens will learn Python through simple programs.
"""

"""
Young Students will cover the fundamental of Python which are:
Variables, Variable Types, Adding Strings and Integers, If Statements,
For Loops, Functions, while loops, capturing User input and simple use
of imports.
"""

# This module generates a random number
import random

# Run program until person guesses correctly
running = True

# Generate a random number for player to guess
number = random.randint(0, 10)

while running:
    # Ask the player to guess the number and store it in a variable
    guess = raw_input("Guess the Number:  ")
    # Convert string into a integer
    guess_int = int(guess)
    # Compare players guess to random number selected
    if number > guess_int:
        print "Too low!"
    if number < guess_int:
        print "Too high!"
    if number == guess_int:
        print "You got it!"
        running = False  # Stop the program once guessed