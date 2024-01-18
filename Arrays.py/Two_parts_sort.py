# Sort 1st part of the array in ascending and second part in Descending order
#---------------------------Using in built sort method----------
arr = [10,8,4,5,3] # expected output 8,10,4,5,3
half = len(arr) // 2
first_half = arr[:half]
second_half = arr[half:]
first_half[:-1].sort() # # Sort the first half (excluding the middle element) in ascending order
second_half[:-1].sort(reverse=True) # Descending order
print(first_half + second_half)
# Tc - O(n log n) coz sorting two half of array by visiting every element inside the array
# Therefore, the overall time complexity is O(n log n) due to the sorting operations dominating the time complexity.
# Sc - O(n)  due to the space required for the two halves.
# ----------------------------
