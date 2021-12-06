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

#Iterate through each index
#Iterate through each number in code
arr2 = []
for instruction in arr:
  code = list(instruction)
  #print("".join(code))
  if code[0] == '1':
    arr2.append(instruction)


arr3 = []
for instruction in arr:
  code = list(instruction)
  #print("".join(code))
  if code[1] == '1':
    arr3.append(instruction)

print(arr3)

#Obviously going to need to use recursion. I'll get to this later.