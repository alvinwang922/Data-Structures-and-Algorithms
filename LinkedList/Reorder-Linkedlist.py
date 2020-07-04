"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        mid = end = head
        while end and end.next:
            mid = mid.next
            end = end.next.next
        tracker, prevNode = mid, None
        while tracker:
            currNode = tracker
            tracker = tracker.next
            currNode.next = prevNode
            prevNode = currNode
        while prevNode.next:
            head.next, head = prevNode, head.next
            prevNode.next, prevNode = head, prevNode.next


print(reorderList(1 -> 2 -> 3 -> 4))
print(reorderList(1 -> 2 -> 3 -> 4 -> 5))
print(reorderList(1))
print("The linkedlists above should be 1->4->2->3, 1->5->2->4->3, and 1.")
