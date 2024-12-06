f = open('input.txt', 'r').read()

word = ('M', 'A', 'S')
directions = (-1, 1)
data = [list(line.strip()) for line in f.splitlines()]
count = 0

def matches(row, col, dirRow, dirCol):
    for i in range(1, 3): 
        newRow = row + dirRow * i
        newCol = col + dirCol * i
        if not (0 <= newRow < len(data) and 0 <= newCol < len(data[i])) or data[newRow][newCol] != word[i]:
            return False
    return True

for row in range(0, len(data), 2):
    for col in range(0, len(data[row]), 2):
        if data[row][col] == 'M':
            for dirRow in directions:
                for dirCol in directions:
                    if dirRow == 0 and dirCol == 0:
                        continue
                    if matches(row, col, dirRow, dirCol):
                        count += 1

print(count)