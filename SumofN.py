#-------------------Using For Loop---------------------
n = int(input())
sum_of_n = 0
for i in range(n + 1):
    sum_of_n += i
print(sum_of_n)
# # TC - O(n) -- for loop is iterating for n time
# # Auxillary Space - 0(1) constant Sum_of_n is taken as extra space to store Sum value
# #------------------Using While loop --------------
# n = int(input())
# sum_of_n = 0
# count = 1
# while count <= n:
#     sum_of_n += count
#     count += 1
# print(sum_of_n)
#TC - 0(n) 
# Auxillary space - O(1) constant Sum_of_n and Count values are taken extra space with Constant values
#----------------------Better to use Formula if the input n value is larger--------------
# n = int(input())
# sum_of_n = (n * (n+1) // 2)
# print(sum_of_n) 
#TC - O(1) worst case -- no need to use any loop
# SC - O(1) sum_of_n    

#-------------------Sum of n natural numbers in given range--------------
# start = int(input())
# end = int(input())
sum_of_n = 0 # for example we'll take a start range as 5 and End as 10 so the Expected output will be
# 5+6+7+8+9+10 = 45 
# for i in range(start, end + 1):
#     sum_of_n += i
# print(sum_of_n)
#TC -- O(n) as we are repeating the loop for n times in the given range
# Sc - O(1) sum_of_n
# ----------- for Optimize solution we can use formula
# Subracting sum of start range  from end range
def sum_of_n_natural_numbers_in_range(start, end):
    return (end * (end + 1) - start * (start - 1)) // 2 # Here we'll get the quotient value
start = int(input())
end = int(input())
result = sum_of_n_natural_numbers_in_range(start, end)
print(result)
# sum = int((num2*(num2+1)/2) - (num1*(num1+1)/2) + num1) to find directly without function
# TC- O(1) no loop is used
#SC- O(1) only result is used to store

