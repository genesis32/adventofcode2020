#!/usr/bin/env python

import math

def find_seat(d, mn, mx):
    if len(d) == 1:
        if d[0] in set(["F", "L"]):
            return mn
        if d[0] in set(["B", "R"]):
            return mx

    new_min = 0
    new_max = 0

    if d[0] in set(["F", "L"]):
        new_min = mn
        new_max = mx - int(math.ceil((mx - mn)/2))
    if d[0] in set(["B", "R"]):
        new_min = mn + int(math.ceil((mx - mn)/2))
        new_max = mx
    
    return find_seat(d[1:], new_min, new_max)

lines = open("day5.txt", "r").readlines()
max_seatid = -1
seatids = []
for line in lines:
    line = line.strip()
    row = line[:-3]
    column = line[-3:]
    seatid = (find_seat(row, 0, 127) * 8) + find_seat(column, 0, 7)
    seatids.append(seatid)
    max_seatid = max(seatid, max_seatid)
    
print("max seatid:", max_seatid)

seatids.sort()
for i in range(0, len(seatids)-1):
    if seatids[i] != seatids[i+1]-1:
        print("my seat", seatids[i]+1)