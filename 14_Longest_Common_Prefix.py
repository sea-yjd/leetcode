# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs):
        ## solution 1:
        # if not strs:
        #     return ''
        # for i in range(0,len(strs[0])):
        #     for string in strs[1:]:
        #         if i >= len(string) or strs[0][i] != string[i]:
        #             return strs[0][:i]
        # return strs[0]
        ## solution 2:
        result = ''
        i = 0
        while True:
            try:
                sets = set(string[i] for string in strs)
#                 print('sets',sets)
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else:
                    break
            except Exception as e:
                break
        return result

S = Solution()
y = S.longestCommonPrefix(["flower","flow","flight"])
print(y)
