# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0 
            stack = []
            depth = 1
            stack.append((root, depth))
            ans = 0
            while len(stack) > 0:
                popped = stack.pop()
                node = popped[0]
                depth = popped[1]
                if node.left:
                    stack.append((node.left, depth+1))
                if node.right:
                    stack.append((node.right, depth+1))
                ans = max(ans, depth)
                print(ans)
            return ans

"""
1,2,NONE 
"""