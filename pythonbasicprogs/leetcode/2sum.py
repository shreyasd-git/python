#2 sum Problem - leet code
# we hve an array and a target value, the sum of any two values of array has to match the target, 
# we need to find those two values from the array

# the below optimal approach > using hashmap or dictionary
# Time Complexity = O(n) as we iterate the whole array once
# Space Complexity = O(n) as we store the whole array in a hashma/dictionary 

from typing import List

num = [1,3,5,8]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} #initialize empty hashmap/dictionary

        for index, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff], index]
            hash_map[num] = index
        return
    
sol = Solution()
print(sol.twoSum([1, 3, 5, 8], 8))  # Output: [1, 2]
