# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p1 = head
        p2 = p1.next
        p1.next = None
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        return p1
