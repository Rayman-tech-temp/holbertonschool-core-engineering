#!/usr/bin/env python3
newline = "{0} = 0x{0:x}\n"
curline = "0 = 0x0\n"
for i in range(0 + 1, 98 + 1):
    if i == 98:
        newline = "{0} = 0x{0:x}"

    curline = curline + newline.format(i)

print(curline)
