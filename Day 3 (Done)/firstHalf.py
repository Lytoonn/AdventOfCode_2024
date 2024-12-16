#!/usr/bin/env python3
import re

f = open('input.txt', 'r').read()

muls = []
pairsDigits = []

pattern = r'mul\(\d+,\d+\)'
digits = r'\d+,\d+'

muls = re.findall(pattern, f)
pairsDigits = [re.findall(digits, i) for i in muls]

list_ = []

for pairs in pairsDigits:
    for subPair in pairs:
        y = subPair.split(',')
        nums = [int(x) for x in y]
        list_.append(nums)

soma = 0
for num in list_:
    soma += num[0]*num[1]
    
print(soma)