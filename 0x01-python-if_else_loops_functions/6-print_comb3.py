#!/usr/bin/python3
for i in range(0, 9):
    for p in range(i+ 1, 10):
        if i == 8:
            print("{}{}".format(i , p))
        else:
            print("{}{}".format(i, p), end=",")
