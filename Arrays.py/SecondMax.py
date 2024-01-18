# To find Second max element from the array we need to take 
# First max as max(arr[0], arr[1])
# Second max as min(arr[0], arr[1])
arr = [30,20,40,60,70] # Expected 60 as output
first_max = max(arr[0], arr[1])
second_max = min(arr[0],arr[1])
for num in arr:
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max and num != first_max:
        second_max = num
print(second_max)
