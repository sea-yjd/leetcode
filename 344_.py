# [344] 反转字符串
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) -1 
        while (left <= right):
            t = s[left]
            s[left] = s[right]
            s[right] = t
            left += 1
            right -= 1
        return s
