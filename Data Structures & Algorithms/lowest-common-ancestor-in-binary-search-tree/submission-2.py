# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #The properties of a BST: left < root, right < root
        
        while root:
            #LCA is on the left side
            if p.val < root.val and q.val < root.val:
                root = root.left
            #LCA is on the right side
            elif p.val > root.val and q.val > root.val:
                root = root.right
            #P and Q are on the right and left subtree, so we can just return the root.
            else:
                return root
            
        
        