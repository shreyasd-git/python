#function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

def max_val_key(my_dict):
    return max(my_dict, key=my_dict.get)

my_dict = {'a':3, 'b':8, 'c':5}

print(max_val_key(my_dict))


#Time Complexity - O(n)  accessing all elements in the dict
#Space Complexity - O(1) - not creting new dict, only storing the current key

#Dry Run
#my_dict.get('a') → 3

#my_dict.get('b') → 8

#my_dict.get('c') → 5

#-------------------------------------------------------------------------------------------#
# Another Example of max to understand better -
# words = ['cat', 'elephant', 'tiger']
# longest = max(words, key=len)
# print(longest)  
# # Output: elephant