#helper functions
def isIncreasingSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
        
def isDecreasingSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False
    return True

def isSafeCountwise(arr):
    for x in range(len(arr) - 1):
        diff = abs(arr[x] - arr[x + 1])
        if diff > 3 or diff < 1:
            return False
    return True

#open file and make each line its own list of integers
file_path = "C:\\Users\\jbwom\\Downloads\\PersonalProjects\\Advent_of_Code\\Year2024\\Day_2\\input.txt"
with open(file_path, "r") as file:
    arrays = []
    for line in file:
        numbers = list(map(int, line.split()))
        arrays.append(numbers)


#Logic for solution
safeCount = 0 
unsafeCount = 0
for array in arrays:
    if isDecreasingSorted(array) or isIncreasingSorted(array): 
        if isSafeCountwise(array):
            safeCount += 1
        else:
            unsafeCount += 1
    else: 
        unsafeCount += 1


print("The number of safe reports is ")
print(safeCount)
print("The number of unsafe reports is")
print(unsafeCount)