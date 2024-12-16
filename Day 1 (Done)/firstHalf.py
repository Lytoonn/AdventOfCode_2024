#!/usr/bin/env python3
f = open("input.txt", "r")

list1 = []
list2 = []

for i in f.readlines():
    nums = i.split()
    list1.append(nums[0])
    list2.append(nums[1])

list1.sort()
list2.sort()

soma = 0

for i in range(0, len(list1)):
    n1 = int(list1[i])
    n2 = int(list2[i])

    if n1<n2:
        soma += n2-n1
    else:
        soma += n1-n2
        
print(soma)

f.close()