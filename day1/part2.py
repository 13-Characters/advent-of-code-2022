input = open("input.txt", encoding="utf-8")
caloriesList = []
calories = 0
for line in input:
    if line != '\n':
        calories = calories + int(line[:-1])
    else:
        caloriesList.append(calories)
        calories = 0
caloriesList.sort()
sum = 0
for num in caloriesList[-3:]:
    sum = sum + num
print(caloriesList[-2:])
print(sum)
