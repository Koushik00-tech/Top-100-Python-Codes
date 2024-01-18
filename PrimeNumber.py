def is_prime(n): # Print all the prime numbers from 1 to 100 which ends with 7
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def ends_with_7(start_range, end_range):
    for i in range(start_range, end_range + 1):
        if i % 10 == 7 and is_prime(i):
            print(i)

start_range = int(input())
end_range = int(input())
ends_with_7(start_range, end_range)

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def print_primes_with_7_in_range(start, end):
#     for i in range(start, end + 1):
#         if i % 10 == 7 and is_prime(i):
#             print(i)

# # Taking input from the user for the range
# start_range = int(input("Enter the starting range: "))
# end_range = int(input("Enter the ending range: "))

# print("Prime numbers ending with 7 between", start_range, "and", end_range, "are:")
# print_primes_with_7_in_range(start_range, end_range)
