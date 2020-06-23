def countNodes(self, root: TreeNode) -> int:
        def traverse(root):
            nonlocal count
            if not root:
                return
            count += 1
            traverse(root.left)
            traverse(root.right)
        count = 0
        traverse(root)
        return count
