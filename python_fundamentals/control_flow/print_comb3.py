#!/usr/bin/env python3
oneDigit = "0{0}"
twoDigit = "{0}"
delim = ", "
i = 0

while i < 90:

    if i == 1:
        curline = oneDigit.format(i) + delim
    elif i > 9 and int(i % 10) == 0:
        i = i + int(i / 10)
    elif i < 10 or i % 10 != int(i / 10) % 10:
        if i < 10 and i > 0:
            curline = curline + oneDigit.format(i) + delim
        elif i > 9 and i < 89:
            curline = curline + twoDigit.format(i) + delim
        elif i == 89:
            curline = curline + twoDigit.format(i)
    i += 1
print(curline)
