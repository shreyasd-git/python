#Merge two linked lists
from typing import Optional

list1 = [1,4,6,8]
list2 = [1,3,5,9,14]

# list3 = sorted(list1 + list2)
# print(list3)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwolists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        curr = d

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        curr.next = list1 if list1 else list2

        return d.next



solution = Solution()
merged_list = solution.mergeTwolists(list1, list2)

# Print the merged linked list
print(merged_list)  # Outputs the linked list in readable form


