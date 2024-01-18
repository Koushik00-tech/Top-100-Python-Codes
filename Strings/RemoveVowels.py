# Remove vowels from String
# String is imutable so, we can't add or remove elements from str
str = input()
vowels = ['A', 'E','I','O','U'] # Taking the list of vowels
new_str = ""
for char in range(len(str)):
    if str[char].upper() not in vowels: # accessing the elements not in vowels using index
        new_str += str[char]
print(new_str)
# TC - O(n) loop is itertion till n values where n is the length of the string
# SC - O(n) new_str variable grows linearly with the size of the input string.
# In each iteration of the loop, a new character is added to new_Str. 