#Advent of Code - Day Three Part One
arr = []
gammaRate = []
epsilonRate = []

#Store input in list
with open("puzzleInput.txt") as file:
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
  #print(arr)
  newNewArr = arr
  if len(arr) == 1:
    return newNewArr
  else:
    global globalCounter
    newArr = []
    zeroCount = 0
    oneCount = 0
    masterKey = 0
    for instruction in arr:
      code = list(instruction)
      if code[globalCounter] == '1':
        oneCount += 1
      else:
        zeroCount += 1
    
    if oneCount >= zeroCount:
      #print("Ones win!")
      masterKey = 1
    else:
      #print("Zero wins!")
      masterKey = 0

    for instruction in arr:
      code = list(instruction)
      if int(code[globalCounter]) == masterKey:
        newArr.append(instruction)

    globalCounter += 1
    #print(newArr)
    return recursiveLoop(newArr)
    #return print(str(oneCount) + " " + str(zeroCount))


x = recursiveLoop(arr)
oxygenRating = str(binaryConverter(list(x[0])))
#print("The oxygen rating is: " + oxygenRating)

co2Rating = 0
globalCounter2 = 0

def recursiveLoop2(arr):
  #print(arr)
  newNewArr = arr
  if len(arr) == 1:
    return newNewArr
  else:
    global globalCounter2
    newArr = []
    zeroCount = 0
    oneCount = 0
    masterKey = 0
    for instruction in arr:
      code = list(instruction)
      if code[globalCounter2] == '1':
        oneCount += 1
      else:
        zeroCount += 1
    
    if zeroCount <= oneCount:
      #print("Zero win!")
      masterKey = 0
    else:
      #print("One wins!")
      masterKey = 1

    for instruction in arr:
      code = list(instruction)
      if int(code[globalCounter2]) == masterKey:
        newArr.append(instruction)

    globalCounter2 += 1
    #print(newArr)
    return recursiveLoop2(newArr)
    #return print(str(oneCount) + " " + str(zeroCount))

y = recursiveLoop2(arr)
co2Rating = str(binaryConverter(list(y[0])))
#print("The oxygen rating is: " + co2Rating)

lifeSupportRating = int(oxygenRating) * int(co2Rating)
print("The life support rating is: " + str(lifeSupportRating))
