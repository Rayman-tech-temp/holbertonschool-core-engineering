#!/usr/bin/env python3
newline = "{0} = 0x{0:x}\n"
curline = ""
for i in range(0, 98 + 1):
    curline = curline + newline.format(i)

print(curline)
