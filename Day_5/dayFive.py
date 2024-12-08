file_path = r"C:\Users\jbwom\Downloads\PersonalProjects\Advent_of_Code\Year2024\AdventOfCode2024\Day_5\input.txt"

with open(file_path, "r") as file:
    data = file.read()


def parse_rules_and_updates(data):
    # Split input into rules and updates
    rules_section, updates_section = data.strip().split("\n\n")
    
    # Parse rules
    rules = {}
    for line in rules_section.splitlines():
        x, y = map(int, line.split('|'))
        if x not in rules:
            rules[x] = []
        rules[x].append(y)
    
    # Parse updates
    updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]
      
    return rules, updates

def is_update_valid(update, rules):
    # Check if the update satisfies the rules
    index_map = {page: idx for idx, page in enumerate(update)}
    for x in rules:
        for y in rules[x]:
            # If both pages are in the update, check their order
            if x in index_map and y in index_map and index_map[x] >= index_map[y]:
                return False
    return True

def find_middle_number(update):
    # Return the middle number of the update
    n = len(update)
    return update[n // 2]

def solve_puzzle(data):
    # Parse input data
    rules, updates = parse_rules_and_updates(data)
    
    # Process updates
    middle_numbers_sum = 0
    for update in updates:
        if is_update_valid(update, rules):
            middle_numbers_sum += find_middle_number(update)
    
    return middle_numbers_sum

result = solve_puzzle(data)

print(f"The sum of middle page numbers from correctly-ordered updates is: {result}")