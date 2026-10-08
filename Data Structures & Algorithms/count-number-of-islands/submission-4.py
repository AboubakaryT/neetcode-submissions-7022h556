class DSU:
  def __init__(self, n):
    #19 
    self.parent = [i for i in range(n)]
    #19
    self.size = [1 for _ in range(n)]

  def find(self, u):
    if self.parent[u] != u:
      self.parent[u] = self.find(self.parent[u])
    return self.parent[u]

  def union(self,u,v):
    rootU, rootV = self.find(u), self.find(v)
    #belongs to the same root parent. 
    if rootU == rootV:
      return False
      
    if self.size[rootU] >= self.size[rootV]:
      self.parent[rootV] = rootU
      self.size[rootV]+=self.size[u]

    elif self.size[rootV] >= self.size[rootU]:
      self.parent[rootU] = rootV
      #Conenct u to v
      self.size[rootU]+=self.size[v]

    return True

      
      
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      #3 * 4 = 12 
      ROWS = len(grid)
      COLS = len(grid[0])
      dsu = DSU(ROWS * COLS)
      directions = [(1, 0), (0, 1),(-1, 0), (0,-1)]
      islands = 0

      def index(r,c):
        return r * COLS + c

      for r in range(ROWS):
        for c in range(COLS):
          if grid[r][c] == "1":
            islands+=1
            for dr, dc in directions:
              nr, nc = r + dr, c + dc
              if nr == ROWS or nr < 0 or nc == COLS or nc < 0 or grid[nr][nc] == "0":
                continue
              if dsu.union(index(r,c),index(nr,nc)):
                islands-=1

      return islands



      