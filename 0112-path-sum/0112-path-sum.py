class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,s):
            if not node:
                return
            s += (node.val)
            if node.left is None and node.right is None:
                if s == targetSum:
                    return True
            return dfs(node.left,s) or dfs(node.right,s)
        return dfs(root,0)