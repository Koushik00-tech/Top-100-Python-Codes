# Hollow pattern
# * * * * 
# *     *
# *     *
# * * * *
# To print the above pattern we'll use nested loop
# Outer loop for Rows and Inner loop for Columns
n = 4
for i in range(1,n+1):
    for j in range(1, n+1):
        if (i==1) | (i==n) | (j==1) | (j==n): # Simple Logic 
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
# TC --> O(n^2) coz we are using nested for loop nested -- For each iteration of outer for loop inner for is printed n times
# SC = O(1) no extra space is taken

