#!/usr/bin/env python

import copy

def get_neighbor_status(lines, row, column):
    ret = {}
    if column == 0:
        ret["left"] = None
    else:
        ret["left"] = lines[row][column-1]

    if row == 0:
        ret["up"] = None
    else:
        ret["up"] = lines[row-1][column]

    if column == len(lines[row])-1:
        ret["right"] = None
    else:
        ret["right"] = lines[row][column+1]

    if row == len(lines)-1:
        ret["down"] = None
    else:
        ret["down"] = lines[row+1][column]

    has_uldiag = column > 0 and row > 0
    if not has_uldiag:
        ret["uldiag"] = None
    else:
        ret["uldiag"] = lines[row-1][column-1] 

    has_urdiag = column < len(lines[row])-1 and row > 0
    if not has_urdiag:
        ret["urdiag"] = None
    else:
        ret["urdiag"] = lines[row-1][column+1] 

    has_lldiag = row < len(lines)-1 and column > 0 
    if not has_lldiag:
        ret["lldiag"] = None
    else:
        ret["lldiag"] = lines[row+1][column-1] 

    has_lrdiag = column < len(lines[row])-1 and row < len(lines)-1
    if not has_lrdiag:
        ret["lrdiag"] = None
    else:
        ret["lrdiag"] = lines[row+1][column+1] 

    return ret

def occupied_on(inp, outp, row, column):
    neighbors = get_neighbor_status(inp, row, column)
    can_sit = len([n for n in neighbors.values() if n in ('L', '.', None)]) == 8
    if can_sit:
        outp[row][column] = "#"
    return can_sit

def empty_on(inp, outp, row, column):
    neighbors = get_neighbor_status(inp, row, column)
    empty = inp[row][column] == "#" and len([n for n in neighbors.values() if n in ('#', )]) >= 4
    if empty:
        outp[row][column] = "L"
    return empty

def print_board(inp):
    for row in range(0, len(inp)):
        line = "".join(inp[row])
        print(line)

def process_board(inp, outp):
    for row in range(0, len(inp)):
        for column in range(0, len(inp[row])):
            if inp[row][column] == '.': 
                continue
            occupied_on(inp, outp, row, column)
            empty_on(inp, outp, row, column)

def diff_boards(inp0, inp1):
    for row in range(0, len(inp0)):
        for column in range(0, len(inp0[row])):
            if inp0[row][column] != inp1[row][column]:
                return True
    
    return False

def num_seats_occupied(inp0):
    ret = 0
    for row in range(0, len(inp0)):
        for column in range(0, len(inp0[row])):
            if inp0[row][column] == '#':
                ret += 1
    
    return ret

if __name__ == "__main__":
    inp = [list(x.strip()) for x in open('day11.txt', 'r').readlines()]
    output = copy.deepcopy(inp)

    while True:
        process_board(inp, output)

        if not diff_boards(inp, output):
            print(num_seats_occupied(output))
            break

        inp = output
        output = copy.deepcopy(inp)


