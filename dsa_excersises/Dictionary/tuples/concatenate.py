#function that takes a tuple of strings and concatenates them, separating each string with a space.


def concatenate(input_tuple):
    return ' '.join(input_tuple)


input_tuple = ('Hello', 'World', 'from', 'Python')
print(concatenate(input_tuple))

#Time Complexity - O(n) - goes over each element of tuple
#Space Complexity - O(n) - creates new string of length equal to tuple length