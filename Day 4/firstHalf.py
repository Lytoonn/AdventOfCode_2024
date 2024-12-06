f = open('input.txt', 'r').read()

word = ('X', 'M', 'A', 'S')
directions = (-1, 0, 1)
data = [list(line.strip()) for line in f.splitlines()]
count = 0

def matches(row, col, dirRow, dirCol):
    for i in range(1, 4): 
        newRow = row + dirRow * i
        newCol = col + dirCol * i
        if not (0 <= newRow < len(data) and 0 <= newCol < len(data[i])) or data[newRow][newCol] != word[i]:
            return False
    return True

for row in range(len(data)):
    for col in range(len(data[row])):
        if data[row][col] == 'X':
            for dirRow in directions:
                for dirCol in directions:
                    if dirRow == 0 and dirCol == 0:
                        continue
                    if matches(row, col, dirRow, dirCol):
                        count += 1

print(count)