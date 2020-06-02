"""
Given a sorted linked list, delete all nodes that have duplicate 
numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prevNode = ListNode(0)
        dummy.next = head
        while head:
            if head.next and head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                prevNode.next = head.next
            else:
                prevNode = prevNode.next
            head = head.next
        return dummy.next

    def main():
        print(deleteDuplicates(1 -> 1 -> 2))
        print(deleteDuplicates(1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5))
        print(deleteDuplicates(1 -> 1 -> 1 -> 2 -> 3))
        print("The LinkedLists above should be 2, 1->2->5, and 2->3.")
