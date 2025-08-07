#reverse the key:value to value:key

def rev_keyval(my_dict):
    # new_dict={}
    # for key, value in my_dict.items():
    #     new_dict[value]=key
        
    # return new_dict
    return {value:key for key,value in my_dict.items()}



my_dict = {'a':1, 'b':2, 'c':3}
print(rev_keyval(my_dict))

#Time Complexity - O(n) - accessing elements in dict once
#Space Complexity - O(n) - returns new dict with reverse key, value pairs  