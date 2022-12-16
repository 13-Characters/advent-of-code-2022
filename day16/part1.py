import re
import itertools
input = open("example_input.txt").readlines()
class Valve():
    def __init__(self, name, flowRate, adjacents):
        self.name = name
        self.flowRate = flowRate
        self.adjacents = adjacents
    def getDistance(self, valve): #Helper function to determine the distance to other valve
        if valve == self:
            return 0
        stop = False
        i = 0
        while not stop:
            vDistance = [(self, 0)]
            for v in vDistance:
                for adj in v[0].adjacents:
                    if adj == valve:
                        return v[1] + 1
                    if adj not in [x[0] for x in vDistance]:
                        vDistance.append((adj, v[1] + 1))

# Parse the input
valves = []
for line in input:
    names = re.findall('[A-Z][A-Z]', line)
    name = names[0]
    flowRate = int(re.search('\d+', line)[0])
    valves.append(Valve(name, flowRate, []))

for i, line in enumerate(input):
    names = re.findall('[A-Z][A-Z]', line)
    adjacents = []
    for name in names[1:]:
        for v in valves:
            if v.name == name:
                adj = v
        adjacents.append(adj)
    valves[i].adjacents = adjacents

for v in valves:
    if v.name == 'AA':
        currentValve = v
stop = False
openOrder = []
for v in valves:
    if v.flowRate > 0:
        openOrder.append(v)
openOrder.insert(0, currentValve)
openOrder.sort(key=lambda x: currentValve.getDistance(x)) # First guess, we will refine this later
maxPressure = 0
time = 0
totalPressure = 0
for i in range(1, len(openOrder)):
    valve = openOrder[i]
    previousValve = openOrder[i - 1]
    pressureReleased = valve.flowRate * (30 - time - (previousValve.getDistance(valve) + 1))
    totalPressure += pressureReleased
    print(f"Minute {time + 1}: Move from {previousValve.name} -> {valve.name}, "
            f"{pressureReleased} released after opening {valve.name}")
    time += previousValve.getDistance(valve) + 1
print(str(totalPressure))
