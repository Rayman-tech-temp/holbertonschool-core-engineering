#!/usr/bin/env python3
newchr = '{0}'
alphabt = ''
for char in range(ord('a'), ord('z') + 1):

    if char != ord('q') and char != ord('e'):
        alphabt = alphabt + newchr.format(chr(char))

print(alphabt)
