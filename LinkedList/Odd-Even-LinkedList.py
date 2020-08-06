"""
Given a singly linked list, group all odd nodes together followed by the 
even nodes. Please note here we are talking about the node number and not 
the value in the nodes.
You should try to do it in place. The program should run in O(1) space 
complexity and O(nodes) time complexity.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode):
        if not head:
            return
        odd = head
        even = evenHead = head.next
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = evenHead
        return head


print(oddEvenList(1 -> 2 -> 3 -> 4 -> 5 -> None))
print(oddEvenList(2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7 -> None))
print("The linkedlists above should be 1->3->5->2->4->None \
    and 2->3->6->7->1->5->4->None.")
