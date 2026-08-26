"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque as dq
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        """
        1:[2], 2: [1,3], 3: [2]

        dfs(1) -> 1:1
        """
        def clone(node):
            if node in clones:
                return clones[node]

            copy = Node(node.val)
            clones[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(clone(n))

            return clones[node]
            
        return clone(node) if node else node