# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        #Left child node must always be less then parent
        #Right child node must always be greater then parent
        #Left subtree must always be smaller then root.
        #Right subtree must always be greater then root.
        def dfs(node, minRoot ,maxRoot):
            if not node: 
                return True

            if node.val <= minRoot or node.val >= maxRoot:
                return False

            return dfs(node.left, minRoot, node.val) and dfs(node.right, node.val, maxRoot)

        return dfs(root, float('-inf'),float('inf'))