import numpy as np
import re

def compareIntegers(a, b):
    if a < b:
        return -1
    if a == b:
        return 0
    if a > b:
        return 1
def compareLists(a, b):
    if type(a) is int:
        a = [a]
    if type(b) is int:
        b = [b]
    for i in range(min(len(a), len(b))):
        if type(a[i]) == list or type(b[i]) == list:
            if compareLists(a[i], b[i]) != 0:
                return compareLists(a[i], b[i])
        else:
            if compareIntegers(a[i], b[i]) != 0:
                return compareIntegers(a[i], b[i])
    return compareIntegers(len(a), len(b))

input = open("input.txt").readlines()

index = 1
result = 0
for i in range(0, len(input), 3):
    a = eval(input[i])
    b = eval(input[i + 1])
    if compareLists(a, b) == -1:
        result += index
        print(index)
    index += 1

print(result)