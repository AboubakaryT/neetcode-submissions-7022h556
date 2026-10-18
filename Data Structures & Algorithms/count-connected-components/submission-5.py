class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        def find(x):
            if x!= par[x]:
                par[x] = find(par[x])
            return par[x]

        def union(u,v):
            rootU, rootV = find(u), find(v)
            if rootU == rootV:
                return False
            
            if rank[rootU] > rank[rootV]:
                par[rootV] = rootU
            elif rank[rootV] > rank[rootU]:
                par[rootU] = rootV
            else:
                rank[rootU]+=1
                par[rootV] = rootU
            return True

        for u,v in edges:
            if union(u,v):
                n-=1
        return n 
            
            