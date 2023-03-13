class Solution(object):
  def right2left(self, node1, node2):
        if node1 is None or node2 is None:
            return None

        node1.next = node2
        self.right2left(node1.left, node1.right)
        self.right2left(node2.left, node2.right)
        self.right2left(node1.right, node2.left)
    # 解法一
  def connect(self, root):
      """
      :type root: Node
      :rtype: Node
      """
      if root == None:
          return 
      self.right2left(root.left, root.right)
      return root
    
  # 解法二：宽度遍历 -----  leetcode结果是错的，问题出在哪里？
  def connect(self, root):
      """
      :type root: Node
      :rtype: Node
      """
      if (root == None):
          return root
      que = []
      que.append(root)
      while (que):
          size = len(que)
          prev = None
          while size > 0:
              node = que.pop()
              if (prev != None):
                  prev.next = node
              if node.left != None:
                  que.append(node.left)
              if node.right != None:
                  que.append(node.right)
              prev = node
              size -= 1
      return root
      
    
