# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(cow,bull):
            if not cow and not bull:
                return True
            elif not cow and bull:
                return False
            elif  cow and not bull:
                return False
            elif cow.val != bull.val:
                return False
            return check(cow.left,bull.left) and check(cow.right,bull.right)
        return check(p,q)