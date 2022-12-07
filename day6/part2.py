def unique(str):
    if sorted(list(str)) == sorted(set(str)):
        return True
    else:
        return False
input = open("input.txt")
line = input.readline()
result = ""
for index in range(len(line) - 14):
    if unique(line[index:index + 14]):
        result = index + 14
        break
print(result)