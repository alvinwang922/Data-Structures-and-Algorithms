# Given a linked list, determine if it has a cycle in it.
# To represent a cycle in the given linked list, we use
# an integer pos which represents the position (0-indexed)
# in the linked list where tail connects to. If pos is -1,
# then there is no cycle in the linked list.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pointer1 = head
        pointer2 = head
        try:
            while pointer2.next.next != None:
                pointer1 = pointer1.next
                pointer2 = pointer2.next.next
                if pointer1 == pointer2:
                    return True
        except:
            return False


print("A linked list with head = [3,2,0,-4] and pos = 1 should return True.")
print("A linked list with head = [1,2] and pos = 0 should return True.")
print("A linked list with head = [1] and pos = -1 should return True.")
