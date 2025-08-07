#function that takes a tuple and a value, 
#and returns a new tuple with the value inserted at the beginning of the original tuple.

def insertatBeginning(t1, element):
    return (element,) + t1

t1 = (2, 3, 4)
element = 1
print(insertatBeginning(t1, element))

#Time Complexity - O(1) - iterates through the elements of the input tuple once
#Space Complexity - O(n) - new tuple is created
