# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        # number = [i+1 for i in range (n*n)]
        number = 1
        upper_bound, left_bound = 0, 0
        lower_bound, right_bound = n - 1, n-1
        while (number <= n * n):
            if upper_bound <= lower_bound:
                for j in range(left_bound, right_bound + 1):
                    res[upper_bound][j] = number
                    number += 1
                upper_bound += 1
            if right_bound >= left_bound:
                for i in range(upper_bound, lower_bound + 1):
                    res[i][right_bound] = number
                    number += 1
                right_bound -= 1
            if upper_bound <= lower_bound:
                for j in range(right_bound, left_bound - 1, -1):
                    res[lower_bound][j] = number
                    number += 1
                lower_bound -= 1
            if right_bound >= left_bound:
                for i in range(lower_bound, upper_bound - 1, -1):
                    res[i][left_bound] = number
                    number += 1
                left_bound += 1
        return res
