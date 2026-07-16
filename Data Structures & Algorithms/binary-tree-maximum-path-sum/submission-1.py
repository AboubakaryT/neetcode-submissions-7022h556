# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum = float('-inf')

        def maxPath(root):
            if not root:
                return 0
            
            left = max(0, maxPath(root.left))
            right = max(0, maxPath(root.right))
            self.sum = max(self.sum, left + right + root.val)
            return max(left,right) + root.val

        maxPath(root)

        return self.sum
        """
        left = max(0, 2), max(0, 0)
        right = max(0,0)
        """