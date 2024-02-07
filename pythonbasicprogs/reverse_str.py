#reverse a string

a = "dugtrio"

def reverse(a):
    str = ""
    for i in a:
        str = i + str
    return str

print("The original String is: ",a)

print("The reversed string is : ", reverse(a))


