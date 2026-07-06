# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and not q:
                return False
        if q and not p:
                return False
        """
        p=[1,2,3]
        q=[1,2,3]
        """
        if p and q:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            if p.val != q.val:
                return False
            if p.val != q.val:
                return False
            return left and right
        return True