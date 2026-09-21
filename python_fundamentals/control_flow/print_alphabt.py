#!/usr/bin/env python3
alphabt = 'a'

for char in range(ord('b'), ord('{')):

    if char != ord('q') and char != ord('e'):
        alphabt = alphabt + chr(char)

print(alphabt.format('q'))
