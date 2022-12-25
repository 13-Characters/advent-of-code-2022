input = open("input.txt").readlines()

sum = 0
values = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
for number in input:
    for place, digit in enumerate(number.replace("\n", "")):
        sum += values[digit] * (5 ** (len(number) - 1 - place)

print(sum)
