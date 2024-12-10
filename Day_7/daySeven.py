from itertools import product
from operator import add, mul

def process_ops(nums, ops):
    if len(nums) == 1:
        return nums[0]
    l, r, *rest = nums
    cur_op, *remaining_ops = ops
    return process_ops([cur_op(l, r)] + rest, remaining_ops)

def process_line(line):
    target, *inputs = map(int, line.replace(':', '').split())
    ops = [add, mul]
    if any(process_ops(inputs, op_combo) == target for op_combo in product(ops, repeat=len(inputs) - 1)):
        return target
    return 0

# Read input from file
input_file = r"C:\Users\jbwom\Downloads\PersonalProjects\Advent_of_Code\Year2024\AdventOfCode2024\Day_7\input.txt"
with open(input_file, 'r') as file:
    data = file.readlines()

# Process each line and calculate the total calibration result
results = [process_line(line.strip()) for line in data]
total_calibration_result = sum(results)

print(f"The total calibration result is: {total_calibration_result}")