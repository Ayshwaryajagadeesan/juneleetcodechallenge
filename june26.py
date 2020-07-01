def sum(self, root, preSum):
      if root==None: return 0
      preSum = preSum*10 + root.val
      if root.left==None and root.right==None: return preSum
      return self.sum(root.left, preSum)+self.sum(root.right, preSum)

  def sumNumbers(self, root: TreeNode) -> int:
      return self.sum(root, 0)
