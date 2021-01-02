"""
Given a linked list, swap every two adjacent 
nodes and return its head.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode):
        dummy = prev = ListNode(None)
        prev.next = head
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            prev.next, first.next, second.next = \
                second, second.next, first
            prev = first
        return dummy.next

    print(swapPairs([1, 2, 3, 4]))
    print(swapPairs([]))
    print(swapPairs([1]))
    print("The linked lists above should be \
        [2, 1, 4, 3], [], and [1].")
