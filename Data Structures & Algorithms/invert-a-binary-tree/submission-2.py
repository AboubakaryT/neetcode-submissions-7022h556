# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)

        return root

        """
        1
       3  2
    7  6  4  5
        """