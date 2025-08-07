#Given a sorted array, find if there are two numbers that add up to a target sum.
#Time Complexity - O(n)	

arr = [1,2,3,4,5,6]
target = 6

def pairtotarget(arr, target):
    left = 0
    right = len(arr) - 1
    curr = 0

    while left < right:
        curr = arr[left] + arr[right]
        if curr == target:
            return arr[left], arr[right]
            #print(arr[left], arr[right])
            #continue
        elif curr > target:
            right -= 1
        else:
            left += 1

    return False

print(pairtotarget(arr, target))