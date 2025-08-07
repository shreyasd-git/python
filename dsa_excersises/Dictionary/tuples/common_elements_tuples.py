#function that takes two tuples and returns a tuple containing the common elements of the input tuples.

def commonElements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2)) #set contains only unique element

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

print(commonElements(tuple1, tuple2))
#output > (4, 5)

#Time Complexity - O(n) - the two input tuples are of equal length, the overall time complexity of the function is O(n)
#Space Complexity - O(n) - new tuple will be no longer than the input tuple 
