from collections import defaultdict, deque

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

def reorder_update(update, rules):
    pass

def reorder_update(update, rules):
    # Build the graph and in-degree count for topological sorting
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Initialize graph and in-degrees for nodes in the update
    for page in update:
        in_degree[page] = 0
    
    # Populate the graph and in-degrees using the rules
    for x, ys in rules.items():
        for y in ys:
            if x in update and y in update:  # Only consider rules for pages in the update
                graph[x].append(y)
                in_degree[y] += 1
    
    # Perform topological sort using Kahn's algorithm
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []
    
    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If the sorted update doesn't cover all pages, it's invalid
    if len(sorted_update) != len(update):
        raise ValueError("Cycle detected in rules; the update cannot be reordered!")
    
    # Reorder the original update list in-place
    update[:] = sorted_update


def solve_puzzle(data):
    # Parse input data
    rules, updates = parse_rules_and_updates(data)
    
    # Process updates
    middle_numbers_sum = 0
    for update in updates:
        if is_update_valid(update, rules) == False:
            
            reorder_update(update, rules)

            middle_numbers_sum += find_middle_number(update)
    
    return middle_numbers_sum

result = solve_puzzle(data)

print(f"The sum of middle page numbers from correctly-ordered updates is: {result}") 