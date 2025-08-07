#max element in a list

list1 = [2,4,1,9,7,16]

n = len(list1) - 1
max = list1[0]

for i in list1:
    if i > max:
        i, max = max, i

print(max)