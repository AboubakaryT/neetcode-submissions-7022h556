# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:   
        res = 0
        def dfs(root):
            if not root:
                return 0
            nonlocal res
            left_path = dfs(root.left)
            right_path = dfs(root.right) 

            diameter = left_path + right_path 
            res = max(res, diameter)
            return max(left_path,right_path) + 1

        dfs(root)
        return res