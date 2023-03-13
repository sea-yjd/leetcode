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
    
  # 解法二：宽度遍历 -- 这里注意：宽度遍历需要队列，而list可以实现堆栈的append()和pop()，对于队列需要用到deque：append()/pop()都是对对尾进行操作，appendleft()
  # 和popleft()都是对对头操作。其中用que的长度size控制搜索的范围，设计巧妙
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if (root == None):
            return root
        que = deque()
        que.append(root)
        while (len(que)>0):
            size = len(que)
            prev = None
            while size > 0:
                node = que.popleft()
                if (prev != None):
                    prev.next = node
                if node.left != None:
                    que.append(node.left)
                if node.right != None:
                    que.append(node.right)
                prev = node
                size -= 1
        return root
      
    
