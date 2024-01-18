# Toggel string -- Converting Lower case to upper and vice versa 
# str = input()
# new_str = "" # to take the output
# for char in str:
#     if char.islower(): # the char in str is lower (T/F)
#         char = char.upper()         
#         # new_str.append(char) # Str will not take append
#         # new_str.format(char)
#     else:
#         char = char.lower()
#         # new_str.append(char)
#         # new_str.format(char)
#     new_str += char #  Concat that updated char into newstr
# print(new_str) # New String we'll get all upper case letters to lower and vice versa
# strings are immutable, meaning you cannot modify them in-place.
# The time complexity of the code is O(n), where n is the length of the input string.
# The space complexity is also O(n). This is because the new_str variable, 
# which stores the modified string, grows linearly with the size of the input string.
# ------------------Using While loop----------------------
str = input()
index = 0 # Initializing a var name index to stop the while loop iteration 
new_str = ""
while index < len(str): # We need to take char from string using index--  While using While loop 
    char = str[index]
    if char.islower():
        char = char.upper()
    else:
        char = char.lower()
    new_str += char
    index += 1
print(new_str)

