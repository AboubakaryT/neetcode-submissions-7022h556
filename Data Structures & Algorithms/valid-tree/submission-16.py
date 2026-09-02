class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adjList = collections.defaultdict(list)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visit = set()
        node = [0, -1]
        
        #if we detect a cycle return False
        def cycle(node, parent):
            if node in visit:
                return True
            visit.add(node)
            for neig in adjList[node]:
                if neig == parent:
                    continue
                cycle(neig, node)

            return False
        
        if cycle(0,-1):
            return False

        return len(visit) == n  

        """
        visit = [0,1]
        queue = [[1,0]]
        {
        0:1,3
        1:0,3
        }
        """