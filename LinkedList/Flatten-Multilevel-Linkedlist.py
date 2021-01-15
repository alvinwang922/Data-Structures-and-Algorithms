"""
You are given a doubly linked list which in addition to 
the next and previous pointers, it could have a child 
pointer, which may or may not point to a separate doubly 
linked list. These child lists may have one or more 
children of their own, and so on, to produce a multilevel 
data structure, as shown in the example below.
Flatten the list so that all the nodes appear in a 
single-level, doubly linked list. You are given the head 
of the first level of the list.
"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node'):
        temp = head
        while temp:
            if temp.child:
                right = temp.next
                temp.next = self.flatten(temp.child)
                temp.next.prev = temp
                temp.child = None
                while temp.next:
                    temp = temp.next
                if right:
                    temp.next = right
                    temp.next.prev = temp
            temp = temp.next
        return head

    print(flatten([]))
    print(flatten([1, 2, 3, 4, 5, 6, None, None,
                   None, 7, 8, 9, 10, None, None, 11, 12]))
    print(flatten([1, 2, None, 3]))
    print("The linked lists above should be [], \
        [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6], and [1, 3, 2].")
