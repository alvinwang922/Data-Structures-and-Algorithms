'''
Merge k sorted linked lists and return it as one 
sorted list. Analyze and describe its complexity.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = currNode = ListNode(0)
        while left and right:
            if left.val < right.val:
                currNode.next = left
                left = left.next
            else:
                currNode.next = right
                right = right.next
            currNode = currNode.next
        currNode.next = left or right
        return dummy.next


print(mergeKLists([1 -> 4 -> 5, 1 -> 3 -> 4, 2 -> 6]))
print(mergeKLists([1 -> 1 -> 1, 1 -> 1 -> 1, 1 -> 1]))
print(mergeKLists([2 -> 4 -> 6]))
print("The LinkedLists above should be 1->1->2->3->4->4->5->6, \
    1->1->1->1->1->1->1->1, and 2->4->6")
