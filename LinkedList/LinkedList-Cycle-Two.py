"""
Given a linked list, return the node where the cycle begins. 
If there is no cycle, return null. To represent a cycle in 
the given linked list, we use an integer pos which represents 
the position (0-indexed) in the linked list where tail connects 
to. If pos is -1, then there is no cycle in the linked list.
Note: Do not modify the linked list.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        try:
            fast = fast.next.next
            slow = slow.next
            while slow is not fast:
                fast = fast.next.next
                slow = slow.next
            tempSlow = head
            while tempSlow is not slow:
                tempSlow = tempSlow.next
                slow = slow.next
            return slow
        except:
            return None

    def main():
        print("A linked list with head = [3,2,0,-4] and pos = 1 should \
            return the node at index 1.")
        print("A linked list with head = [1,2] and pos = 0 should return \
            the node at index 0.")
        print("A linked list with head = [1] and pos = -1 should return None.")
