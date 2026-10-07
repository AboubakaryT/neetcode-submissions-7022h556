"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:          
        if not node:
            return None
        clones = {}
        stack = [node]
        visited = set()
        print(clones)
        while stack:
            old = stack.pop()
            clones[old] = Node(val = old.val)
            for neigh in old.neighbors:
                if neigh in visited:
                    continue
                visited.add(neigh)
                stack.append(neigh)
                
        for old, new in clones.items():
            for neigh in old.neighbors:
                clones[old].neighbors.append(clones[neigh])
        
        return clones[node]
        