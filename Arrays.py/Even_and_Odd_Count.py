# Count of even and odd numbers in an array by taking input from the user
arr = list(map(int, input().split())) # this will take str as input from the user and convert str to int and split
even_count = 0
odd_count = 0
for element in arr:
    if element % 2 == 0:
        even_count += 1 
    else:
        odd_count += 1
print(even_count)
print(odd_count)
# TC - O(n) loop will iterate till n values
# SC - O(1) increase the count values by with even and odd_count taken 
# -------------------- Print Even elements and odd elements in an array
arr = list(map(int, input().split())) # this will take str as input from the user and convert str to int and split
even_elements = [] # Taking new var to store even elements 
odd_elements = []
for element in arr:
    if element % 2 == 0:
        even_elements.append(element)
    else:
        odd_elements.append(element)
print(*even_elements)
print(*odd_elements)
# TC - O(n + n) where n is the length of the array and another n is to check even values and odd values by iterating to n values
# Sc - O(n) where even and odd arrays are taking constant space
 
