# Check if its SAFE when the order is Ascending
def asc(numList: int) -> int:
    flag = True

    for j in range(0, len(numList)-1):
        if ((numList[j+1]-numList[j]) > 3) or (numList[j+1] == numList[j]):
            flag = False

    if flag == True:
        return 1
    return 0

# Check if its SAFE when the order is Descending
def desc(numList: int) -> int:
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

        numList = i.split()
        numList = [int(item) for item in numList]
        
        if sorted(numList) == numList:
            count += asc(numList)

        elif sorted(numList, reverse=True) == numList:
            count += desc(numList)
        
        else:
            for j in range(0, len(numList)):
                newList = numList.copy()
                newList.pop(j)
                
                if sorted(newList) == newList:
                    count += asc(newList)

                elif sorted(newList, reverse=True) == newList:
                    count += desc(newList)
    print(count)

main()