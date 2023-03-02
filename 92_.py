#
# @lc app=leetcode.cn id=92 lang=python
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 采用递归解法
successor = None
class Solution(object):
    def reversefirstN(self, head, n):
        global successor
        if n == 1:
            successor = head.next
            return head
        last = Solution.reversefirstN(self, head.next, n-1)
        head.next.next = head
        head.next = successor
        return last
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head == None or head.next==None:
            return head

        if left == 1:
            return(Solution.reversefirstN(self, head, right))
        head.next = Solution.reverseBetween(self, head.next, left-1, right-1)
        return head
