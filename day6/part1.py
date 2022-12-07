def unique(str):
    if sorted(list(str)) == sorted(set(str)):
        return True
    else:
        return False
input = open("input.txt")
line = input.readline()
result = ""
for index in range(len(line) - 4):
    if unique(line[index:index + 4]):
        result = index + 4
        break
print(result)