## 16. 3Sum Closest
import numpy as np
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        val_min = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            p = i + 1
            q = len(nums) - 1
            while(p < q):
                val = nums[i] + nums[p] + nums[q]
                if abs(val - target) < abs(val_min - target):
                    val_min = val
                if val == target:
                    return target
                elif val < target:
                    p += 1
                else:
                    q -= 1 

        return val_min
        
S = Solution()
y = S.threeSumClosest([-1,2,1,-4],1)
print(y)
