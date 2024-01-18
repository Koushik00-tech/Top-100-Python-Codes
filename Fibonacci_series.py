# Fibonacci Series is the Unq sequence of numbers where --  a Number is sum of two previous numbers in the Sequence
# ------------------------Iteration method-------
num = int(input())
n1, n2 = 0,1 # 1st we need to take 1st two numbers in the sequence as 0 and 1 to start the sequence
# Initializing 1st two numbers Outside the Loop
print("Fibonacci Seies", n1,n2, end =" ")
for i in range(2, num):
    fibb = n1 + n2 # we'll take Fibb as a varibale to store 
    n1 = n2
    n2 = fibb
    print(fibb, end = " ")

print()
#Tc -- O(n) -- we are repeating the loop n times
#SC -- O(1) -- N1 and n2, fibb as extra space to store constant values

# -----------------------While Loop-----------------
num = int(input())
n1, n2 = 0,1 # 1st we need to take 1st two numbers in the sequence as 0 and 1 to start the sequence
# Initializing 1st two numbers Outside the Loop
count = 0 # we need to take the count var to stop the loop after the specific condition is met!
print("Fibonacci Seies", n1,n2, end =" ")
while count < num - 2:
    fibb = n1 + n2
    n1, n2 = n2, fibb # Swapping is happeing here where n1 = n2 and n2 = Fibb
    print(fibb, end = " ")
    count+=1

print() # move to new line to Enter next inputs in the console if equired
# Time and Space Complexity for this medthod is also the same
# -----------------------Using recursion ------------------
n = int(input()) # upto n numbers
def fibonacci(n):
    if n< 2: # base condition
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("Fibonacci Sequence:", end=" ")
for i in range(n):
    print(fibonacci(i), end = " ")
