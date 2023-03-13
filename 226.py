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
    # 解法一：遍历思维
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
    
    # 解法二：分解思维
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root
