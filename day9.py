#!/usr/bin/env python

lines = [int(x.strip()) for x in open('day9.txt', 'r').readlines()]

def sum_to_90433990():
    for x in range(0, len(lines)):
        res = [lines[x]]
        res_sum = lines[x]
        for y in range(x+1, len(lines)):
            res.append(lines[y])
            res_sum += lines[y]
            if res_sum > 90433990:
                break
            if res_sum == 90433990:
                return res
    return None


def no_sum(idx, v):
    start = idx-25
    end = idx

    for x in range(start, end+1):
        for y in range(start+1, end+1):
            if lines[x]+lines[y] == v:
                return True
    
    print("does not sum", v)
    return False

def find_missing():
    idx = 25 
    while True:
        if idx >= len(lines):
            break

        no_sum(idx, lines[idx])

        idx += 1

r = sum_to_90433990()
print(min(r) + max(r))
find_missing()