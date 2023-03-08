# [151] 反转字符串中的单词
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        l = s.split()
        for i in range(len(l)):
            l[i] = l[i][::-1]
        return ' '.join(l)
