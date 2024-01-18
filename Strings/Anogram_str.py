# Anagram means if all the chars in str one are in str two we can say it as Anagram
str1 = input()
str2 = input()
if len(str1) != len(str2):
    print("Not an Anagram")
else:
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2) # sorting the strings in ascending order based on their unicode points
    if sorted_str1 == sorted_str2:
        print("Anagram")
    else:
        print("Not an Anagram")
# By sorting the characters in both strings, you are essentially 
# creating a normalized representation of the strings where the order of characters is not considered.
#  After sorting, you can compare the sorted strings directly to check if they are composed of the same characters.
# This approach has a time complexity of O(n log n) due to the sorting operation, where n is the length of the strings