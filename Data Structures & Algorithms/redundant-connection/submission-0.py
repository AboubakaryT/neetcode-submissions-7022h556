from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Graph labled from 1 to n, n-1 edges
        Return the edge that makes the graph into a Tree
        """
        adjList = defaultdict(list)
        n = len(edges)
        visit = [False] * (n + 1)
        cycle = set()
        cycleStart = -1
        #Every cycle we find we will add to cycle. 
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node, parent):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True

            visit[node] = True

            for nei in adjList[node]:
                if nei == parent:
                    continue
                if dfs(nei,node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
            
        dfs(1,-1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        return []
                

                

        
        
        