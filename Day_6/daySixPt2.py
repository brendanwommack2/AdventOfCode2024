file_location = "C:\\Users\\jbwom\\Downloads\\PersonalProjects\\Advent_of_Code\\Year2024\\AdventOfCode2024\\Day_6\\input.txt"

# Create the map of the lab
labMap = []
with open(file_location, "r") as input_file:
    for line in input_file:
        labMap.append(list(line.strip()))

# Directions for movement: Up, Right, Down, Left
directions = {
    '^': (-1, 0),  # Up
    '>': (0, 1),   # Right
    'v': (1, 0),   # Down
    '<': (0, -1)   # Left
}

# Rotation logic
next_direction = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

# Find the starting position and direction
for i, row in enumerate(labMap):
    for j, cell in enumerate(row):
        if cell in directions:
            start_pos = (i, j)
            start_dir = cell
            break

# Function to simulate guard movement
def simulate_guard(labMap, start_pos, start_dir):
    rows, cols = len(labMap), len(labMap[0])
    visited_states = set()
    guard_pos = start_pos
    guard_dir = start_dir

    while True:
        # Save the current state (position and direction)
        state = (guard_pos, guard_dir)
        if state in visited_states:
            return True  # Loop detected
        visited_states.add(state)

        # Determine next position
        di, dj = directions[guard_dir]
        next_pos = (guard_pos[0] + di, guard_pos[1] + dj)

        # Check if the next position is outside the map
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            return False  # Guard leaves the map

        # Check if the next position is an obstacle
        if labMap[next_pos[0]][next_pos[1]] == '#':
            # Turn 90° right
            guard_dir = next_direction[guard_dir]
        else:
            # Move forward
            guard_pos = next_pos

# Count valid positions for new obstruction
valid_positions = 0
rows, cols = len(labMap), len(labMap[0])

for i in range(rows):
    for j in range(cols):
        # Skip existing obstacles and the guard's starting position
        if labMap[i][j] == '#' or (i, j) == start_pos:
            continue

        # Place the obstruction temporarily
        labMap[i][j] = '#'

        # Check if it causes a loop
        if simulate_guard(labMap, start_pos, start_dir):
            valid_positions += 1

        # Remove the obstruction
        labMap[i][j] = '.'

print(f"Number of valid positions for the obstruction: {valid_positions}")
