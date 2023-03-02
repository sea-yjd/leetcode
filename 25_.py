#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverse(self, a, b):
        # [a, b) 之间进行反转
        pre = None
        cur = a
        nxt = a
        while (cur != b):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 解法一：递归
        if head == None or head.next == None:
            return head
        a = b = head
        for i in range(k):
            if (b == None):
                return head
            b = b.next
        newHead = Solution.reverse(self, a, b)
        a.next = Solution.reverseKGroup(self, b, k)
        return newHead

        # 解法二：利用数组
        head_ = head
        array = [head.val]
        while head.next != None:
            array.append(head.next.val)
            head = head.next
        len_ = len(array)
        num = int(len_ / k)
        i = 0
        while (i + k) <= len_:
            p = array[i: i+k]
            p = p[::-1]
            array[i: i+k] = p
            i = i + k
        # arr2list
        new_head = p = ListNode(array[0])
        i = 1
        while(i < len_):
            p.next = ListNode(array[i])
            p = p.next
            i = i + 1
        return new_head
