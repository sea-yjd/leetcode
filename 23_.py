#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个升序链表
#
from Queue import PriorityQueue
import heapq
# @lc code=start
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# 解法一：所有数据进堆--> 小根堆排序
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 所有数都进堆，利用小根堆函数，直接一个一个弹出最小值
        # 没有充分利用：每个链表都是升序这一信息，可以在k个数上面进行小根堆排序。
        # q = PriorityQueue()
        heap = []
        root = res = ListNode(None)
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        while heap:
            res.next = ListNode(heapq.heappop(heap))
            res = res.next
        return root.next
      
# 解法二：头结点进堆
# 采用优先级heap
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = []
        for head in lists:
            if head:
                heapq.heappush(l, (head.val, head))
        dummy_node = ListNode(-1)
        cur = dummy_node

        while l:
            _, head = heapq.heappop(l)
            cur.next = head
            cur = cur.next
            if head.next:
                heapq.heappush(l, (head.next.val, head.next))
        return dummy_node.next


# 采用优先级接口PriorityQueue   

class Solution(object):
    def mergeKLists(self, lists):
        head = point = ListNode(0)
        q = PriorityQueue(maxsize=len(lists))
        for idx, l in enumerate(lists):
            if l:
                q.put((l.val, l))
        while q.qsize() > 0:         ## TODO:这里重点关注：与heap不同，必须写.qsize
            _, point.next = q.get()
            point = point.next
            if point.next:
                q.put((point.next.val, point.next))
        return head.next
## In the event that two or more of the lists have the same 
# val, this code will error out since the queue module will 
# compare the second element in the priority queue which is 
# a ListNode object (and this is not a comparable type).
# 因此改为以下代码：

class Solution(object):
    def mergeKLists(self, lists):
        head = point = ListNode(0)
        q = PriorityQueue(maxsize=len(lists))
        for idx, l in enumerate(lists):
            if l:
                q.put((l.val, idx, l))
        while q.qsize() > 0:
            _, list_idx, point.next = q.get()
            point = point.next
            if point.next:
                q.put((point.next.val,list_idx, point.next))
        return head.next

# 采用优先级接口+比较器         --> 用比较器就可以实现大到小等指定的排序 
class Compare():
    def __init__(self, head):
        self.head = head
    def __lt__(self, other):
        return self.head.val < other.head.val
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        point = dummy
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((Compare(l)))
        while q.qsize() > 0:
            k = q.get().head
            point.next = k
            point = point.next
            if k.next:
                q.put((Compare(k.next)))
        return dummy.next
