# Object oriented attempt
import numpy as np
import re

class File():
    def __init__(self, name, size, parent=""):
        self.name = name
        self.parent = parent
        self.size = size


input = open("input.txt")
directories = []
currentDirectory = ""
parents = []
for line in input:
    if line.find("$ cd ") == 0 and line.find("$ cd .") != 0:
        currentDirectory = File(line[5:-1], 0, parent=currentDirectory)
        parents.append(currentDirectory)
        if currentDirectory not in directories:
            directories.append(currentDirectory)
    if line.find("$ cd .") == 0:
        parents.pop()
        currentDirectory = parents[-1]
    if re.fullmatch("\d+ .+", line[:-1]) != None:
        size, fileName = line.split()
        for parent in parents:
            parent.size += int(size)

results = []
for directory in directories:
    if directory.size > (30000000 - 70000000 + directories[0].size):
        results.append(directory.size)
results.sort()

print(results[0])