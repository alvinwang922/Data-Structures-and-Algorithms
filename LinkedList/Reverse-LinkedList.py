# Reverse a singly linked list.


# Recursive solution:
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head, prev=None):
        if not head:
            return prev
        currNode, head.next = head.next, prev
        return self.reverseList(currNode, head)


# Iterative solution:
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
    prevNode = None
    while head:
        currNode = head
        head = head.next
        currNode.next = prevNode
        prevNode = currNode
    return prevNode


print("A linked list 1->2->3->4->5->None should become 5->4->3->2->1->None")
