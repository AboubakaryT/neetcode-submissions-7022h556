class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]
        rank = [1] * n
        
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
            

        def union(u,v):
            rootU = find(u)
            rootV = find(v)

            if rootU == rootV:
                return False
                
            if rank[rootU] > rank[rootV]:
                p[rootV] = rootU
            elif rank[rootV] > rank[rootU]:
                p[rootU] = rootV
            else:
                rank[rootU]+=1
                p[rootV] = rootU
    
            return True
            

        
        for u,v in edges:
            if union(u,v):
                n-=1

        return n
            
