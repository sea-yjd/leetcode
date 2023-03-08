# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        need, window = defaultdict(int), defaultdict(int)
        left, right = 0, 0
        verify = 0
        anagrams = []
        for i in p:
            need[i] += 1
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    verify += 1
            while right - left == len(p):
                if verify == len(need):
                    anagrams.append(left)
                d = s[left]
                left += 1
                ## 注意：以下注释的代码不可用，只有当==时，删掉left才verify-1.
                # if d in need:
                #     window[d] -= 1
                #     if window[d] < need[d]:
                #         verify -= 1
                if d in need:
                    if window[d] == need[d]:
                        verify -= 1
                    window[d] -= 1
        return anagrams
