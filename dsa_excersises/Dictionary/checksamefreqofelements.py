#function which takes two lists as parameters and check if two given lists have the same frequency of elements.

def check_same_frequency(list1, list2):
    def count_elements(list3):
        counter = {}
        for i in list3:
            counter[i] = counter.get(i, 0) + 1
        return counter
    
    return count_elements(list1) == count_elements(list2)

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))

#Time Complexity - O(n) - O(n1 + n2 + min(m1, m2)), where n1 and n2 are the lengths of list1 and list2, 
#                         and m1 and m2 are the numbers of distinct elements in list1 and list2
#Space Complexity - O(n) - O(m1 + m2), where m1 and m2 are the numbers of distinct elements in list1 and list2