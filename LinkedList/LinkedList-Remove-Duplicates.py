"""
Given a sorted linked list, delete all duplicates 
such that each element appear only once.
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
        currNode = head
        while currNode:
            if currNode.next and currNode.val == currNode.next.val:
                currNode.next = currNode.next.next
            else:
                currNode = currNode.next
        return head

    def main():
        print(deleteDuplicates(1 -> 1 -> 2))
        print(deleteDuplicates(1 -> 1 -> 2 -> 3 -> 3))
        print(deleteDuplicates(1 -> 3 -> 5))
        print("The LinkedLists above should be 1->2, 1->2->3, and 1->3->5.")
