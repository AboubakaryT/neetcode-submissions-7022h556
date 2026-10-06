import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        newPoints = []
        for x, y in points:
            newPoints.append((x,y,math.hypot(x, y)))
        newPoints.sort(key=lambda x: x[2])
        i = 0
        print(newPoints)
        while len(res) < k:
            res.append([newPoints[i][0],newPoints[i][1]])
            i+=1
        return res