#Find two elements from array whose sumation is equal to given target value

def findelements(arr1, target):
    seen = {} #initialize empty dict
    
    for i, num in enumerate(arr1):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
        
print(findelements([2,7,11,15],9))

