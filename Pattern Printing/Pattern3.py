# Triangle Pattern
#    *
#   ***
#  *****
# *******
n = 4 # no of rows
for i in range(n): # Row 
    for j in range(n-i-1): # Column
        print(" ", end=" ")
    for j in range(i*2+1):
        print("*", end=" ")
    print()
