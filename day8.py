#!/usr/bin/env python

import copy

def run_failed_acc_value():
    idx = 0
    global_acc = 0
    while True:
        if idx == len(instructions): break
        if instructions[idx][2] == 1:
            print("global_acc", global_acc)
            break
        instructions[idx][2] += 1
        if instructions[idx][0] == "nop":
            idx += 1
        elif instructions[idx][0] == "jmp":
            idx += instructions[idx][1]
        elif instructions[idx][0] == "acc":
            global_acc += instructions[idx][1]
            idx += 1

def run_program(instructions):
    idx = 0
    global_acc = 0
    while True:
        if idx == len(instructions):
            print("global_acc", global_acc)
            return True
        if instructions[idx][2] == 1:
            return False
        instructions[idx][2] += 1
        if instructions[idx][0] == "nop":
            idx += 1
        elif instructions[idx][0] == "jmp":
            idx += instructions[idx][1]
        elif instructions[idx][0] == "acc":
            global_acc += instructions[idx][1]
            idx += 1

def part2():
    idx = 0
    while True:
        my_instructions = copy.deepcopy(instructions)
        if my_instructions[idx][0] == "nop":
            my_instructions[idx][0] = "jmp"
            if run_program(my_instructions):
                print("success")
                break
        elif my_instructions[idx][0] == "jmp":
            my_instructions[idx][0] = "nop"
            if run_program(my_instructions):
                print("success")
                break
        idx += 1

lines = [x.strip() for x in open('day8.txt', 'r').readlines()]

instructions = []
for line in lines:
    instruction, value = line.split()
    instructions.append([instruction, int(value), 0])

part2()