class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        """
        stack = [38,1,(36,3),]
        stackTemp = 30 -> 36 -> 35
        stackIndex = 0 -> 3 -> 5
        """
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0] :
                popped = stack.pop()
                stackTemp = popped[0]
                stackIndex = popped[1]
                day = i - stackIndex
                res[stackIndex] = day
            stack.append([t,i])
        return res     