#!/usr/bin/env python3
newchr = '{0}'
alphabt = newchr
for char in range(ord('a'), ord('z') + 1):

    if char != ord('q') and char != ord('e'):
        if char == ord('a'):
            alphabt = alphabt.format(chr(char))

        else:
            alphabt = alphabt + newchr.format(chr(char))

print(alphabt)
