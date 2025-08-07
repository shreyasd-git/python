#Kth largest element
k = 2
arr1 = [-3,-2,-5,-8,-1]
n = len(arr1) #5

for i in range(len(arr1)):
    for j in range(i+1,len(arr1)):
        if arr1[i] > arr1[j]:
            arr1[i], arr1[j] = arr1[j], arr1[i]
            continue

print("Sorted array is: ",arr1)

if k<(n+1) and k>0:
    r = int(n-k)
    print(arr1[r])
else:
    print(f"k should be less than {n} and greater than 0")




