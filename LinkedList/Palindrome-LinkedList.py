"""
Given a singly linked list, determine if it is a palindrome.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode):
        if not head or not head.next:
            return True
        front, back = [], []
        slow, fast = head, head
        while fast and fast.next:
            front.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        while slow:
            back.append(slow.val)
            slow = slow.next
        back.reverse()
        if front == back[:len(front)]:
            return True
        return False


print(isPalindrome(1 -> 2))
print(isPalindrome(1 -> 2 -> 2 -> 1))
print(isPalindrome(1 -> 0 -> 1 -> 1))
print("The booleans above are False, True, False.")
