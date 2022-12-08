import numpy as np
import re

input = open("input.txt")
directoryDictionary = {}
currentDirectory = "//"
parents = ["/"]
directoryName = ""
for line in input:
    if line.find("$ cd ") == 0 and line.find("$ cd .") != 0:
        parents.append(currentDirectory)
        for parent in parents:
            directoryName += parent + "/"
        if directoryName not in directoryDictionary:
            directoryDictionary[directoryName] = 0 # This will represent the size of the directory
    if line.find("$ cd .") == 0:
        parents.pop()
    if re.fullmatch("\d+ .+", line[:-1]) != None:
        size, fileName = line.split()
        for parent in parents:
            directoryDictionary[directoryName] += int(size)

result = 0
for name, size in directoryDictionary.items():
    if size <= 100000:
        print(f"{name} | size = {size}")
        result += size

print(result)