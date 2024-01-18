# Count of Distinct elements in an array
arr = [1,2,4,2,5,4,7] # 5 Expected output
distinct_el = []
for element in arr:
    if element not in distinct_el: # 
        distinct_el.append(element)
print(len(distinct_el))
# TC : O(n * 2) each element will check all the elements in an array for n times 
# Sc : O(n) distinct_el arr is taken extra space to store distinct values
# --------------------------Using Set --------------------------
# If we want to take the input from the user for array 
# need to split the input elements using list and map methods as taken below
arr = list(map(int, input().split())) # Map is used to convert strings to int
distinct_el = set(arr)
count = len(distinct_el)
print(count) # This will give count of distinct elements in a array
# TC - O(n)  
# Sc - O(k) is to store distinct values using set() method 