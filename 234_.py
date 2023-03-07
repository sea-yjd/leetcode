# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 解法一：链表转数组
        head2list = []
        while head:
            head2list.append(head.val)
            head = head.next
        if head2list == head2list[::-1]:
            return True
        else:
            return False
        
        # 解法二：反转一半链表
        if head == None or head.next == None:
            return True
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        nxt = slow.next
        slow.next = None
        while nxt:
            f = nxt.next
            nxt.next = slow
            slow = nxt
            nxt = f
        while head != None and slow != None:
            if (head.val == slow.val):
                head = head.next
                slow = slow.next
            else:
                return False
        return True



    # 解法三：递归
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.left = head
        return Solution.traverse(self, head)
    def traverse(self, right):
        if right == None:
            return True
        res = Solution.traverse(self, right.next)
        res = res and (right.val == self.left.val)
        self.left = self.left.next
        return res
