import re
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
input = open("input.txt").readlines()
monkeys = {}
for line in input:
    name, expression = line.split(": ")
    expression = expression.replace("\n", "")
    if re.match("\d+", expression):
        expression = int(expression)
    monkeys[name] = expression

print(calculate("root"))
