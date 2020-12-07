#!/usr/bin/env python

def group_answered_yes2(group):
    answered_yes = []
    for person in group: 
        answered_yes.append(set(person))

    if len(answered_yes) == 1:
        return len(answered_yes[0])

    a = answered_yes[0].intersection(*answered_yes[1:])
    return len(a)

def group_answered_yes(group):
    answered_yes = set()
    for person in group: 
        for q in person:
            answered_yes.add(q)
    return len(answered_yes)

lines = open("day6.txt", "r").readlines()
num_valid_records = 0
current_group = []
num_answered = 0
for line in lines:
    line = line.strip()
    if line == "":
        num_answered += group_answered_yes2(current_group)
        current_group = []
        continue
    current_group.append(line)

num_answered += group_answered_yes2(current_group)
print("num_answered:", num_answered)