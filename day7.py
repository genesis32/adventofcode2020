#!/usr/bin/env python

import re

lines = [x.strip() for x in open('day7.txt', 'r').readlines()]

mapping = dict()
for line in lines:
    root_bag = re.search(r'(\w+ \w+) bags contain', line)[1]
    sub_bags = re.findall(r'(\d+) (\w+ \w+) bag', line)
    if not root_bag in mapping:
        mapping[root_bag] = dict([(b[1], int(b[0])) for b in sub_bags])

def find_shiny_gold():
    def find_shiny_gold_helper(mapping, keys, path, ret):
        for k in keys:
            if k == 'shiny gold':
                ret.append(tuple(path))
            else:
                path.append(k)
                find_shiny_gold_helper(mapping, mapping[k].keys(), path, ret)
                path.remove(k)
    s = set()
    for m in mapping:
        ret = []
        find_shiny_gold_helper(mapping, mapping[m].keys(), [m], ret)
        for path in ret:
            for bag in path:
                s.add(bag)
    return len(s)


def shiny_gold_contains():
    def shiny_gold_contains_helper(mapping, sub_bags):
       if len(sub_bags) == 0: 
           return 0
       total = 0
       for bag in sub_bags:
           child_bags = shiny_gold_contains_helper(mapping, mapping[bag])
           if child_bags > 0:
            total += (sub_bags[bag] + sub_bags[bag] * child_bags)
           else:
            total += sub_bags[bag] 
       return total

    return shiny_gold_contains_helper(mapping, mapping['shiny gold'])
        
print(find_shiny_gold())
print(shiny_gold_contains())
