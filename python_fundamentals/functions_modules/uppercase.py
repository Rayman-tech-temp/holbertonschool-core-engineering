#!/usr/bin/env python3

def uppercase(str):
    newstr = ''
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            newstr = newstr + chr(ord(i)-32)
        else:
            newstr = newstr + i

    print(newstr.format(''))
