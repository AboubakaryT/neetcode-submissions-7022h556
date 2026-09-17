class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        par = [i for i in range(n)]
        rank = [1] * n 
        def find(x):
            if x != par[x]:
                #Find root parent
                par[x] = find(par[x])
            #return root parent
            return par[x]
        

        def union(u,v):
            rootU,rootV = find(u), find(v)
            #Cycle detected
            if rootU == rootV:
                return False
            #if the rank is greater we know it's the parent root
            if rank[rootU] > rank[rootV]:
                #Change the parent
                par[rootV] = rootU
            elif rank[rootV] > rank[rootU]:
                par[rootU] = rootV
            else:
                rank[rootU]+=1
                par[rootV] = rootU

            return True
        
        for u,v in edges:
            if not union(u,v):
                return False
        return True