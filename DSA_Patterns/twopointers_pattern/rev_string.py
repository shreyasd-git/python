#Reverse a string (2 pointers)
#Brute Force - For loop
#Optimal O(n) > Two pointers [left(start), Right(end)] 

s = 'shreyas'

def revstr(s):
    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

s = 'shreyas'
print(revstr(s))


