#Helper Function
def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),    #Right
        (0, -1),   #Left
        (1, 0),    #Down
        (-1, 0),   #Up
        (1, 1),    #Down-right
        (1, -1),   #Down-left
        (-1, 1),   #Up-right
        (-1, -1)   #Up-left
    ]
    
    def is_valid_position(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def search_from_position(r, c, direction):
        dr, dc = direction
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if not is_valid_position(nr, nc) or grid[nr][nc] != word[i]:
                return False
        return True

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:  #Start search if the first letter matches
                for direction in directions:
                    if search_from_position(r, c, direction):
                        count += 1

    return count


#Parse the input file into a 2D grid
file_location = "C:\\Users\\jbwom\\Downloads\\PersonalProjects\\Advent_of_Code\\Year2024\\AdventOfCode2024\\Day_4\\input.txt"

with open(file_location, "r") as file:
    grid = [list(line.strip()) for line in file]

#Search for occurrences of "XMAS"
word_to_find = "XMAS"
occurrences = count_word_occurrences(grid, word_to_find)

print(f"The word '{word_to_find}' appears {occurrences} times in the grid.")

