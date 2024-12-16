#!/usr/bin/env python3
f = open("input.txt", "r")

numList = []
count = 0

for i in f.readlines():

    flag = True

    numList = i.split()
    numList = [int(item) for item in numList]
    
    if sorted(numList) == numList:
        for j in range(0, len(numList)-1):
            if ((numList[j+1]-numList[j]) > 3) or (numList[j+1] == numList[j]):
                flag = False

        if flag == True:
            count+=1

    elif sorted(numList, reverse=True) == numList:
        for j in range(0, len(numList)-1):
            if ((numList[j]-numList[j+1]) > 3) or (numList[j+1] == numList[j]):
                flag = False

        if flag == True:
            count+=1

print(count)