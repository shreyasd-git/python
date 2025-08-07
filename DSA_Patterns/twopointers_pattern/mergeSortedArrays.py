#Merge Sorted arrays

arr1=[1,2,4,5]
arr2=[7,9,10]

def merge_arr(arr1, arr2):
    i = 0
    j = 0
    merged = []

    while i < len(arr1) > 0 and j < len(arr2) > 0:
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            merged.append(arr2[j])
            j += 1

    #append pending item of array 1 fter above while loop condition
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    #append pending item of array 2 fter above while loop condition
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
            
    return merged

print(merge_arr(arr1, arr2))
