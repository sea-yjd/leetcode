## 10. Regular Expression Matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s)
        len_p = len(p)
        table = [[False] * (len_p + 1) for _ in range(len_s + 1)]
        for i in range(len_s + 1):
            for j in range(len_p + 1):
                if i == 0 and j == 0:
                    table[i][j] = True
                elif i == 0:
                    if p[j-1] == '*':
                        table[i][j] = table[i][j-2]
                    else:
                        table[i][j] = False
                elif j == 0:
                    table[i][j] = False

                else:
                    if p[j-1] == s[i-1] or p[j-1] == '.':
                        table[i][j] = table[i-1][j-1]
                    elif p[j-1] == '*':
                        if table[i][j-2] == True:
                            table[i][j] = True
                        elif p[j-2] == s[i-1] or p[j-2] == '.':
                            table[i][j] = table[i-1][j]
                        else:
                            table[i][j] = False
        return table[len_s][len_p]
S = Solution()
y = S.isMatch('aa','a*')
print(y)
