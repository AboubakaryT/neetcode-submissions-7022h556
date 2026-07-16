# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        inorderMap = {}
        for i, val in enumerate(inorder):
            inorderMap[val] = i
        
        self.pre = 0
        def build(left, right):
                if left > right:
                    return None
                val = preorder[self.pre]
                self.pre+=1

                root = TreeNode(val)

                mid = inorderMap[val]

                root.left = build(left, mid-1)
                root.right = build(mid + 1, right)
                return root

        return build(0, len(inorder) - 1)
