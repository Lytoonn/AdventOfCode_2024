#!/usr/bin/env python3
def asc(numList: list) -> int:
    flag = True

    for j in range(0, len(numList)-1):
        if ((numList[j+1]-numList[j]) > 3) or (numList[j+1] == numList[j]):
            flag = False

    if flag == True:
        return 1
    return 0

def desc(numList: list) -> int:
    flag = True

    for j in range(0, len(numList)-1):
        if ((numList[j]-numList[j+1]) > 3) or (numList[j+1] == numList[j]):
            flag = False

    if flag == True:
        return 1
    
    return 0

def main():
    f = open("input.txt", "r")

    numList = []
    count = 0

    for i in f.readlines():

        flag = False
        
        numList = i.split()
        numList = [int(item) for item in numList]

        if sorted(numList) == numList:
            if asc(numList):
                count += 1
                flag = True

        elif sorted(numList, reverse=True) == numList:
            if desc(numList):
                count += 1
                flag = True
        
        if flag==False:
            
            for j in range(0, len(numList)):
                newList = numList.copy()
                newList.pop(j)
                if sorted(newList) == newList:
                    if asc(newList):
                        count += 1
                        break

                elif sorted(newList, reverse=True) == newList:
                    if desc(newList):
                        count += 1
                        break
                    
    print(count)

main()