input = open("input.txt", encoding="utf-8")
mostCalories = 0
calories = 0
for line in input:
    if line != '\n':
        calories = calories + int(line[:-1])
    else:
        calories = 0
    if calories > mostCalories:
        mostCalories = calories
        print(line)
print(mostCalories)
