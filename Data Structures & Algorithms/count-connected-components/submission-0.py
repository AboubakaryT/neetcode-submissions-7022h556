from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        0 - 1 
        1 - 0, 2 
        2 - 1
        3 - 4
        4 - 5 
        """
        res = 0
        adjList = defaultdict(list)
        visit = [False] * n

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def bfs(node):
            queue = deque()
            queue.append(node)
            visit[node] = True
            while queue:
                curr = queue.popleft()
                for nei in adjList[curr]:
                    if not visit[nei]:
                        queue.append(nei)
                        visit[nei] = True
        
        for node in range(n):
            #If visit[node] = False, we traverse the graph
            if not visit[node]:
                bfs(node)
                res+=1

        return res
            
        

        
           
        """

        """
            