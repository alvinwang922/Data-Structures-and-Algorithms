"""
You are given two non-empty linked lists representing two 
non-negative integers. The digits are stored in reverse 
order and each of their nodes contain a single digit. Add 
the two numbers and return it as a linked list. You may 
assume the two numbers do not contain any leading zero, 
except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = l1
        second = l2
        while first and second:
            sum = first.val + second.val
            if sum > 9:
                if not first.next:
                    first.next = ListNode(1)
                elif not second.next:
                    second.next = ListNode(1)
                else:
                    second.next.val = second.next.val + 1
            first.val = sum % 10
            second.val = sum % 10
            first = first.next
            second = second.next
        if second and not first:
            return l2
        return l1

    def main():
        print(addTwoNumbers((2 -> 4 -> 3) + (5 -> 6 -> 4)))
        print(addTwoNumbers((1) + (9 -> 9 -> 9)))
        print(addTwoNumbers((1 -> 2 -> 3) + (9 -> 7)))
        print("The LinkedLists above should be 7 -> 0 -> 8, \
            0 -> 0 -> 0 -> 1, and 0 -> 0 -> 4.")
