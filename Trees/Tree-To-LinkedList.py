"""
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List 
in place. You can think of the left and right pointers as synonymous 
to the predecessor and successor pointers in a doubly-linked list. 
For a circular doubly linked list, the predecessor of the first element 
is the last element, and the successor of the last element is the first 
element. We want to do the transformation in place. After the 
transformation, the left pointer of the tree node should point to its 
predecessor, and the right pointer should point to its successor. You 
should return the pointer to the smallest element of the linked list.
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node'):
        if not root:
            return
        dummy = Node(0, None, None)
        prev = dummy
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right

    print(treeToDoublyList([]))
    print(treeToDoublyList([4, 2, 5, 1, 3]))
    print(treeToDoublyList([2, 1, 3]))
    print("The linked lists above should be [], [1, 2, 3, 4, 5], \
        and [1, 2, 3].")
