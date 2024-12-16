f = open('input.txt', 'r').read()

data = [list(line.strip()) for line in f.splitlines()]
count = 0

for row in range(len(data)-1):
    for col in range(len(data[row])-1):
        if data[row][col] == 'A':
            if data[row-1][col-1] == 'M' and data[row+1][col+1] == 'S' and data[row-1][col+1] == 'M' and data[row+1][col-1] == 'S' or data[row-1][col-1] == 'S' and data[row+1][col+1] == 'M' and data[row-1][col+1] == 'S' and data[row+1][col-1] == 'M' or data[row-1][col-1] == 'M' and data[row+1][col+1] == 'S' and data[row-1][col+1] == 'S' and data[row+1][col-1] == 'M' or data[row-1][col-1] == 'S' and data[row+1][col+1] == 'M' and data[row-1][col+1] == 'M' and data[row+1][col-1] == 'S':
                count+=1

print(count)