import numpy as np

input = open("input.txt")
crateSpace = np.zeros((9, 56), dtype=np.int8) # 9 piles of (at max 56 crates)
moveInstructions = False
for lineNum, line in enumerate(input):
    if lineNum == 8:
        moveInstructions = True
    if moveInstructions == False:
        for h, i in enumerate(range(1,36,4)):
            if np.int8(ord(line[i])) == 32:
                crateSpace[h][7 - lineNum] = 0
            else:
                crateSpace[h][7 - lineNum] = np.int8(ord(line[i]))

    if moveInstructions == True:
        if line.find("move") == 0:
            quantity, fr, to = int(line.split()[1]), int(line.split()[3]), int(line.split()[5])
            top = None
            move = []
            for crateInd, crate in enumerate(crateSpace[fr - 1]):
                if crate == 0:
                    top = crateInd - 1
                    break
            for i in range(quantity): # Remove the crates from this stack
                move.append(crateSpace[fr - 1][top - i])
                crateSpace[fr - 1][top - i] = 0
            for crateInd, crate in enumerate(crateSpace[to - 1]):
                if crate == 0:
                    top = crateInd - 1
                    break
            for i in range(quantity): # Adds the crates to the other stack
                crateSpace[to - 1][top + 1 + i] = move[i]

result = ""
for pile in crateSpace:
    previousCrate = chr(0)
    for crate in pile:
        if crate == 0:
            result += previousCrate
            break
        previousCrate = chr(crate)
print(result)