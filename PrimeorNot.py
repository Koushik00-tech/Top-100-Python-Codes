# without writing a function
# prime means - A number divible by one and it self or having only two factors 
# if the number is having more than two factors than that number is not a prime number
# ----------------------With Function-----------------------------
# def is_prime(n): # if we take 5 as input
#     if n < 2: # F
#         return False
#     for i in range(2, n): 
#         if n % i == 0:
#             return False
#     return True
# n = 15
# if is_prime(n):
#     print("Prime")
# else:
#     print("Not Prime") 

# ---------------------
# for i in range(2,n):
#     if n % i == 0: # Now we'll check the iteration -- F
#         print("Not a prime") 
#     else:
#         print("Prime")
# -------------------Prime Or Not
n = int(input())
prime = 1
for i in range(2, n):
    if n % i == 0:
        prime = 0
        break
if prime:
    print("Prime Number")
else:
    print("Not a Prime Number")