#python - leetcode
#Remove duplicates from array list

# #BRUTE FORCE - using another list
# nums = [1,1,2]
# n = len(nums)
# uniq_list=[nums[0]]

# for i in range(1, len(nums) ):
#     print(nums[1], nums[i-1])
#     if nums[i] != nums[i-1]:
#         uniq_list.append(nums[i])
# print(uniq_list)



#In Place operation

nums = [1,2,3,4,4]
i = 0 #counter to traverse over the 

for j in range(1, len(nums)):
    if nums[i] != nums[j]:
        i = i+1
        nums[i] = nums[j]
print(nums[:i+1])      #to get the new/modified array
#print(i+1)            #to get length of the new
