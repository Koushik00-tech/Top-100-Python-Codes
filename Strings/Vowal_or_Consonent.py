# Check given char is vowel or consonent
# str = input()
# if str.upper() == 'A' or str.upper() == 'E' or str.upper() == 'I' or str.upper() == 'O' or str.upper() == 'U':
#     print("Given Character is Vowel")
# else:
#     print("Consonent")
# TC - O(n) Linear where we are directly checking with if else condition
# Sc - O(n) constant space 
#--------------------------Count of Vowels and Consonents in the string-----------
str = input()
vowel_count = 0
consonent_count = 0
for char in str:
    if char.upper() in "AEIOU": # We can directly use in to check the char in the str
        vowel_count += 1
    else:
        consonent_count += 1

print(vowel_count, "Vowels")
print(consonent_count,"Consonants")