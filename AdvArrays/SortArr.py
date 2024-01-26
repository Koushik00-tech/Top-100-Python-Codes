# Sort the array of 0,1,2 values without using any alogrithm
# array = [1, 2, 0, 2, 1, 0, 2, 1, 0, 2, 0, 1]
# Count_of_0 = 3
# Count_of_1 = 3
# Count_of_2 = 3
# Expected output : [0,0,0,1,1,1,2,2,2]
arr = [1, 2, 0, 2, 1, 0, 2, 1, 0, 2, 0, 1]
Count_of_0 = arr.count(0)
Count_of_1 = arr.count(1)
Count_of_2 = arr.count(2)
new_arr = [] # To store values of sorted list
for i in range(Count_of_0):  # i value is index of the array
    new_arr.append(0)
for i in range(Count_of_1):
    new_arr.append(1)
for i in range(Count_of_2):
    new_arr.append(2)
print(new_arr)
# sorting of the values directly appended as per the taken count values of the specific element in the array

