# Dive the number with its iterations, if the remainder is Zero than it is a Factor of that number
# Time and Space Complexity to find the factors is
# Tc --> O(n) -- Loop is repeating untill n number of input size
# SC - O(1) -- i is taking extra space to run the loop which is Constant
# ---------------Using While Loop
# n = int(input())
# i = 1 # Take the 1st iteration as one to end the loop at specified condition
# while i <= n:
#     if (n % i == 0):
#         print(i, end = " ")
#     i += 1 # Increasing the iteration by 1 
# #------------------Using Function
# def factors(n):
#     i = 1
#     while i <= n:
#         if int(n % i == 0):
#             print(i, end= " ")
#         i+= 1
# n = int(input())
# factors(n) # Function call 
# ------------------ Using For Loop ----------------
n = 8
for i in range(1,n+1):
    if n % i == 0:
        print(i, end=" ")


