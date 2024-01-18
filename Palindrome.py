# A number is said to be palindrome if they look same on the striaght and reverese ordee
# Ex --> 1221 is a palindrome but 1234 is not
# --------------------Using General Iteration using While Loop
# n = int(input())
# temp = n # taking temp as a variable and storing the number
# rev = 0
# while temp > 0:
#     rem = temp % 10 # to store the remainder
#     rev = (rev * 10) + rem
#     temp = temp // 10 # to get quotient value and check for nxt iteration
# if n == rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

#TC - O(log n) the loop is itertaion to every digit in n where the digits are in n is proportional to log10(n).
#SC - O(1) we are using temp and rev to store the constant values
# ------------------------Using String Slicing
# n = 1234
# rev = (str(n)[::-1])
# if n == int(rev): # n is in int format and rev is in str format
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
#TC - O(log n)  
# SC - O(log n) The space complexity is O(log10(n)) as well. The space required for the string representation of the reversed number scales with the number of digits in n.
# ------------------------Recursion
def recursion_rev(num, rev):
    if num == 0:
        return rev
    
    rem = int(num % 10) # the number of recursive calls is proportional to the number of digits in the input number, which is log10(n).
    rev = (rev * 10) + rem
    return recursion_rev(int(num / 10), rev) # Passing the function it self is know as recursion

num = 1234
rev = 0
reverse = recursion_rev(num, rev)
print("Palindrom" if num == reverse else print("Not a Palindrome"))
