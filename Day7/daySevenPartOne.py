#Advent of Code - Day Seven Part One
import random #import random for aesthetic fun...

#Store input in list
with open("puzzleInput.txt") as file:
    for line in file:
      instruction = line.rstrip()
      nums = str(instruction).split(",")

#iterate through input list & calculate the 
fuelArr = []
sum = 0
arrLength = (len(nums) + 1)

for counter in range(1, arrLength):
  for index in  nums:
    diff = abs(int(index) - counter)
    sum += diff
    print("🦀" * random.randint(1,4))
  fuelArr.append(sum)
  sum = 0

#Arbitrarily large number for comparison
minNum = 1000000000000000

#Iterate through fuelArr to find the lowest amount
for num in fuelArr:
  if num < minNum:
    minNum = num
print("Crabs aligned. Best fuel consumption: " + str(minNum))