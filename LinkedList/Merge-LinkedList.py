"""
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.
"""


# Recursive solution:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# Iterative solution:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if not l1:
            return l2
        elif not l2:
            return l1
        final = temp = ListNode(min(l1.val, l2.val))
        if l1.val <= l2.val:
            l1 = l1.next
        else:
            l2 = l2.next
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2
        return final


print(mergeTwoLists(1 -> 2 -> 4, 1 -> 3 -> 4))
print(mergeTwoLists(1, 2))
print(mergeTwoLists())
print("The linkedlists above should be 1->1->2->3->4->4, 1->2, and None.")
