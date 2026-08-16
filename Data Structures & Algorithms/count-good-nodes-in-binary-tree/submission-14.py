# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        2
       / \
          4
          /\
         10 8
             \
              4

        root=[2,null,4,10,8,null,null,4]
        """

        self.res = 0
        def dfs(root, check):
            if not root:
                return
            if root.val >= check:
                self.res+=1
            check = max(root.val, check)
            dfs(root.left, check)
            dfs(root.right,check)

        dfs(root,root.val)
        return self.res




            
            


        
    