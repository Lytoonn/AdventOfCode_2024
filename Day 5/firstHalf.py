#!/usr/bin/env python3
f = open('input.txt', 'r')

def check_rule(nums, rule):
    read = set()
    for n in nums:
        if n in rule and len(rule[n].intersection(read))>0:
            return 0
        read.add(n)
    return nums[len(nums)//2]

rules = {}
count = 0

for i in f.readlines():
    if len(i.split()) == 0:
        break
    a, b = [int(x) for x in i.strip().split('|')]
    if a not in rules:
        rules[a] = set()
    rules[a].add(b)

for i in f.readlines():
    nums = [int(x) for x in i.strip().split(',')]
    print(nums)