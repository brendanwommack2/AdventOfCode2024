file_location = "C:\\Users\\jbwom\\Downloads\\PersonalProjects\\Advent_of_Code\\Year2024\\AdventOfCode2024\\Day_6\\input.txt"

#create the iterable map of the lab using the provided file. 
labMap = []

with open(file_location, "r") as input_file:
    for line in input_file:
        # Strip trailing whitespace and convert the line into a list of characters
        row = list(line.strip())
        labMap.append(row)

# movements
directions = {
    '^': (-1, 0),  # Up
    '>': (0, 1),   # Right
    'v': (1, 0),   # Down
    '<': (0, -1)   # Left
}

# rotation logic
next_direction = {
    '^':'>',
    '>':'v',
    'v':'<',
    '<':'^'
}

# Find the starting position and direction
for i, row in enumerate(labMap):
    for j, cell in enumerate(row):
        if cell in directions:
            guard_pos = (i, j)
            guard_dir = cell
            break

# Set of visited positions
visited_positions = set()
visited_positions.add(guard_pos)

# Simulate guard's movement
rows, cols = len(labMap), len(labMap[0])

while True:
    # Determine next position
    di, dj = directions[guard_dir]
    next_pos = (guard_pos[0] + di, guard_pos[1] + dj)
    
    # Check if the next position is outside the map
    if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
        break  # Guard leaves the mapped area

    # Check if the next position is an obstacle
    if labMap[next_pos[0]][next_pos[1]] == '#':
        # Turn 90° right
        guard_dir = next_direction[guard_dir]
    else:
        # Move forward
        guard_pos = next_pos
        visited_positions.add(guard_pos)
        # Mark the path (optional, for visualization)
        labMap[guard_pos[0]][guard_pos[1]] = 'X'


# Output the number of distinct positions visited
print(f"Distinct positions visited: {len(visited_positions)}")