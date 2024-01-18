# Sum of digits of a given number
# n = input()
# sum_of_elements = 0
# for i in n:
#     sum_of_elements += int(i)
# print(sum_of_elements)

# ------------------------- Brute Force approach using While loop
# n = 1234
# sum = 0
# while n != 0:
#     digit = int(n % 10) # 4 + 3 + 2 + 1
#     sum += digit
#     n = n/10
# print(sum)
#TC - O(log n) loop is repeating digit times which is as long as the condition goes to 0

# -------------- Using recursion 
num = 1234
def find_sum(num):
    if num == 0:
        return 0
    return int(num % 10) + find_sum(num /10) # remainder + quotient -- 4 + 6
print(find_sum(num))
