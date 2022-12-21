# At least it's better then putting the structure in Minecraft and manually counting each block of obsidian
input = open("input.txt")
def isAdjacent(coord1, coord2):
    diff = [abs(coord1[i] - coord2[i]) for i in range(len(coord1))]
    if diff.count(0) == len(coord1) - 1 and diff.count(1) == 1:
        return True
    return False
def listAdjacents(coord):
    result = []
    for i in range(3):
        adj = list(coord)
        adj[i] = adj[i] - 1
        result.append(tuple(adj))
        adj[i] = adj[i] + 2
        result.append(tuple(adj))
    return result
coordList = []
adjacents = []
for line in input:
    coordList.append(eval(f"({line})"))

corner = tuple([max([c[i] for c in coordList]) + 2 for i in range(3)]) # Corner of bounding box (hopefully this isn't filled)
outsideAir = [corner]
#Flood fill
while True:
    listSize = len(outsideAir)
    for block in outsideAir:
        for adj in listAdjacents(block):
            inRange = True
            for i in range(3):
                if adj[i] not in range(-1, corner[i] + 1):
                    inRange = False
            if adj not in outsideAir and adj not in coordList and inRange:
                outsideAir.append(adj)
    if len(outsideAir) == listSize:
        break

area = 6 * len(outsideAir)
for c1 in outsideAir:
    for c2 in outsideAir:
        if c1 == c2: continue
        if isAdjacent(c1, c2): area -= 1

corner = [x + 2 for x in corner]
print(area - (2*corner[0]*corner[1]) - (2*corner[0]*corner[2]) - (2*corner[1]*corner[2]))