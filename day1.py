#!/usr/bin/env python

def find_two_that_sum(input, target):
    for v in input:
        other_value = target - v
        try:
            input.index(other_value) 
            print("target=%d v=%s product=%d" % (target, (v, other_value), v * other_value))
            return
        except:
            pass

def find_three_that_sum(input, target):
    for i in range(0, len(input)):
        for j in range(i+1, len(input)):
            for k in range(j+1, len(input)):
                sum = input[i] + input[j] + input[k]
                if sum == target:
                    prod = input[i] * input[j] * input[k]
                    print("target=%d v=%s product=%d" % (target, (input[i], input[j], input[k]), prod))
                    return
        
input = sorted([int(x) for x in open("day1.txt", "r").readlines()])
find_two_that_sum(input, 2020)
find_three_that_sum(input, 2020)