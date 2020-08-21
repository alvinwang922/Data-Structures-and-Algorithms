"""
Given a non-empty, singly linked list with head node head, 
return a middle node of linked list.
If there are two middle nodes, return the second middle node.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow


print(middleNode([1, 2, 3, 4, 5]))
print(middleNode([1, 2, 3, 4, 5, 6]))
print(middleNode([1, 2, 3]))
print("The nodes above should be [3, 4, 5], [4, 5, 6], and [2, 3].")
