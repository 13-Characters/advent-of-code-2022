import re
input = open("example_input.txt").readlines()
class Valve():
    def __init__(self, name, flowRate, adjacents):
        self.name = name
        self.flowRate = flowRate
        self.adjacents = adjacents

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
time = 0
totalPressure = 0
opened = []
while not stop:
    opened.append(currentValve)
    valvesByDistance = [currentValve]
    distances = [0] # Parallel lists may be a bad idea
    pressures = []
    i = 0
    while i < len(valves):
        for adj in valvesByDistance[i].adjacents:
            if adj not in valvesByDistance:
                valvesByDistance.append(adj)
                distances.append(distances[i] + 1) # Append the distance from currentValve
        i += 1
    for j, valve in enumerate(valvesByDistance):
        if valve not in opened:
            pressureReleased = valve.flowRate * (30 - time - (distances[j] + 1))
            pressures.append(pressureReleased)
        else:
            pressures.append(0)

    if max(pressures) == 0:
        for valve in opened:
            totalPressure += valve.flowRate * (30 - time)
            time = 29
            stop = True
        if stop == True: break
    for p in range(len(pressures)):
        if pressures[p] != 0:
            nearest = distances[p]
            break
    indexOfNextValve = 0
    for p in range(len(pressures)):
        if distances[p] > nearest:
            break
        if pressures[p] > pressures[indexOfNextValve]:
            indexOfNextValve = p
    print(f"Minute {time + 1}: Move from {currentValve.name} -> {valvesByDistance[indexOfNextValve].name}, "
          f"{pressures[indexOfNextValve]} released after opening {valvesByDistance[indexOfNextValve].name}")
    totalPressure += pressures[indexOfNextValve]
    time += (distances[indexOfNextValve] + 1)
    currentValve = valvesByDistance[indexOfNextValve]

print(totalPressure)
