#!/usr/bin/env python

def find_path(forest):
    xindex = 0
    num_trees = 0
    for row in forest:
        if xindex >= len(row):
            return -1

        if row[xindex] == '#':
            num_trees += 1
        xindex += 3

    return num_trees

def find_path2(forest, x_stride, y_stride):
    num_jumps_per_line = len(forest[0]) / x_stride
    num_dupes = int(len(forest)/num_jumps_per_line)+1
    forest = [f*num_dupes for f in forest]
    xindex = 0
    num_trees = 0
    for currenty in range(0, len(forest), y_stride):
        if xindex >= len(forest[currenty]):
            return -1

        if forest[currenty][xindex] == '#':

            num_trees += 1
        xindex += x_stride

    return num_trees

# print(find_path([x.rstrip()*33 for x in open("day3.txt", "r").readlines()]))

a = find_path2([x.rstrip() for x in open("day3.txt", "r").readlines()], 1, 1)
b = find_path2([x.rstrip() for x in open("day3.txt", "r").readlines()], 3, 1)
c = find_path2([x.rstrip() for x in open("day3.txt", "r").readlines()], 5, 1)
d = find_path2([x.rstrip() for x in open("day3.txt", "r").readlines()], 7, 1)
e = find_path2([x.rstrip() for x in open("day3.txt", "r").readlines()], 1, 2)

print(a * b * c * d * e)