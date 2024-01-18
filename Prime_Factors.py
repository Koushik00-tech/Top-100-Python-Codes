# To find the prime factors
# Step1-  Need to find the factors of a number
# Step2- Check they are prime or not and prime the prime factors
# ----------------------Using Function----------
def prime_factors(n):
    if n < 4:
        return n
    arr = []
    while n > 1:
        for i in range(2, int(n+2//2)): # Iterting the loop for less range of input to optmize the code
            if i == (1 + n // 2): # To check prime 
                arr.append(n)
                n = n// n
            if n % i == 0: # to find the factors
                arr.append(i)
                n = n // i
                break
    return arr
n = 10
result = prime_factors(n)
print(*result) # -- By using the stars we can remove brackets from the result...
