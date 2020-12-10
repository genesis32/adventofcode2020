#!/usr/bin/env python

lines = [int(x.strip()) for x in open('day10.txt', 'r').readlines() if x != ""]
lines.sort()
lines.insert(0, 0)
lines.append(lines[-1]+3)

memory = dict()
def valid_adapters(i, memory):
    if lines[i] == lines[-1]: 
        return 1

    ret = 0
    for j in range(i+1, len(lines)):
        diff = lines[j] - lines[i]
        if diff > 3:
            break

        if i in memory:
            return memory[i]

        ret += valid_adapters(j, memory)

    memory[i] = ret
    return ret

def how_many_diff(): 
    idx = 0 
    diff_one = 0 
    diff_three = 0
    while True:
        if idx >= len(lines)-1: break

        diff = lines[idx+1] - lines[idx]
        if diff == 1:
            diff_one += 1
        elif diff == 3:
            diff_three += 1

        idx += 1
    print(diff_one * diff_three)

# how_many_diff()
memory = {}
print(valid_adapters(0, memory))
