from collections import deque
from enum import Enum
Direction = Enum("Direction", ["NORTH", "SOUTH", "WEST", "EAST"])
def move(elf):
    global roundNum, elves
    directionOrder = deque([Direction.EAST, Direction.NORTH, Direction.SOUTH, Direction.WEST])
    adjacents = [(x, y) for x in range(elf[0] - 1, elf[0] + 2) for y in range(elf[1] - 1, elf[1] + 2)]
    adjacents.remove(elf)
    canMoveNorth = (elf[0] - 1, elf[1] - 1) not in elves and (elf[0], elf[1] - 1) not in elves and (elf[0] + 1, elf[1] - 1) not in elves
    canMoveSouth = (elf[0] - 1, elf[1] + 1) not in elves and (elf[0], elf[1] + 1) not in elves and (elf[0] + 1, elf[1] + 1) not in elves
    canMoveEast = (elf[0] + 1, elf[1] - 1) not in elves and (elf[0] + 1, elf[1]) not in elves and (elf[0] + 1, elf[1] + 1) not in elves
    canMoveWest = (elf[0] - 1, elf[1] - 1) not in elves and (elf[0] - 1, elf[1]) not in elves and (elf[0] - 1, elf[1] + 1) not in elves
    # Implement the changing list of directions
    directionOrder.rotate(-roundNum)
    # This is really bad
    if all([adj not in elves for adj in adjacents]): return elf
    for dir in directionOrder:
        if dir == Direction.NORTH and canMoveNorth: return (elf[0], elf[1] - 1)
        if dir == Direction.SOUTH and canMoveSouth: return (elf[0], elf[1] + 1)
        if dir == Direction.EAST and canMoveEast: return (elf[0] + 1, elf[1])
        if dir == Direction.WEST and canMoveWest: return (elf[0] - 1, elf[1])
    return elf

input = open("input.txt").readlines()

elves = []
for yCoord, line in enumerate(input):
    line = line.replace("\n", "")
    for xCoord, char in enumerate(line):
        if char == '#':
            elves.append((xCoord, yCoord))


roundNum = 1
while roundNum <= 10:
    proposals = []
    for i, elf in enumerate(elves): proposals.insert(i, move(elf))
    for i, proposal in enumerate(proposals):
        if proposals.count(proposal) > 1:
            indices = filter(lambda x: proposals[x] == proposal, range(len(proposals)))
            for ij in list(indices):
                proposals[ij] = elves[ij]

    elves = proposals
    roundNum += 1

result = 0
xMin = min([elf[0] for elf in elves])
xMax = max([elf[0] for elf in elves])
yMin = min([elf[1] for elf in elves])
yMax = max([elf[1] for elf in elves])

for y in range(yMin, yMax + 1):
    for x in range(xMin, xMax + 1):
        if (x, y) not in elves:
            result += 1
print(result)