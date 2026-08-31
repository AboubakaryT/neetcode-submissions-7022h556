from collections import deque as dq, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
            
        adjList = defaultdict(list)
        for f,t in edges:
            adjList[f].append(t)
            adjList[t].append(f)

        visited = set()
        queue = dq()
        queue.append([0, -1])
        visited.add(0)
    
        while queue:
            node,parent = queue.popleft()
            for neigh in adjList[node]:
                if neigh == parent:
                    continue
                if neigh in visited:
                    return False
                visited.add(neigh)
                queue.append([neigh,node])


        
        return len(visited) == n

            
        