class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        r=self.invertTree(root.right)
        l=self.invertTree(root.left)
        root.right=l
        root.left=r
        return root
