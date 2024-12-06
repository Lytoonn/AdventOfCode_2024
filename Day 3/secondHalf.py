import re

f = open('input.txt', 'r').read()

pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
digits = r'\d+,\d+'

muls = re.findall(pattern, f)

flag = True
do_muls = []
list_ = []


for i in range(0, len(muls)):
    if muls[i] == 'do()':
        flag = True
    elif muls[i] == 'don\'t()':
        flag = False
    elif flag == True:
        do_muls.append(muls[i])

pairsDigits = [re.findall(digits, i) for i in do_muls]

for pairs in pairsDigits:
    for subPair in pairs:
        y = subPair.split(',')
        nums = [int(x) for x in y]
        list_.append(nums)

soma = 0
for num in list_:
    soma += num[0]*num[1]
    
print(soma)