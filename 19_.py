# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkList:
    def __init__(self) -> None:
        self.head = None
    def initList(self, data):
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r
    def printlist(self, head):
        if head == None: return
        node = head
        while node != None:
            print(node.val, end = '')
            node = node.next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.val == None: return []
        len_ = 1
        head_ = head
        while head_.next != None:
            len_ += 1
            head_ = head_.next
        position = len_ - n + 1
        p = ListNode(0)
        r = p
        i = 1
        while (i <= len_):
            if i != position:
                p.next = ListNode(head.val)
                p = p.next
                head = head.next
            else:
                head = head.next
            i += 1
        return r.next
    
## 只遍历一次的解法：
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head: return
        if (not head.next) and (n==1):
            return 
        p1 = head
        for i in range(n):
            p1 = p1.next
        p2 = dummy = ListNode(0)
        p2.next = head
        while (p1 is not None):
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next   # TODO：注意这里不要写成 p2 = p2.next.next，否则指向的值都不改变
        while p2:
            p2 = p2.next
        return dummy.next
    
if __name__=='__main__':
    a = Solution()
    l = LinkList()
    head = [1,2,3,4,5]
    head = l.initList(head)
    l.printlist(head)
    print("\n")
    output = a.removeNthFromEnd(head, n=2)
    l.printlist(output)
