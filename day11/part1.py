input = open("input.txt").readlines()
monkeyList = []
operands = [] # this exists because i couldn't figure out a good way for lambda to be "by value" and not "by reference"
class monkey():
    def __init__(self, items, method, test, throwToT, throwToF):
        self.items = items.reverse() # First items to be inspected are last in the array
        self.method = method
        self.test = test
        self.throwToT = throwToT
        self.throwToF = throwToF
        self.inspectCount = 0
    def inspection(self):
        self.items[-1] = self.method(self.items[-1])
        self.items[-1] = self.items[-1] // 3
        if self.test(self.items[-1]):
            self.throwToT.items.insert(0, self.items[-1])
        else:
            self.throwToF.items.insert(0, self.items[-1])
        self.items.pop()
        self.inspectCount += 1

for num in range(0, len(input), 7):
    # Interpret starting items
    items = input[num + 1].removeprefix("  Starting items:")
    items = items.split(", ")
    items = [int(x) for x in items]
    # Operation into Python method
    operation = input[num + 2]
    operation = eval(f"lambda old: {operation.removeprefix('  Operation: new =')}") # stolen from the python discord
    # https://discord.com/channels/267624335836053506/1051367410856366150/1051386288328159242
    # Test into Python method
    test = input[num + 3]
    test = eval(f"lambda x: x % {int(test.removeprefix('  Test: divisible by '))} == 0")
    # Throw to T
    throwToT = input[num + 4]
    throwToT = int(throwToT.removeprefix('    If true: throw to monkey '))
    # Throw to F
    throwToF = input[num + 5]
    throwToF = int(throwToF.removeprefix('    If false: throw to monkey '))
    monkeyAdd = monkey(items, operation, test, throwToT, throwToF)
    monkeyAdd.items = items
    monkeyAdd.method = operation
    monkeyAdd.test = test
    monkeyList.append(monkeyAdd)

for monkey in monkeyList:
    monkey.throwToT = monkeyList[monkey.throwToT]
    monkey.throwToF = monkeyList[monkey.throwToF]
# I stg in part 2 if they ask for like 1000 rounds or some shit
for i in range(20):
    for monkey in monkeyList:
        while len(monkey.items) != 0:
            monkey.inspection()

counts = []
for monkey in monkeyList:
    counts.append(monkey.inspectCount)
counts.sort(reverse=True)
print(counts[0] * counts[1])

