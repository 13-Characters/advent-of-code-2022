input = open("input.txt")
crateSpace = [] # List of Strings
moveInstructions = False
for lineNum, line in enumerate(input):
    if moveInstructions == False and line[1] == "1": # wow python has short circuit evaluation
        moveInstructions = True
    if moveInstructions == False:
        for h, i in enumerate(range(1,36,4)):
            if h >= len(crateSpace):
                crateSpace.append("")
            if line[i] != " ":
                crateSpace[h] = line[i] + crateSpace[h] # First characters = bottom, last characters = top
    if moveInstructions == True:
        if line.find("move") == 0:
            quantity, fr, to = int(line.split()[1]), int(line.split()[3]), int(line.split()[5])
            move = []
            for i in range(quantity): # Remove the crates from this stack
                move.append(crateSpace[fr - 1][-1])
                crateSpace[fr - 1] = crateSpace[fr - 1][:-1]
            for i in range(quantity): # Adds the crates to the other stack
                crateSpace[to - 1] += move[i]
result = ""
for pile in crateSpace:
    result += pile[-1]
print(result)