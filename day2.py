#!/usr/bin/env python

def is_password_valid(line):
    num_times, symbol, password = line.split()
    symbol = symbol[:-1]
    minn, maxn = [int(x) for x in num_times.split("-")]
    num_symbols_in_password = password.count(symbol)
    return num_symbols_in_password >= minn and num_symbols_in_password <= maxn

def is_password_valid2(line):
    num_times, symbol, password = line.split()
    symbol = symbol[:-1]
    minn, maxn = [int(x) for x in num_times.split("-")]
    return (password[minn-1] == symbol or password[maxn-1] == symbol) and not (password[minn-1] == symbol and password[maxn-1] == symbol)

lines = open("day2.txt", "r").readlines()

num_valid = 0
for line in lines:
    if is_password_valid2(line):
        num_valid += 1
print("num valid: ", num_valid)
