#function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

def elementSum(tuple1, tuple2):
    # list1 = []
    if len(tuple1) != len(tuple2):
        raise ValueError("Input tuples must have the same length.")
    
    # for i in range(len(tuple1)):
    #     sum = 0
    #     sum = tuple1[i] + tuple2[i]
    #     list1.append(sum)

    result = tuple(a + b for a, b in zip(tuple1, tuple2)) #Use the zip function to pair corresponding elements of the input tuples
    return result

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(elementSum(tuple1,tuple2))
#Output - (5, 7, 9)

#Time Complexity - O(n) - traverse the tuples once
#Space Complexity - O(n) - new tuple is created of the size of input tuple
