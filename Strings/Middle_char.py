# I need to print middle char in the string-------------
# If the length is Even need to print two chars from middle or if the length is odd we need to print the middle char
# -----------------------Ignore if the length of the char is even -------------------
str = input()
# for char in str: 
#     if len(str) % 2 == 1:
#         middle = len(str) // 2 # this will give quotient value ex : if length is 7 // 2 = 3 as quotient
#         print(str[middle]) 
#         break
# -------------------------using while loop-------------------
# index = 0 # To stop the loop at specified condition
# while index < len(str):
#     if len(str) % 2 == 1:
#         middle_char = len(str) // 2
#         print(str[middle_char])
#         break
#     index += 1
# -------------------------------Recursion---------------
def recursive_middle_char(str):
    if len(str) % 2 == 1:
        middle_char = len(str) // 2
        print(str[middle_char])
    else:
         # Recursive case: call the function again with the substring excluding the first and last characters
        recursive_middle_char(str[1:-1])  

recursive_middle_char(str)

