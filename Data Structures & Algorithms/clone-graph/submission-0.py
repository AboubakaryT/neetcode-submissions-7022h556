"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        """
        1:[2], 2[1,3], 3 [2]
        """
        def clone(node):
            if node in clones:
                return clones[node]

            copy = Node(node.val)
            clones[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            return copy

        return clone(node) if node else node
