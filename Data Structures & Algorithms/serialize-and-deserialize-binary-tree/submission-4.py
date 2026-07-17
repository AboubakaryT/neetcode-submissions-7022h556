# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    preorderString =[]

    def preorderToString(self, root):
        if not root:
            self.preorderString.append("N")
            return 
        self.preorderString.append((str(root.val)))
        self.preorderToString(root.left)
        self.preorderToString(root.right)
        
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.preorderString = []
        self.preorderToString(root)
        return ",".join(self.preorderString)
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0
        print(vals)
        def dfs():
            if vals[self.i] == "N":
                self.i+=1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        
