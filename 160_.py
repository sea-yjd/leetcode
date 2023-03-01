# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        # 解法一：拼接
        p1 = headA
        p2 = headB
        while (p1 != p2):
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next
            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next

        return p1

        # 解法二：求两者长度   !!
        p1 = headA
        lenA = 0
        while p1:
            p1 = p1.next
            lenA += 1
        p2 = headB
        lenB = 0
        while p2:
            p2 = p2.next
            lenB += 1
        p1, p2 = headA, headB
        if (lenA > lenB):
            for i in range(lenA - lenB):
                p1 = p1.next
        else:
            for i in range(lenB - lenA):
                p2 = p2.next
        while(p1 != p2):
            # if p1 == None:
            #     return p1
            # elif p2 == None:
            #     return p2
            # else:
            p1 = p1.next
            p2 = p2.next
        return p1
        
        # 解法三：闭环
        dummy = headA
        while dummy.next:
            dummy = dummy.next
        dummy.next = headB
        # 判断是否存在环
        fast = slow = headA
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if (slow == fast):
                break
        if not fast or not fast.next:
            dummy.next = None   # 将headA与headB分开
            return None
        # 否则，存在环
        slow = headA
        while fast != slow:
            slow = slow.next
            fast = fast.next
        dummy.next = None
        return fast
        
        # 解法四：哈希（空间复杂度较高）
        first_set = set()
        curr = headA
        while curr:
            first_set.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in first_set:
                return curr
            curr = curr.next
        return None
