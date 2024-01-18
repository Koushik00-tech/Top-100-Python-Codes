# Reverse a string
#-------------------using slicing and -1 index ---------
str = input()
print(str[::-1])
# #Tc O(n) 
#SC O(1) nothing is taken as extra space to print
# --------------------For loop-------------------
str = input()
rev_str = ""
for char in str:
    rev_str = char + rev_str # For each iteration char is added at the begining of the original str
    # SO that we can get original string
print(rev_str)
# -----------------------Using while loop--------------
str = input()
rev_str = ""
index = 0
while index < len(str):
    rev_str = str[index] + rev_str
    index += 1
print(rev_str)
# -----------------Recursion-------------
def recursive_rev(str):
    if len(str) <= 1: # Base condition, Without this the loop will not stop 
        return str
    else:
        return str[-1] + recursive_rev(str[:-1])  # Recursion statement
str = input()
print(recursive_rev(str))

