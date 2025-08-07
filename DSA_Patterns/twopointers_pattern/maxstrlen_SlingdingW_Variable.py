#SlidingWindow Varaible

#Check max string length with unique characters only

str1 = 'abacdbad'

def max_str(str1):
    seen = set()
    start = 0
    end = 0
    max_len = float('-inf')

    for end in range(len(str1)):
        while str1[end] in seen:
            seen.remove(str1[start])
            start += 1

        seen.add(str1[end])
        max_len = max(max_len, end - start + 1)

    return max_len

print(max_str(str1))