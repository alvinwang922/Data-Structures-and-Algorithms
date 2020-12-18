"""
You are given a perfect binary tree where all 
leaves are on the same level, and every parent 
has two children. The binary tree has the 
following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its 
next right node. If there is no next right 
node, the next pointer should be set to None.
Initially, all next pointers are set to None.
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node'):
        head, nodes, i = root, [root], 0
        while i < len(nodes):
            currNode = nodes[i]
            if currNode:
                nodes.append(currNode.left)
                nodes.append(currNode.right)
                currNode.next = nodes[i + 1]
            i += 1
        while head:
            head.next = None
            head = head.right
        return root

    print(connect([1, 2, 3, 4, 5, 6, 7]))
    print("The tree above should be \
        [1, None, 2, 3, None, 4, 5, 6, 7, None]")
