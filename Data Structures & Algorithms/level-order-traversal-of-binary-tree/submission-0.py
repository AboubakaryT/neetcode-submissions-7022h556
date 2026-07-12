# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        next_queue = []
        result= []
        level = []
        while queue:
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            result.append(level)
            queue = next_queue
            next_queue = []
            level = []
        #queue = [4,5,6,7], next_queue =[], level = [2,3]
        #res = [[1],[2,3] ]
        return result