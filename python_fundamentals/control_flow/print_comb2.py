#!/usr/bin/env python3
oneDigit = "0{0}"
twoDigit = "{0}"
delim = ", "

for i in range(0, 99 + 1):

    if i == 0:
        curline = oneDigit.format(i) + delim
    elif i < 10 and i > 0:
        curline = curline + oneDigit.format(i) + delim
    elif i > 9 and i < 99:
        curline = curline + twoDigit.format(i) + delim
    elif i == 99:
        curline = curline + twoDigit.format(i)

print(curline)
