"""
Remove all elements from a linked list of integers 
that have value val.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int):
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        prev, curr = head, head.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return head

    # A faster solution
    def removeElements2(self, head: ListNode, val: int):
        while head and head.val == val:
            head = head.next
        curr = head
        while curr:
            if curr.next and curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

    print(removeElements([], 1))
    print(removeElements([2], 2))
    print(removeElements([1, 2, 6, 3, 4, 5, 6], 6))
    print("The linked lists above should be None, None, \
        and [1, 2, 3, 4, 5].")
