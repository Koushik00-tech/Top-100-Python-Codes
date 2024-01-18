# Reverse array 
#----------------------Using Swap---------
# Access elements from start index and End Index and Swap them
arr = [1,2,3,4,5]
start = 0
end = len(arr) - 1
while start < end:
    arr[start] ,arr[end] = arr[end],arr[start] 
    start += 1 # Increaing the start value by one 
    end -= 1  # Decreasing the end index by one

print(arr)
# TC - O(n) while loop is itertng to n values of input 
# Since every element is visited once, the time complexity is linear with respect to the number of elements in the array.
# SC - O(1) start and end are taken extra space to store constant values
# -----------------------------Using Recursion-----------------------
# A funtion calling it self untill a specified conditon(Base condition) is met
def reverse_arr_using_recursion(A,start,end):
    if start <= end: # base condtion where the recursion will stop calling again
        return  
    A[start], A[end] = A[end], A[start]
    reverse_arr_using_recursion(A, start+1, end+1)

A = [1,2,3,4,5]
reverse_arr_using_recursion(A,0,4) # We need to mention the values of Start and End inside the arguments of Function
print(A)

