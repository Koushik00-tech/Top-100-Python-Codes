#--------------------Length of the str with out inbuilt len method
str = input()
count = 0
for _ in str:
    count += 1
print(count)
# TC - O(n) Repeating the loop till n values
# Sc - O(1) taking count as extra space with 
