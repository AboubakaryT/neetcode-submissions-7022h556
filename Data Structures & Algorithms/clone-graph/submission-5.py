"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque 
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:          
        if not node:
            return None

        queue = deque([node])
        oldToNew = {node: Node(val = node.val)}

        while queue:
            curr = queue.popleft()
            for neigh in curr.neighbors:
                if neigh not in oldToNew:
                    oldToNew[neigh] = Node(val = neigh.val)
                    queue.append(neigh)
                oldToNew[curr].neighbors.append(oldToNew[neigh])

        return oldToNew[node]  