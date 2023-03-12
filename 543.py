#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self, ):
        self.maxlength = 0
    def maxdepth(self, root):
        if root == None:
            return 0
        leftlength = self.maxdepth(root.left)
        rightlength = self.maxdepth(root.right)
        self.maxlength = max(leftlength + rightlength, self.maxlength)
        return max(leftlength, rightlength) + 1
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxdepth(root)
        return self.maxlength
