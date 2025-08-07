#SlidingWndow  fixed
#You are given an integer array nums consisting of n elements, and an integer k.
#Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.

#step 1 - get max average by iterating through the array

arr1 = [1,12,-5,-6,50,3]
k = 4

def max_avg(arr1,k):
    start=0
    end=0
    max_sum = float('-inf')
    curr_max = 0

    for end in range(len(arr1)):
        curr_max += arr1[end]
        
        if end - start == k - 1:
            max_sum = max(max_sum, curr_max)
            curr_max = curr_max - arr1[start]
            start += 1

    return max_sum/k

print(max_avg(arr1,k))  