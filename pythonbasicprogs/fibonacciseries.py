#Fibonacci series

# def fibonacci(n):
#     list1 = [0,1]
#     i=0
#     j=1

#     while len(list1) < n:
#         sum_val = i + j
#         list1.append(sum_val)
#         i = j
#         j = sum_val

#     return list1

# print(fibonacci(9))


#Using Recursion

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
for i in range(10):
    print(fibo(i))
