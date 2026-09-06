class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        [[0,1],[1,2],[2,3],[1,3],[1,4]]
        """
        p = [i for i in range(n)]
        rank = [1] * n
        print(p)
        if len(edges) != n-1:
            return False
        #Finds Parent for DSU
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
            if not union(u,v):
                return False

        return True