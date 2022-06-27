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
