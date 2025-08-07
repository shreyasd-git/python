#function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.


def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))


input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(get_diagonal(input_tuple))
#Output > (1, 5, 9)

#TimeComplexity - O(n) - iterates through the indices of the input tuple
#Space Complexity is O(n) - it creates a new tuple containing the diagonal elements, which has a length equal to the length of the input tuple.