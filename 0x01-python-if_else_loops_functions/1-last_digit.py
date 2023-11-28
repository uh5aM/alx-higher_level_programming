#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstN = number % 10
if number > 5:
    print("Last digit of {:d} is {:d} and is  greater than 5".format(number, lstN))
if lstN < 0:
    lstN = ((number * -1) % 10) * -1
elif lstN ==0:
    print("Last digit of {:d} is {:d} and is less 0".format(number, lstN))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, lstN))
