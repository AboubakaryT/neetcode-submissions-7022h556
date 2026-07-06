# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal = [0]
        def height(root):
            if not root:
                 return 0
            left = height(root.left)
            right = height(root.right)
            balance = right - left
            bal[0] = max(bal[0], abs(balance))

            return 1 + max(right, left)
            """
            1
           2  3 
             4  
            """

            
        height(root)
        if bal[0] == 1 or bal[0] == 0 or bal[0] == -1:
            return True
        else: 
            return False
        

            
            






        