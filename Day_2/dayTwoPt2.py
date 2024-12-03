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

def removeEachElement(lst):
    return [lst[:i] + lst[i+1:] for i in range(len(lst))]

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
    x = removeEachElement(array)
    #x is a list of lists with one element removed from each
    localCount = 0
    for i in x:
        if isDecreasingSorted(i) or isIncreasingSorted(i): 
            if isSafeCountwise(i):
                localCount += 1
            else:
                localCount += 0
        else: 
            localCount += 0

    if localCount > 0:
        safeCount += 1
    else:   
        unsafeCount += 1

print("Now considering the problem dampener...")
print("The number of safe reports is ")
print(safeCount)
print("The number of unsafe reports is")
print(unsafeCount)