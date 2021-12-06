#Advent of Code - Day Two Part Two

arr = []
depth = 0
horPos = 0
aim = 0

#Store input in list
with open("puzzleInput.txt") as file:
    for line in file:
      instruction = line.rstrip()
      arr.append(instruction)

for instruction in arr:
  steps = instruction.split(" ")
  #steps[0] --> keyword
  #steps[1] --> number
  if(steps[0] == "forward"):
    horPos += int(steps[1])
    depth += aim * int(steps[1])
  elif (steps[0] == "down"):
    #depth += int(steps[1])
    aim += int(steps[1])
  else:
    #depth -= int(steps[1])
    aim -= int(steps[1])

print(horPos * depth)