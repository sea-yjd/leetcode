# [315] 计算右侧小于当前元素的个数
#

# @lc code=start

           
class Solution(object):
    class Pair:
        def __init__(self, val, id):
            self.val = val
            self.id = id

    def Mergesort(self, arr, l, r):
        if (l == r):
            return 
        m = l + ((r - l) >> 1)
        self.Mergesort(arr, l, m) 
        self.Mergesort(arr, m+1, r)
        self.mergeprocess(arr, l, m, r)
    def mergeprocess(self, arr, l, m, r):
        helper = [self.Pair(0, 0) for _ in range(r - l + 1)]
        i = 0
        p1 = l
        p2 = m+1
        while (p1 <= m and p2 <= r):
            if arr[p1].val > arr[p2].val:
                helper[i] = arr[p1]
                self.count[arr[p1].id] += (r-p2+1)
                p1 += 1
            else:
                helper[i] = arr[p2]
                p2 += 1
            i += 1
        while (p1 <= m):
            helper[i] = arr[p1]
            i += 1
            p1 +=1
        while (p2 <= r):
            helper[i] = arr[p2]
            i += 1
            p2 += 1
        for i in range(r-l+1):
            arr[l+i] = helper[i]

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return [0]
        arr = [self.Pair(nums[i], i) for i in range(len(nums))]
        self.count = [0 for _ in range(len(nums))]
        self.Mergesort(arr, 0, len(nums)-1)
        return self.count
