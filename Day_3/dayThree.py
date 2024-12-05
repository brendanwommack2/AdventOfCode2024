#regular expressions
import re

#open file and turn the text into one large string
file_path = "C:\\Users\\jbwom\\Downloads\\PersonalProjects\\Advent_of_Code\\Year2024\\AdventOfCode2024\\Day_3\\input.txt"
with open(file_path, "r") as file:
    text = file.read()

#re expression and find matches
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, text)

#find the sum of the pairs
total_sum = sum(int(x) * int(y) for x, y in matches)

print(total_sum)