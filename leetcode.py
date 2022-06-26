from typing import Optional
## 1. Two Sum
"""
nums = [2,7,11,15]
target = 22
dict = {}
for i in nums:
    j = target-i
    start_index = nums.index(i)
    next_index = start_index + 1
    temp_nums = nums[next_index:]
    if j in temp_nums:
        k = (nums.index(i),next_index+temp_nums.index(j))
"""
## 2. add two numbers
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
l1 = ListNode(l1)
l2 = ListNode(l2)
def list2num(list):
    list = [str(i) for i in list]
    s = ''
    for i in list:
        s = s + i
    s = s[::-1]
    return int(s)

def num2list(num):
    s = str(num)[::-1]
    a = []
    [a.append(i) for i in s]
    a = [int(i) for i in a]
    return a
num1 = list2num(l1)
num2 = list2num(l2)
num3 = num1 + num2
list3 = num2list(num3)
print(list3)
"""
"""
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

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
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
addTwoNumbers(l1,l2)

"""

"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        # :type l1: ListNode
        # :type l2: ListNode
        # :rtype: ListNode
        # 创建节点值为None的头节点，r和p指向头节点，r用来返回答案，p用来遍历
        r = p = ListNode(None)
        # s用来表示是否进位，初始化进位为0
        s = 0
        while l1 or l2 or s:
            # 若l1或l2存在，则将l1的值与l2的值相加，若s为1，则下次加1
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            # 将s取余(个位)作为p的下一个节点值
            p.next = ListNode(s % 10)
            # s取模
            s = s // 10
            # 向后遍历
            p = p.next
            # 若l1存在，则向后遍历
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # 返回 r 的下一个节点, 因为 r 指向的是空的头结点,
        # 下一个节点才是新建链表的后序节点
        return r.next


def main():
    S = Solution()
    nums = []
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    head1 = ListNode(l1[0])
    head2 = ListNode(l2[0])
    p1 = head1
    p2 = head2
    r1 = head1
    r2 = head2
    for i in l1[1:]:
        p1.next = ListNode(i)
        p1 = p1.next
    for j in l2[1:]:
        p2.next = ListNode(j)
        p2 = p2.next

    res = S.addTwoNumbers(r1, r2)
    while res:
        nums.append(res.val)
        res = res.next
    return nums


if __name__ == '__main__':
    result = main()
    print(result)
"""

## 在做leetcode中和链表相关的题目时，不需要自己写输入输出，但是我们在进行本地调试的时候需要自己编写输入输出代码，完整代码如下：
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