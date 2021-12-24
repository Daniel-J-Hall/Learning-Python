import numpy as np
import keyboard
from time import sleep

zeros = np.zeros([7, 7])
ones = np.ones([1, 1])

x0 = 3
x1 = 4

y0 = 3
y1 = 4

zeros[x0:x1, y0:y1] = ones
print(zeros, "\n")

while True:
    sleep(0.06)
    if x0 == 8 or x1 == 8 or y0 == 8 or y1 == 8:
        print("You fell out of the world.")
        break
    if x0 == -1 or x1 == -1 or y0 == -1 or y1 == -1:
        print("You fell out of the world.")
        break

    if keyboard.is_pressed("up"):
        x0 += -1
        x1 += -1

        zeros = np.zeros([7, 7])
        zeros[x0:x1, y0:y1] = ones

        print(zeros)
        print(f"|X0: {x0}|X1: {x1}|Y0: {y0}|Y1: {y1}|\n")

    if keyboard.is_pressed("down"):
        x0 += 1
        x1 += 1

        zeros = np.zeros([7, 7])
        zeros[x0:x1, y0:y1] = ones

        print(zeros)
        print(f"|X0: {x0}|X1: {x1}|Y0: {y0}|Y1: {y1}|\n")

    if keyboard.is_pressed("left"):
        y0 += -1
        y1 += -1

        zeros = np.zeros([7, 7])
        zeros[x0:x1, y0:y1] = ones

        print(zeros)
        print(f"|X0: {x0}|X1: {x1}|Y0: {y0}|Y1: {y1}|\n")

    if keyboard.is_pressed("right"):
        y0 += 1
        y1 += 1

        zeros = np.zeros([7, 7])
        zeros[x0:x1, y0:y1] = ones

        print(zeros)
        print(f"|X0: {x0}|X1: {x1}|Y0: {y0}|Y1: {y1}|\n")
