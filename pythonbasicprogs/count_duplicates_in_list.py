#count duplicates


def itemcount(list1):
    #initialte a dict
    count={}
    for item in list1:
        if item in count:
            count[item] = count[item] + 1
        else:
            count[item] = 1

    return {key: value for key, value in count.items() if value > 1}
    
list1 = [1,2,2,4,5,6,4]
duplicates = itemcount(list1)
print(duplicates)