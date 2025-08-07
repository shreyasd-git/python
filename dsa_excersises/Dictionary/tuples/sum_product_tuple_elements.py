#function that calculates the sum and product of all elements in a tuple of numbers.


def sum_prdt_tuple(input_tuple):
    sum=0
    prodt=1

    for i in input_tuple:
        sum = sum + i
        prodt = prodt * i

    return sum, prodt

input_tuple = (1, 2, 3, 4)
print(sum_prdt_tuple(input_tuple))
#Output > (10, 24)

#Time Complexity - O(n) - all elements of the tuple will be traversed
#Space Coplexity - O(1) - constant amount of space requird to store the sum and product 