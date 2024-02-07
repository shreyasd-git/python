#sort Array

# n = len(arr)
# print(n)

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

original_arr=[4,5,1,7,8] 
print("Original array is: ",original_arr)


bubblesort(original_arr)
print("Sorted array is: ",bubblesort(original_arr))