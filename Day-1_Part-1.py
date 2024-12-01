# Advent of code 2024 day 1 part 1

ColA = []
ColB = []

# Read the file and split the numbers into two arrays
with open('D:\Assorted_Scripts\AdventOfCode2024\Day1\RawInput.txt', 'r') as file:
    for line in file:
        # Split the line on whitespace and convert to integers
        num1, num2 = map(int, line.split())
        ColA.append(num1)
        ColB.append(num2)

ColA.sort()
ColB.sort()

# Create a new array to store the differences
Differences = [abs(a - b) for a, b in zip(ColA, ColB)]

print(sum(Differences))