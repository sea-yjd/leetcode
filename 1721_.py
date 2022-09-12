class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head_ = head
        array = [head.val]
        while (head.next != None):
            array.append(head.next.val)
            head = head.next
        len_ = len(array)
        k1 = k-1
        k2 = len_ - k
        t = array[k1]
        array[k1] = array[k2]
        array[k2] = t

        # output a list
        head_new = p = ListNode(array[0])
        i = 1
        while (i < len_) :
            p.next = ListNode(array[i])
            p = p.next
            i += 1
        return head_new
