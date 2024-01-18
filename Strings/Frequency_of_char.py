# To find the frequency of char in str
str = input()
char = input()
count = 0
for i in str: # While the str index must be intergers not the str values we directly took i as a iteration varibale and repeated the loop until L values
    if char == i: # if char is equal to the char in the str then need to increase the count by...
        count += 1
print(count)  # Iterate the loop till L values where L is the Length of the str
# Tc - O(n) where each char of the str is iterated untill n values where n is the length of the string
# SC  - O(n) where count var took extra space to store the count values if we find the char in the string
# --------------------Using While ------------
str = input()
char = input()
index = 0 # To terminate the while loop at chars inside the str will become zero
count = 0
while index < len(str): 
    if char == str[index]:
        count += 1
    index += 1 # Evvery time in while loop don't forget to update the index(var decalard for iteration)
print(count)
