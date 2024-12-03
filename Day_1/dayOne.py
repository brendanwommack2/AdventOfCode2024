#Bubble Sort Function for sorting the lists later
def bubbleSort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

    return 0

#Open file and put the two lists in separate arrays
file_path = "C:\\Users\\jbwom\\Downloads\\PersonalProjects\\Advent_of_Code\\Year2024\\Day_1\\data.txt"

left_list = []
right_list = []

with open(file_path, "r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)


#sort the lists
bubbleSort(left_list)
bubbleSort(right_list)


#sum the differences between the sorted list elements
sum = 0
i = 0


while i < len(left_list):
    if left_list[i] > right_list[i]:
        sum += (left_list[i] - right_list[i])
    if left_list[i] < right_list[i]:
        sum += (right_list[i] - left_list[i])
    if left_list[i] == right_list[i]:
        sum += 0

    i += 1



print(left_list)
print(right_list)
print("The final sum is ")

print(sum)