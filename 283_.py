def removeK(self, nums, k):
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != k:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums == [] or nums == [0]:
            return nums
        left = Solution.removeK(self, nums, 0)
        for i in range(left, len(nums)):
            nums[i] = 0
        return nums
