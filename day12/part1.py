# I can not do pathfinding
import string
import numpy as np
input = open("input.txt").readlines()
heightMap = np.zeros((len(input), len(input[0]) - 1), dtype=int)
adjacency = {}
visited = []

for i, line in enumerate(input):
    for j, char in enumerate(line):
        if j < heightMap.shape[1] and char in string.ascii_lowercase:
            heightMap[i][j] = string.ascii_lowercase.index(char)
        if char == 'S':
            start = (i, j)
            heightMap[i][j] = 0
        if char == 'E':
            end = (i, j)
            heightMap[i][j] = 25

visited.append(start)
# There's definitely a better way of doing this
i = 0
stop = False
while not stop:
    current = visited[i]
    numOfTraversables = 0
    adjacents = [(current[0] - 1, current[1]), (current[0], current[1] - 1), (current[0] + 1, current[1]), (current[0], current[1] + 1)]
    for a in adjacents:
        traversable = a[0] in range(heightMap.shape[0]) and a[1] in range(heightMap.shape[1]) and \
                      heightMap[a[0]][a[1]] - heightMap[current[0]][current[1]] <= 1
        if traversable:
            numOfTraversables += 1
            if a in adjacency and a not in visited:
                adjacency[a].append(current)
            if a not in adjacency and a not in visited:
                adjacency[a] = [current]
            if a not in visited:
                visited.append(a)
            if a == end:
                stop = True
                break
    if numOfTraversables != 0:
        i += 1

path = []
tracer = end # traces the path back
while True:
    if tracer in adjacency:
        path.append(tracer)
        tracer = adjacency[tracer][0]
    else:
        break
print(len(path))