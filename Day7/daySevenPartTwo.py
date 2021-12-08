#Advent of Code - Day Three Part One
import random #import random for aesthetic fun...

#Store input in list
with open("puzzleInput.txt") as file:
    for line in file:
      instruction = line.rstrip()
      nums = str(instruction).split(",")

"""
I originally attempted to create a recrusive function that would add the numbers from n to 0, however something like this causes a "maximum recursion depth exceeded" error, so I scrapped it.

crabs = 0

def crabCrusher(num):
  global crabs
  if num == 1:
    return crabs + 1
  else:
    crabs += num
    return crabCrusher(num - 1)

"""

#factorial but for summation... sumtorial
def sumtorial(num):
  return int(((num**2) + num) / 2)

#Iterate through input list & calculate the 
fuelArr = []
sum = 0
arrLength = (len(nums) + 1)

for counter in range(1, arrLength):
  for index in nums:
    diff = abs(int(index) - counter)
    diff = sumtorial(diff)
    sum += diff
    print("Loading" + "." * random.randint(1,4))
  fuelArr.append(sum)
  sum = 0

#Arbitrarily large number for comparison
minNum = 1000000000000000

#Iterate through fuelArr to find the lowest amount
for num in fuelArr:
  if num < minNum:
    minNum = num
print("Crabs aligned. Best fuel consumption: " + str(minNum))