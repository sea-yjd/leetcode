class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        max = 0
        start = -1
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = i
                if max < (i - start): max = i-start
            else:
                if start < dict[s[i]]:
                    start = dict[s[i]]         
                dict[s[i]] = i
                if max < (i - start): max = i-start
        return max
    
 # [3] 无重复字符的最长子串
#
# 解法二：使用滑动窗口套路
# @lc code=start
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = defaultdict(int)
        left, right = 0, 0
        length = 0
        while right < len(s):
            c = s[right]
            if c not in window or window[c] == 0:
                window[c] += 1
                right += 1
                if right - left > length:
                    length = right - left
            else:
                # right停止
                d = s[left]
                window[d] -= 1
                left += 1
        return length
