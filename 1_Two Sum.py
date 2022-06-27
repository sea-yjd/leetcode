class Solution:
    def twoSum(self, nums, target):
    ## method 1:
        dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target - nums[i]] , i]
    ## method 2:
#         for i in nums:
#             j = target - i
#             start_index = nums.index(i)
#             next_index = start_index + 1
#             temp_nums = nums[next_index : ]
#             if j in temp_nums:
#                 return(nums.index(i),next_index + temp_nums.index(j))
