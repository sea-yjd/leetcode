class Solution:
    def convert(self, s: str, numRows: int):
        if numRows <= 1 or numRows >= len(s):
            return s
        p = ['' for _ in range(numRows)]
        row = 0
        step = 1
        for i in s:
            p[row] += i
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row = row + step
        return ''.join(p)
S = Solution()
y = S.convert(s = "AB", numRows = 1)
print(y)
