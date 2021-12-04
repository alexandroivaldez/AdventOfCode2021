#Advent of Code - D1P1

depthMeasurements = []
increases = -1
prevDepth = 0

with open("puzzleInput.txt") as file:
    for line in file:
        depth = int(line.rstrip())

        if depth > prevDepth:
          increases = increases + 1
          
        depthMeasurements.append(depth)

        prevDepth = depth

print("Total increases: " + str(increases))