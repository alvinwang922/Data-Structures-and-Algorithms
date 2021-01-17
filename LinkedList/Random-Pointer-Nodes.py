"""
A linked list is given such that each node contains
an additional random pointer which could point to
any node in the list or null. Return a deep copy of
the list. The Linked List is represented in the
input/output as a list of n nodes. Each node is
represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to
n-1) where random pointer points to, or null if it
does not point to any node.
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None,
                 random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return
        curr, d = head, {}
        while curr:
            d[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                d[curr].next = d[curr.next]
            if curr.random:
                d[curr].random = d[curr.random]
            curr = curr.next
        return d[head]

    print(copyRandomList([[7, None], [13, 0], [11, 4],
                          [10, 2], [1, 0]]))
    print(copyRandomList([[1, 1], [2, 1]]))
    print(copyRandomList([[3, None], [3, 0], [3, None]]))
    print("The linked lists above should be [[7, None], \
        [13, 0], [11, 4], [10, 2], [1, 0]], [[1, 1], [2, 1]], \
            and [[3, None], [3, 0], [3, None]]")
