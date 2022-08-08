# 18. 4sum
class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        
        nums = sorted(nums)
        result = set()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                p = j + 1
                q = len(nums) - 1
                while(p < q):
                    sum = nums[i] + nums[j] + nums[p] + nums[q]
                    if sum == target:
                        if (nums[i] , nums[j] , nums[p] , nums[q]) not in result:
                            result.add((nums[i] , nums[j] , nums[p] , nums[q]))
                    if sum < target:
                        p += 1
                    else:
                        q -= 1

        return list(result) 

S = Solution()
y = S.fourSum(nums = [-3,-1,0,2,4,5], target = 2)
print(y)
