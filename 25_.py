class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # list2array
        head_ = head
        array = [head.val]
        while head.next != None:
            array.append(head.next.val)
            head = head.next
        len_ = len(array)
        num = int(len_ / k)
        i = 0
        while (i+k)<=len_:
            p = array[i:i+k]
            p = p[::-1]
            array[i:i+k] = p
            i = i + k
        # array2list
        new_head = p = ListNode(array[0])
        i = 1
        while(i < len_):
            p.next = ListNode(array[i])
            p = p.next
            i = i + 1
        return new_head
