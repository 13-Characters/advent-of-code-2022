import time
input = open("input.txt")

solidTiles = []
heights = []
startTime = time.time_ns()
for line in input: # Rock walls
    coords = line.split('->')
    coords = [(int(c.split(',')[0]), int(c.split(',')[1])) for c in coords]
    for i in range(len(coords) - 1):
        if coords[i][0] == coords[i + 1][0]: # If vertical
            t = [coords[i][1], coords[i + 1][1]]
            for j in range(min(t), max(t) + 1):
                solidTiles.append((coords[i][0], j))
        else: # If horizontal
            t = [coords[i][0], coords[i + 1][0]]
            for j in range(min(t), max(t) + 1):
                solidTiles.append((j, coords[i][1]))
                heights.append(coords[i][1])

walls = len(solidTiles)
floor = max(heights) + 2
sCoords = [(500, 0)]
result = 0
while True:
    sCoord = sCoords[-1]
    if (sCoord[0], sCoord[1] + 1) in solidTiles:
        if (sCoord[0] - 1, sCoord[1] + 1) not in solidTiles: # Place down-left
            sCoords.append((sCoord[0] - 1, sCoord[1] + 1))
        else:
            if (sCoord[0] + 1, sCoord[1] + 1) not in solidTiles: # Place down-right
                sCoords.append((sCoord[0] + 1, sCoord[1] + 1))
            else: # Place directly above
                solidTiles.append(sCoord)
                sCoords.pop()
                result += 1
                if sCoord == (500, 0):
                    break
    else:
        if sCoord[1] == floor - 1:
            solidTiles.append(sCoord)
            sCoords.pop()
            result += 1
            continue # I spent a lot of time debugging before adding this line
        sCoords.append((sCoord[0], sCoord[1] + 1))
for i in range(0, 12):
    str = ''
    for j in range(489, 513):
        if (j, i) in solidTiles:
            if solidTiles[-1] == (j, i):
                str += 'X'
            else:
                if solidTiles.index((j, i)) < walls:
                    str += '#'
                else:
                    str += 'o'
        else:
            str += "."
    print(str)
print('\n')

print(result)
print(f"{(time.time_ns() - startTime) / 1000000000} seconds") # This solution is slow but not as slow as it was before
