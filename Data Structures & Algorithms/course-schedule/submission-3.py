from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Khans Algorithm. Can Detect Cycles using Topological Ordering.
        Repeatly remove nodes that does not depend on another node, and 
        add them to the Topological Ordering. As Nodes without dependecies 
        are removed from the graph. New Nodes without dependecies should become free. 
        We keep going until all nodes are gone, or a cycle has been detected. 
        """
    
        indegree = [0] * numCourses
        queue = deque()
        #This or defaultdict is acceptable. 
        adjList = [[] for _ in range(numCourses)]
        #Find degree of all nodes, there must be at LEAST one with no degree in order for this algorithm to return True.
        #Adjacency List traversal later.
        for u, v in prerequisites:
            indegree[v]+=1
            adjList[u].append(v)
        #If no nodes are being depended on, append to queue. 
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        finish = 0 #Used to track if we finished the same amount of courses as num courses.
        while queue:
            #Only pop nodes that don't rely on other nodes.
            pop = queue.popleft()
            finish+=1
            for neighbor in adjList[pop]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return finish == numCourses      
        