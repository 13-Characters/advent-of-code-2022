import re
import itertools
from collections import deque
import time as tim
input = open("input.txt").readlines()
start_time = tim.time_ns()
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
end_parse_time = tim.time_ns()
for v in valves:
    if v.name == 'AA':
        currentValve = v
openableValves = {v for v in valves if v.flowRate > 0}



def calcPressure(path, startingValve, time=0, pressure=0):
    # Starting conditions
    time = time
    totalPressure = int(pressure)
    path = [startingValve] + list(path)

    for i in range(1, len(path)):
        valve = path[i]
        previousValve = path[i - 1]
        pressureReleased = valve.flowRate * (30 - time - (previousValve.getDistance(valve) + 1))
        time += previousValve.getDistance(valve) + 1
        if time > 30: break
        totalPressure += pressureReleased
    return valve, time, totalPressure

def findBestPath(path, currentValve, startingTime=0):
    maxPressure = 0
    averagePressure = 0
    if len(path) < 2: iterate = enumerate(itertools.permutations(path))
    else: iterate = enumerate(itertools.permutations(path, 2))
    for count, segment in iterate:
        startingTime = startingTime
        valve, time, partialPressure = calcPressure(segment, currentValve, time=startingTime)
        averagePressure = (averagePressure * count + partialPressure) / (count + 1)
        if partialPressure > averagePressure:
            remaining = path - set(segment)
            if remaining and time < 30:
                totalPressure = partialPressure + findBestPath(remaining, valve, startingTime=time)
            else:
                totalPressure = partialPressure
            if totalPressure > maxPressure:
                maxPressure = totalPressure
        if startingTime == 0 and count % 10 == 0:
            print(count, f"{(tim.time_ns() - start_time) / 1000000000} s")
    return int(maxPressure)

print(findBestPath(openableValves, currentValve))
end_time = tim.time_ns()
print(f"Parsing time: {(end_parse_time - start_time) / 1000000000} seconds\n"
      f"Check path time: {(end_time - start_time) / 1000000000} seconds")
