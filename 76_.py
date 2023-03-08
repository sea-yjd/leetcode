# [76] 最小覆盖子串
#
from collections import defaultdict
# @lc code=start
class Solution(object):
  # 采用滑动窗口解题
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        window, need = defaultdict(int), defaultdict(int)
        for i in t:
            need[i] += 1
        left, right, verify = 0, 0, 0
        length = float('inf')
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    verify += 1
            while (verify == len(need)):
                if right - left < length:
                    length = right - left
                    start = left
                d = s[left]
                left += 1
                if d in need:
                    window[d] -= 1
                    if window[d] < need[d]:
                        verify -= 1
        return "" if length == float('inf') else s[start:start+length]
