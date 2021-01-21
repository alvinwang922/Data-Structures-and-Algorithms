"""
Given the head of a linked list, rotate the list 
to the right by k places.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int):
        if not head or not k:
            return head
        temp = head
        l = 1
        while temp.next:
            l += 1
            temp = temp.next
        temp.next = head
        k = k % l
        temp = head
        for _ in range(l - k - 1):
            temp = temp.next
        ans = temp.next
        temp.next = None
        return ans

    print(rotateRight([], 1))
    print(rotateRight([1, 2, 3, 4, 5], 2))
    print(rotateRight([0, 1, 2], 4))
    print("The linked lists above should be [], \
        [4, 5, 1, 2, 3], and [2, 0, 1].")
