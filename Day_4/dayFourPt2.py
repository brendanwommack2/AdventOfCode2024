#Helper
def count_x_mas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    xmas_count = 0

    #check all possible 3x3 sub-grids
    for r in range(1, rows - 1):  # Avoid edges
        for c in range(1, cols - 1):  # Avoid edges
            #Check if the center is 'A'
            if grid[r][c] != 'A':
                continue
            
            #Check diagonals
            top_left = grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1]
            bottom_left = grid[r + 1][c - 1] + grid[r][c] + grid[r - 1][c + 1]

            #Check if both diagonals match "MAS" or "SAM"
            if (top_left == "MAS" or top_left == "SAM") and (bottom_left == "MAS" or bottom_left == "SAM"):
                xmas_count += 1

    return xmas_count


#Parse the input file into a 2D grid
file_location = "C:\\Users\\jbwom\\Downloads\\PersonalProjects\\Advent_of_Code\\Year2024\\AdventOfCode2024\\Day_4\\input.txt"

with open(file_location, "r") as file:
    grid = [list(line.strip()) for line in file]

#Count X-MAS patterns in the grid
xmas_count = count_x_mas_patterns(grid)

print(f"The number of X-MAS patterns is: {xmas_count}")