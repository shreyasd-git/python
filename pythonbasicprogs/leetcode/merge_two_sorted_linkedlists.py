#merge to sorted linked lists

#eg. list1 = [1,2,4]
#    list2 = [1,3,4]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode()
        curr = dummy

        #while list1 and list2 are not null
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1 #moving curr pointer to head of list1 
                list1 = list1.next #moving list1 head to next node
            else:
                curr.next = list2
                list2 = list2.next

            #move pointer to next node
            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        #return head of the new list -> dummy.next is referring the next/1st (not 0th node) node of the new list
        return dummy.next