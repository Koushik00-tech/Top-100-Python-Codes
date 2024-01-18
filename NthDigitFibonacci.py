# In Fibonacci Series we need to find nth number ex--> if the series is 0 1 1 2 -- 4th number is 2
# n = int(input()) 
# n1,n2 = 0,1
# if n == 0:
#     print(n) 
# elif n == 1:
#     print(0)
# else:
#     for _ in range(3,n+1): 
#         fibb = n1 + n2
#         n1, n2 = n2, fibb # n1 = n2 and n2 = Fibb

# print(n,"th Number in Fibonacci Series is :", n2)
# ---------------------Using While Loop-----------
n = int(input()) 
n1,n2 = 0,1
if n == 0:
    print(n) 
elif n == 1:
    print(0)
else:
    count = 0
    while count < n+2:
        fibb = n1+n2
        n1, n2 = n2, fibb

print(n2)
