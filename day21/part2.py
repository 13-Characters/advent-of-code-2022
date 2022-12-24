import re
input = open("input.txt").readlines()
def calculate(name):
    if name in monkeys:
        if type(monkeys[name]) == int:
            return monkeys[name]
        else:
            if '+' in monkeys[name]:
                name1, name2 = monkeys[name].split(" + ")
                return calculate(name1) + calculate(name2)
            if '-' in monkeys[name]:
                name1, name2 = monkeys[name].split(" - ")
                return calculate(name1) - calculate(name2)
            if '*' in monkeys[name]:
                name1, name2 = monkeys[name].split(" * ")
                return calculate(name1) * calculate(name2)
            if '/' in monkeys[name]:
                name1, name2 = monkeys[name].split(" / ")
                return calculate(name1) // calculate(name2)
    else:
        raise Exception("oh no name isn't in monkeys")
monkeys = {}
parents = {}
for line in input:
    name, expression = line.split(": ")
    expression = expression.replace("\n", "")
    if re.match("\d+", expression):
        expression = int(expression)
    monkeys[name] = expression

for name, expression in monkeys.items():
    if type(expression) == str:
        name1, operator, name2 = monkeys[name].split()
        parents[name1] = name
        parents[name2] = name

unknowns = ["humn"]
while True:
    if parents[unknowns[-1]] == "root":
        break
    unknowns.append(parents[unknowns[-1]])

monk1 = monkeys["root"].split()[0]
result = calculate(monkeys["root"].split()[2])
unknowns.reverse()
for un in unknowns:
    if type(monkeys[un]) == str:
        name1, operator, name2 = monkeys[un].split()
    else:
        print(result)
        break
    if name1 in unknowns:
        if operator == "/":
            result *= calculate(name2)
        if operator == "-":
            result += calculate(name2)
        if operator == "+":
            result -= calculate(name2)
        if operator == "*":
            result //= calculate(name2)
    if name2 in unknowns:
        if operator == "/":
            result = calculate(name1) / result
        if operator == "-":
            result = calculate(name1) - result
        if operator == "+":
            result -= calculate(name1)
        if operator == "*":
            result //= calculate(name1)
