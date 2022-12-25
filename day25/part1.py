input = open("input.txt").readlines()

sum = 0
values = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
values2 = ["0", "1", "2", "=", "-"]
for number in input:
    numberValue = 0
    number = number.replace("\n", "")
    for place, digit in enumerate(number):
        numberValue += values[digit] * (5 ** (len(number) - 1 - place))
    sum += numberValue

print(sum)
result = ""
while sum > 0:
    digit = values2[sum % 5]
    if sum % 5 > 2:
        sum += 5
    sum = sum // 5
    result = digit + result
print(result)
