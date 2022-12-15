import functools

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
packetList = [[[2]], [[6]]]

result = 0
for line in input:
    if line != '\n':
        a = eval(line)
        packetList.append(a)
    else:
        continue

packetList.sort(key=functools.cmp_to_key(compareLists))
result = (packetList.index([[2]]) + 1) * (packetList.index([[6]]) + 1)
print(result)