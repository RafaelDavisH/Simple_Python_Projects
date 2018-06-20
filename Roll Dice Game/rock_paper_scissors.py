#!/bin/python3

from random import randint
player = input('rock (r), paper (p) or scissors (s)?')

# ===== Player =====
if player == 'r':
    print('0', 'vs', end=' ')

elif player == 'p':
    print('___', 'vs', end=' ')

else:
    player = 's'
    print('>8', 'vs', end=' ')

chosen = randint(1, 3)
# print(chosen)

# ===== Computer =====
if chosen == 1:
    computer = 'r'
    print('0')

elif chosen == 2:
    computer = 'p'
    print('___')

else:
    computer = 's'
    print('>8')

# print(computer)


# ===== Check the result =======
if player == computer:
    print('DRAW!')

elif player == 'r' and computer == 's':
    print('Player wins!')

elif player == 'r' and computer == 'p':
    print('Computer wins!')

elif player == 'p' and computer == 'r':
    print('Player wins!')

elif player == 'p' and computer == 's':
    print('Computer wins!')

elif player == 's' and computer == 'p':
    print('Player wins!')

elif player == 's' and computer == 'r':
    print('Computer wins!')