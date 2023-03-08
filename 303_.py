# [303] 区域和检索 - 数组不可变
#

# @lc code=start
# 解法一：
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        presum = 0
        for i in range(left, right+1):
            presum += self.nums[i]
        return presum
     
# 解法二：前缀和数组
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.preSum = [0 for _ in range(len(nums)+1)]
        for i in range(1, len(nums)+1):
            self.preSum[i] = self.preSum[i-1] + nums[i-1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.preSum[right + 1] - self.preSum[left]
