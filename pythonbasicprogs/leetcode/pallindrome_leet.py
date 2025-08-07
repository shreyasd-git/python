#pallirom > mirror image

#for string
# a = "malayalam"

# def isPallindrome(a):
#     for i in range(0, int((len(a)/2))):
#         if a[i] != a[int(len(a)-i-1)]:
#             return False
#     return True

# if (isPallindrome(a)):
#     print("Yes string is Pallindrome")
# else:
#     print("No, String is not Pallinrome")



#For integer number without converting to str
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # x=str(x)
        # for a in range(int(len(x)//2)):
        #     if x[a] != x[int(len(x)-1-a)]:
        #         return False
        # return True

        original = x
        rev_num = 0

        while x > 0:
            digit = x % 10  # as we want to reverse the number, this gives last digit
            rev_num = rev_num * 10 + digit  #adds tens place to for the rev_num
            x = x // 10 # to eliminate the last digit from x
            print(rev_num)
        if rev_num == original:
            return True
        return False
    
