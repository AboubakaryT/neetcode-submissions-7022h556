from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Cycle detection problem = graph
        """
        courses = defaultdict(list)
        seen = set()

        def cycle(course, seen):
            if course in seen:
                return True
            seen.add(course)
            for p in courses[course]:
                if p in seen:
                    return True
                cycle(p, seen)
            courses[course]= []
            seen.remove(course)
            return False
            
        
        for p,c in prerequisites:
            courses[p].append(c)


        for course in range(numCourses):
            if cycle(course ,seen):
                return False

        return True