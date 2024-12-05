f = open("input.txt", "r")

list1 = []
list2 = []

for i in f.readlines():
    nums = i.split()
    list1.append(nums[0])
    list2.append(nums[1])

soma = 0

for i in range(0, len(list1)):
    count = list2.count(list1[i])
    aux = int(list1[i]) * count
    soma += aux

print(soma)

f.close()