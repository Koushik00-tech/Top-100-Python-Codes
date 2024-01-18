# To check the frequency of element inside an array
# ------------------------Using Basic Iteration-----------

# arr = [1,2,4,5,2,7,8,2]
# element_to_count = 2
# freq = 0
# for element in arr: # Loop variable
#     if element == element_to_count:
#         freq += 1
# print("Frequecy of", element_to_count, "is:", freq)

# Tc = O(n) Loop is iterating till n values of array where n is the length of the array
# The space complexity is O(1) because the algorithm uses a constant amount of additional space, 
# regardless of the input size. The only variables used are element_to_count, frequency, and the loop variable element.
#------------------------Using while loop----------
arr = [1,2,4,5,2,7,8,2]
element_to_count = 2
freq = 0
index = 0 # Index taken to stop the while loop after reaching last index
L = len(arr)
while index < L:
    if arr[index] == element_to_count:
        freq += 1
    index += 1
print(freq)