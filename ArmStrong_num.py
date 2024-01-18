# Armstrong number is a num is equal to sum of powers of their length
# we check whether the sum of the digits of each number to the power the length of the number is equal to the number itself or not. 
# If the number is the same as the original, it’s an Armstrong number.

n = 371 # It is an ArmStrong number -- (3)3 + (7)3 + (1)3 == 371
num = n # Duplicating the Original number 1st 
digit, sum = 0,0
L = len(str(n))
for i in range(L):
    digit = int(num%10) # Taking each digit from the given number -- need to divide the number with 10 to get remainder x
    num = num/10 # updating the remaining number
    sum += digit ** L
if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# Tc - O(log n) -- Each digit is taken from the loop and repeating the loop till length of the number
# Sc - O(1) -- digit and sum , L are taken extra space to store constant values
# The amount of extra space used by the algorithm remains constant regardless of the input size.
# ------------------- Using While Loop
n = 371
num = n
digit, sum = 0,0
L = len(str(n))
while num > 0: # As long as the num becomes Zero
    digit = int(num % 10)
    num = num / 10
    sum += digit ** L
if sum == n:
    print("ArmStrong Number")
else:
    print("Not an ArmStrong Number")

