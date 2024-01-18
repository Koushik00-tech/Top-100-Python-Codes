# We need to get max or largest number in an array----------
#---------------------Basic Iteration using for loop-----------
# n = [10,20,5,4,6]
# max = n[0]
# for i in n:
#     if i > max:
#         max = i
# print(max)
# TC -- O(log n) running the loop for each value of n 
# Sc - O(1) max is taken extra space to store the max value
# ---------------------Inbuilt Method-----------------------------
# user_array = list(map(int, input().split()))
# print(max(user_array)) # Inbuilt max method
#----------------------While Loop-------------------------------
arr = list(map(int, input().split()))
index = 0
max_el = arr[0]
length = len(arr)
while index < length:
    if index > max_el:
        max_el = index

print(max_el)

