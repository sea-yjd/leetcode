"""
在做leetcode中和链表相关的题目时，不需要自己写输入输出，但是我们在进行本地调试的时候需要自己编写输入输出代码，完整代码如下：
"""
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class LinkList:
    def __init__(self):
        self.head = None
    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为data内的数据创建结点，建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r
    def printlist(self,head):
        if head == None:return
        node = head
        while node != None:
            print(node.val, end=' ')
            node = node.next

class Solution:
    def addTwoNumbers(self, l1, l2):

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        dummy = ListNode(0)
        p = dummy
        carry = 0

        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next

        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next

        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                p = p.next

        if carry == 1:
            p.next = ListNode(1)

        return dummy.next
if __name__=='__main__':
    a = Solution()
    l = LinkList()
    l1 = [9,8,7,6]
    l2 = [6,5,7,1]
    l1 = l.initList(l1)
    l2 = l.initList(l2)
    l.printlist(l1)
    print("\r")
    l.printlist(l2)
    print("\r")
    l3 = a.addTwoNumbers(l1,l2)
    l.printlist(l3)
