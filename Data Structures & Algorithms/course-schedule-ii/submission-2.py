from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        seen = set()
        preReqs = defaultdict(list)
        for p, c in prerequisites:
            preReqs[p].append(c)

        def cycle(course,seen):
            if course in seen:
                return True
            
            seen.add(course)
            for p in preReqs[course]:
                if p in seen:
                    return True
                cycle(p,seen)
                
            preReqs[course] = []
            if course not in res:
                res.append(course)
            seen.remove(course)
            return False

        for course in range(numCourses):
            if cycle(course, seen):
                return []
        return res

        """
        numCourses=2
        prerequisites=[[0,1]]
        preReqs = [0:1]
        """