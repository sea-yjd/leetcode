# @lc app=leetcode.cn id=48 lang=python
#
# [48] 旋转图像
#
# 顺时针旋转：沿着主对角线镜像交换，之后每一行的元素翻转
# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        return matrix
