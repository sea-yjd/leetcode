class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 0:
            return []
        
        ans = set()
        
        nums.sort()
        for i in range(len(nums)-1):
            j = i+1
            p = len(nums) - 1
            while(j<p):
                if nums[i]+nums[j]+nums[p]==0:
                    ans.add((nums[i],nums[j],nums[p]))
                if nums[i]+nums[j]+nums[p] > 0:
                    p -= 1
                else:
                    j += 1
                    
        return list(ans)
 
