#LeetCode prob 88
#Merge Sorted Arrays - nums1 is m+n

nums1 = [0,1, 0,0,0,1,2,3,0,] #m=3
nums2 = [2,3,4] #n=3
print(len(nums1))
n = len(nums1)
for i in reversed(range(n)):
    #print('i is', i, nums1)
    if nums1[i]==0:
        #print(f'Found 0 at {i} of {nums1}')
        nums1.remove(nums1[i])
        #print('removed', i, nums1)
    else:
        print(f'Not zero at {i}')
    

print(nums1)
nums1.extend(nums2)
print(sorted(nums1))


arr3 = [2,3,4,3,5,8]

for a in range(len(arr3)):
    min_val = a
    for b in range(a+1,len(arr3)):
        if arr3[min_val] > arr3[b]:
            min_val = b
    arr3[a],arr3[min_val] = arr3[min_val], arr3[a]
print("This is sorted array 3: ", arr3)
    



