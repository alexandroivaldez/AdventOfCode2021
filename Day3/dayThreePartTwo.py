#Advent of Code - Day Three Part One
arr = []
gammaRate = []
epsilonRate = []

#Store input in list
with open("test.txt") as file:
    for line in file:
      instruction = line.rstrip()
      arr.append(instruction)

#Iterate through each index
for counter in range(5):
  oneCount = 0
  zeroCount = 0
  #Iterate through each number in code
  for instruction in arr:
    code = list(instruction)
    if code[counter] == '1':
      oneCount += 1
    else:
      zeroCount += 1
  #Append either 0 or 1 to gammaRate
  if oneCount > zeroCount:
    gammaRate.append(str(1))
    epsilonRate.append(str(0))
  else:
    gammaRate.append(str(0))
    epsilonRate.append(str(1))

#print(gammaRate)
#print(epsilonRate)

#Turn list into binary code
gammaRate = list("".join(gammaRate))
epsilonRate = list("".join(epsilonRate))

#Convert binary code to int
def binaryConverter(arr):
  value = 0
  for i in range(len(arr)):
    digit = arr.pop()
    if digit == '1':
      value = value + pow(2, i)
  return value

#print(binaryConverter(gammaRate) * binaryConverter(epsilonRate))

#Recursive iteration through the loop filtering for '1'. Still missing the if statement that's checking which value is  greater & going from there.

globalCounter = 0

def recursiveLoop(arr):
  print(arr)
  if len(arr) == 1:
    return 1
  else:
    global globalCounter
    newArr = []
    for instruction in arr:
      code = list(instruction)
      #print("".join(code))
      if code[globalCounter] == '1':
        newArr.append(instruction)
    globalCounter += 1
    return recursiveLoop(newArr)
    
        
recursiveLoop(arr)