class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if root.left and root.right:
            return min(left, right) + 1
        
        return max(left, right) + 1