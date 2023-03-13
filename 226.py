# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def exchange(self, root):
        if root == None:
            return 
        self.exchange(root.left)
        self.exchange(root.right)
        # exchange
        tmp = root.left
        root.left = root.right
        root.right = tmp

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.exchange(root)
        # self.pre(root)
        return root
