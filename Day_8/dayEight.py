from collections import defaultdict

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def find_antennas(grid):
    antennas = defaultdict(list)
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != '.':
                antennas[char].append((y, x))
    return antennas

def calculate_antinodes(antennas, grid_height, grid_width):
    antinodes = set()
    for coords in antennas.values():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                diff = tuple(a - b for a, b in zip(coords[j], coords[i]))
                
                for _idx, _dir in [(i, -1), (j, 1)]:
                    pos = tuple([a + b * _dir for a, b in zip(coords[_idx], diff)])
                    if 0 <= pos[0] < grid_height and 0 <= pos[1] < grid_width:
                        antinodes.add(pos)
    
    return antinodes

def solve_puzzle(input_file):
    grid = read_input(input_file)
    antennas = find_antennas(grid)
    antinodes = calculate_antinodes(antennas, len(grid), len(grid[0]))
    return len(antinodes)

# Solve the puzzle
input_file = r"C:\Users\jbwom\Downloads\PersonalProjects\Advent_of_Code\Year2024\AdventOfCode2024\Day_8\input.txt"
result = solve_puzzle(input_file)
print(f"The number of unique antinode locations is: {result}")
