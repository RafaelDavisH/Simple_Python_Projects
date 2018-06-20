#!/bin/python3

from turtle import *


# === Build the Race Track
# write(0)  # turtle draws track markings for the race
# forward(100)  # turtle draw a line using the turtle
# write(5)  # turtle draws track markings for the race

# writing all the numbers in between to create markings
# write(0)
# # forward(20)
# # write(1)
# # forward(20)
# # write(2)
# # forward(20)
# # write(3)
# # forward(20)
# # write(4)
# # forward(20)
# # write(5)
# # forward(20)

speed(10)  # speed up the turtle so it draws faster.
penup()  # lifting the pen up or there will be a line drawn when moving the turtle
goto(-140, 140)  # moving the turtle to the top left

# create the markings with a for loop
for step in range(16):  # to get the turtle to print from 0 - 5 the range needs to be `range(6)`.
    write(step, align='center')  # center the numbers to the vertical lines.
    right(90)       # _
    forward(10)    # |  draw vertical lines to create a track
    pendown()      # |  right(90) makes the turtle turn right 90 degrees.
    forward(150)  # <   Moving forward(10) before putting the pen down leaves a small
    penup()        # |  gap between the number and the start of the line. After drawing
    backward(160)  # |  the line you lift up the pen and go backward(160) the length of the line plus the gap.
    left(90)        # -
    forward(20)

