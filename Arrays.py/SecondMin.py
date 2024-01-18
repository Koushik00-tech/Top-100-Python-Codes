# To find Second min from an array
# ---------------------------Using iteratio(Brute force) approach straight forward--------------
arr = [10,5,7,5,6] # expected 6 as output 
arr = list(map(int, input("Enter the Values of Array: ").split())) 
first_min = min(arr[0], arr[1])
second_min = max(arr[0], arr[1])
for num in arr:
    if num < first_min:
        second_min = first_min
        first_min = num
    elif num < second_min and num != first_min:
        second_min = num
print(second_min)
# Tc - O(n) the loop is iterating for n values of array 
# SC - O(n) coz list created to store the input values
# -------------------Using While loop-------------------
arr = list(map(int, input("Enter the Values of Array: ").split())) 
num = 2 # Coz we have already assumed index 0 and 1 values 
first_min = min(arr[0], arr[1])
second_min = max(arr[0], arr[1])
L = len(arr) 
while num < L:
    if arr[num] < first_min:
        second_min = first_min
        first_min = arr[num]
    elif arr[num] < second_min and arr[num] != first_min:
        second_min = arr[num] # Coz we took array length as the itertions no the entire array
    num += 1
print(second_min)

