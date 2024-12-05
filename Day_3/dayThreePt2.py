#regular expressions
import re

#open file and turn the text into one large string
file_path = "C:\\Users\\jbwom\\Downloads\\PersonalProjects\\Advent_of_Code\\Year2024\\AdventOfCode2024\\Day_3\\input.txt"
with open(file_path, "r") as file:
    text = file.read()

#re expression and find matches
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

mul_enabled = True
total_sum = 0

# Find all matches for mul, do, and don't instructions
instructions = re.finditer(rf"{mul_pattern}|{do_pattern}|{dont_pattern}", text)

# Process instructions in order
for match in instructions:
    if match.group(1) and match.group(2):  # This is a mul(X, Y) instruction
        if mul_enabled:
            x, y = int(match.group(1)), int(match.group(2))
            total_sum += x * y
    elif match.group(0) == "do()":
        mul_enabled = True
    elif match.group(0) == "don't()":
        mul_enabled = False

print(total_sum)