#Missing Number from arr
#Trick - find sum of first n numbers (total) and then subtract the sum of array elements 

def misselement(arr,n):
    #Get Sum of first n natural nums
    total = n * (n + 1) // 2 

    #sum of array elements
    sum_arr = sum(arr)

    missing = total - sum_arr

    return missing

print(misselement([1,2,3,4,6],6))

