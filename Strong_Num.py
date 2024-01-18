# A number is said to be strong when sum of digit's factorial is equal to that number
# Ex--> 145 is Strong Number coz--> 1! + 4! + 5! --> 1 + 24 + 120 = 145
n = 135
num = n # Duplicating the number to check 
#----------------Approach-1 Getting all the factorials from 1 to 9 ---------
sum = 0
f = [0] * 10
f[0] = 0
f[1] = 1
for i in range(2,10):
    f[i] = f[i-1] * i
# Implementation
while(num):
    digit = int(num % 10) # Taking out every digit from the given number
    num = num / 10
    sum += f[digit]
if (sum == n):
    print("Strong Number")
else:
    print("Not a Strong Number")
# Time Complexity -- O(log n)  where every digit is taken and Loop is Iterated for length of n times
    #  This is because the number of digits in n determines the number of iterations.
# SC --> O(1) where sum digit are taken extra space to store constant values

