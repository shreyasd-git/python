#function which takes two dictionaries as parameters and merge them and sum the values of common keys.
#Tip - when asked to merge 2 dictionaries - create copy of one dict and loop over keys of other second dict and add its values to the values of keys from dict1 


def merge_dicts(dict1, dit2):
    #make a copy of dit1 to store te  merged dict
    result = dict1.copy()

    #loop over items in dict2 and add their values to the keys:values of dict1
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value

    return result


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

print(merge_dicts(dict1, dict2))
#Output - {'a': 1, 'b': 5, 'c': 7, 'd': 5}

#Time Complexity - O(n) - accessing each item in dict ateast once
#Space Complexity - O(n+m) - n is number of elements in dict1 an m is number of elements in dict2,
#                            In worst case dict1, dict2 cold have all unique keys hence n+m in merged dict (result)