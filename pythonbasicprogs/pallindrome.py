#pallirom > mirror image

a = "malayalam"

def isPallindrome(a):
    for i in range(0, int((len(a)/2))):
        if a[i] != a[int(len(a)-i-1)]:
            return False
    return True

if (isPallindrome(a)):
    print("Yes string is Pallindrome")
else:
    print("No, String is not Pallinrome")