"""
Given a linked list, remove the n-th node from the end of list and return its head.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        tracker1 = head
        tracker2 = head
        while n > 0:
            tracker1 = tracker1.next
            n -= 1
        if not tracker1:
            return head.next
        while tracker1.next:
            tracker1 = tracker1.next
            tracker2 = tracker2.next
        tracker2.next = tracker2.next.next
        return head


print(removeNthFromEnd(1 -> 2 -> 3 -> 4 -> 5, 2))
print(removeNthFromEnd(5 -> 1, 2))
print(removeNthFromEnd(1, 1))
print("The linkedlists above should be 1->2->3->5, 1, and None.")
