# [54] 螺旋矩阵
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        upper_bound = 0
        lower_bound = m-1
        left_bound = 0
        right_bound = n-1
        res = []
        while len(res) < m * n:
            # 下面的代码中要注意'if'不能写成'while'
            # <= 不能写成 <, 因为当对立的两边界相等时，还有元素要遍历
            # 从左往右
            if upper_bound <= lower_bound:
                for j in range(left_bound, right_bound + 1):
                    res.append(matrix[upper_bound][j])
                upper_bound += 1
            # 从上往下
            if left_bound <= right_bound:
                for i in range(upper_bound, lower_bound + 1):
                    res.append(matrix[i][right_bound])
                right_bound -= 1
            # 从右往左
            if upper_bound <= lower_bound:
                for j in range(right_bound, left_bound - 1, -1):
                    res.append(matrix[lower_bound][j])
                lower_bound -= 1
            # 从下往上
            if left_bound <= right_bound:
                for i in range(lower_bound, upper_bound -1 , -1):
                    res.append(matrix[i][left_bound])
                left_bound += 1
        return res
