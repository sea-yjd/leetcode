# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while (left <= right):
            if numbers[left] + numbers[right] == target:
                return [left, right]
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
