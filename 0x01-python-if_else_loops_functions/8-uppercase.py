#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            print("{:c}".format(ord(s) - 32), end='')
        else:
            print(s, end='')
    print()
