from collections import deque

filename = "puzzleFile.txt"

stacks = []
moves = []

with open(filename, "r") as f:
    for line in f:
        if len(line) > 1 and line[1] == '1':
            stackCount = int(line.strip()[-1])
            for i in range(0, stackCount):
                stacks.append(deque([]))
with open(filename, "r") as f:
    for line in f:
        if 'move' in line:
            splitLine = line.strip().split(' ')
            moves.append([int(splitLine[1]), int(
                splitLine[3]), int(splitLine[5])])
        else:
            if line != '\n' and line[1] != '1':
                stripLine = line.strip().split(' ')
                for i in range(0, stackCount):
                    if stripLine[i][1] != '.': # had to modify puzzle input to have [.] in it to stop blank spaces causing issues. probably not the best answer here
                        stacks[i].append(stripLine[i][1])

for move in moves:
    els = []
    for i in range(0, move[0]):
        els.append(stacks[move[1] - 1].popleft())
    for i in range(0, move[0]):
        stacks[move[2] - 1].appendleft(els.pop())

sol = ''
for j in range(0, stackCount):
    sol += stacks[j][0]
print(sol)