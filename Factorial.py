# Factorial of a number ex: 5 --> 5 x 4 x 3 x 2 x 1 --> 120
# n = 5
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
# print(fact)

# --------------Using Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return ((n) * factorial(n-1))
n = 5
result = factorial(n)
print(result)

# ------------ Using While Loop -------
n = 5
fact = 1
count = 1
while count <= n:
    fact = fact * count
    count += 1
print(fact)
