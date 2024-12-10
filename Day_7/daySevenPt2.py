from itertools import product
from operator import add, mul
from functools import reduce

# Helpers
def concat(a, b):
    return int(str(a) + str(b))

def process_ops(nums, ops):
    return reduce(lambda x, y: y[0](x, y[1]), zip(ops, nums[1:]), nums[0])

def process_line(line):
    target, *inputs = map(int, line.replace(':', '').split())
    ops = [add, mul, concat]
    if any(process_ops(inputs, op_combo) == target for op_combo in product(ops, repeat=len(inputs) - 1)):
        return target
    return 0

# Read input from file
file_location = "C:\\Users\\jbwom\\Downloads\\PersonalProjects\\Advent_of_Code\\Year2024\\AdventOfCode2024\\Day_7\\input.txt"

with open(file_location, 'r') as file:
    data = file.readlines()

# Process each line and calculate the total calibration result
results = [process_line(line.strip()) for line in data]
total_calibration_result = sum(results)

print(f"The total calibration result is: {total_calibration_result}")