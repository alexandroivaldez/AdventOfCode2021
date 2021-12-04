#Advent of Code - D1P2

depthMeasurements = []
sumMeasurements = []
increases = -1
prevDepth = 0
windowPosition = 0

with open("puzzleInput.txt") as file:
    #---- Part One ----
    for line in file:
        depth = int(line.rstrip())
        if depth > prevDepth:
          increases = increases + 1 
        depthMeasurements.append(depth)
        prevDepth = depth
    print("Total increases: " + str(increases))

    #-------------------
    #Iterate through depthMeasurments list
    #print(depthMeasurements)
    for counter in depthMeasurements:
      while(windowPosition + 1 != (len(depthMeasurements) - 1)):
        sum = 0
        for windowOpening in range(windowPosition, windowPosition + 3):
          sum += depthMeasurements[windowOpening]
        #print(sum)
        sumMeasurements.append(sum)
        #print("----")
        windowPosition += 1

print(sumMeasurements)

increases2 = -1
prevNum = 0
for num in sumMeasurements:
  if prevNum < num:
    increases2 += 1
  prevNum = num

print(increases2)

      

     
      





