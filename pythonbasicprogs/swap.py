#swap two numbers with therd variable

#Approch 1 - Optimal
a = 1
b = 25

a,b = b,a 

print("Afer Swapping: a=",a,"b=",b)

#Approach 2
#a=1 b=25
a = a + b //26
b = a - b //1
a = a - b //25

print("Afer Swapping: a=",a,"b=",b)