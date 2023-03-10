# [215] 数组中的第K个最大元素
# 本题目要求时间复杂度O(n)

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 解法一：快排思想
        if nums == None:
            return 
        preset = random.choice(nums)
        left, mid, right = [], [], []
        for i in nums:
            if i > preset:
                left.append(i)
            elif i == preset:
                mid.append(i)
            else:
                right.append(i)
        if len(left) >= k:
            return self.findKthLargest(left, k)
        elif len(left) + len(mid) < k:
            return self.findKthLargest(right, k-len(left)-len(mid))
        else:
            return mid[0]

        # 解法二：小根堆思想
        heaptree = []
        for i in nums:
            heapq.heappush(heaptree, i)
            while (len(heaptree) > k):
                heapq.heappop(heaptree)
        return heapq.heappop(heaptree)
